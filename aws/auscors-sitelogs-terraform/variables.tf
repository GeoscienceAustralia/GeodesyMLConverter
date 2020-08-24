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

variable "credstash_role_arn" {
  description = "Credstash role to lookup Oauth2 credentials"
  default     = "arn:aws:iam::094928090547:role/CredstashReader"
}

variable "oauth2_url" {
  description = "Geodesy Web Services Oauth2 provider URL."
}

variable "gws_url" {
  description = "Geodesy Web Services URL for Lambda to retrieve GeodesyML from."
  default     = "https://dev.geodesy.ga.gov.au"
}

variable "gws_oidc_client_id_key" {
  description = "Credstash key for Geodesy Web Services OpenId Connect client id."
  default     = "GwsSystemUser"
}

variable "gws_oidc_client_password_key" {
  description = "Credstash key for Geodesy Web Services OpenId Connect client password."
}

variable "gws_system_user_key" {
  description = "Credstash key for Geodesy Web Services system user name."
  default     = "GwsSystemUser"
}

variable "gws_system_user_password_key" {
  description = "Credstash key for Geodesy Web Services system user name."
}

variable "read_only_user_arns" {
  description = "ARN for user with cross account access to bucket - for accessesing with service role at GA."
  type = "list"
}

variable "submitter_arns" {
  description = "ARNs for users who can submit text site logs to the incoming bucket"
  type = "list"
  default = ["arn:aws:iam::688660191997:root"]
}
