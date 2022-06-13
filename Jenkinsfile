pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('print the list of modified files')
        {
            steps{
                String getChangedFilesList() {
                    changedFiles = []
                    for (changeLogSet in currentBuild.changeSets)
                    { 
                        for (entry in changeLogSet.getItems()) 
                        { 
                            for (file in entry.getAffectedFiles()) 
                            {
                                changedFiles.add(file.getPath()) 
                            }
                         }
                    }

                     return changedFiles

                }
                
            }
        }       
    }
}

    


