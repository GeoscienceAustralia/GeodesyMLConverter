resource "aws_s3_bucket" "data_bucket" {
  bucket = "${var.application}-converted-${var.environment}"

  lifecycle {
    # Will change to true before prod deployment
    prevent_destroy = false
  }

  versioning {
    enabled = true
  }

  tags {
    environment = "${var.environment}"
    application = "${var.application}"
    owner       = "${var.owner}"
  }

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "${var.read_only_user_arn}"
            },
            "Action": [
		"s3:ListBucket", 
		"s3:GetObject"
	    ],
	    "Resource": [
		"arn:aws:s3:::${var.application}-converted-${var.environment}",
                "arn:aws:s3:::${var.application}-converted-${var.environment}/*"
            ]
        }
    ]
}
POLICY
}

output "bucket_name" {
  value = "${aws_s3_bucket.data_bucket.id}"
}
