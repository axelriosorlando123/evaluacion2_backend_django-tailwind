fruteria tienda mvc

aplicacion hecha en python usando django + tailwind

INSTRUCCIONES

descargar o clonar el repositorio

Si descargaste el `.zip`, descomprímelo en el escritorio

Luego abre una terminal dentro de esa carpeta con cm/powershell o en vscode:
---------------------------------------------------------------------------------------
crea un entorno virtual en la terminal:

py -m venv venv

Si aparece el error “running scripts is disabled…”, ejecuta (como administrador):

Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

Luego vuelve a activar:

.\venv\Scripts\Activate.ps1
---------------------------------------------------------------------------------------
INSTALA LAS DEPENDENCIAS

pip install django
---------------------------------------------------------------------------------------
APLICA MIGRACIONES

python manage.py makemigrations
python manage.py migrate
---------------------------------------------------------------------------------------
CREA UN USUARIO ADMINISTRADOR

python manage.py createsuperuser
---------------------------------------------------------------------------------------

EJECUTA EL SERVIDOR

python manage.py runserver
---------------------------------------------------------------------------------------

PARA ACCEDER A LA APLICACION VISITA:
- [http://127.0.0.1:8000](http://127.0.0.1:8000)
- [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

El proyecto incluye Tailwind vía CDN, en `catalogo/templates/catalogo/home.html`:

<script src="https://cdn.tailwindcss.com"></script>
------------------------------------------------------------------------------

FUNCIONALIDADES

Listar y crear productos,clientes,ventas 
CRUD completo
graficos de productos mas vendidos y clientes con mas ventas  
Mensajes de éxito/error
Sistema de registro e inicio de sesión para clientes.
Solo los usuarios autenticados pueden acceder a las funcionalidades que no son el.
Logout
Panel admin  
Base de datos SQLite

----------------------------------------------------------------------

COMANDOS

| Acción | Comando |
|--------|----------|
| Crear entorno virtual | `py -m venv venv` |
| Activar entorno virtual | `.\venv\Scripts\Activate.ps1` |
| Instalar dependencias | `pip install django` |
| Crear migraciones | `python manage.py makemigrations` |
| Aplicar migraciones | `python manage.py migrate` |
| Crear superusuario | `python manage.py createsuperuser` |
| Ejecutar servidor | `python manage.py runserver` |
| Salir del entorno | `deactivate` |

----------------------------------------------------------------------

EVALUACION 2 BACK END

APLICACION MVC 
alumno: Axel Ríos

Tecnologías:
Python 3.10+
Django 4.x
TailwindCSS (CDN)
SQLite3

