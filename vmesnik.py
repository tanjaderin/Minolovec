import bottle
import model


tezavnost = ''
minolovec = model.Polje(tezavnost)

@bottle.get('/')
def index():
    return bottle.template('base.html')

@bottle.get('/igra/')
def zacni_novo_igro():
    st_vrstic = bottle.request.forms.getunicode('st_vrstic')
    st_stolpcev = bottle.request.forms.getunicode('st_stolpcev')
    st_bombic = bottle.request.forms.getunicode('st_bombic')
    global tezavnost
    tezavnost = model.zacetek_igre(st_vrstic, st_stolpcev, st_bombic)
    return bottle.template('igra.tpl.txt', igra = model.Polje(tezavnost) )


@bottle.post('/<pozicija : int> /')
def odkrij():
    #pozicija = bottle.request.forms.getunicode('pozicija')
    minolovec.odkrivaj(pozicija)
    bottle.redirect('/igra/') 

@bottle.post("/nova_igra/")
def nova():
    minolovec.zacetek_igre()
    bottle.redirect("/")
   

    

bottle.run(reloader= True, debug= True)