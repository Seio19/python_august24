list1 = [2, 3, 5, 5, 8, 10, 13]

print(list1)

for i in range(len(list1)):
	print(list1[i], end=' ')
	
for element in l1: # type: ignore # For each loop
	print(element, end=' ')
	
print(list1[:])
print(list1[::])
print(list1[:4]) # [2, 3, 5, 5]

print(l1[0:1]) # type: ignore # [2] 
print(l1[:6:2]) # type: ignore # 2 5 8

print(l1[-2:1:-2]) # type: ignore # [10, 5]

print(l1[::-1]) # type: ignore # prints the list in reverse

n = int(input('Enter size of Original array: '))

original_array = []
print(f'Enter {n} elements of the Original Array')
for i in range(n):
	original_array.append(int(input()))

m = int(input('Enter size of transported array: '))

transported_array = list()
print(f'Enter {m} elements of the transported Array')
for i in range(m):
	transported_array.append(int(input()))

original_array.sort()
transported_array.sort()

print(original_array)
print(transported_array)

missing_elements_array = []
j = 0

if m == 0:
	missing_elements_array = original_array
else:
	for i in range(len(original_array)):
		if original_array[i] == transported_array[j]:
			j += 1
		else:
			missing_elements_array.append(original_array[i])
		if j == m and i != n-1:
			missing_elements_array.extend(original_array[i+1:])
			break
		
print('Missing elements are: ', set(missing_elements_array))