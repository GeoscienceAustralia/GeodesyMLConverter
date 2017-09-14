#!/usr/bin/env bash

if [ ! -e /opt/terraform ]; then
    curl -fSL "https://releases.hashicorp.com/terraform/0.6.15/terraform_0.6.15_linux_amd64.zip" -o terraform.zip
    sudo unzip terraform.zip -d /opt/terraform
    rm -f terraform.zip
fi
sudo ln -s /opt/terraform/terraform /usr/bin/terraform
