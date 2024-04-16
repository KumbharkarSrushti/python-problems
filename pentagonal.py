S1,S2=map(str,input().split())
T1,T2=map(str,input().split())
P=("A" and "C") or ("E" and "C") or ("B" and "D") or ("C" and "E") or ("D" and "A") or ("D" and "B") or ("E" and "B") or ("B" and "E") or ("C" and "A") or ("A" and "D")
if (T1 and T2) == P:
  print("yes")
else:
  print("no")