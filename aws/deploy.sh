#!/usr/bin/env bash

set -e
environment=$1
terraform_state=$2

cd auscors-sitelogs-terraform/
./modules/lambda/create-deployment-package.sh

terraform init \
	-backend-config "bucket=${terraform_state}" \
	-backend-config "lock_table=${terraform_state}" \
	-backend-config "region=ap-southeast-2" \
	-backend-config "key=auscors-sitelogs/${environment}/terraform.tfstate"

terraform get
terraform plan -var-file=$environment.tfvars
terraform apply -var-file=$environment.tfvars
