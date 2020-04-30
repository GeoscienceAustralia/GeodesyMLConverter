#!/usr/bin/env bash

set -e

pytest

cd aws/

if [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
    dryRun="--dry-run"
fi

case "${TRAVIS_BRANCH}" in
    "next")
        aws configure set aws_access_key_id "${AWS_ACCESS_KEY_ID}"
        aws configure set aws_secret_access_key "${AWS_SECRET_ACCESS_KEY}"
        aws configure set region ap-southeast-2
        ./deploy.sh --env dev $dryRun
    ;;
    "master")
        aws configure set aws_access_key_id "${AWS_ACCESS_KEY_ID}"
        aws configure set aws_secret_access_key "${AWS_SECRET_ACCESS_KEY}"
        aws configure set region ap-southeast-2
        ./deploy.sh --env test $dryRun
    ;;
    "prod")
        aws configure set aws_access_key_id "${AWS_ACCESS_KEY_ID_PROD}"
        aws configure set aws_secret_access_key "${AWS_SECRET_ACCESS_KEY_PROD}"
        aws configure set region ap-southeast-2
        ./deploy.sh --env prod $dryRun
    ;;
esac
