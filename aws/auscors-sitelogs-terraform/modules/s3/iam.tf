# Text site log submitter
resource "aws_iam_role" "submitter_role" {
  name = "${var.application}_submitter_role_${var.environment}"
  path = "/"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "AWS": ["${join("\",\"", var.submitter_arns)}"]
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# The policy to allow writing to the incoming bucket
resource "aws_iam_role_policy" "s3_write_incoming_bucket_policy" {
  name = "${var.application}_s3_write_incoming_bucket_policy_${var.environment}"
  role = "${aws_iam_role.submitter_role.id}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
		"s3:ListBucket", 
		"s3:GetObject",
		"s3:PutObject"
      ],
      "Resource": [
          "${aws_s3_bucket.incoming_bucket.arn}",
          "${aws_s3_bucket.incoming_bucket.arn}/*"
      ]
    }
  ]
}
EOF
}
