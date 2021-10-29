# => (Inclus) este -
# <=> (Echivalent) este =
# ∨ (Sau) este |
# ∧ (Si) este &
# ¬ (Not) este !


s=str(input())
prop=[c for c in s if c!=" "]
true=1
c=0
o=1
nr_paranteze_deschise=0
nr_paranteze_inchise=0
conector_unar=["!"]
conector_binar=["&", "|", "-", "="]
poz_paranteze=[]

for j in prop:
    nr_paranteze_deschise += j.count("(")
    nr_paranteze_inchise += j.count(")")


x=len(poz_paranteze)-1
    
for i in range (len(prop)):
    if prop[i]=="(" and o==1:
        poz_paranteze.append(i)
    if prop[0]!="(":
        true=0
        print("Nu exista paranteza deschisa la inceput")
        break
    if i>0:
        if prop[i]=="(" and prop[i-1]==")":
            true=0
            print("Nu exista niciun conector intre paranteze")
            o=0
            break
    if prop[i]=="(":
        print("{}.'{}' Trebuie sa urmeze o formula compusa".format(i, prop[i]))
        if i==len(prop)-1:
            print("Nu exista nimic dupa {}".format(prop[i]))
            true==0
            break
        if prop[i+1]=="(" or (prop[i+1].isalpha() or prop[i+1] in conector_unar):
            continue
        else:
            print("Nu exista nicio propozitie dupa {}".format(prop[i]))
            true=0
            break

    if prop[i] in conector_unar:
       if prop[i+1].isalpha() or prop[i+1]=="(":
           print("{}.'{}' Conector logic unar, urmeaza fie propozitie atomica, fie formula compusa".format(i, prop[i]))
           continue
       else:
           print("Nu exista nicio propozitie dupa {}".format(prop[i]))
           true=0
           break

    if prop[i] in conector_binar:
        if i<len(prop)-1:
            if prop[i+1] in conector_binar or prop[i+1] in conector_unar:
                print("Nu exista paranteze intre conectori")
        if i<len(prop)-1:
            if prop[i-1]==")" and prop[i+1]=="(":
                print("{}.'{}' Conector logic binar, asteapta fie propozitie atomica fie formula compusa".format(i, prop[i]))
                continue

    if prop[i].isalpha():
       if i==len(prop)-1:
           true=0
           break
       print("{}.'{}' Propozitie atomica, formula bine formata, trebuie sa urmeze un conector binar sau paranteza inchisa".format(i, prop[i]))
       if prop[i+1] in conector_binar:
        print("{}.'{}' Conector logic binar, asteapta fie propozitie atomica fie formula compusa".format(i+1, prop[i+1]))
        continue
       elif prop[i-1] in conector_binar or prop[i-1] in conector_unar:
            if prop[i+1]==")":
                print("{}.'{}' Paranteza inchisa, inchide paranteza de la punctul {}".format(i+1, prop[i+1], poz_paranteze[x]))
                x=x-1
                c=c+1
                continue
       elif prop[i+1] not in conector_binar:
            true=0
            print("Nu exista niciun conector dupa {}".format(prop[i]))
            break
       elif prop[i-1] in conector_binar:
            if prop[i+1]!=")":
                true=0
                print("Paranteza nu este inchisa dupa {}".format(prop[i]))
                break
       else:
         true=0
         break

    if prop[i] in conector_binar:
        if i==len(prop)-1:
            print("Nu urmeaza nimic dupa {}".format(prop[i]))
            true==0
            break
        if prop[i+1].isalpha():
            continue
        elif prop[i+1]=="(":
            continue
        else:
            print("Nu urmeaza o formula bine formata dupa {}".format(prop[i]))
            true=0
            break
    y=i

x=len(poz_paranteze)-(c+1)
paranteze_inchise=nr_paranteze_inchise-c
y=i-paranteze_inchise
z=prop[len(prop)-1].isalpha()
if len(prop)-1>y and o==1:
    if z==False:
        if prop[y+1]==")":
            if paranteze_inchise > 0:
                while paranteze_inchise > 0 and x<len(prop) and x>=0 and y<len(prop):
                    print("{}.'{}' Paranteza inchisa, inchide paranteza de la punctul {}".format(y+1, prop[y], poz_paranteze[x]))
                    y=y+1
                    x=x-1
                    paranteze_inchise=paranteze_inchise-1
if z==True:
    if prop[y-1] in conector_binar:
        print("Nu exista paranteza inainte de {}".format(prop[y]))
    else:
        print()
        print(prop[y], "nu are niciun conector inainte")

if nr_paranteze_inchise < nr_paranteze_deschise:
    dif=nr_paranteze_deschise-nr_paranteze_inchise
    if dif>1:
        print()
        print("       |")
        print("       v")
        print(dif, "paranteze nu au fost inchise")
    else:
       print()
       print("       |")
       print("       v")
       print("O paranteza nu a fost inchisa")
elif nr_paranteze_inchise > nr_paranteze_deschise:
    dif=nr_paranteze_inchise-nr_paranteze_deschise
    if dif>1:
        print()
        print("       |")
        print("       v")
        print("Au fost inchise {} paranteze in plus".format(dif)) 
    else:
        print()
        print("       |")
        print("       v")
        print("A fost inchisa o paranteza in plus")
if true==1 and nr_paranteze_inchise==nr_paranteze_deschise:
    print()
    print("       |")
    print("       v")
    print("Este formula propozitionala")
else:
  print()
  print("       |")
  print("       v")
  print("Nu este formula propozitionala")
