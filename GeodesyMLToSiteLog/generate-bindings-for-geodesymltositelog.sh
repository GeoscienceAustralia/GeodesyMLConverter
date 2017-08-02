#!/usr/bin/env bash

set -e
PYTHON_PREFIX=${BASH_SOURCE%/*}/..
PYXBGEN=${PYTHON_PREFIX}/pyxbgen

${PYXBGEN} -u "${PYTHON_PREFIX}/GeodesyML/schemas/geodesyML.xsd" \
	-m geodesymltositelog_bindings \
	--archive-path "${PYTHON_PREFIX}"/pyxb/bundles/common/raw/:"${PYTHON_PREFIX}"/pyxb/bundles/opengis/raw/:.:+
