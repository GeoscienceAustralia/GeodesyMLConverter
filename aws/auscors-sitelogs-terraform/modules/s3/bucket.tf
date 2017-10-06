resource "aws_s3_bucket" "incoming_bucket" {
  bucket = "${var.application}-incoming-${var.environment}"

  lifecycle {
    # Will change to true before prod deployment
    prevent_destroy = false
  }

  versioning {
    enabled = true
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
		"s3:GetObject",
		"s3:PutObject"
	    ],
	    "Resource": [
            "arn:aws:s3:::${var.application}-incoming-${var.environment}",
            "arn:aws:s3:::${var.application}-incoming-${var.environment}/*"
        ]
        }
    ]
}
POLICY

  tags {
    environment = "${var.environment}"
    application = "${var.application}"
    owner       = "${var.owner}"
  }
}

output "incoming_bucket_name" {
  value = "${aws_s3_bucket.incoming_bucket.id}"
}

output "incoming_bucket_arn" {
  value = "${aws_s3_bucket.incoming_bucket.arn}"
}

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
