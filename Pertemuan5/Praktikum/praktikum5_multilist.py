#belajar membuat multi list 
Fighter_UFC = [
                ["Aspinall","Gane","Pahlovic"],
                ["Pereira","Ankalaev","Ulbelrg"],
                ["Khamzat","DDP","RDR"]
]


print("GOAT UFC:",Fighter_UFC[1][0])

for fighter in Fighter_UFC:
    for i in fighter:
        print('Fighter:',i)