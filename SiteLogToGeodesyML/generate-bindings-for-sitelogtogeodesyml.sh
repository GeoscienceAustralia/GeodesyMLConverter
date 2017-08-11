#!/usr/bin/env bash

set -e

scriptDir=${BASH_SOURCE%/*}
pyxb=$(pip show pyxb | grep ^Location: | cut -f2 -d: | sed 's/^ //')/pyxb

pyxbgen -u "$scriptDir/modified-schemas/geodesyML.xsd" \
	-m sitelogtogeodesyml_bindings \
	--archive-path "$pyxb"/bundles/common/raw/:"$pyxb"/bundles/opengis/raw/:.:+

