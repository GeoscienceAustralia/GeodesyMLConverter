variable "region" {
  default = "ap-southeast-2"
}

variable "tf_state_bucket" {
  description = "Name of terraform state S3 bucket."
  default     = "auscors-terraform-state-dev"
}

variable "tf_state_table" {
  description = "Name of terraform state lock DDB table."
  default     = "auscors-terraform-state-dev"
}

variable "environment" {
  description = "Deployment environment. Suffixes most created objects."
  default     = "dev"
}

variable "application" {
  description = "Application name. Used to prefix most created objects, including terraform state file."
  default     = "auscors-sitelogs"
}

variable "owner" {
  description = "Application owner."
  default     = "Geodesy Operations"
}

variable "sns_arn" {
  description = "ARN of SNS topic which converter Lambda is invoked by."
  default     = "arn:aws:sns:ap-southeast-2:094928090547:DevGeodesy-SiteLogReceived-EYB2P4K966EE"
}

variable "gws_url" {
  description = "Geodesy Web Services URL for Lambda to retrieve GeodesyML from."
  default     = "dev.geodesy.ga.gov.au"
}

variable "read_only_user_arn" {
  description = "ARN for user with cross account access to bucket - for accessesing with service role at GA."
  default     = "arn:aws:iam::688660191997:user/svc_fetch_geodesyml_sitelogs"
}
