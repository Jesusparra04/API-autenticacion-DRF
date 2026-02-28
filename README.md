 ## 🚀 API de Autenticación – Django REST Framework (DRF)

API de autenticación de usuarios desarrollada con Django y Django REST Framework (DRF), utilizando autenticación basada en Token.

Permite el registro, inicio de sesión, autenticación y gestión básica de usuarios mediante endpoints seguros.

## 📌 Tecnologías Utilizadas

🐍 Python

🌐 Django

🔗 Django REST Framework

🔐 Token Authentication

🗄️ SQLite / PostgreSQL / MySQL (configurable)



## ⚙️ Instalación
1️⃣ Clonar el repositorio
git clone https://github.com/Jesusparra04/API-autenticacion-DRF.git
cd nombre-del-repo
2️⃣ Crear y activar entorno virtual
python -m venv venv

En Windows:

venv\Scripts\activate

En Linux/Mac:

source venv/bin/activate
3️⃣ Instalar dependencias
pip install -r requirements.txt
4️⃣ Aplicar migraciones
python manage.py migrate
5️⃣ Crear superusuario (opcional)
python manage.py createsuperuser
6️⃣ Ejecutar servidor
python manage.py runserver
🔐 Configuración de Autenticación por Token

En settings.py:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

Luego ejecutar:

python manage.py migrate
📡 Endpoints Principales
📝 Registro de usuario

POST /api/register/

{
  "username": "usuario",
  "email": "correo@email.com",
  "password": "12345678"
}
🔑 Login (Obtener Token)

POST /api/login/

{
  "username": "usuario",
  "password": "12345678"
}

Respuesta:

{
  "token": "abc123xyz456..."
}
👤 Perfil de Usuario (Protegido)

GET /api/profile/

Headers:

Authorization: Token abc123xyz456...
🧪 Cómo probar la API


## Puedes usar:

Postman

Insomnia

Thunder Client (VS Code)

curl

##
Autenticación basada en Token

Endpoints protegidos

Manejo de permisos

Validación de datos con Serializers


## 📌 Mejoras Futuras

Refresh Token con JWT

Recuperación de contraseña

Confirmación por email

Roles y permisos personalizados

## autor: Jesús Parra
Backend Developer | Flask & Django




