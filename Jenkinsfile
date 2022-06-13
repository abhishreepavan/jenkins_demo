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
                sh 'git diff HEAD^ HEAD -name-status'
            }
        }
    }
}

                
       


    


