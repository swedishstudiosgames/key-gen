# Product Key Generator In Python 3

```
import os,random,string
def generate_keys(n):
    keys=set()
    characters=string.ascii_uppercase+string.digits
    rng=random.SystemRandom()
    while len(keys)<n:
        key='-'.join([''.join(rng.choices(characters,k=4))for i in range(5)])
        keys.add(key)
    return list(keys)
def write_keys_to_file(keys):
    filepath=os.path.join(os.getcwd(),"keygen.txt")
    with open(filepath,"w")as file:
        for i,key in enumerate(keys):
            if i in[20,21,24,52,68,79,142,419,442,464,584,586,665,852,988,989,992,994,1193,1336,19131,19132,25564,25574]:file.write(f"{key} {get_key_type(i)}\n")
            else:file.write(f"{key}\n")
    return filepath
def get_key_type(i):
    key_types={20:"FTP?",21:"SSH?"if random.random()<0.5 else"SFTP?",24:"SMTP?",52:"DNS?",68:"Nice!",79:"HTTP?",142:"IMAP?",419:"Smoke Weed Everyday!",442:"HTTPS?",464:"SMTPS?",584:"IMAP?",586:"SMTP?",665:"Satan!"if random.random()<0.2 else random.choice(['The Devil!','Lucifer Lux!','Beelzebul!','Beelzebub!']),852:"DTLS?",988:"FTPS?",989:"FTPS?",992:"IMAPS?",994:"POP3S?",1193:"OpenVPN?",1336:"Hacker!"if random.random()<0.5 else"Elite!",19131:"Minecraft: Bedrock Edition?",19132:"Minecraft: Bedrock?",25564:"Minecraft: Java Edition?" if random.random()<0.5 else"Minecraft: Java Edition query?",25574:"Minecraft: Java Edition RCON?"}
    return key_types.get(i,"")
n=int(input("Enter the number of product keys you want to generate: "))
keys=generate_keys(n)
filepath=write_keys_to_file(keys)
print(f"The product keys are saved in the following file: {filepath}")
```

Output:
```
Enter the number of product keys, That you want to generate here: 

```
