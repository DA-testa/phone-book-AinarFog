# python3

def enter():
  a=int(input())
  list=[]
  for i in range(a):
    ph=input().split(" ")
    ph[1]=int(ph[1])
    ph[0]=ph[0].lower()  
    list.append(ph)
  return list

def add(q1,q2,pb):
  for i in range(len(pb)):
    ph=pb[i]
    if (q1 in ph.values()):
      del pb[i]
      break
  pb.append({"num":q1,"name":q2})
  return pb    

def delete(pb,q1):
  for i in range(len(pb)):
    ph=pb[i]
    if (q1 == ph.get("num")):
      del pb[i]
      return pb
      break
  return pb

def find(pb,q1):
  q2=0
  for i in range(len(pb)):
    ph=pb[i]
    if(q1 == ph.get("num")):
      q2=1
      print(ph.get("name"))
      break
  if (q2==0):
    print("not found")

def dict(list):
  phones=[]
  for i in range(len(list)):
    ph=list[i]
    if("add" in ph):
      phones=add(ph[1],ph[2],phones)
    elif("find" in ph):
      find(phones,ph[1])
    elif("del" in ph):
      phones=delete(phones,ph[1])
if __name__ =='__main__':
  dict(enter())
