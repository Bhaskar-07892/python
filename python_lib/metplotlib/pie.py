import matplotlib.pyplot as plt

marks = [80 , 81 , 64 , 94 ,81]
sub = [ 'hindi','english', 'maths', 'science', 'sst' ]
c = ['red','blue', 'green','hotpink','yellow']

plt.pie(marks,labels=sub,colors=c,autopct=' %1.1f%%')
plt.legend()
plt.show()