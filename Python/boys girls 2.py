def can_arrange_students(num_cases, cases):
  results = []
  for case in cases:
    n = case[0]  
    boys = case[1]  
    girls = case[2]  

    boys.sort()
    girls.sort()  

    arranged = [] 
    i, j = 0, 0  
    turn = 0 
    while i < len(boys) and j < len(girls):
      if turn == 0:
        arranged.append(boys[i])
        i += 1
      else:
        arranged.append(girls[j])
        j += 1
      turn = (turn + 1) % 2  

    
    arranged += boys[i:]
    arranged += girls[j:]

   
    feasible = True
    for k in range(1, len(arranged)):
      if arranged[k - 1] == arranged[k]:
        feasible = False
        break

    results.append("YES" if feasible else "NO")

  return results

if __name__ == "__main__":
  num_cases = int(input())
  cases = []
  for _ in range(num_cases):
    n = int(input())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    cases.append((n, boys, girls))

  results = can_arrange_students(num_cases, cases)
  for result in results:
    print(result)