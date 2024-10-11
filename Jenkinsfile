pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub_creds') // Use your Jenkins credentials ID
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Umed24/DEVOPS_Worksync.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    // Build backend Docker image
                    sh 'docker build -t your-dockerhub-username/worksync-backend ./backend'

                    // Build frontend Docker image
                    sh 'docker build -t your-dockerhub-username/worksync-frontend ./frontend'
                }
            }
        }

        stage('Push Docker Images to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub using Jenkins credentials
                    sh """
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker push your-dockerhub-username/worksync-backend
                    docker push your-dockerhub-username/worksync-frontend
                    """
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
