# AWS Variables
variable "region" {
  default = "ap-southeast-2"
}

variable "dead_letter_queue_arn" {}
variable "bucket_name" {}

#Tags
variable "application" {}
variable "owner" {}
variable "environment" {}
