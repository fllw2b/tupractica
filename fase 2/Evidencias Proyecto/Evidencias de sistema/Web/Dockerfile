FROM python:3.11-slim

# Instalar dependencias del sistema necesarias para MySQL y Pillow
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    python3-dev \
    libjpeg-dev \
    libpng-dev

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Establecer variables de entorno
ENV PORT=8000
ENV PYTHONUNBUFFERED=1

# Comando para ejecutar migraciones y luego gunicorn
CMD python manage.py migrate && gunicorn djangoTuPractica.wsgi
