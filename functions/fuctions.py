def fun(str,num):
    if num==0:
        index=0
        while index<len(str):
            if index%2!=0:
                print(str[index],end='')
            index+=1
    elif num==1:
        index=0
        while index<len(str):
            if index%2==0:
                print(str[index],end='')
            index+=1
    print()

fun('TRACXN',0)
fun('TRACXN',1)
