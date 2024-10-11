pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DOCKERHUB_CREDENTIALS') // Make sure 'DOCKERHUB_CREDENTIALS' is set up in Jenkins
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

        stage('Build Backend Docker Image') {
            steps {
                script {
                    bat 'docker build -t "umed24/backend:latest" -f backend/Dockerfile ./backend'
                }
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                script {
                    bat 'docker build -t "umed24/frontend:latest" -f frontend/Dockerfile ./frontend'
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

        stage('Push Backend Docker Image to DockerHub') {
            steps {
                script {
                    bat 'docker push umed24/backend:latest'
                }
            }
        }

        stage('Push Frontend Docker Image to DockerHub') {
            steps {
                script {
                    bat 'docker push umed24/frontend:latest'
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
                // Place cleanWs inside a node block
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
