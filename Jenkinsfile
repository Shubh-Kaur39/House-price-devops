pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'docker build -t house-price-app .'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Code Quality') {
            steps {
                sh 'pylint app.py'
            }
        }

        stage('Security Scan') {
            steps {
                sh 'bandit -r .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 8501:8501 house-price-app'
            }
        }

        stage('Release') {
            steps {
                sh 'docker tag house-price-app house-price-app:v1'
            }
        }
    }
}