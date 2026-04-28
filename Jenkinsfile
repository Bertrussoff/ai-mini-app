pipeline {
    agent any

    environment {
        IMAGE_NAME = "ai-mini-app"
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
                docker build -t ai-mini-app -f docker/Dockerfile .
                '''
            }
        }

        stage('Load Image to Minikube') {
            steps {
                sh '''
                echo "Loading image into Minikube..."
                minikube image load ai-mini-app
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
                kubectl get pods
                '''
            }
        }
    }
}
