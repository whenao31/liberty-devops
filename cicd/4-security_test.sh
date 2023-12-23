SONARQUBE_URL=$1
YOUR_PROJECT_KEY=$2
SONAR_AUTH_TOKEN=$3

cd ..
docker run \
    --rm \
    -e SONAR_HOST_URL="http://${SONARQUBE_URL}" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=${YOUR_PROJECT_KEY}" \
    -e SONAR_TOKEN=${SONAR_AUTH_TOKEN} \
    -v "./backend:/usr/src" \
    --network=host \
    sonarsource/sonar-scanner-cli

