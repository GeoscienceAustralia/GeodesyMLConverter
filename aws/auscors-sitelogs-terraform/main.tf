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
  source = "./modules/s3/"

  read_only_user_arns = "${var.read_only_user_arns}"
  submitter_arns      = "${var.submitter_arns}"

  environment = "${var.environment}"
  application = "${var.application}"
  owner       = "${var.owner}"
}

module "lambda" {
  source       = "./modules/lambda/"

  sns_arn      = "${var.sns_arn}"
  incoming_bucket_name  = "${module.s3.incoming_bucket_name}"
  incoming_bucket_arn  = "${module.s3.incoming_bucket_arn}"
  bucket_name  = "${module.s3.bucket_name}"
  credstash_role_arn  = "${var.credstash_role_arn}"
  gws_oidc_client_id_key = "${var.gws_oidc_client_id_key}"
  gws_oidc_client_password_key = "${var.gws_oidc_client_password_key}"
  gws_system_user_key = "${var.gws_system_user_key}"
  gws_system_user_password_key = "${var.gws_system_user_password_key}"
  oauth2_url   = "${var.oauth2_url}"
  gws_url      = "${var.gws_url}"
  ftp_sitelogs = "${var.ftp_sitelogs}"
  sitelog_ftp_host         = "${var.sitelog_ftp_host}"
  sitelog_ftp_username     = "${var.sitelog_ftp_username}"
  sitelog_ftp_password_key = "${var.sitelog_ftp_password_key}"
  parameter_store_role_arn = "${var.parameter_store_role_arn}"
  environment  = "${var.environment}"
  application  = "${var.application}"
  owner        = "${var.owner}"
}
 
