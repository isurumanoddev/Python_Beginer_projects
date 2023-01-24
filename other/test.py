names = ["ab","bc","cd","av","ad"]

def find_name(name):
    if name[0] == "a":
        return name


m = filter(find_name, names)
for i in m:
    print(i)
