objects = dict()
while (text := input()) != "":
    while text != "":
        index = text.find(" ")
        if index != -1:
            word = text[:index]
            text = text[(index + 1):]
        else:
            word = text
            text = "" 

        if word not in objects:
            objects[word] = 1
        else:
            objects[word] += 1

for obj in objects:
    print(obj, objects[obj])