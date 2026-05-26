pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat 'docker build -t house-price-app .'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Code Quality') {
            steps {
                bat 'pylint app.py'
            }
        }

        stage('Security Scan') {
            steps {
                bat 'bandit -r .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker run -d -p 8501:8501 house-price-app'
            }
        }

        stage('Release') {
            steps {
                bat 'docker tag house-price-app house-price-app:v1'
            }
        }
    }
}