import random

prob_rn = [0, 0, 0]
prob_rn[0] = random.randint(1, 9)
prob_rn[1] = random.randint(1, 9)
while prob_rn[0] == prob_rn[1]:
    prob_rn[1] = random.randint(1, 9)
prob_rn[2] = random.randint(1, 9)
while prob_rn[0] == prob_rn[2] or prob_rn[1] == prob_rn[2]:
    prob_rn[2] = random.randint(1, 9)
print(prob_rn)
prob = str(prob_rn[0]) + str(prob_rn[1]) + str(prob_rn[2])
count = 0
a = 0
b = 0
info=[]
while True:
 ans = input("input number")
 # k=0
 t = list(set(ans))
 if len(t) !=3: # or 사용은 최소화
     print("중복된 숫자를 입력하지 마세요")
     continue
 if len(ans) !=3:
     print("한번에 3개의 숫자를 입력하세요")
 if not ans.isdigit():
     print("Please input only number")
     continue
 # for i in range(len(ans)):
 #     for j in range(i+1,len(ans)):
 #         if ans[i]==ans[j]:
 #                 k=1
 # if k==1:
 #  print("같은숫자만 입력하세요")
 #  continue

 count += 1
 strike = 0
 ball = 0
 for i in range(len(prob)):
     for j in range(len(ans)):
         if i == j and prob[i] == ans[j]:
             strike += 1
         if i != j and prob[i] == ans[j]:
             ball += 1
 info.append([strike, ball])
 if strike == 3:
    print("you win")
    sum =[0,0]
    for i in info:
        sum[0] += i[0]
        sum[1] += i[1]
    avg = [sum[0]/count,sum[1]/count]
    print("average: {} strike, {} ball".format(avg[0], avg[1]))
    break

 print ("제{}구, {} strike {} ball".format(count,strike,ball))
 continue

a=[4,5,7,2,1]
for i in range(len(a)-1):
     for j in range(i+1,len(a)):
         if a[i] > a[j]:
             t= a[i]
             a[i]=a[j]
             a[j]=t
print(a)







