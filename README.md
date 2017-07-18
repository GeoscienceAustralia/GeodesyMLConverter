# GMLConverter
Tools for converting between Geodesy XML Site Log and Text Site Log formats

## Deployment

```bash
cd GeodesyMLToSiteLog/lambda_package
zip xml_converter_lambda.zip -r xml_converter_lambda.py xml2log.py xml2log_bindings.py pyxb/ iso3166/
mv xml_converter_lambda.zip ../terraform/modules/lambda/

cd ../terraform

terraform init \
	-backend-config "bucket=auscors-terraform-state-dev" \
	-backend-config "lock_table=auscors-terraform-state-dev" \
	-backend-config "region=ap-southeast-2" \
	-backend-config "key=auscors-sitelogs/dev"

terraform get
terraform plan
terraform apply
```
