from jassent import spaceList


def book(contentOfRoom, whatYouWantToCheck):
    for i in range(len(contentOfRoom)):
        for t in range(len(contentOfRoom[i])):
            if contentOfRoom[i][t] == 'whatYouWantToCheck':
                print('your rooms',contentOfRoom[i][:t-1], 'is',  contentOfRoom[i][t+1:])
