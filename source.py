import json
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
from sys import argv
import subprocess

repo = git.Repo("/home/ec2-user/jenkins_demo")

repoDiffs = repo.head.commit.diff('HEAD~1')
print(repoDiffs)
path=[]
for item in repoDiffs:

    Source = item.a_path
    path = os.path.split(Source)
    f=open('src_dest.json')
    src_data = f.read()
    src_load = json.loads(src_data)
    service=path[0]
    try:
        if service in src_load:
           source = src_load[service]['src']
           destination = src_load[service]['dest']
           print(source)
           print(destination)
           cmd = ["ansible-playbook",
           "-i inventory",
           "ansible-playbook.yml",
           "-extra-vars src=source dest=destination service=service"
            ]

        subprocess.call(cmd)

    except ValueError:
        print ("input correct service file")

            

        






    







