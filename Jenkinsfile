pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('printing recent commit') {
            steps {
                sh 'git diff HEAD^ HEAD -name-status'
            }
        }
    }
}

                
       


    


