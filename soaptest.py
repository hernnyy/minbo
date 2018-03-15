from suds.client import Client

proxySettings = {'http':'http://TAH55733:207324u4@srispw003p000.bancopatagonia.net.ar:8080/'}
client = Client(url='http://www.banguat.gob.gt/variables/ws/TipoCambio.asmx?WSDL',proxy = proxySettings)
##client.set_options()

request = client.factory.create('tns:Variables')
request.variable = '29'
##request.CountryName = 'Venezuela'
response = client.service.Variables(request)
print(request)
##print(response)
print(response.CambioDia.Var[0].venta)
print(response.CambioDia.Var[0].compra)


request1 = client.factory.create('tns:TipoCambioFechaInicialMoneda')
request1.moneda = '29'
request1.fechainit = '10/03/2018'
response1 = client.service.TipoCambioFechaInicialMoneda(request1)
print(request1)
print(response1.Vars.Var[2].venta)
#print(response1.CambioDia.Var[0].compra)