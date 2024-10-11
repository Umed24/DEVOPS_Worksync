pipeline {
    agent any

    environment {
        // Define the DockerHub credentials and GitHub credentials
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub_creds') // Replace with your actual credentials ID for DockerHub
        GITHUB_CREDENTIALS = credentials('github-creds') // Replace with your GitHub credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from the correct branch
                    git branch: 'master', // Use 'main' if your default branch is 'main'
                        url: 'https://github.com/Umed24/DEVOPS_Worksync.git',
                        credentialsId: GITHUB_CREDENTIALS
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
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        def backendImage = docker.image("umed24/backend:latest")
                        backendImage.push() // Push the backend image to DockerHub
                    }
                }
            }
        }

        stage('Push Frontend Docker Image to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        def frontendImage = docker.image("umed24/frontend:latest")
                        frontendImage.push() // Push the frontend image to DockerHub
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
