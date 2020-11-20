environment="prod"
read_only_user_arns=[
  "arn:aws:iam::688660191997:user/svc_fetch_geodesyml_sitelogs",
  "arn:aws:iam::621723668284:root",
  "arn:aws:iam::604917042985:root",
  "arn:aws:iam::434115853596:root"
]
sns_arn="arn:aws:sns:ap-southeast-2:094928090547:ProdGeodesy-SiteLogReceived-H4450D6513IG"
gws_oidc_client_id_key="GwsOidcClientId"
gws_oidc_client_password_key="ProdGwsOidcClientPassword"
gws_system_user_id_key="GwsSystemUser"
gws_system_user_password_key="ProdGwsSystemUserPassword"
oauth2_url="https://prodgeodesy-openam.geodesy.ga.gov.au/openam/oauth2"
gws_url="https://gws.geodesy.ga.gov.au"
ftp_sitelogs = true
sitelog_ftp_host = "ftp.ga.gov.au"
sitelog_ftp_username = "ftptrans2"
sitelog_ftp_password_key = "/ftp-ga-gov-au/user/ftptrans2/password"
parameter_store_role_arn = "arn:aws:iam::334594953176:role/parameter-store-prod-read-only"
