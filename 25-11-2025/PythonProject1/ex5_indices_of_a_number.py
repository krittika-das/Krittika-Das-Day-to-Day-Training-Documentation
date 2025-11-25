nums=[5, 2, 7, 5, 9, 5, 3]
n=int(input())
x=[]
for i in range(0, len(nums)):
    if nums[i]==n:
        x.append(i)
print(x)