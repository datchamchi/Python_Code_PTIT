class CauHoi:
    def __init__(self,ten,soluong):
        self.ten= ten
        self.soluong = soluong

t= int(input())
arr=[]
while t>0:

   s= input()
   t-=1
   count=0
   question = CauHoi(s,count)

   ques= input()

   while(len(ques) >0 and t>0):
       question.soluong+=1
       t-=1
       if(t>0): ques= input()
       if(len(ques)==0):
           t-=1
           break

   arr.append(question)
   if(t==0):break

for q in arr:
    print(q.ten +': '+ str(q.soluong))


