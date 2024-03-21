var=open('new.txt','w+')
var.write('Hello')

var.close()
var=open('new.txt','r')
print(var.read())
