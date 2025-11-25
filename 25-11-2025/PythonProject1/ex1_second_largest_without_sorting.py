nums=[23, 89, 12, 78, 55, 42]
first=nums[0]
second=nums[0]
for n in nums:
    if n>first:
        first=n
for n in nums:
    if n!=first and n>second:
        second=n
print("Largest no: ", second)

