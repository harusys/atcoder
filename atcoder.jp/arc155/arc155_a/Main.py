for _ in range(int(input())):
  n,k=map(int,input().split())
  s=input()
  c=n//(2*n)
  k%=2*n
  if c&1:
    if k>n:
      ans=s+s[n-(k-n):]
    else:
      ans=s[:k]
  else:
    if k>n:
      ans = s[::-1] + s[::-1][n - (k - n):]
    else:
      ans=s[::-1][:k]
  if (ans+s)==(ans+s)[::-1]and (s+ans)==(s+ans)[::-1]:
    print("Yes")
  else:
    print("No")