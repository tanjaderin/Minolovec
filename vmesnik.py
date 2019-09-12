import bottle
import model



minolovec = model.Polje()


@bottle.get('/')
def index():
    return bottle.template('base1.html')

@bottle.post('/igra/')
def zacni_novo_igro():
    st_vrstic = int(bottle.request.forms.get('st_vrstic'))
    st_stolpcev = int(bottle.request.forms.get('st_stolpcev'))
    st_bombic = int(bottle.request.forms.get('st_bombic'))
    minolovec.nastavitev(st_vrstic, st_stolpcev, st_bombic)
    return bottle.template('igra.html', igra = minolovec )


@bottle.post('/<vrstica : int>/<stolpec : int>/')
def odkrij_polje():
    #pozicija = bottle.request.forms.getunicode('pozicija')
    minolovec.odkrivanje(vrstica, stolpec)
    bottle.redirect('/igra/') 
   

@bottle.post("/nova_igra/")
def nova_igra():
    minolovec.zacetek_igre()
    bottle.redirect("/")
   
@bottle.get("/img/<slika>")
def pokazi_sliko(slika):
    return bottle.static_file(slika, root="img")



    

bottle.run(reloader= True, debug= True)