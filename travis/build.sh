#!/usr/bin/env bash

set -e

pytest

cd aws/

if [ "${TRAVIS_PULL_REQUEST}" = "false" ]; then
	aws configure set aws_access_key_id "${TRAVIS_AWS_ACCESS_KEY_ID}" --profile geodesy
	aws configure set aws_secret_access_key "${TRAVIS_AWS_SECRET_KEY_ID}" --profile geodesy
	aws configure set region ap-southeast-2 --profile geodesy
	case "${TRAVIS_BRANCH}" in
		"next")
			./deploy.sh dev auscors-terraform-state-dev
		;;
		"master")
			./deploy.sh test auscors-terraform-state-dev
		;;
	esac
fi
