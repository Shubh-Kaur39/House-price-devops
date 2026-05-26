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
                bat 'docker run --rm house-price-app pytest'
            }
        }

        stage('Code Quality') {
            steps {
                bat 'docker run --rm house-price-app pylint app.py'
            }
        }

        stage('Security Scan') {
            steps {
                bat 'docker run --rm house-price-app bandit -r .'
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