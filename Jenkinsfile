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
                    bat 'docker run -p 8777:5001 --name wog_container world_of_games_image'
                },
                test: {
                    bat 'python tests/e2e.py'
                    bat 'docker stop wog_container'
                }
            )
        }
        stage('Push'){
            bat 'docker tag world_of_games_image shanimarco/world_of_games'
            bat 'docker push shanimarco/world_of_games'
        }
    }
}