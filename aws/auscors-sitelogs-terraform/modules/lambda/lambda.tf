resource "aws_lambda_function" "fetch_site_logs_from_ftp_sites" {
  filename         = "${path.module}/fetch_site_logs_from_ftp_sites_lambda.zip"
  function_name    = "${var.application}-fetch-from-ftp-sites-lambda-${var.environment}"
  role             = "${aws_iam_role.iam_role.arn}"
  handler          = "fetch_site_logs_from_ftp_sites.lambda_handler"
  runtime          = "python2.7"
  source_code_hash = "${base64sha256(file("${path.module}/fetch_site_logs_from_ftp_sites_lambda.zip"))}"
  memory_size      = 512
  timeout          = 300

  dead_letter_config {
    target_arn = "${aws_sns_topic.dead_letter_queue.arn}"
  }

  environment {
    variables = {
      incoming_bucket_name         = "${var.incoming_bucket_name}"
      gws_url                      = "${var.gws_url}"
    }
  }
}

resource "aws_cloudwatch_event_rule" "every_15_minutes" {
    name = "every-15-minutes"
    description = "Fires every 15 minutes"
    schedule_expression = "rate(15 minutes)"
}

resource "aws_cloudwatch_event_target" "check_remote_site_logs_every_15_minutes" {
    rule = "${aws_cloudwatch_event_rule.every_15_minutes.name}"
    target_id = "fetch_site_logs_from_ftp_sites"
    arn = "${aws_lambda_function.fetch_site_logs_from_ftp_sites.arn}"
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_fetch_site_logs_from_ftp_sites" {
    statement_id = "AllowExecutionFromCloudWatch"
    action = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.fetch_site_logs_from_ftp_sites.function_name}"
    principal = "events.amazonaws.com"
    source_arn = "${aws_cloudwatch_event_rule.every_15_minutes.arn}"
}

resource "aws_lambda_function" "ingest_text_site_log" {
  filename         = "${path.module}/ingest_text_site_log_lambda.zip"
  function_name    = "${var.application}-ingest-incoming-lambda-${var.environment}"
  role             = "${aws_iam_role.iam_role.arn}"
  handler          = "ingest_text_site_log_lambda.lambda_handler"
  runtime          = "python2.7"
  source_code_hash = "${base64sha256(file("${path.module}/ingest_text_site_log_lambda.zip"))}"
  memory_size      = 512
  timeout          = 30

  dead_letter_config {
    target_arn = "${aws_sns_topic.dead_letter_queue.arn}"
  }

  environment {
    variables = {
      credstash_role_arn           = "${var.credstash_role_arn}"
      gws_oidc_client_id_key       = "${var.gws_oidc_client_id_key}"
      gws_oidc_client_password_key = "${var.gws_oidc_client_password_key}"
      gws_system_user_key          = "${var.gws_system_user_key}"
      gws_system_user_password_key = "${var.gws_system_user_password_key}"
      oauth2_url                   = "${var.oauth2_url}"
      gws_url                      = "${var.gws_url}"
    }
  }
}

resource "aws_lambda_permission" "allow_s3" {
    statement_id = "AllowExecutionFromS3Bucket"
    action = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.ingest_text_site_log.arn}"
    principal = "s3.amazonaws.com"
    source_arn = "${var.incoming_bucket_arn}"
}

resource "aws_s3_bucket_notification" "incoming_bucket_notification" {
    bucket = "${var.incoming_bucket_name}"
    lambda_function {
        lambda_function_arn = "${aws_lambda_function.ingest_text_site_log.arn}"
        events = ["s3:ObjectCreated:*"]
    }
}

resource "aws_lambda_function" "xml_converter" {
  filename         = "${path.module}/geodesymltositelog_lambda.zip"
  function_name    = "${var.application}-lambda-${var.environment}"
  role             = "${aws_iam_role.iam_role.arn}"
  handler          = "geodesymltositelog_lambda.lambda_handler"
  runtime          = "python2.7"
  source_code_hash = "${base64sha256(file("${path.module}/geodesymltositelog_lambda.zip"))}"
  memory_size      = 512
  timeout          = 30

  dead_letter_config {
    target_arn = "${aws_sns_topic.dead_letter_queue.arn}"
  }

  environment {
    variables = {
      output_bucket_name = "${var.bucket_name}"
      gws_url            = "${var.gws_url}"
    }
  }
}

resource "aws_lambda_permission" "allow_sns" {
  statement_id   = "AllowExecutionFromSNS"
  action         = "lambda:InvokeFunction"
  function_name  = "${aws_lambda_function.xml_converter.function_name}"
  principal      = "sns.amazonaws.com"
  source_arn     = "${var.sns_arn}"
}

resource "aws_sns_topic_subscription" "topic_subscription" {
  topic_arn = "${var.sns_arn}"
  protocol  = "lambda"
  endpoint  = "${aws_lambda_function.xml_converter.arn}"
}

output "registration_lambda_arn" {
  value = "${aws_lambda_function.xml_converter.arn}" 
}
