pipeline {
    agent any

    stages {
        stage('Clone Git') {
            steps {
                git branch: 'master', url: 'https://github.com/Ben-Brahim-amal/jenkins-projet.git'
            }
        }
        stage('Install Python Dependencies') {
            steps {
                bat 'pip install requests'
            }
        }
        stage('Run Script') {
            steps {
                bat 'python.py'
            }
        }
    }
}
