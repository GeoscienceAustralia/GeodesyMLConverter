# AWS Variables
variable "region" {
  default = "ap-southeast-2"
}

#Tags
variable "application" {}
variable "owner" {}
variable "environment" {}

variable "read_only_user_arns" {
  type = list(string)
}

variable "submitter_arns" {
  type = list(string)
}
