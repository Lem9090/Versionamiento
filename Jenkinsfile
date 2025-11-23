pipeline {
    agent any

    stage('Deploy con Docker Compose') {
            steps {
                echo "🚀 Desplegando con Docker Compose..."
                bat '''
                docker compose down || exit /b 0
                docker compose up -d --build
                '''
            }
        }

    post {
        ...
    }
}
