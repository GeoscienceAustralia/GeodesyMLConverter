#!/usr/bin/env bash

set -e

cd "$HOME"

if [ -z "$(ls -A terraform)" ]; then
    curl -fSL "https://releases.hashicorp.com/terraform/0.10.5/terraform_0.10.5_linux_amd64.zip" -o terraform.zip
    unzip terraform.zip -d terraform
    rm -f terraform.zip
fi
