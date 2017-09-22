resource "aws_lambda_function" "xml_converter" {
  filename         = "${path.module}/geodesymltositelog_lambda.zip"
  function_name    = "${var.application}-lambda-${var.environment}"
  role             = "${var.iam_role_arn}"
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
