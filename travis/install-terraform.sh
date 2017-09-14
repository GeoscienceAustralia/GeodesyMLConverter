#!/usr/bin/env bash

set -e

cd "$HOME"

if [ -z "$(ls -A terraform)" ]; then
    curl -fSL "https://releases.hashicorp.com/terraform/0.6.15/terraform_0.6.15_linux_amd64.zip" -o terraform.zip
    unzip terraform.zip -d terraform
    rm -f terraform.zip
fi
