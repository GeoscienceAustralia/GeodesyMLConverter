#!/usr/bin/env bash

set -e
export TF_VAR_environment=$1
export TF_VAR_tf_state_bucket=$2
export TF_VAR_tf_state_table=$2

cd auscors-sitelogs-terraform/
./modules/lambda/create-deployment-package.sh

terraform init \
    -backend-config "bucket=${TF_VAR_tf_state_bucket}" \
    -backend-config "lock_table=${TF_VAR_tf_state_table}" \
    -backend-config "region=ap-southeast-2" \
    -backend-config "key=auscors-sitelogs/${TF_VAR_environment}/terraform.tfstate"

terraform get
terraform plan -var-file=$TF_VAR_environment.tfvars
terraform apply -var-file=$TF_VAR_environment.tfvars
