pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub-creds')  // DockerHub credentials ID in Jenkins
        AWS_ACCESS_KEYS = credentials('AWS_ACCESS_KEYS')         // AWS credentials ID in Jenkins
    }

    triggers {
        githubPush()  // Automatically triggers the pipeline on a GitHub push
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
                    sh 'docker build -t umed24/worksync:01 .'  // Build Docker image
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'Dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        sh 'docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD'
                    }
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    sh 'docker push umed24/worksync:01'
                }
            }
        }

        stage('Terraform Init') {
            steps {
                script {
                    sh 'terraform init'  // Initialize Terraform
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                script {
                    sh 'terraform plan'  // Show Terraform changes
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                script {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS_ACCESS_KEYS']]) {
                        sh 'terraform apply -auto-approve'  // Apply Terraform changes
                    }
                }
            }
        }

        stage('Logout from DockerHub') {
            steps {
                script {
                    sh 'docker logout'
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean workspace
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
