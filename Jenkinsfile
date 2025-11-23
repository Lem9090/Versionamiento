pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo "📥 Clonando repositorio desde Gitea..."
                git branch: 'main',
                    url: 'https://gitea.com/axolot/Versionamiento.git'
            }
        }

        stage('Mostrar archivos') {
            steps {
                echo "📂 Listando archivos del proyecto..."
                sh 'ls -R'
            }
        }

        stage('Verificar sintaxis Python') {
            steps {
                echo "✅ Verificando sintaxis básica de archivos .py..."
                sh '''
                    if command -v python3 >/dev/null 2>&1; then
                      python3 -m py_compile $(git ls-files "*.py")
                    else
                      echo "Python3 no está instalado en el agente, se omite esta verificación."
                    fi
                '''
            }
        }
    }

    post {
        always {
            echo "🏁 Pipeline finalizado (éxito o fallo)."
        }
        success {
            echo "✅ ÉXITO: build correcto."
        }
        failure {
            echo "❌ FALLO: revisar logs en Jenkins."
        }
    }
}
