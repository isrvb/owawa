from zapv2 import ZAPv2

# Configurar el objeto ZAP
zap = ZAPv2()

# Iniciar una nueva sesión en ZAP
zap.core.new_session()

# Configurar el objetivo del escaneo
target = "http://example.com"
zap.core.access_url(target)

# Esperar hasta que el escaneo esté completo
while int(zap.pscan.records_to_scan) > 0:
    print('Escaneando... {} URLs restantes'.format(zap.pscan.records_to_scan))
    time.sleep(2)

# Obtener los resultados del escaneo
alerts = zap.core.alerts()

# Mostrar los resultados del escaneo
for alert in alerts:
    print('URL: {}'.format(alert['url']))
    print('Prioridad: {}'.format(alert['risk']))
    print('Descripción: {}'.format(alert['description']))
    print('---')
