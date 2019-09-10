import bottle
import model



minolovec = model.Polje()

# id = vislice.nova_igra()
# igra, poskus = vislice.igre[id]

@bottle.get('/')
def index():
    return bottle.template('base.html')

@bottle.get('/igra/')
def zacni_novo_igro():
    st_vrstic = bottle.request.forms.getunicode('st_vrstic')
    st_stolpcev = bottle.request.forms.getunicode('st_stolpcev')
    st_bombic = bottle.request.forms.getunicode('st_bombic')
    tezavnost = model.zacetek_igre(st_vrstic, st_stolpcev, st_bombic)
    return bottle.template('igra.tpl', igra = model.Polje(tezavnost) )

@bottle.post('/igra/')
def odkrij():
    pozicija = bottle.request.forms.getunicode('pozicija')
    minolovec.odkrivaj(pozicija)
    bottle.redirect('/igra/') #požene novo
   

    

bottle.run(reloader= True, debug= True)