# MiProyecto
Visionarios 04 ficha 2348223


## Contribuir

Para contribuir sigue estos pasos: 

1. Crea el entorno en python el comando es:
```
python -m venv <nombre de tu entorno>: recomendado "env"
```

2. Añade el nombre de tu entorno al archivo `.gitignore` env ya está.

3. Instala las dependencias del proyecto usando el comando:
```
pip install -r requirements.txt
```

4. Usando el archivo `.env.example` crea tu archivo `.env` con los parametros y rellenalos con sus respectivas credenciales, por ejemplo: DB_PORT=3306 que es el puerto por defecto de mysql.

5. Si estas utilizando otra base de datos debes installar el driver que exige [Django](https://docs.djangoproject.com/en/4.1/ref/databases/) por ejemplo: `pip install pymysql`

6. Comandos basicos para ejecutar: 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Como realizar Backup de la base de datos

Los backups se crearan en la carpeta `./backups`.
Sigue estos comandos:
- Hacer un backup: `python manage.py dbbackup` 
- Restaurar a un backup: `python manage.py dbrestore -i <nombre del backup .dump>`.
  Ejemplo: `python manage.py dbrestore -i default-Usuario-2022-12-14-184641.dump`


### Errores conocidos

Estos son unos de los errores conocidos del proyecto y sus soluciones.

- Al crear un backup: Error running mysqldump: El sistema no puede encontrar el archivo.
  Solución: Añadir la ruta de `C:\Program Files\MySQL\MySQL Server 8.0\bin` en las variables de entorno que es donde se encuentra el archivo `mysqldump.exe` de igual forma con los otros drivers (base de datos) con su respectivo dump.