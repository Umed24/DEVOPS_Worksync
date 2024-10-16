pipeline {
    agent any

    environment {
        // Use the correct DockerHub credential ID from your Jenkins (Dockerhub-creds)
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub-creds') 
        AWS_ACCESS_KEYS = credentials('AWS_ACCESS_KEYS')  // AWS credentials
    }

    triggers {
        githubPush()  // Automatically triggers the pipeline when a push is made to the GitHub repo
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'master',
                        url: 'https://github.com/Umed24/DEVOPS_Worksync.git'
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
                        bat '''
                        docker login -u %DOCKERHUB_USER% -p %DOCKERHUB_PASSWORD%
                        '''
                    }
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    // Push the worksync:01 image to DockerHub
                    bat 'docker push umed24/worksync:01'
                }
            }
        }

        stage('Terraform Init') {
            steps {
                script {
                    // Set AWS credentials for Terraform
                    def awsAccessKey = AWS_ACCESS_KEYS.accessKeyId
                    def awsSecretKey = AWS_ACCESS_KEYS.secretAccessKey

                    // Set AWS environment variables for Terraform
                    bat """
                    set AWS_ACCESS_KEY_ID=${awsAccessKey}
                    set AWS_SECRET_ACCESS_KEY=${awsSecretKey}
                    terraform init
                    """
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                script {
                    // Show Terraform changes
                    bat 'terraform plan'  // Using bat for Windows compatibility
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                script {
                    // Apply Terraform changes
                    bat 'terraform apply -auto-approve'  // Using bat for Windows compatibility
                }
            }
        }

        stage('Logout from DockerHub') {
            steps {
                script {
                    bat 'docker logout'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean the workspace after the pipeline run
                node {
                    cleanWs()
                }
            }
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
