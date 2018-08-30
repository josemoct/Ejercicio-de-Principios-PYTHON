# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class EmpresaAbstracta(object):

	def __init__(self, envio):
		self.envio=envio

	def recogerPaquete(self):
		print "Se ha recogido del paquete "
		self.envio.procesarEnvio()

	def enviarPaquete(self):
		self.envio.enviar()

	def entregarPaquete(self):
		self.envio.procesarEntrega()
		print "Se ha entregado el paquete "

class EmpresaServientrega(EmpresaAbstracta):

	def __init__(self,envio):
		super(EmpresaServientrega,self).__init__(envio)

class Envio(object):

	def procesarEnvio(self):
		pass

	def enviar(self):
		pass

	def procesarEntrega(self):
		pass

class EnvioAvion(Envio):

	def procesarEnvio(self):
		print "El paquete se ha cargado en el avion"

	def enviar(self):
		print "El paquete esta volando por el aire"

	def procesarEntrega(self):
		print "El paquete se ha descargado en el aeropuerto"

class EnvioBarco(Envio):

	def procesarEnvio(self):
		print "El paquete se ha cargado en el barco"

	def enviar(self):
		print "El paquete esta navegando por el mar"

	def procesarEntrega(self):
		print "El paquete se ha descargado en el puerto"


print "Transportes disponibles para enviar su pedido"
print "1. Envio por barco"
print "2. Envio por Avion"
transporteEnvio = input("Elija el tipo de transporte para entregar su pedido\n")

if transporteEnvio==1:
        envio = EnvioBarco()
elif transporteEnvio==2:
        envio = EnvioAvion()        


while transporteEnvio!=2 and transporteEnvio!=1:
        print "Introdusca un numero valido"
        transporteEnvio = input("Elija el tipo de transporte para entregar su pedido\n")
        if transporteEnvio==1:
                envio = EnvioBarco()
        elif transporteEnvio==2:
                envio = EnvioAvion()        


sucursal1 = EmpresaServientrega(envio)
sucursal1.recogerPaquete()
sucursal1.enviarPaquete()
sucursal1.entregarPaquete()
