pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build + Tests + Sécurité') {
            steps {
                sh '''
                # Nettoyage ancien environnement
                rm -rf venv

                # Création venv propre
                python3 -m venv venv

                # Sécurisation pip (IMPORTANT pour Jenkins)
                venv/bin/python -m ensurepip --upgrade || true
                venv/bin/python -m pip install --upgrade pip

                # Installation dépendances projet
                venv/bin/python -m pip install -r requirements.txt

                # Tests unitaires
                venv/bin/python -m pytest tests/

                # Outils sécurité
                venv/bin/python -m pip install bandit safety

                # Analyse sécurité code
                venv/bin/python -m bandit -r src -ll
                venv/bin/python -m safety check
                '''
            }
        }

        stage('Nettoyage') {
            steps {
                sh '''
                rm -rf venv
                '''
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
