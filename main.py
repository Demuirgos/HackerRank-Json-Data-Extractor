import json
import os
import re
langExtention = {'cpp14': ".cpp", 'cpp': ".cpp", 'python3': ".py", 'c': ".c", 'pypy3': ".py", 'csharp': ".cs", 'bash': ".bash", 'visualbasic': ".vb", 'text': ".txt", 'oracle': ".sql", 'mysql': ".sql", 'java8': ".java", 'java': ".java", 'pypy': ".py", 'javascript': ".js", '["html", "js", "css"]': ".html", 'tsql': ".sql", 'php':".php", 'fsharp': ".fs"}
dataFile = open("Demuirgos_data.json","r").read()
jsonData=json.loads(dataFile)
challenges={}
if not os.path.exists("solved"):
    os.mkdit("solved")
if not os.path.exists("partial"):
    os.mkdit("partial")

for submission in jsonData["submissions"]:
    challengeName = re.sub("(\\|\/|\"|<|>|\:|\||\?|\*)","",submission["challenge"])
    if(challengeName in challenges):
        if submission["score"]>=challenges[challengeName]["score"]:
            challenges[challengeName]["score"]=submission["score"]
            challenges[challengeName]["code"]=submission["code"]
            challenges[challengeName]["language"]=submission["language"]
    else:
        challenge={}
        challenge["score"]=submission["score"]
        challenge["code"]=submission["code"]
        challenge["language"]=submission["language"]
        challenges[challengeName]=challenge
for challenge in challenges:
    path=""
    if(challenges[challenge]["score"]==1):
        path = "solved"+"//"
    else :
        path = "partial"+"//"
    problemFile=open(path+challenge+langExtention[challenges[challenge]["language"]],"w")
    problemFile.write(challenges[challenge]["code"])
