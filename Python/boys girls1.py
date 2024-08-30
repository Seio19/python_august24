from unittest import result


def can_arrange_students(num_cases, cases):
  results = []
  for case in cases:
    n = case[0]  
    boys = case[1] 
    girls = case[2]

boys.sort() # type: ignore
girls.sort()  # type: ignore
  
arranged = []  
i, j = 0, 0  
turn = 0  

while i < len(boys) and j < len(girls): # type: ignore
  if turn == 0:
    arranged.append(boys[i]) # type: ignore
    i += 1
  else:
    arranged.append(girls[j]) # type: ignore
    j += 1
  turn = (turn + 1) % 2  

arranged += boys[i:] # type: ignore
arranged += girls[j:] # type: ignore

feasible = True
for k in range(1, len(arranged)):
  if arranged[k - 1] == arranged[k]:
    feasible = False
    break

result.append("YES" if feasible else "NO")