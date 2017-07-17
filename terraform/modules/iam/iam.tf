resource "aws_iam_role" "iam_role" {
  name = "${var.application}_iam_role_${var.environment}"
  path = "/"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# The policy to allow access to the bucket
resource "aws_iam_role_policy" "s3_policy" {
  name = "${var.application}_s3_policy_${var.environment}"
  role = "${aws_iam_role.iam_role.id}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:Put*"
      ],
      "Resource": ["arn:aws:s3:::${var.bucket_name}/*"]
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "allow_log_creation" {
  name   = "${var.application}-allow-log-creation-${var.environment}"
  role   = "${aws_iam_role.lambda_role.id}"
  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
POLICY
}

output "iam_role_arn" {
  value = "${aws_iam_role.lambda_role.arn}"
}
