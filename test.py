from src.schemas.common.PlmnId import PlmnId, Mnc, Mcc

a = PlmnId(mcc=Mcc('208'), mnc=Mnc('93'))

b = [
    {
        "mcc": "208",
        "mnc": "93"
    },
    {
        "mcc": "123",
        "mnc": "45"
    }
]

# c = PlmnId(**b[0])

# d = {"mcc": "208", "mnc": "93"}

# print(a)
# print(b)
# print(c)
# print(d)

# if a == c:
#     print(True)

if a in b:
    print(True)