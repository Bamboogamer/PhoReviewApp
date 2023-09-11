def getLogin():
    loginInfo = open("login.txt", "r") \
                 .readline() \
                 .split(";")

    return loginInfo[0], loginInfo[1]


if __name__ == '__main__':
    print(getLogin())