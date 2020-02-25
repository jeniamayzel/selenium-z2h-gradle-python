pipeline {
    agent {
            docker { image 'maven:3-alpine'}
        }

    options {
        timestamps ()
    }

    stages {
        stage ('Build') {
            steps {
                script {
                    sh "chmod 775 gradlew"
                    sh "./gradlew build"
                }
            }
        }
    }
}
