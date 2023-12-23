#!/bin/bash

SONARQUBE_URL=$1
YOUR_PROJECT_KEY=$2
SONAR_AUTH_TOKEN=$3


pipeline_id="$(echo $RANDOM | md5sum | head -c 20; echo;)"

# Make steps scripts files executables
chmod +x 1-gen_docs.sh 2-build_container.sh 3-unit_test.sh 4-security_test.sh 5-run_app.sh 6-destroy_app_infra.sh

option=1
while [[ $option != 7 ]] ; do
cat << "EOF"

"**********************************"
"*      CI/CD PIPELINE            *"

Please ingress the number of the step
to be executed according to these options:

1. Generate documentation HTML
2. Container images building
3. Backend unit test execution
4. SonarQube security test
5. Deploy 3-tier app
6. Destroy App infrastructure
7. Exit

*****************************************
EOF
read option
  case $option in
    1)
      clear
      ./1-gen_docs.sh $pipeline_id
      ;;
    2)
      clear
      ./2-build_container.sh $pipeline_id
      ;;
    3)
      clear
      ./3-unit_test.sh
      ;;
    4)clear
      ./4-security_test.sh $SONARQUBE_URL $YOUR_PROJECT_KEY $SONAR_AUTH_TOKEN
      ;;
    5)clear
      ./5-run_app.sh
      ;;
    6)clear
      ./6-destroy_app_infra.sh
      ;;
    7)
      echo "See ya ;)"
      ;;
    *)
      echo "Not a valid option :("
      ;;
  esac
done

