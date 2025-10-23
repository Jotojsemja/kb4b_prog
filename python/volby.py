import random

lidi = 10000000 # 10m


def volba():
    volba = random.choices(strany, preference,  k=1)[0]
    hlasy_stran[volba] += 1
    


strany = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]
preference  = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]  # data ze STEM 28.9.
hlasy_stran ={strana: 0 for strana in strany}


volici = random.randint(lidi*0.5, lidi*0.8)


for i in range(volici):
    volba()


for i in range(len(strany)):
    print(strany[i], hlasy_stran[strany[i]])
    
    if hlasy_stran[strany[i]] > 0:
        print(round(hlasy_stran[strany[i]]/volici*100, 2), "%")
    if (round(hlasy_stran[strany[i]]/volici*100)) > 5:
        print("*" *(round(hlasy_stran[strany[i]]/volici*100)))
    else:
        print("-" *(round(hlasy_stran[strany[i]]/volici*100)))