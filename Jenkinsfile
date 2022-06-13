pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('prinintg commit') {
            steps {
                sh 'git diff HEAD^ HEAD'
            }
        }
    }
}

                
       


    


