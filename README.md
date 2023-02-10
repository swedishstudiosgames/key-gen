# Product Key Generator In Python 3

```
import os,random,string
def k(n):
    k=[];c=string.ascii_uppercase+string.digits
    for i in range(n):
        key='-'.join([''.join(random.choices(c,k=4))for i in range(5)])
        k.append(key)
    return k
def f(keys):
    o=os.name;n="keygen.txt";l=os.getcwd()+"\\"+n if o=='nt'else os.getcwd()+"/"+n
    with open(l,"w")as file:
        for key in keys:file.write(key+"\n")
    return l
n=int(input("Enter the number of keys you want to generate: "))
keys=k(n)
l=f(keys)
print(f"The product keys are saved in the following file: {l}")
```

Output:
```
Enter the number of keys you want to generate: 

```
