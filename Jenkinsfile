pipeline {
    agent any
    environment {
        GITHUB_CREDENTIALS = credentials('github-creds')  // GitHub credentials
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub_creds')  // DockerHub credentials
        DOCKER_IMAGE = 'umed24/worksync'  // DockerHub repository
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from GitHub
                git url: 'https://github.com/Umed24/DEVOPS_Worksync.git',
                    credentialsId: GITHUB_CREDENTIALS,
                    branch: 'main'  // Use your main branch here
            }
        }
        stage('Build Backend Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}_backend", "-f backend/Dockerfile .")
                }
            }
        }
        stage('Build Frontend Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}_frontend", "-f frontend/Dockerfile .")
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        docker.image("${DOCKER_IMAGE}_backend").push()
                        docker.image("${DOCKER_IMAGE}_frontend").push()
                    }
                }
            }
        }
    }
}
