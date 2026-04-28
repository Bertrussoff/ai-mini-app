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

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t $IMAGE_NAME -f docker/Dockerfile .
                '''
            }
        }

        stage('Load Image to Minikube') {
            steps {
                sh '''
                echo "Loading image into Minikube..."
                minikube image load $IMAGE_NAME
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                echo "Deploying to Kubernetes..."
                sed -i "s|image: ai-mini-app:.*|image: $IMAGE_NAME|g" k8s/deployment.yaml
                kubectl apply -f k8s/
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl get pods
                '''
            }
        }
    }
}
