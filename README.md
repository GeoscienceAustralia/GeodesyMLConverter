[![Build Status](https://travis-ci.org/GeoscienceAustralia/GeodesyMLConverter.svg?branch=master)](https://travis-ci.org/GeoscienceAustralia/GeodesyMLConverter)

# GeodesyML Site Log Converter
Command line tools for converting between GeodesyML site log and text site log formats:

* `sitelog-to-geodesyml`
* `geodesyml-to-sitelog`

## Installation

```bash
pip install -r requirements.txt
pip install .
```

## Tests

``` bash
python setup.py build
python setup.py test
```

## Deployment to AWS Lambda

```bash
cd aws/
./deploy {environment} {terraform-state-bucket}
```

