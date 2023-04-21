Steps:

1. Create a bigtable instance in your GCP project.
2. Build the docker image: docker build -t <tag> .
3. Push the docker image to your repository: docker push <>..
4. Create the deployment in your kubernetes cluster: kubectl create -f deployment.yaml
5. Login to the pod: kubectl exec -ti <> -- sh
6. Run the app using: go run app.go -project <project-id> -instance <bigtable-instance-id>
  
  
NOTE: In the deployment.yaml(line: 17, 20), Ensure to set the values of KSA and image as per your environment.
