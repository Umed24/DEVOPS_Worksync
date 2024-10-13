pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub-creds') // Ensure the 'DOCKERHUB_CREDENTIALS' is configured in Jenkins
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
                    withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_CREDENTIALS', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
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
