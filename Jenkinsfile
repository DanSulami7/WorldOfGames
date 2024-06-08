pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/DanSulami7/WorldOfGames.git'
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t my_image_name .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run my_image_name'
            }
        }

         stage('Test') {
            steps {
                sh 'python Tests/e2e.py'
            }
        }
    }
}
