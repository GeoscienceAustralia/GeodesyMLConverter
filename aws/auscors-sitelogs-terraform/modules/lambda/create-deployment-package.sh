#!/usr/bin/env bash

scriptDir=$(readlink -f "${BASH_SOURCE[0]%/*}")
sourceDir=$(readlink -f "$scriptDir"/../../../..)

virtualenv "$scriptDir"/python2-env
. "$scriptDir"/python2-env/bin/activate

(cd "$sourceDir" && pip install -r requirements.txt)
(cd "$sourceDir" && pip install . --upgrade)

sitePackages=$(pip show pyxb | grep ^Location: | cut -f2 -d: | sed 's/^ //')

(cd "$sitePackages" && zip "$scriptDir"/geodesymltositelog_lambda.zip -r \
    pyxb \
    iso3166 \
    GeodesyMLToSiteLog)

(cd "$scriptDir" && zip geodesymltositelog_lambda.zip -r geodesymltositelog_lambda.py)
