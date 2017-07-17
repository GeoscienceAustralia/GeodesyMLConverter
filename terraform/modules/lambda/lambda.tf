resource "aws_lambda_function" "xml_converter" {
  filename         = "${path.module}/xml_converter_lambda.zip"
  function_name    = "${var.application}-lambda-${var.environment}"
  role             = "${aws_iam_role.lambda_role.arn}"
  handler          = "registration.lambda_handler"
  runtime          = "python2.7"
  source_code_hash = "${base64sha256(file("${path.module}/xml_converter_lambda.zip"))}"

  environment {
    variables = {
      output_bucket_name = "${var.bucket_name}"
    }
  }
}

output "registration_lambda_arn" {
  value = "${aws_lambda_function.xml_converter.arn}" 
}
