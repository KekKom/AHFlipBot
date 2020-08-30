from requests import get

def Average(lst):
    try:
        return sum(lst) / len(lst)
    except:
        return 0

def getName(uuid):
    uuuid = []

    for i in range(len(uuid)):
        uuuid.append(uuid[i])

    uuuid.insert(8, '-')
    uuuid.insert(13, '-')
    uuuid.insert(18, '-')
    uuuid.insert(23, '-')

    uuid = ""

    print(uuuid)
    try:
        b = ''.join(uuuid)

    except AttributeError:
        import string
        b = string.join(uuuid, '')
    print(uuid)

    data = get("https://sessionserver.mojang.com/session/minecraft/profile/" + b).json()
    print(data)
    return str(data["name"])
