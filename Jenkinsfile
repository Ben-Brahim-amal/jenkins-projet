pipeline {
    agent any

    stages {
        stage('Clone Git') {
            steps {
                git branch: 'master', url: 'https://github.com/Ben-Brahim-amal/jenkins-projet.git'
            }
        }
        stage('Run Script') {
            steps {
                bat 'script-python.py'
            }
        }
    }
}
