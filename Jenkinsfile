pipeline {
    agent any

    environment {
        // Use the correct DockerHub credential ID from your Jenkins
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub-creds')
        AWS_ACCESS_KEYS = credentials('AWS_ACCESS_KEYS')  // AWS credentials
    }

    triggers {
        githubPush()  // Automatically triggers the pipeline on a push to the GitHub repo
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from the GitHub repository
                    git branch: 'master', url: 'https://github.com/Umed24/DEVOPS_Worksync.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with the tag worksync:01
                    bat 'docker build -t "umed24/worksync:01" .'
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'Dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        // Login to Docker Hub
                        bat 'docker login -u %DOCKERHUB_USER% -p %DOCKERHUB_PASSWORD%'
                    }
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    // Push the worksync:01 image to Docker Hub
                    bat 'docker push umed24/worksync:01'
                }
            }
        }

        stage('Terraform Init') {
            steps {
                script {
                    // Initialize Terraform
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                script {
                    // Plan Terraform changes
                    sh 'terraform plan'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS_ACCESS_KEYS']]) {
                    script {
                        // Apply Terraform changes
                        sh 'terraform apply -auto-approve'
                    }
                }
            }
        }

        stage('Logout from DockerHub') {
            steps {
                script {
                    // Logout from Docker Hub
                    bat 'docker logout'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean the workspace after the pipeline run
                cleanWs()
            }
        }
        failure {
            script {
                // Handle failure (e.g., notify team, rollback)
                echo 'Build failed!'
            }
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
