# Sistema de Gestión de Estudiantes

Aplicación de escritorio desarrollada en **Python** con **Tkinter** y
**SQLite** para administrar estudiantes mediante operaciones CRUD
(Crear, Leer, Actualizar y Eliminar).

## Características

-   Agregar estudiantes.
-   Editar información existente.
-   Eliminar registros.
-   Actualizar la tabla de datos.
-   Base de datos local con SQLite.
-   Interfaz gráfica desarrollada con Tkinter.

## Tecnologías utilizadas

-   Python 3
-   Tkinter
-   SQLite3

## Estructura del proyecto

``` text
📁 proyecto/
│── sistema_estudiantes.py
│── estudiantes.db
└── README.md
```

## Instalación

1.  Clona el repositorio:

``` bash
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
```

2.  Entra en la carpeta del proyecto:

``` bash
cd TU-REPOSITORIO
```

3.  Ejecuta el programa:

``` bash
python sistema_estudiantes.py
```

## Base de datos

La aplicación crea automáticamente el archivo `estudiantes.db` la
primera vez que se ejecuta.

La tabla contiene los siguientes campos:

  Campo     Tipo
  --------- ---------
  id        INTEGER
  nombre    TEXT
  carrera   TEXT
  nota      REAL

## Captura de pantalla

Agrega aquí una imagen de la interfaz del programa cuando la subas a
GitHub.

``` md
![Sistema](captura.png)
```

## Autor

**Jandro**

Estudiante de Desarrollo de Software.

## Licencia

Este proyecto fue desarrollado con fines educativos.
