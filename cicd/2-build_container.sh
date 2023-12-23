pipeline_id=$1

echo "Building containers ..."
cd ../frontend
docker build -t "frontend-${pipeline_id}" .
cd ../backend
docker build -t "backend-${pipeline_id}" .
echo "Container image building done"