# Emprinet - Blog - Evaluation - Eleno Willians
 Prueba Tecnica para la empresa Emprinet : Blog con Flask y Postgresql

Challenger: Programador backend junior (Python - Flask- SQLAlchemy - PostgreSQL) 

Resumen :
En esta prueba técnica, estarás trabajando en una sencilla aplicación Flask que permite a los usuarios crear y ver "posts". Cada post debe tener un título, contenido y fecha/hora de creación. Utilizarás SQLAlchemy para definir e interactuar con una base de datos PostgreSQL que almacenará los posts.

Requisitos 
Deberás completar las siguientes tareas:
● Definir un modelo SQLAlchemy para la entidad Post, incluyendo los campos requeridos (id, title, content, y created_at). El campo id debe ser la clave primaria, y el campo created_at debe establecerse automáticamente a la fecha/hora actual cuando se crea un nuevo post. 
● Defina una ruta Flask que permita a los usuarios crear una nueva entrada a través de un formulario web. El formulario debe incluir campos para el título y el contenido de la entrada. 
● Definir una ruta Flask que permita a los usuarios ver una lista de todas las entradas, ordenadas por created_at en orden descendente. La lista debe incluir el título, el contenido y la fecha de creación de la entrada. 
● Definir una ruta Flask que permita a los usuarios ver una entrada específica por su id.

Restricciones
Usted debe adherirse a las siguientes restricciones: 
● Utilizar Python 3 y las últimas versiones de Flask, SQLAlchemy y psycopg2-binary. 
● Utilizar PostgreSQL como base de datos. 
● Utilizar la sintaxis declarativa de SQLAlchemy para definir el modelo Post. 
● Usar las plantillas incorporadas de Flask y el manejo de formularios para crear el formulario web para crear nuevas entradas. 
● Utilizar SQLAlchemy para consultar la base de datos y recuperar las entradas para su visualización. 
● Utiliza Git para el control de versiones, y confirma tu código regularmente mientras trabajas.

Estracto del Proyecto Terminado:
Se implementó además de un CRUD para la administración de los POSTS, un CRUD de comentarios sobre los POST.
Se distinguen tres tipos de vistas:
1- Pública: Cualquier usuario sin estar logueado, puede SOLO VER los posteos y comentarios realizados sobre los mismos, quien los realizó y su fecha.
2- Privada (Usuario común): Puede ver los posteos y los comentarios de otros usuarios, pero estos PUEDEN COMENTAR los posts.
3- Privada Privilegiada (Administrador): Puede realizar lo que realizan los otros dos niveles de usuarios, pero además SOLO EL PUEDE CREAR LOS POSTS, MODIFICARLOS O ELIMINARLOS.
Se implementó tambien un SISTEMA DE REGISTRO DE USUARIOS.
Se adicionaron templates teniendo como temática los colores y fotos de la empresa, como así tambien su logo.
Se estructuro el proyecto bajo la modalidad Blueprint a los fines de garantizar su escalabilidad.
