import json
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
from sys import argv
import subprocess

repo = git.Repo("/home/ec2-user/ansible/jenkins_demo")
#take latest pull of the repo
repoDiffs = repo.head.commit.diff('HEAD~1')
path=[]
for item in repoDiffs:

    Source = item.a_path
    path = os.path.split(Source)
    f=open("/home/ec2-user/jenkins_demo/src_dest.json")
    src_data = f.read()
    src_load = json.loads(src_data)
    service=path[0]
    try:
        if service in src_load:
           source = src_load[service]['src']
           destination = src_load[service]['dest']
           print(source)
           print(destination)
           cmd = ["/usr/bin/ansible-playbook","/home/ec2-user/ansible/jenkins_demo/ansible-playbook.yml","-extra-vars src={} dest={} service={}".format(source, destination, service)]
           subprocess.call(cmd)
#meaningfulelsestatement
    except ValueError:
        print ("input correct service file")

            

        






    







