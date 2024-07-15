# ECOMMERCE

1. [`CREACIÓN DE ENTORNO VIRTUAL DE PYTHON`](#creacion-entorno-virtual)
    1. 1.[`CREACIÓN ENTORNO VIRTUAL EN WINDOWS`](#creacion-entorno-virtual-windows)
    1. 2.[`CREACIÓN ENTORNO VIRTUAL EN LINUX (UBUNTU)`](#creacion-entorno-virtual-linux)
2. [`INSTALACIÓN DE DEPENDENCIA EN ENTORNO VIRTUAL`](#instalacion-dependencias)
3. [`DESPLIEGUE MYSQL CON DOCKER`](#despliegue-mysql-docker)
4. [`CONFIGURACIÓN MYSQL EN MÁQUINAS DUOC`](#configurar-mysql-duoc)
5. [`CONFIGURACIÓN MYSQL EN DJANGO`](#configuracion-mysql-django)
6. [`MIGRACIÓN ESQUEMA DJANGO EN MYSQL`](#migracion-esquema-django-mysql)
7. [`DESPLIEGUE APLICACIÓN WEB`](#despliegue-aplicacion-web)


<a name="creacion-entorno-virtual"></a>

## CREACIÓN DE ENTORNO VIRTUAL DE PYTHON

Como buena práctica la industria se decanta por la generación de ambientes virtuales a la hora del desarrollo de aplicaciones. Esto permite mejorar y configurar solo las dependencias necesarias para la compilación y despliegue de proyectos, utilizando de forma óptima los recursos.

<a name="creacion-entorno-virtual-windows"></a>

### CREACIÓN ENTORNO VIRTUAL EN WINDOWS

Para crear un entorno virtual en python deberemos descargar en windows la siguiente libreria con pip.

```shell
pip install virtualenv
```

Posteriormente deberemos crear nuestro entorno virtual con el comando.

```shell
virtualenv env
```

**Nota**: 
- env corresponde al nombre de nuestro entorno virtual puede tener cualquier nombre, pero este directorio no debe ser copiado ni compartido ya que almacena rutas del computador donde se cree.
- Debe estar instalado y configurado los path de python y de pip.

Para activar el entorno virtual deberemos ejecutar el siguiente comando desde gitbash.

```shell
. env/Scripts/activate
```

<a name="creacion-entorno-virtual-linux"></a>

### CREACIÓN ENTORNO VIRTUAL EN LINUX (UBUNTU)

Para crear un entorno virtual en python deberemos descargar en linux la siguiente libreria con pip.

```shell
sudo pip3 install virtualenv
```

Posteriormente deberemos crear nuestro entorno virtual con el comando.

```shell
virtualenv env
```

**Nota**: 
- env corresponde al nombre de nuestro entorno virtual puede tener cualquier nombre, pero este directorio no debe ser copiado ni compartido ya que almacena rutas del computador donde se cree.
- Debe estar instalado y configurado los path de python y de pip.

Para activar el entorno virtual deberemos ejecutar el siguiente comando desde una terminal.

```shell
source env/bin/activate
```


<a name="instalacion-dependencias"></a>

## INSTALACIÓN DE DEPENDENCIA EN ENTORNO VIRTUAL

Para instalar las dependencias dentro de nuestro entorno virtual utilizamos el siguiente comando.

```shell
pip install -r requirements.txt
```


<a name="despliegue-mysql-docker"></a>

## DESPLIEGUE MYSQL CON DOCKER

Para desplegar el motor de MySQL deberemos ejecutar los siguientes comandos.

### DOCKER BUILD IMAGE

Comando para construir imagen docker con mysql.

```shell
docker build -t mysql-portafolio-db:1.0.0 .
```

### DOCKER RUN CONTAINER

Comando para crear un contenedor con el motor en ejecución

```shell
docker run -d -p 3306:3306 --name mysql-portafolio-container  mysql-portafolio-db:1.0.0
```

Para conectarse a MySQL que se encuentra en el contenedor de docker mediante Workbench MySQL se deben usar los siguientes datos.

```shell
username: root
password: 1234567890
host: 127.0.0.1
port: 10306
database: ecommerce_db
```

<a name="configurar-mysql-duoc"></a>

## CONFIGURACIÓN MYSQL EN MÁQUINAS DUOC

Para poder hacer uso de MySQL en duoc junto a Django es de vital importancia actualizar la contraseña de MySQL, ya que no posee una. Para ello debemos ingresar a Workbench MySQL y ejecutar el siguiente script.


```shell
USE mysql;
ALTER USER 'root'@'localhost' IDENTIFIED BY '1234567890';
FLUSH PRIVILEGES;

CREATE DATABASE ecommerce_db;
```

<a name="configuracion-mysql-django"></a>

## CONFIGURACIÓN MYSQL EN DJANGO

Se debe configurar la conexión de MySQL en Django dentro del archivo setting.py.


```shell
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_db',
        'USER': 'root',
        'PASSWORD': '1234567890',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**Nota:** Los datos pueden variar dependiendo de configuración de la base de datos que se utilice.


<a name="migracion-esquema-django-mysql"></a>

## MIGRACIÓN ESQUEMA DJANGO EN MYSQL

Para migrar el esquema que posee django deberemos ejecutar los comandos.

```shell
python manage.py makemigrations
python manage.py migrate
```

Para crear un usuario para el mantenedor (admin) se debe ejecutar el comando.

```shell
python manage.py createsuperuser
```

<a name="despliegue-aplicacion-web"></a>

## DESPLIEGUE APLICACIÓN WEB

Para desplegar la aplicación web ejecutamos el siguiente comando.

```shell
python manage.py runserver
```

Para visualizar el sitio deberemos hacerlo en la ruta [http://localhost:8000](http://localhost:8000)
