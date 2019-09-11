import bottle
import model


tezavnost = ''
minolovec = model.Polje(tezavnost)
zastava = False

@bottle.get('/')
def index():
    return bottle.template('base.html')

@bottle.get('/igra/')
def zacni_novo_igro():
    st_vrstic = bottle.request.query['st_vrstic']
    st_stolpcev = bottle.request.query['st_stolpcev']
    st_bombic = bottle.request.query['st_bombic']
    global tezavnost
    tezavnost = st_vrstic, st_stolpcev, st_bombic
    return bottle.template('igra.html', igra = model.Polje(tezavnost) )


@bottle.post('/<pozicija : int, int> /')
def odkrij_polje():
    #pozicija = bottle.request.forms.getunicode('pozicija')
    minolovec.odkrivaj(pozicija)
    bottle.redirect('/igra/') 

@bottle.post("/nova_igra/")
def nova_igra():
    minolovec.zacetek_igre()
    bottle.redirect("/")
   
@bottle.get("/img/<slika>")
def pokazi_sliko(slika):
    return bottle.static_file(slika, root="img")

#@bottle.post('/zastava/')
#def postavi_zastavo():
#    if zastava == False:
#        zastava = True
#        minolovec.
#    else:
#        bottle.redirect('/igra/') 

    

bottle.run(reloader= True, debug= True)