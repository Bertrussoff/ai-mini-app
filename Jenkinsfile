pipeline {
    agent any

    environment {
        IMAGE_NAME = "ai-mini-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Bertrussoff/ai-mini-app.git'
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

        stage('Load Image into Minikube') {
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
                kubectl apply -f k8s/
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "Checking pods..."
                kubectl get pods
                '''
            }
        }
    }
}