#!/usr/bin/env bash

scriptDir=$(readlink -f "${BASH_SOURCE[0]%/*}")
sourceDir=$(readlink -f "$scriptDir"/../../../..)

if [ "$VIRTUAL_ENV" == "" ]; then
    virtualenv "$sourceDir"/python2-env
    . "$sourceDir"/python2-env/bin/activate
    (cd "$sourceDir" && pip install -r requirements.txt)
    (cd "$sourceDir" && pip install .)
fi

pip install requests

sitePackages=$(pip show requests | grep ^Location: | cut -f2 -d: | sed 's/^ //')

(cd "$sitePackages" && zip "$scriptDir"/fetch_site_logs_from_ftp_sites_lambda.zip -r \
    requests \
    chardet \
    certifi \
    idna \
    urllib3)

(cd "$sourceDir" && zip "$scriptDir"/fetch_site_logs_from_ftp_sites_lambda.zip fetch_site_logs_from_ftp_sites.py)
