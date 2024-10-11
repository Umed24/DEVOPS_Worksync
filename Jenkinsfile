pipeline {
    agent any

    environment {
        // Define DockerHub credentials
        DOCKERHUB_USERNAME = 'umed24' // Replace with your Docker Hub username
        DOCKERHUB_PASSWORD = 'Umedmujawar2@' // Replace with your Docker Hub password
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from the correct branch
                    git branch: 'master', // Use 'main' if your default branch is 'main'
                        url: 'https://github.com/Umed24/DEVOPS_Worksync.git'
                }
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                script {
                    // Build the backend Docker image
                    docker.build("umed24/backend:latest", "-f backend/Dockerfile ./backend")
                }
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                script {
                    // Build the frontend Docker image
                    docker.build("umed24/frontend:latest", "-f frontend/Dockerfile ./frontend")
                }
            }
        }

        stage('Push Backend Docker Image to DockerHub') {
            steps {
                script {
                    echo "Pushing backend Docker image to DockerHub..."
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_USERNAME}:${DOCKERHUB_PASSWORD}") {
                        def backendImage = docker.image("umed24/backend:latest")
                        backendImage.push('latest') // Push the backend image with the latest tag
                    }
                }
            }
        }

        stage('Push Frontend Docker Image to DockerHub') {
            steps {
                script {
                    echo "Pushing frontend Docker image to DockerHub..."
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_USERNAME}:${DOCKERHUB_PASSWORD}") {
                        def frontendImage = docker.image("umed24/frontend:latest")
                        frontendImage.push('latest') // Push the frontend image with the latest tag
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after every build
        }

        success {
            echo 'Build succeeded!'
        }

        failure {
            echo 'Build failed!'
        }
    }
}
