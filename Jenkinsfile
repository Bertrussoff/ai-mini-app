pipeline {
    agent any

    environment {
        IMAGE_NAME = "ai-mini-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/YOUR_USERNAME/ai-mini-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                eval $(minikube docker-env)
                docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/
                '''
            }
        }
    }
}
