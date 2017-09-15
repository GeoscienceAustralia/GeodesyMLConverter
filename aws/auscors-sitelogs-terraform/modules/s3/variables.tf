# AWS Variables
variable "region" {
  default = "ap-southeast-2"
}

#Tags
variable "application" {}
variable "owner" {}
variable "environment" {}

variable "read_only_user_arn" {}
