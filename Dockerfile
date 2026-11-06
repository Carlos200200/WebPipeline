# 1. Usar una imagen oficial de Python ligera
FROM python:3.13-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
# Esto es por seguridad y no romper nada del container
# A partir de aqui toda operacion se hace en esta carpeta (nos movimos a ella)
WORKDIR /app

# 3. Copiar el archivo de dependencias primero (SOURCE DEST)
COPY requirements.txt .

# 4. Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código de la aplicación
# COPY <Fuente Local> <Destino Workdir>, No olvidar que estamos en /app 
COPY . .

# 6. Crear un usuario que sea quien ejecute la app
# Esto hay que hacerse despues de pip install
RUN useradd --create-home UsuarioApp

# 7. Asignar permisos
RUN chown -R UsuarioApp:UsuarioApp /app

# 8. Usar este usuario a partir de aqui
USER UsuarioApp

# 9. Exponer el puerto en el que corre Flask (por defecto 5000)
EXPOSE 5000

# 10. Comando para ejecutar la aplicación usando Gunicorn (estándar de producción)
# El valor final es <archivo python app.py> y <Variable que uno pone al llamar a flask>
# La cantidad de workers se puede especificar inclusive con una variable de entorno
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
