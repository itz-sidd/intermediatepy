import json

# prsn={"name":"john","age":20,"city":"LA"}

# personJSON=json.dumps(prsn,indent=4,sort_keys=True)
# print(personJSON)

# # with open('prsn.json','w')as file:
# #     json.dump(prsn,file)

# with open('prsn.json','r')as file:
#     prsn=json.loads(personJSON)
#     print(prsn)


class User:

    def __init__(self,name,age):
        self.name=name
        self.sge=age

user=User("Mady",43)

def encode_user(o):
    if isinstance(o,User):
        return{'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        return TypeError
    

from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self,o):
        if isinstance(o,User):
            return{'name':o.name,'age':o.age,o.__class__.__name__:True}
    
        return JSONEncoder.default(self,o)
    
userJSON=UserEncoder().encode(user)
print(userJSON)

user=json.loads(userJSON)
print(user.name)
