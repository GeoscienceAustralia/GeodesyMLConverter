#!/usr/bin/env bash

set -e

while [[ $# -gt 0 ]]; do
    case $1 in
        -e|--env)
        environment="$2"
        shift
        shift
        ;;
        -s|--state-bucket)
        stateBucket="$2"
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

export TF_VAR_environment=$environment
export TF_VAR_tf_state_bucket=$stateBucket
export TF_VAR_tf_state_table=$stateBucket

cd auscors-sitelogs-terraform/
./modules/lambda/create-deployment-package.sh
./modules/lambda/create-ingest-text-site-log-package.sh
./modules/lambda/create-fetch-site-logs-from-ftp-sites-package.sh

terraform init \
    -backend-config "bucket=${TF_VAR_tf_state_bucket}" \
    -backend-config "lock_table=${TF_VAR_tf_state_table}" \
    -backend-config "region=ap-southeast-2" \
    -backend-config "key=auscors-sitelogs/${TF_VAR_environment}/terraform.tfstate"

terraform get
terraform plan -var-file=$TF_VAR_environment.tfvars

if [ -z "$dryRun" ]; then
    terraform apply -var-file=$TF_VAR_environment.tfvars
fi
