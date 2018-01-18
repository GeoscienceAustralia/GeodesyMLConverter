#!/usr/bin/env bash

set -e

while [[ $# -gt 0 ]]; do
    case $1 in
        -e|--env)
        environment="$2"
        shift
        shift
        ;;
        --dry-run)
        dryRun=true
        shift
        ;;
        *)
        shift
        ;;
    esac
done

export TF_VAR_application=auscors-sitelogs
export TF_VAR_environment=${environment:-dev}
export TF_VAR_tf_state_bucket=geodesy-ops-terraform-state-$TF_VAR_environment
export TF_VAR_tf_state_table=terraform-state-lock

cd auscors-sitelogs-terraform/
./modules/lambda/create-deployment-package.sh
./modules/lambda/create-ingest-text-site-log-package.sh
./modules/lambda/create-fetch-site-logs-from-ftp-sites-package.sh

terraform init \
    -backend-config "bucket=${TF_VAR_tf_state_bucket}" \
    -backend-config "lock_table=${TF_VAR_tf_state_table}" \
    -backend-config "region=ap-southeast-2" \
    -backend-config "key=$TF_VAR_application/terraform.tfstate"

terraform get
yes yes | terraform plan -var-file="$TF_VAR_environment".tfvars

if [ -z "$dryRun" ]; then
    yes yes | terraform apply -var-file="$TF_VAR_environment".tfvars
fi
