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
        stage('Test') {
            parallel(
                run: {
                    sh 'docker run -p 8777:5001 --name wog_container world_of_games_image'
                },
                test: {
                    sh 'python tests/e2e.py'
                    sh 'docker stop wog_container'
                }
            )
        }
        stage('Push'){
            sh 'docker tag world_of_games_image shanimarco/world_of_games'
            sh 'docker push shanimarco/world_of_games'
        }
    }
}