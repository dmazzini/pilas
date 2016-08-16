import pilasengine
pilas = pilasengine.iniciar()

oni = pilas.actores.Mono()

oni.imagen = pilas.imagenes.cargar('oni1.png')

oni.imagen_reir = pilas.imagenes.cargar('oni2.png')

oni.imagen_normal = pilas.imagenes.cargar('oni1.png')

oni.aprender('arrastrable')

papi = pilas.actores.Mono()

papi.imagen = pilas.imagenes.cargar('papi1.png')
papi.imagen_normal = pilas.imagenes.cargar('papinerd.png')
papi.imagen_reir =pilas.imagenes.cargar('papi1.png')
papi.aprender('arrastrable')

def capturar(oni, cosa):
 
	cosa.eliminar()
    
	oni.sonreir()
pinguin = pilas.actores.Pingu()
pilas.colisiones.agregar('mono', 'aceituna', capturar)
pilas.colisiones.agregar('mono', 'banana', capturar)
pelotas = pilas.actores.Pelota()*10
aceitunas = pilas.actores.Aceituna()*5
bananas = pilas.actores.Banana()*10
oni.aprender(pilas.habilidades.RebotarComoPelota)
bombas = pilas.actores.Bomba()*10
pilas.ver(bombas)