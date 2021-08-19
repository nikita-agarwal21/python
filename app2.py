name=['john','dog','fish','dog','john','god','wolf']
unique=[]
for names in name:
    if names not in unique:
        unique.append(names)
print(unique)
