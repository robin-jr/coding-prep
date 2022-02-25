from operator import contains
from pathlib import Path
from typing import List

class Skill:
    def __init__(self,name:str,level:int) -> None:
        self.name=name
        self.level=level

# class Role:
#     def __init__(self,roll_number:int,skill:Skill) -> None:
#         self.roll_number=roll_number
#         self.skill=skill

class Contributor:
    def __init__(self,name :str,skills :List(Skill)) -> None:
        self.name=name
        self.skills=skills
        self.isAssigned=False
        self.assigned_role=None

class Project:
    def __init__(self,name:str,duration:int,score:int,best_before:int,roles:List(Role),skills:List(Skill)) -> None:
        self.name=name
        self.duration=duration
        self.score=score
        self.best_before=best_before
        # self.roles=roles
        self.skills=skills
        self.contributors=[]


#Solution

projects : List(Project)=[]
contributors : List(Contributor)=[]

projects.sort(lambda x:x.score-x.duration) #sorting projects based on priority
#priority is determined using score-duration -- score should be high, duration should be low

result=[]

def canDo(project:Project):
    for role_skill in project.skills:
        c=filter(lambda x: x.skills.contains(role_skill) ,contributors)
        # c=sorted(lambda x:[],c) #need to sort them based on skill level ascending and choose the first

        if len(c)>0 and c[0].assigned_role is not None:
            c[0].assigned_role=role_skill
    project.contributors=[]

while len(projects)>1:  # TODO: should include the case when no project can be done
    for project in projects:
        if canDo(project): #canDo() will populate the "project.contributors" list
            result.append(project)
            projects.remove(project)
            break
    
