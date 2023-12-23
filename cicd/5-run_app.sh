cd ../terraform

terraform init
terraform plan
terraform apply -target="null_resource.run_local_infra" --auto-approve