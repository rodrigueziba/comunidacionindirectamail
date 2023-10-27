
# Comunicación indirecta - Emulador Correo Masivo

Consigna:
Gestión de Colas de Correo Electrónico: En sistemas de envío de correos masivos, las colas de mensajes aseguran la entrega eficiente de correos electrónicos y permiten reintentos en caso de fallos. 
Se pide: 
Emular clientes que pretenden enviar correos "masivos" y el servidor de correos que deberá realizar la correspondiente entrega. De ser posible agregue de forma aleatoria la eventualidad de que un correo no pueda entregarse y deba reintentar más tarde.



## Instalación

Descargar https://www.apache.org/dyn/closer.cgi?filename=/activemq/5.18.3/apache-activemq-5.18.3-bin.zip&action=download

```bash
  cd [activemq_install_dir]
```

Donde [activemq_install_dir] es donde esté descompmrimido ActiveMQ. Por ejemplo c:\Archivos de programa\ActiveMQ-5.x.
Después


```bash
  bin\activemq start
```
    

# Ver la interfaz de administrador
Abrir
URL: http://127.0.0.1:8161/admin/

Login: admin

Passwort: admin

# Para modificar el ip del servidor en caso que este configurado como localhost

Ubicar y abrir el archivo de configuración principal de Apache ActiveMQ se llama activemq.xml, en la carpeta conf. 

Modificar la dirección IP localhost y el puerto 61616. Debes cambiar localhost a la dirección IP o el nombre de host de la máquina desde la que queres que ActiveMQ escuche las conexiones. Para escuchar en todas las interfaces de red, cambia de localhost a 0.0.0.0:


```bash
<transportConnector name="openwire" uri="tcp://0.0.0.0:61616?maximumConnections=1000&amp;wireFormat.maxFrameSize=104857600"/>
```


# Instalar stomp
 Para poder usar ActiveMQ con python

```bash
  pip install stomp.py
```

# Instalar faker
 Para poder generar datos aleatorios

```bash
  pip install Faker
```

En dos terminales o maquinas diferentes ejecutar

```bash
  python mail.py
```
