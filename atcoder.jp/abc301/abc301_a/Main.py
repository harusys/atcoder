from collections import Counter

N = int(input())
S = input()
Sc = Counter(S)
 
if Sc['T'] == Sc['A'] and S[N-1] == 'T':
    print('A')
elif Sc['T'] == Sc['A'] and S[N-1] == 'A':
    print('T')
elif Sc['T'] > Sc['A']:
    print('T')
else:
    print('A')