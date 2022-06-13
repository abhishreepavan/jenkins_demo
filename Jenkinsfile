pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('ssh into a instance') {
            steps {
                sshagent(['8ca3a089-4d8e-47a5-bc2d-c52d40aed6e9']) {
                    sh 'ssh -o StrictHostKeyChecking=no user@hostname.com uptime'
                    script{
                        try {
                            sh 'cd jenkins_demo'
                            sh 'git diff HEAD^.. '}
                        catch(error){
                            sh 'cd jenkins_demo'
                            sh 'git diff HEAD^.. '}
                    }

                    }
            }
        }
    }
}

                
       


    


