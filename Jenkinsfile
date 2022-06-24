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
                    sh 'ssh -o StrictHostKeyChecking=no ec2-user@ip-172-31-6-32 uptime'
                script{
                    try {
                            sh 'ssh ec2-user@ip-172-31-6-32 pwd'
                            sh 'ssh ec2-user@ip-172-31-6-32 cd jenkins_demo | git diff --name-only HEAD^..'}
                            sh 'ssh ec2-user@ip-172-31-6-32 ansiblePlaybook credentialsId: '8ca3a089-4d8e-47a5-bc2d-c52d40aed6e9', disableHostKeyChecking: true, installation: 'ansible', inventory: 'inventory', playbook: 'ansible-playbook.yml''
                        catch(error){
                            sh 'cd jenkins_demo'
                            sh 'git diff --name-only HEAD^.. '}
                    }

                    }
            }
        }
        stage(' copying config file to server') {
         steps {
             ansiblePlaybook credentialsId: '8ca3a089-4d8e-47a5-bc2d-c52d40aed6e9', disableHostKeyChecking: true, installation: 'ansible', inventory: 'inventory', playbook: 'ansible-playbook.yml'
         }
        }
    }
}

                
       


    


