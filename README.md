# tallerLLM

En este taller intengramos un pequeño aplicativo que consulta documentos que ya hemos cargado a una base de datos pinecone como vectores que podemos consultar,
luego en base a un query del usuario, usamos una IA para leer estos archivos y obtener una respuesta.

## Iniciando

antes de iniciar toca tener los siguiente Prerrequisitos y tener el proyecto copiado en nuestro entorno local.

### Prerrequisitos

* Git 
* Python
* llave de el api de openai

### Instalando el proyecto

Debes abrir tu terminal, dirigirte al directorio donde quieras que este el proyecto y usar el siguiente comando

```
git clone https://github.com/santiagoOsp01/tallerLLM.git
```
luego te metes a este directorio y ejecutas los siguientes comandos

```
pip install langchain 
pip install openai==0.27.8
pip install tiktoken
pip install requests
pip install pydantic
pip install pinecone-client
```
ya despues de tener estas dependencias toca primero llenar nuestra base de datos en pinecone con los documentos que
aparecen en el directorio del proyectoy correr el siguiente script para subirlos a la base de datos que se llama textloader.py y lo corremos, haciendo los cambios necesarios
para subirlo a tu index en la base de datos, o este paso se puede saltar si se usa la base de datos ya configurada anteriormente, entonces esto no importaria ni se correria

![image](https://github.com/santiagoOsp01/tallerLLM/assets/111186366/9e33f8c2-dfb1-458f-a608-d7c9b9eca1fd)

si se quiere cambiar toca cambiar la variable llamada api_key y el nombre del index index_name="taller"

### Corriendo Localmente

Despues de haber configurado en ambiente de ejecución, podremos iniciar la aplicación

```
python .\app\main.py
```
y ya nos saldra una terminal donde le podrmos hacer varias preguntas y este nos responderia

![image](https://github.com/santiagoOsp01/tallerLLM/assets/111186366/95cb6887-8bde-4801-9956-3c92010f1087)


## Version

1.0-SNAPSHOT

## Autores

Santiago Ospina Mejia

## Licencia

GNU General Public License family

## Agradecimientos

* Luis Daniel Benavides Navarro
