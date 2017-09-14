#!/usr/bin/env bash

# if [ ! -e terraform ]; then
curl -fSL "https://releases.hashicorp.com/terraform/0.6.15/terraform_0.6.15_linux_amd64.zip" -o terraform.zip
sudo unzip terraform.zip -d terraform
rm -f terraform.zip
# fi
