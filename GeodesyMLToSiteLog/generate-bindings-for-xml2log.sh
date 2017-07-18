#!/usr/bin/env bash

set -e
PYTHON_PREFIX=${HOME}/.local
PYXBGEN=${PYTHON_PREFIX}/bin/pyxbgen

wget https://raw.githubusercontent.com/GeoscienceAustralia/GeodesyML/master/schemas/geodesyML.xsd
${PYXBGEN} -u geodesyML.xsd -m xml2log_bindings --archive-path "${PYTHON_PREFIX}"/lib/python2.7/site-packages/pyxb/bundles/common/raw/:"${PYTHON_PREFIX}"/lib/python2.7/site-packages/pyxb/bundles/opengis/raw/:.:+
