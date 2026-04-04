# n=int(input("몇 팩토리얼을 구할까요?"))
# def fact(x):
#     res=1
#     for i in range(1,x+1):
#         res*=i
#     return res
# print(fact(n))

# n=int(input("파이의 근사값을 몇의 자리 수 까지 더할까요?"))
# res=3
# for i in range(n):
#     total=1/res
#     res+=2
#     total*=-1
# print(4*(1-total))
    
res=0
shark=list(map(int,input().split()))
for i in range(len(shark)):
    res+=shark[i]
print(round(res/i)) #round 

# shark.sort()
# # 홀수면 1 2 3 4 5 -> 3
# print(shark[len(shark)//2])

# # 짝수면 1 2 3 4 -> (2+3)/2
# print((shark[len(shark)//2]+shark[len(shark)//2-1])/2)




    