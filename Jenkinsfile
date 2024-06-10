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
                sh 'docker build -t world_of_games_image .'
            }
        }
        stage('Test and Run') {
            parallel {
                stage('Run Container') {
                    steps {
                        sh 'docker run -d -p 8777:5001 --name wog_container world_of_games_image'
                    }
                }
                stage('Run Tests') {
                    steps {
                        sh 'python Tests/e2e.py'
                    }
                    post {
                        always {
                            sh 'docker stop wog_container'
                        }
                    }
                }
            }
        }
        stage('Push') {
            steps {
                sh 'docker tag world_of_games_image DanSulami7/world_of_games'
                sh 'docker push DanSulami7/world_of_games'
            }
        }
    }
}
