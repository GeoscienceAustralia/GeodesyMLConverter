provider "aws" {
  region = "${var.region}"
}

data "terraform_remote_state" "state" {
  backend = "s3"
  config {
    bucket     = "${var.tf_state_bucket}"
    lock_table = "${var.tf_state_table}"
    region     = "${var.region}"
    key        = "${var.application}/${var.environment}/terraform.tfstate"
  }
}

terraform {
  backend "s3" {}
}

module "s3" {
  source      = "./modules/s3/"

  environment = "${var.environment}"
  application = "${var.application}"
  owner       = "${var.owner}"
}

module iam {
  source      = "./modules/iam/"

  bucket_name = "${module.s3.bucket_name}"

  environment = "${var.environment}"
  application = "${var.application}"
  owner       = "${var.owner}"
}

module "lambda" {
  source       = "./modules/lambda/"

  sns_arn      = "${var.sns_arn}"
  bucket_name  = "${module.s3.bucket_name}"
  iam_role_arn = "${module.iam.iam_role_arn}"

  environment  = "${var.environment}"
  application  = "${var.application}"
  owner        = "${var.owner}"
}
 
