resource "aws_s3_bucket" "data_bucket" {
  bucket = "${var.application}-converted-${var.environment}"

  lifecycle {
    # Will change to true before prod deployment
    prevent_destroy = true
  }

  versioning {
    enabled = true
  }

  tags {
    environment = "${var.environment}"
    application = "${var.application}"
    owner       = "${var.owner}"
  }
}

output "bucket_name" {
  value = "${aws_s3_bucket.data_bucket.id}"
}
