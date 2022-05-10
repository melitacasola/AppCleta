#Título del Proyecto AppCleta
App Cleta es un proyecto que comenzo con la idea de crear una comunidad donde, ciclistas de la ciudad y provincia de Cordoba puedan compartir sus rutas cotidianas.

Nos hemos divido la tarea entre los dos compañeros que quedamos en el cursado de Python:
Meli se encargo de ver como serian los formularios, datos a ingresar y que se encuentre estetita y funcionando los links en el Blog. A su vez, realiza el armado del videito del funcionamiento de la página.
Fer se encargo de elegir plantilla, dar preforma, y la parte de login, logout, registro y avatars. Además del armado del README, para poder colocar fotografías.-


Comenzando 🚀
Descarga los archivos de la app en tu PC


Mira Deployment para conocer como desplegar el proyecto.

Pre-requisitos 📋
Para que el programa funcione necitas tener Visual Studio Code o cualquier otro programa de similares caracteristicas.-


Da un ejemplo
Instalación 🔧
Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose
para poder ejecutar la App Ingresa a https://github.com/FersMeloni/AppCleta.git o https://github.com/melitacasola/AppCleta.git
1) hace click en el boton verde que dice "Code"
2) elegir la opcion "download ZIP"
![image](https://user-images.githubusercontent.com/102829516/167635493-f223eb5e-ff5f-47e6-9f86-a8828882d62e.png)

4) ir a la carpeta descargas
5) descomprimir el zip AppCleta-main
6) Abrir Visual Studio Code - 
7) Ir al menu Archivo y buscar la opción de 'Abrir Carpeta'
8) ![image](https://user-images.githubusercontent.com/102829516/167635943-ed3e28c6-6c42-4eb4-a5d2-27506892aca3.png)



9) Buscar la carpeta en donde descargaste el Zip AppCleta-main, deberas ver, 3 carpetas,  AppCleta, CletaPedia y Media
10) ![image](https://user-images.githubusercontent.com/102829516/167636241-5326f851-d818-42bd-8fe6-cd46e4ae40f9.png)




11) Presiona la opcion seleccionar carpeta, Visual Studio Code, puede preguntar si confias en los Autores de la carpeta, presiona que si en caso de querer ingrsar a la APP
12) una vez momentada la carpeta ir al Menu - Terminal y elegir la opcion 'Nuevo Terminal ' 
13) ![image](https://user-images.githubusercontent.com/102829516/167636446-5bb74207-b6b5-483f-8b07-0edf3992f81a.png)




14) Con el nuevo terminal abierto Abajo de la pantalla con el directorio dónde se encuentra el archivo manage.py ejecutamos el comando:
1) python manage.py check AppCoder
2) python manage.py makemigrations
3) python manage.py migrate
y por último:
4) python manage.py runserver
15) ![image](https://user-images.githubusercontent.com/102829516/167636814-6c686d23-01b8-4143-a4ba-6f19e829d1d6.png)

todos estos comandos, nos permitirán acceder a esta Base de Datos, y a la página sin problemas. 


16) si todo va bien deberia salir el siguiente dialogo
          System check identified no issues (0 silenced).
          May 10, 2022 - 09:58:40
          Django version 4.0.3, using settings 'CletaPedia.settings'
          Starting development server at http://127.0.0.1:8000/
          Quit the server with CTRL-BREAK. 
12) Presiona Ctrl + Click del Mouse en http://127.0.0.1:8000/ para ingresar a la APP


Ejecutando las pruebas ⚙️
Inicio de AppCleta
![image](https://user-images.githubusercontent.com/102829516/167637803-ec4e52bb-737d-4873-8d70-51208c808471.png)


En la Barra de navegacion podras accedar a los menus de la App, 
tene en cuenta que para acceder a algunos menus deberas estar logueado
![image](https://user-images.githubusercontent.com/102829516/167638260-4b0c67f5-e4f6-4537-81cb-13ce498bc7a3.png)



Tambien podras encontrar acceso a todos los menus en la pagina 
![image](https://user-images.githubusercontent.com/102829516/167638544-66e39f29-d140-4897-911c-b6c6ef4ca7ee.png)




Para ingresar 


![image](https://user-images.githubusercontent.com/102829516/167638682-95b0ef4c-5528-4a5d-b948-0eb3032d44d0.png)


Si no estas Registrado podras registar un usuario
![image](https://user-images.githubusercontent.com/102829516/167638810-b8bdf9c8-4519-4b0c-88c1-e805a3df24f1.png)


IMPORTANTE 📌
Para hacer Pruebas favor de utilizar
Usuario=Usuario
Password=Cambio.1

SuperUsusario para acceder al Panel de ADMIN
Usuario_Admin
Cambio.2



![image](https://user-images.githubusercontent.com/102829516/167645896-c9270cdf-9eb4-48c2-b12a-6ddcc4a28303.png)



en nosotros podras conocernos un poco mas a los que participamos de la cracion de la APP

![image](https://user-images.githubusercontent.com/102829516/167645977-71400e7a-e315-4c1d-8ac0-5d05a28840db.png)



en el Menu RutaBici podras ingresar las Rutas que quieres compartir con la comunidad tambien podras ver las Rutas cargadas por otros usuarios

![image](https://user-images.githubusercontent.com/102829516/167646091-e4d183fb-27e6-4333-be67-6fe2988f6fef.png)





![image](https://user-images.githubusercontent.com/102829516/167646297-6109fc21-2382-401a-b5e8-95d0972fd7e8.png)


En el munu Autores podras Ingresar tus datos como Autor de Rutas de Bici ver los Autores que participan de la comunidad


![image](https://user-images.githubusercontent.com/102829516/167646418-e2a17424-cae0-4c62-9bd4-9ca251128b17.png)



![image](https://user-images.githubusercontent.com/102829516/167646557-b1cc6488-1699-42f1-8dee-5dea364ee639.png)



Podras Buscar las rutas que Crean nuestros Autores 

![image](https://user-images.githubusercontent.com/102829516/167646747-217661e0-fda4-41ac-b4b6-34c33f5a333a.png)



![image](https://user-images.githubusercontent.com/102829516/167647008-a9a76d2b-d281-46b2-93db-d64580e94190.png)

En Desarrollo 🛠️
Al crear un usuario nuevo y navegar por la Pagina, puede salir un problema al intentar volver al inicio.
Al analizar el error, nos encontramos que el nuevo usuario no tiene asignado Avatar, este solo se puede asignar desde el panel de administracion.
el problema esta en estudio y se corregira para futuras versiones.-


Construido con 🛠️
Lenguaje Python /HTML
Herramienta: Visual Studio Code 
Framework: Django


Versionado 📌
Version 01

Autores ✒️ 
Melisa Casola - Trabajo Formularios, HTMLs y documentacion Tecnica
Fernando Meloni - Trabajo Registros, Avatar y documentacion Tecnica



Licencia 📄
Sin licencia, desarrolado para CODER-HOUSE

Expresiones de Gratitud 🎁
Gracias a nuestras familias, por el aguante!!
Gracias a los profesores, tutores (FRED!) y toda la comunidad CODER HOUSE por los aportes a la realizacion de esta APP
