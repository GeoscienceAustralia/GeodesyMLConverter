#!/usr/bin/env bash

set -e
PYTHON_PREFIX=${BASH_SOURCE%/*}/..
PYXBGEN=${PYTHON_PREFIX}/pyxbgen

${PYXBGEN} -u "${PYTHON_PREFIX}/modified-schemas/geodesyML.xsd" \
    -m sitelogtogeodesyml_bindings \
	--archive-path "${PYTHON_PREFIX}"/pyxb/bundles/common/raw/:"${PYTHON_PREFIX}"/pyxb/bundles/opengis/raw/:.:+
