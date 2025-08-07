pipeline {
    agent any

    stages {
        stage('Clone Git') {
            steps {
                git branch: 'master', url: 'https://github.com/Ben-Brahim-amal/jenkins-projet.git'
            }
        }

        stage('Check PATH') {
            steps {
                bat 'echo %PATH%'
            }
        }
            
        
        stage('Run Script') {
            steps {
                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" script.py'
                }
        }

    }
}
