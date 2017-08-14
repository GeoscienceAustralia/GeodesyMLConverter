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
pip install -r requirements-dev.txt
python setup.py test
```

## Deployment to AWS Lambda

```bash
cd ../aws/auscors-sitelogs-terraform
./modules/lambda/create-deployment-package.sh

terraform init \
	-backend-config "bucket=auscors-terraform-state-dev" \
	-backend-config "lock_table=auscors-terraform-state-dev" \
	-backend-config "region=ap-southeast-2" \
	-backend-config "key=auscors-sitelogs/dev"

terraform get
terraform plan
terraform apply
```
