pipeline {
    agent any

    stages {
       stage('ssh into a instances....') {
            steps {
                sshagent(['8ca3a089-4d8e-47a5-bc2d-c52d40aed6e9']) {
                    sh 'ssh -o StrictHostKeyChecking=no ec2-user@ip-172-31-6-32 uptime'
                script{
                    try {
                             sh 'ssh ec2-user@ip-172-31-6-32 whoami'
                             sh 'ssh ec2-user@ip-172-31-6-32 sudo -i && cd /home/ec2-user/ansible/jenkins_demo && source /home/ec2-user/abhi/bin/activate && python3 source.py'
                    }
                    catch(error){
                            print("error")
                    }

                    }
            }
        }
                    
    }
  }
}

                
       


    


