pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('printing recent commit message') {
            steps {
                sh 'git diff HEAD~25 HEAD –name-status'
            }
        }
    }
}

                
       


    


