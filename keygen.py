import os,random,string,time
def gk2(n1):
    k2=set()
    c2=string.ascii_uppercase+string.digits
    rng=random.SystemRandom()
    while len(k2)<n1:
        k1='-'.join([''.join(rng.choices(c2,k=4))for i in range(5)])
        k2.add(k1)
    return list(k2)
def wk2tf(k2):
    fp=os.path.join(os.getcwd(),"keygen.txt")
    with open(fp,"w")as f1:
        for i,k1 in enumerate(k2):
            if i in[20,21,24,52,68,79,142,419,442,464,584,586,665,852,988,989,992,994,1193,1336,19131,19132,25564,25574]:f1.write(f"{k1} {gkt(i)}\n")
            else:f1.write(f"{k1}\n")
    return fp
def gkt(i):
    kt2={20:"FTP?",21:"SSH?"if random.random()<0.5 else"SFTP?",24:"SMTP?",52:"DNS?",68:"Nice!",79:"HTTP?",142:"IMAP?",419:"Smoke Weed Everyday!",442:"HTTPS?",464:"SMTPS?",584:"IMAP?",586:"SMTP?",665:"Satan!"if random.random()<0.2 else random.choice(["The Devil!","Lucifer Lux!","Beelzebul!","Beelzebub!"]),852:"DTLS?",988:"FTPS?",989:"FTPS?",992:"IMAPS?",994:"POP3S?",1193:"OpenVPN?",1336:"Hacker!"if random.random()<0.2 else random.choice(["Elite!","Access Granted!","Access Denied!","We're In!"]),19131:"Minecraft: Bedrock Edition?",19132:"Minecraft: Bedrock?",25564:"Minecraft: Java Edition?" if random.random()<0.5 else"Minecraft: Java Edition query?",25574:"Minecraft: Java Edition RCON?"}
    return kt2.get(i,"")
n1=int(input("Enter the number of product keys you want to generate? "))
time.sleep(2)
print("Please wait...",end=" ",flush=True)
time.sleep(0.08)
print("While i'm generating this file for you.")
time.sleep(4)
print("Done! The file 'keygen.txt' has been successfully generated,",end=" ",flush=True)
time.sleep(0.08)
k2=gk2(n1)
fp=wk2tf(k2)
print(f"The product keys are saved in the following file: '{fp}'")
time.sleep(3)
print("Thank you for your patience, And goodbye! :)")
time.sleep(4)
