#!/usr/bin/env bash

scriptDir=$(readlink -f "${BASH_SOURCE[0]%/*}")
sourceDir=$(readlink -f "$scriptDir"/../../../..)

if [ "$VIRTUAL_ENV" == "" ]; then
    virtualenv "$sourceDir"/python2-env
    . "$sourceDir"/python2-env/bin/activate
    (cd "$sourceDir" && pip install -r requirements.txt)
    (cd "$sourceDir" && pip install .)
fi

pip install requests lambda-packages cryptography==2.7 credstash==1.16.1

sitePackages=$(pip show requests | grep ^Location: | cut -f2 -d: | sed 's/^ //')

(cd "$sitePackages" && zip "$scriptDir"/ingest_text_site_log_lambda.zip -r \
    requests \
    credstash.py \
    ipaddress.py \
    asn1crypto \
    enum \
    chardet \
    idna \
    certifi \
    urllib3 \
    pyxb \
    iso3166 \
    SiteLogToGeodesyML)

tar -xzvf "$sitePackages"/lambda_packages/cryptography/python2.7-cryptography-1.9.tar.gz
tar -xzvf "$sitePackages"/lambda_packages/cffi/python2.7-cffi-1.7.0.tar.gz

zip "$scriptDir"/ingest_text_site_log_lambda.zip -r \
    cryptography \
    cffi \
    _cffi_backend.so

(cd "$scriptDir" && zip ingest_text_site_log_lambda.zip -r ingest_text_site_log_lambda.py)
