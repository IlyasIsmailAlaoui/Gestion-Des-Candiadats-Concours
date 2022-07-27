from tkinter import *
from tkinter import messagebox
pff=Tk()
pff.title("Concours")
pff.geometry("800x400")
pff.minsize(200,200)
pff.config(bg="#FED823")

#--------------------------------------------------------------------------------------------------------------
def run(main_window):
    global valeur1 
    global valeur2
    global valeur3
    global valeur4
    global var
    window=Toplevel(main_window)
    window.title("Saisir un candidat")
    window.geometry("800x400")
    window.minsize(200,200)
    window.config(bg="#DDD510")     
    CIN=Label(window,text='Numero du CIN :',fg='blue',bg='#11A5C8',font='Calibri 18 bold').grid(row=0,column=0)
    valeur1=StringVar()
    champ1=Entry(window,bg='white',font='Arial 14 ',textvariable=valeur1).grid(row=0,column=2)
    Nom=Label(window,text='Nom :',fg='blue',bg='#CFAB4A',font='Calibri 18 bold ').grid(row=2,column=0)
    valeur2=StringVar()
    champ2=Entry(window,bg='white',font='Arial 14 ',textvariable=valeur2).grid(row=2,column=2)
    lolo=Label(window,text='Prenom :',fg='blue',bg='#C811C3',font='Calibri 18 bold ').grid(row=4,column=0)
    valeur3=StringVar()
    champ3=Entry(window,bg='white',font='Arial 14 ',textvariable=valeur3).grid(row=4,column=2)
    Age=Label(window,text='Age :',fg='blue',bg='#C88411',font='Calibri 18 bold ').grid(row=6,column=0)
    valeur4=StringVar()
    champ4=Entry(window,bg='white',font='Arial 14 ',textvariable=valeur4).grid(row=6,column=2)                                                                                        
    Decision=Label(window,text='Decision :',fg='blue',bg='#EE4944',font='Calibri 18 bold ').grid(row=8,column=0)
    var=StringVar()
    b1=Radiobutton(window,text='admis',variable=var,value='admis',bg='#CFAB4A',font='Arial 14 ').grid(row=8,column=1)
    b2=Radiobutton(window,text='refuse',variable=var,value='refusé',bg='#CFAB4A',font='Arial 14 ').grid(row=8,column=2)
    b3=Radiobutton(window,text='ajourne',variable=var,value='ajourné',bg='#CFAB4A',font='Arial 14 ').grid(row=8,column=3)
    enregistrer=Button(window,text='Enregistrer',font='Arial 14 ',command=saisir).grid(row=15,column=400)
    window.mainloop()
    
def saisir():
    f=open("Concours.txt","a")
    NCIN=valeur1.get()
    nom=valeur2.get()
    lolo=valeur3.get()
    Age=valeur4.get()
    Decision=var.get()
    f.write(NCIN+";"+nom+";"+lolo+";"+Age+";"+Decision+"\n")
    f.close()

def admis():
    try:
        f=open("Concours.txt","r")
        contenu=f.readlines()
        f.close()
    except:
        contenu=[]
    fiche=open("Admis.txt","w")
    fiche.close()
    fiche=open("Admis.txt","a")
    for i in contenu:
        sépare=i.split(";")
        if sépare[-1]=="admis\n":
            fiche.write(i)
    fiche.close()

def attente():
    try:
        atnt=open("Admis.txt","r")
        line=atnt.readlines()
        atnt.close()
    except:
        line=[]
    fichier=open("Attente.txt","a")
    for j in line:
        select=j.split(";")
        sage=select[-2]
        if int(sage)>=30:
            fichier.write(select[0]+";"+select[1]+";"+select[2]+"\n")
            fichier.close()

def statistiques():
    try:
        to=open("Concours.txt","r")
        tal=to.readlines()
        to.close()
    except:
        tal=[]
    total=len(tal)
    #----------------
    try:
        ad=open("Admis.txt","r")
        mis=ad.readlines()
        ad.close()
    except:
        mis=[]
    admis=len(mis)
    #----------------
    jour=0
    ref=0
    for l in tal:
        sep=l.split(";")
        if sep[-1]=="refuse\n":
            ref+=1
        elif sep[-1]=="ajourne\n":
            jour+=1
    #----------------
    if total == 0:
        stat = 0
        stat2 = 0
        stat3 = 0
    else:
        stat=(admis/total)*100
        stat2=(ref/total)*100
        stat3=(jour/total)*100
    admission=str(stat)+"%"
    refus=str(stat2)+"%"
    ajournation=str(stat3)+"%"
    messagebox.showinfo("Statistiques","Les Admis"+admission+"\nLes refuses"+refus+"\nLes ajournes"+ajournation,icon ='info')
    #----------------
def supprimer():
    try:
        sup=open("Admis.txt","r")
        satr=ad.readlines()
        sup.close()
    except:
        satr=[]
    for x in satr:
        lsep=x.split(";")
        suppr=lsep[-2]
        if int(suppr)<30:
            save=[]
            save.append(j)
            sup=open("Admis.txt","w")
            sup.writelines(save)
            sup.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
titre=Label(pff,text='Gestion des candiadats',fg='blue',bg='#FED823',font='Arial 28 bold').pack()
frame1=Frame(pff,bg='blue').pack()
frame2=Frame(pff,bg='blue').pack()
saisie=Button(frame1,text='Saisir un candiadat',fg='blue',bg='#21CFF9',font='Arial 14 bold',command=lambda: run(pff)).pack()
admis=Button(frame1,text='Les admis',fg='blue',bg='#21CFF9',font='Arial 14 bold',command=admis).pack()
attente=Button(frame2,text="Liste d'attente",fg='blue',bg='#21CFF9',font='Arial 14 bold',command=attente).pack()
statistiques=Button(frame2,text='Statistiques',fg='blue',bg='#21CFF9',font='Arial 14 bold',command=statistiques).pack()

def crée_par():
   messagebox.showinfo("Créé par",
                       "Ilyas ISMAILI ALAOUI\nNé le 28/11/2010\nElève de la 1er année du cycle secondaire collégial",
                       icon ='info')
créé_par=Button(frame1,text='Créé par !?',fg='blue',bg='#FED823',font='Arial 14 bold',command=crée_par).pack(padx=15,pady=15)
pff.mainloop()
