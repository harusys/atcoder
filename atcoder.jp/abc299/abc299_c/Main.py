_ = input()
S = input()
print(len(max(S.split("-")))) if "-" in S and "o" in S else print(-1)