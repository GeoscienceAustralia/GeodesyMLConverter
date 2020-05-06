#!/usr/bin/env bash

set -e

pytest

cd aws/

if [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
    dryRun="--dry-run"
fi

export AWS_DEFAULT_REGION=ap-southeast-2

case "${TRAVIS_BRANCH}" in
    "test")
        ./deploy.sh --env test $dryRun
    ;;
    "prod")
        export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID_PROD
        export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY_PROD
        ./deploy.sh --env prod $dryRun
    ;;
    *)
        ./deploy.sh --env dev $dryRun
    ;;
esac
