#################################################################################################
# POSTOPEK PROGRAMIRANJA
#
# 1. OBMOČJE IGRE:
#   -mreža s 16 polji, list of lists
# 
# 2. FUNKCIJE ZA ZDRUŽEVANJE
#   -združitev ploščic levo, desno, gor in dol
#
# 3. ZAČETEK IGRE 
#   -prazna mreža z dvema ploščicama, ki imasta vrednost 2 ali 4 
# 
# 4. "RUNDE" IGRE:
#   - možnost združevanja levo, desno, gor in dol 
#   - prikaz novega območja 
#   - koda za preverjanje ali je bil premik uspešen ali ne 
#
# 5. DODAJA NOVEGA POLJA:
#
# 6. ZMAGA/PORAZ
################################################################################################

# POSKUSNO OBMOČJE, za preverjanje naše kode
obmocje = [[0, 0, 2, 2], [2, 2, 2048, 0], [4, 0, 0, 4], [0, 2, 0, 0]]

###############################################################################################

# VELIKOST OBMOČJA
VELIKOST_OBMOCJA = 4

###############################################################################################

# FUNKCIJA ZA PRIKAZ, območje bo prikazala kot v klasični igri 2048
def prikaz():
    #katera vrednost je najdaljša (vrednosti so lahko enomestne, dvmestne, trimestne ali štirimestne)
    najvecja = obmocje[0][0]
    for vrstica in obmocje:
        for element in vrstica:
            #ali je vrednost elementa večja od trenutne največje vrednosti
            if element > najvecja:
                najvecja = element

   #število potrebovanih presledkov glede na dolžino najdaljše vrednosti  
    st_presledkov = len(str(najvecja))

    for vrstica in obmocje:
        trenutna_vrstica = '|' # med vsako vrednjostjo želim imeti navpično črto
        for element in vrstica:
            # če je enlement 0, bi radi dodali space
            if element == 0:
                trenutna_vrstica += ' ' * st_presledkov + '|'
            # če ne, dodamo vrednost
            # če imamo trimesto število, morajo vse enomestna števila imeti pred njimi dva presledka, dvomestna števila pa le enega 
            else:
                trenutna_vrstica += (' ' * (st_presledkov - len(str(element)))) + str(element) + '|'
        print(trenutna_vrstica)
    #za dodatno vrstico
    print() 

prikaz()

######################################################################################################################## 

# MERGE LEVO
def zdruzi_eno_vrstico_levo(vrstica):
    # vse elemente moramo premakniti kar se da levo
    for j in range(VELIKOST_OBMOCJA - 1): #zanka bo v našem primeru šla 3x
        # for zanaka ki pogleda vse vrednosti od desne proti levi
        for i in range(VELIKOST_OBMOCJA - 1, 0, -1):
            # če je prazno polje levo, potem premakni
            if vrstica[i - 1] == 0:
                vrstica[i - 1] = vrstica[i] #premik v levo
                vrstica[i] = 0

    #združimo vse vrdnosti levo
    for i in range(VELIKOST_OBMOCJA - 1):
        #ali je element ki ga trenutno gledamo enak tistemu ki je zraven
        if vrstica[i] == vrstica[i + 1]:
            vrstica[i] *= 2
            vrstica[i + 1] = 0

    #še enkrat premaknemo vse levo
    for i in range(VELIKOST_OBMOCJA - 1, 0, -1):
        if vrstica[i - 1] == 0:
            vrstica[i - 1] = vrstica[i] 
            vrstica[i] = 0
    return vrstica

# FUNKCIJA, KI ZDRUŽI CELOTNO OBMOČJE V LEVO
def zdruzi_levo(trenutno_obmocje):
    #združi vsako vrstico v območju
    for i in range(VELIKOST_OBMOCJA):
        trenutno_obmocje = zdruzi_eno_vrstico_levo(trenutno_obmocje[i])
    
    return trenutno_obmocje

zdruzi_levo(obmocje)
prikaz()



    




