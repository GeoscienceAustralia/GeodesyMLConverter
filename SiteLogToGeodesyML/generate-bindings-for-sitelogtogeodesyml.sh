#!/usr/bin/env bash

set -e
PYTHON_PREFIX=.
PYXBGEN=${PYTHON_PREFIX}/pyxbgen

${PYXBGEN} -u ../modified-schemas/geodesyML.xsd \
	-m sitelogtogeodesyml \
	--archive-path "${PYTHON_PREFIX}"/pyxb/bundles/common/raw/:"${PYTHON_PREFIX}"/pyxb/bundles/opengis/raw/:.:+
