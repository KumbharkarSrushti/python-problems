input=int(input())
if input>=0 and input<=2:
    print("infant")
elif input>=3 and input<=12:
    print("child")
elif input>=13 and input<=19:
    print("Teenager")
elif input>=20 and input<=65:
    print("Adult")
else:
    print("Senior")