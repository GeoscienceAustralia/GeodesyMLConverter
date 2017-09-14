#!/usr/bin/env bash

scriptDir=$(readlink -f "${BASH_SOURCE[0]%/*}")
sourceDir=$(readlink -f "$scriptDir"/../../../..)

echo "****************"
echo $scriptDir
echo $sourceDir

virtualenv "$sourceDir"/python2-env

echo "activate*******"
head "$scriptDir"/python2-env/bin/activate

echo "pip*******"
head "$scriptDir"/python2-env/bin/activate
head "$scriptDir"/python2-env/bin/pip


. "$scriptDir"/python2-env/bin/activate

echo "&&&&&&&&&&"

(cd "$sourceDir" && pip install -r requirements.txt)
(cd "$sourceDir" && pip install . --upgrade)

sitePackages=$(pip show pyxb | grep ^Location: | cut -f2 -d: | sed 's/^ //')

(cd "$sitePackages" && zip "$scriptDir"/geodesymltositelog_lambda.zip -r \
    pyxb \
    iso3166 \
    GeodesyMLToSiteLog)

(cd "$scriptDir" && zip geodesymltositelog_lambda.zip -r geodesymltositelog_lambda.py)
