# Product Key Generator In Python 3

```
import random,string def g(k,s,l=16):return s.join(''.join(random.choices(k,k=l//4))for _ in range(4)) keys=[g(string.ascii_lowercase+string.digits,'-')for i in range(int(input("Enter the number of keys you want to generate: ")))]with open("keygen.txt",'w')as file: for key in keys:file.write(key+'\n') print("Keys have been written to the file keygen.txt")
```

Output:
```
Enter the number of keys you want to generate:
Keys have been written to the file keygen.txt
```
