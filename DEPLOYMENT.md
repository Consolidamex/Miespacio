# TI Platform - Sistema de Gestión de Activos y Tickets

Una plataforma Django para la gestión de activos informáticos y creación de tickets de soporte.

## Características

- 📊 **Gestión de Activos IT**: Crear, editar, listar y eliminar activos con número de serie
- 🎫 **Sistema de Tickets**: Crear tickets, buscar, filtrar por estado y asignar
- 🔐 **Autenticación**: Sistema de login integrado
- 🔍 **Búsqueda y Filtrado**: Busca tickets por título/descripción y filtra por estado
- 📄 **Paginación**: Listados paginados (10 items por página)

## Requisitos Previos

- Python 3.11+
- pip
- SQLite3 (incluido con Python)

## Instalación Local

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Consolidamex/Miespacio.git
   cd ti_platform
   ```

2. **Crear y activar el entorno virtual**
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # Windows PowerShell
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones**
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Aplicación: http://127.0.0.1:8000
   - Admin: http://127.0.0.1:8000/admin/

## Despliegue en Producción

### Opción 1: Heroku/Railway

**Paso 1:** Prepare el proyecto
```bash
pip install gunicorn whitenoise
pip freeze > requirements.txt
```

**Paso 2:** Cree un Procfile (ya incluido)

**Paso 3:** Configure variables de entorno en la plataforma
- `SECRET_KEY`: Genere una clave segura
- `DEBUG`: false
- `ALLOWED_HOSTS`: your-domain.com

**Paso 4:** Despliegue
- Con Heroku: `git push heroku main`
- Con Railway: Conecte su repositorio GitHub

### Opción 2: PythonAnywhere

1. Registrarse en https://www.pythonanywhere.com/
2. Subir código vía Git
3. Configurar virtualenv
4. Crear web app Django 5.2
5. Actualizar ALLOWED_HOSTS en settings.py
6. Recargar la app

### Opción 3: DigitalOcean / AWS / Azure

Ejecute en servidor:
```bash
# Instalación
git clone <tu-repo>
cd ti_platform
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Ejecutar con gunicorn
gunicorn --bind 0.0.0.0:8000 --workers 4 config.wsgi
```

Configure Nginx/Apache como proxy inverso.

## Estructura del Proyecto

```
ti_platform/
├── config/              # Configuración principal
├── it_admin/            # App de gestión de activos
├── tickets/             # App de tickets
├── accounts/            # Autenticación
├── templates/           # Plantillas HTML
├── manage.py
├── requirements.txt
├── Procfile
└── runtime.txt
```

## URLs Disponibles

- `/` - Inicio (redirige a activos)
- `/it/` - Página de inicio de activos
- `/it/activos/` - Listar activos
- `/it/activos/crear/` - Crear activo
- `/it/activos/<id>/editar/` - Editar activo
- `/it/activos/<id>/eliminar/` - Eliminar activo
- `/tickets/listar/` - Listar tickets
- `/tickets/crear/` - Crear ticket (requiere login)
- `/tickets/<id>/` - Detalle del ticket
- `/accounts/login/` - Login
- `/accounts/logout/` - Logout
- `/admin/` - Panel de administración

## Notas de Seguridad

- Cambiar `SECRET_KEY` en producción
- Asegurar HTTPS
- Usar variables de entorno para configuración sensible
- Configurar base de datos robusta (PostgreSQL en producción)

## Soporte

Para issues o preguntas, contacte al equipo de desarrollo.
