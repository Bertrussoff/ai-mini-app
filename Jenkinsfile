pipeline {
    agent any

    environment {
        IMAGE_NAME = "ai-mini-app:${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Bertrussoff/ai-mini-app.git'
            }
        }

        stage('Build Docker Image (Inside Minikube)') {
            steps {
                sh '''
                echo "Switching to Minikube Docker..."
                eval $(minikube docker-env)

                echo "Building image: $IMAGE_NAME"
                docker build -t $IMAGE_NAME -f docker/Dockerfile .
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                echo "Updating deployment with new image..."

                sed -i "s|image: ai-mini-app:.*|image: $IMAGE_NAME|g" k8s/deployment.yaml

                kubectl apply -f k8s/
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl rollout status deployment ai-app
                kubectl get pods -o wide
                '''
            }
        }
    }
}
