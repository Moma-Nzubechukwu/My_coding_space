from jassent import spaceList


def check_for_hotel(hi, contentOfRoom):
    fin = []
    for h in range(len(contentOfRoom)):
        if hi in spaceList(contentOfRoom[h]):
            hello = spaceList(contentOfRoom[h])
            if hello[-1][0].isdecimal():
                hello[-1] = int(hello[-1])
                if hello[-1] > 0:
                    y = hello.index(hi)
                    fin = [hello[y], hello[-1]]
                elif hello[-1] <= 0:
                    y = hello.index(hi)
                    fin = [hello[y], hello[-1]]
            else:
                if hello[-1][:-1] == 'yes':
                    y = hello.index(hi)
                    fin = [hello[y], hello[-1]]
                elif hello[-1][:-1] == 'none':
                    y = hello.index(hi)
                    fin = [hello[y], hello[-1]]


    return fin
