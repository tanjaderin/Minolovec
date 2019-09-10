import model


def izpis_stanja(polje):
    besedilo = 
    ' Število vrstic : {0} Število stolpcev : {1} število bombic : {2}'.format(polje.st_stolpcev,
     polje.st_vrstic, 
     polje.st_bomobic)
     return besedilo

def izpis_zmage(polje):
    besedilo = 'Čestitke, uspešno ste preživeli mino-lov'
    return besedilo

def izpis_poraza(polje):
    besedilo = 'BUMMM, ojej razneslo vas je!'
    return besedilo

def izberi_tezavnost():
    input("izberi težavnost od 1 do 3:")

def nacin_igre():
    if izberi_tezavnost() == 1:
        return 9, 9, 10
    elif izberi_tezavnost() == 2:
        return 10, 10, 30
    elif izberi_tezavnost() == 3:
        return 15, 15, 50
    else:
        EnvironmentError

def pozeni_vmesnik():
    igra = model.zacetek_igre(nacin_igre()))
    while True:
        print(izpis_stanja(igra))
        polje = igra.odkrivanje(MANJKA VNOS)
        if polje == model.ZMAGA:
            print(izpis_zmage)
            return
        if polje == model.PORAZ:
            print(izpis_poraza)
            return

pozeni_vmesnik()
