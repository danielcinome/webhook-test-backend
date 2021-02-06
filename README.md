# Prueba tecnica - TodoLegal

## Proyecto
1. Generar mockup data de un valor de cambio de las siguientes opciones en 5 días diferentes: 
		Euros a dólares
		Pesos chilenos a dólares
		Soles a dólares
2. Almacenar los datos de valor de cambio en una base de datos.
3. Desarrollar un prototipo de API REST que permite consultar el valor de cambio almacenado en la base de datos
4. Al finalizar el proceso que golpee el webhook con URL https://webhook.site/14693700-0cce4ef4-9961-e927cf90c008 con un body que incluya el cambio consultado


## Descripción
Para la solución de este proyecto he utilizado el lenguaje de programación Python y usado un entorno virtual para evitar el conflicto de dependencias y para que se facilite la ejecución en otro entorno local. A continuación encontrarás los pasos para ejecutar el proyecto en tu máquina local.
####  Configuración
1. clonar el repositorio `git clone https://github.com/danielcinome/todolegal-test-backend.git`

2. ir a la carpeta todolegal-test-backend con el comando `cd todolegal-test-backend`
---

File Name|Description
---|---
[config_venv	](https://github.com/danielcinome/todolegal-test-backend/blob/main/config_venv)| En éste archivo encontrara la configuración para su ambiente local, contiene una serie de scripts de instalación de paquetes necesarios para correr el proyecto.
|.env| Crea este Archivo de manera local. NO esta presente en el repositorio por buenas practicas, sin embargo por fines de prueba, dejo los keys=values necesarios.
`API_HOTS=127.0.0.1`
`API_POTR=3000`
`WEBHOOK_URL="https://webhook.site/83bee475-9903-4dc0-b23c-dd44b0a2582b"`

#### Nota: El webhook proporcionado en la descripción de la prueba parece haber caducado por lo cual genere el del key `WEBHOOK_URL`

3. Para la instalación ejecute el siguiente comando `./config_venv` y espere un tiempo a que finalice el proceso.

En este punto usted tiene su ambiente listo para empezar a correr el proyecto.

4. Ahora iniciaremos nuestro entorno virtual con el siguiente comando
	`source venv/bin/activate`
	
	![N|Solid](https://i.ibb.co/wr5YLWQ/venv.png)

5. En una nueva terminal debemos iniciar la base de datos, para esto puede usar
	`sqlite3 mock_data_db/mock_data.db`
	
	![N|Solid](https://i.ibb.co/pPPW450/termianlsql.png")

6. Perfecto, ahora podemos correr el archivo principal, para esto use
	`python3 api/v1/server.py`
	
	![N|Solid](https://i.ibb.co/bvTbvPR/runproject.png" )


Nuestro proyecto ahora esta corriendo, así que puedes empezar hacer las consultas a nuestra Api, para esto he dejado una descripción de los endpoints y cómo debes realizar las consultas.

---
### EndPoints
| Path | Method | Description   |
|--|--|--|
| `/api/exchange_value/<par_divisas>` | get | Obtiene todos los registros de un par de divisas  |
| `/api/exchange_value/<par_divisas>/<date>` | get | Obtiene el valor de cambio de un par de divisa en base a la fecha |
---
### Realizando consultas
En este paso he hecho uso de postman, el cual nos permite de manera rápida probar nuestros endpoints, veamos.

![N|Solid](https://i.ibb.co/GPkZX3d/postman.png )

En esta primera petición e usado el endpoint `/api/exchange_value/pen-usd` el cual me responde con todos los registros existentes en la base de datos del par de divisas PEN-USD, con esto ahora tomaremos una fecha y usaremos el siguiente endpoint.

![N|Solid](https://i.ibb.co/HpgCVD0/postman2.png)

Cómo vez hemos usado `/api/exchange_value/pen-usd/1-5-2021` agregando la fecha que escogimos anterior mente y ahora podemos ver el valor de cambio presente en esa fecha. por ultimo veamos cómo hemos golpeado nuestro webhook.

![N|Solid](https://i.ibb.co/6WfqsDV/webhopok.png)


## Author

- Daniel Chinome - [Github](https://github.com/danielcinome) / [Twitter](https://twitter.com/DanielChinome)
