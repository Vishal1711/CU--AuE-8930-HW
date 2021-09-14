def divide():
    return 5/0

try:
    divide()
    print(divide())

except:
    print('divisionbyzeroerro')
