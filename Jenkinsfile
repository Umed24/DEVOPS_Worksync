pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub-creds')
        AWS_CREDENTIALS = credentials('aws-creds')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Ensure Docker is installed and available in the PATH
                    def dockerImage = "umed24/worksync:01"

                    // Build the Docker image
                    sh """
                    docker build -t ${dockerImage} .
                    """
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    // Login to Docker Hub
                    sh """
                    echo "${DOCKER_CREDENTIALS_PSW}" | docker login -u "${DOCKER_CREDENTIALS}" --password-stdin
                    """
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    sh """
                    docker push ${dockerImage}
                    """
                }
            }
        }

        stage('Terraform Init') {
            steps {
                script {
                    // Initialize Terraform
                    sh """
                    terraform init
                    """
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                script {
                    // Plan Terraform deployment
                    sh """
                    terraform plan
                    """
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                script {
                    // Apply Terraform configuration
                    sh """
                    terraform apply -auto-approve
                    """
                }
            }
        }
    }

    post {
        always {
            // Logout from DockerHub
            script {
                sh """
                docker logout
                """
            }
            // Clean up workspace
            cleanWs()
        }
        failure {
            // Actions to take on failure
            echo 'Build failed!'
        }
    }
}
