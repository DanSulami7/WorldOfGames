pipeline {
    agent any

//     environment {
//         // Define any environment variables needed
//         DATABASE_URL = 'your_database_url'
//         API_KEY = 'your_api_key'
//     }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git 'https://github.com/DanSulami7/WorldOfGames.git'
            }
        }

        stage('Build') {
            steps {
                // Build the project, e.g., for a Node.js project
                sh 'npm install'
                sh 'npm run build'
            }
        }

        stage('Test') {
            steps {
                // Run tests
                sh 'npm test'
            }
//             post {
//                 always {
//                     // Archive test results
//                     junit 'reports/**/*.xml'
//                 }
//             }
        }

        stage('Docker Build') {
            steps {
                // Build Docker image
                sh 'docker build -t My_image_name .'
            }
        }

//         stage('Deploy') {
//             steps {
//                 // Deploy the Docker container
//                 sh 'docker run -d -e DATABASE_URL=$DATABASE_URL -e API_KEY=$API_KEY your_image_name'
//             }
        }
    }
}
