_ = input()
nums = list(map(int, input().split()))
cnt = 0

# Basic
while all(num%2==0 for num in nums):
    nums = [num/2 for num in nums]
    cnt += 1
print(cnt)

# Advanced
# cnt = float('inf')
# for num in nums:
#     cnt = min(cnt, len(bin(num)) - bin(num).rfind('1') - 1)
# print(cnt)