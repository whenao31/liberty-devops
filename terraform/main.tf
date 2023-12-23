resource "null_resource" "run_local_infra" {

    provisioner "local-exec" {
    command = <<-EOT
      cd ..
      docker-compose up --force-recreate --build -d
      docker image prune -f
      docker-compose -f compose.yaml up -d 
    EOT
  }
  
}

resource "null_resource" "run_sonarqube" {

    provisioner "local-exec" {
    command = <<-EOT
      cd ../sonarqube
      docker-compose up --force-recreate --build -d
      docker image prune -f
      docker-compose -f compose.yml up -d 
    EOT
  }
  
}