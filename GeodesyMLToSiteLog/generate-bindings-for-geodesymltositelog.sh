#!/usr/bin/env bash

set -e
PYTHON_PREFIX=.

${PYTHON_PREFIX}/pyxbgen -u ../GeodesyML/schemas/geodesyML.xsd \
	-m geodesymltositelog_bindings \
	--archive-path "${PYTHON_PREFIX}"/pyxb/bundles/common/raw/:"${PYTHON_PREFIX}"/pyxb/bundles/opengis/raw/:.:+
