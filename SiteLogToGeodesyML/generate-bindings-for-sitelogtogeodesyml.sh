#!/usr/bin/env bash

set -e

SCRIPT_DIR=${BASH_SOURCE%/*}
PYTHON_PREFIX=${SCRIPT_DIR}/..

PYXBGEN=${PYTHON_PREFIX}/pyxbgen

${PYXBGEN} -u "${SCRIPT_DIR}/modified-schemas/geodesyML.xsd" \
    -m sitelogtogeodesyml_bindings \
	--archive-path "${PYTHON_PREFIX}"/pyxb/bundles/common/raw/:"${PYTHON_PREFIX}"/pyxb/bundles/opengis/raw/:.:+
