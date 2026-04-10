pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build + Tests + Sécurité') {
            steps {
                sh '''
                # Nettoyage workspace + venv
                rm -rf venv

                # Création environnement virtuel propre
                python3 -m venv venv
                chmod -R 755 venv

                # Mise à jour pip (IMPORTANT: via python)
                venv/bin/python -m pip install --upgrade pip

                # Installation dépendances
                venv/bin/python -m pip install -r requirements.txt

                # Tests
                venv/bin/python -m pytest tests/

                # Analyse sécurité
                venv/bin/python -m pip install bandit safety
                venv/bin/python -m bandit -r src -ll
                venv/bin/python -m safety check
                '''
            }
        }

        stage('Nettoyage') {
            steps {
                sh 'rm -rf venv'
            }
        }
    }

    post {
        success {
            echo "Pipeline exécuté avec succès."
        }
        failure {
            echo "Pipeline échoué"
        }
        always {
            echo "Fin du pipeline"
        }
    }
}
