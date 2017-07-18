#!/usr/bin/env bash

set -e
pip download pyxb
tar -xzvf PyXB-1.2.5.tar.gz
rm PyXB-1.2.5.tar.gz
cd PyXB-1.2.5 || exit
export PYXB_ROOT
PYXB_ROOT=$(pwd)
./pyxb/bundles/opengis/scripts/genbind
python setup.py install --prefix=.
mv lib/python2.7/site-packages/pyxb ../
mv bin/pyxbgen ../
cd ..
rm -rf PyXB-1.2.5
