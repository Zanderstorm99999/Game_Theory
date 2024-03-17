def to_upper(name:str) -> str:
    return name.upper()



str1 = 'GeeksforGeeks'

upper = lambda name: name.upper()
another = to_upper
print(another(str1))
