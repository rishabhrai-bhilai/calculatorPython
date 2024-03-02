pipeline {
    agent any

    environment {
        DOCKER_USERNAME = credentials('rishabh8797')
    }
    
    stages {
        stage('Clone from GitHub') {
            steps {
                script {
                    // Define your GitHub repository URL
                    def gitRepoUrl = 'https://github.com/rishabhrai-bhilai/calculatorPython.git'

                    // Define the branch to clone (e.g., 'main')
                    def gitBranch = 'main'

                    // Clone the repository
                    git branch: gitBranch, url: gitRepoUrl
                }
            }
        }
        
        
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover -s .'  // Run unit tests from the current directory
            }
        }
        
        stage('Containerize') {
            steps {
                sh 'docker build -t calculator-app .'  // Build Docker image
            }
        }
        
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'rishabh8797', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'  // Login to Docker Hub
                    sh 'docker tag calculator-app $DOCKER_USERNAME/calculator-app'  // Tag Docker image
                    sh 'docker push $DOCKER_USERNAME/calculator-app'  // Push Docker image to Docker Hub
                }
            }
        }
        
        
        stage('Deployment with Ansible') {
            steps {
                ansiblePlaybook playbook: 'deploy.yml', inventory: 'hosts', extras: "-e DOCKER_IMAGE=$DOCKER_USERNAME/calculator-app"
            }
        }

        
    }

}

