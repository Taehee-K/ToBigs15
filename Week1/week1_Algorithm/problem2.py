initial = input()
final = []

for i in range(len(initial)):
    if i==0:
        final.append(initial[i])
        continue
    elif final[len(final)-1]==initial[i]:
        continue
    else: 
        final.append(initial[i])

# print(final)
print(''.join(final)) # List의 Element들을 공백없이 붙임