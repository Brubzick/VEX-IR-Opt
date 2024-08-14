from longest_common_part import FindComPart

a = [1,2,3,4]
b = [1,2,3,4]

for i in range(0, len(a)-len(b)+1):
    print(a[i:i+len(b)])