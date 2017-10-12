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

# The policy to allow lambda to assume any role
resource "aws_iam_role_policy" "assume_role" {
  name = "${var.application}_assume_role_${var.environment}"
  role = "${aws_iam_role.iam_role.id}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
          "sts:AssumeRole"
      ],
      "Resource": "*"
    }
  ]
}
EOF
}

# The policy to allow reading from incoming bucket
resource "aws_iam_role_policy" "s3_read_incoming_bucket_policy" {
  name = "${var.application}_s3_read_incoming_bucket_policy_${var.environment}"
  role = "${aws_iam_role.iam_role.id}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:Get*"
      ],
      "Resource": ["arn:aws:s3:::${var.incoming_bucket_name}/*"]
    }
  ]
}
EOF
}

# The policy to allow reading from incoming bucket
resource "aws_iam_role_policy" "s3_write_incoming_bucket_policy" {
  name = "${var.application}_s3_write_incoming_bucket_policy_${var.environment}"
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
      "Resource": ["arn:aws:s3:::${var.incoming_bucket_name}/*"]
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
  role   = "${aws_iam_role.iam_role.id}"
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

resource "aws_iam_role_policy" "publish_to_dlq" {
  name   = "${var.application}-publish-to-dlq-${var.environment}"
  role   = "${aws_iam_role.iam_role.id}"
  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "sns:Publish"
      ],
      "Effect": "Allow",
      "Resource": "${aws_sns_topic.dead_letter_queue.arn}"
    }
  ]
}
POLICY
}

