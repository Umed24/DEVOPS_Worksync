pipeline {
    agent any

    environment {
        // Define DockerHub credentials and GitHub credentials
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub-creds') // Replace with your actual credentials ID for DockerHub
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

        stage('Login to DockerHub') {
            steps {
                script {
                    // Login to DockerHub
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                }
            }
        }

        stage('Push Backend Docker Image to DockerHub') {
            steps {
                script {
                    // Push the backend Docker image to DockerHub
                    def backendImage = docker.image("umed24/backend:latest")
                    backendImage.push() // Push the backend image to DockerHub
                }
            }
        }

        stage('Push Frontend Docker Image to DockerHub') {
            steps {
                script {
                    // Push the frontend Docker image to DockerHub
                    def frontendImage = docker.image("umed24/frontend:latest")
                    frontendImage.push() // Push the frontend image to DockerHub
                }
            }
        }

        stage('Logout from DockerHub') {
            steps {
                script {
                    // Logout from DockerHub
                    sh 'docker logout'
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
