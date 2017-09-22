variable "region" {
  default = "ap-southeast-2"
}

variable "incoming_bucket_name" {}
variable "incoming_bucket_arn" {}
variable "bucket_name" {}
variable "sns_arn" {}
variable "credstash_role_arn" {}
variable "gws_oidc_client_id_key" {}
variable "gws_oidc_client_password_key" {}
variable "gws_system_user_key" {}
variable "gws_system_user_password_key" {}
variable "oauth2_url" {}
variable "gws_url" {}

variable "application" {}
variable "environment" {}
variable "owner" {}
