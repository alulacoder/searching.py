arr = list(map(str,input("enter letter (put a space between every letter) - ").split()))
lett = str(input("enter the letter that you are searching for - "))

# if lett in arr:
#     print("key exists")
# else:
#     print("key doesn't exist :(")

for elem in arr:
    if elem == lett:
        print("key exists")

    else:
        continue
        