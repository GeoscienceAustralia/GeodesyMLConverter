# GMLConverter
Tools for converting between Geodesy XML Site Log and Text Site Log formats

## Deployment

Deploying GeodesyMLToSiteLog to Lambda using terraform.

```bash
./install-pyxb.sh
pip install iso3166 --target=.

cd GeodesyMLToSiteLog

./generate-bindings-for-geodesymltositelog.sh

zip geodesymltositelog_lambda.zip -r \
	geodesymltositelog_lambda.py geodesymltositelog.py \
	geodesymltositelog_bindings.py ../pyxb/ \
	../iso3166/

mv geodesymltositelog_lambda.zip ../aws/auscors-sitelogs-terraform/modules/lambda/

cd ../aws/auscors-sitelogs-terraform

terraform init \
	-backend-config "bucket=auscors-terraform-state-dev" \
	-backend-config "lock_table=auscors-terraform-state-dev" \
	-backend-config "region=ap-southeast-2" \
	-backend-config "key=auscors-sitelogs/dev"

terraform get
terraform plan
terraform apply
```
