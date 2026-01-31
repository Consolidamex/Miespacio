# Despliegue en PythonAnywhere - Guía Paso a Paso

## Paso 1: Registrarse en PythonAnywhere

1. Ve a https://www.pythonanywhere.com/
2. Haz clic en "Sign up"
3. Elige el plan **Beginner** (gratis, suficiente para pruebas)
4. Completa el formulario y verifica tu email

## Paso 2: Acceder a tu Cuenta

1. Inicia sesión en tu dashboard
2. Necesitarás el usuario y contraseña que creaste

## Paso 3: Descargar el Código desde GitHub

En la consola web de PythonAnywhere:

```bash
# Ve a tu directorio home
cd ~

# Clona tu repositorio
git clone https://github.com/Consolidamex/Miespacio.git
cd Miespacio
```

## Paso 4: Crear un Virtualenv

1. Ve a **Web app** → **Add a new web app**
2. Elige **Manual configuration**
3. Selecciona **Python 3.11**
4. En la siguiente pantalla, verás el comando para crear el virtualenv:

```bash
mkvirtualenv --python=/usr/bin/python3.11 miespacio
```

Ejecuta este comando en la consola web de PythonAnywhere.

## Paso 5: Instalar Dependencias

Con el virtualenv activado:

```bash
pip install -r ~/Miespacio/requirements.txt
```

## Paso 6: Configurar la Web App

1. Ve a **Web app** → Tu app (debería aparecer)
2. En **Code** → **Source code**: `/home/tu_usuario/Miespacio`
3. En **Virtualenv**: `/home/tu_usuario/.virtualenvs/miespacio`
4. En **WSGI configuration file**: Haz clic para editar

Reemplaza el contenido del WSGI con:

```python
import os
import sys

# Agregar el directorio del proyecto
path = '/home/tu_usuario/Miespacio'
if path not in sys.path:
    sys.path.append(path)

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Reemplaza `tu_usuario` con tu nombre de usuario de PythonAnywhere**

## Paso 7: Ejecutar Migraciones

En la consola web:

```bash
cd ~/Miespacio
python manage.py migrate
```

## Paso 8: Crear Superusuario

```bash
python manage.py createsuperuser
```

Ingresa:
- **Username:** (tu usuario)
- **Email:** (tu email)
- **Password:** (contraseña segura)

## Paso 9: Configurar Variables de Entorno

En **Web app** → Tu app → **Edit web config**

Añade en la sección de variables de entorno:

```
DEBUG=False
ALLOWED_HOSTS=tu_usuario.pythonanywhere.com
SECRET_KEY=tu-clave-secreta-larga-y-aleatoria
```

### Generar SECRET_KEY segura:

En la consola web:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copia el resultado y úsalo como `SECRET_KEY`.

## Paso 10: Recargar la App

1. Ve a **Web app** → Tu app
2. Haz clic en el botón **Reload** (arriba en verde)
3. Espera 30 segundos

## Paso 11: Acceder a tu Aplicación

Tu app estará disponible en:
```
https://tu_usuario.pythonanywhere.com/
```

## URLs Principales

- https://tu_usuario.pythonanywhere.com/it/ — Activos
- https://tu_usuario.pythonanywhere.com/it/activos/ — Listar activos
- https://tu_usuario.pythonanywhere.com/tickets/listar/ — Tickets
- https://tu_usuario.pythonanywhere.com/admin/ — Panel admin

## Troubleshooting

### Si ves error 500:

1. Ve a **Web app** → **Error log** y revisa los errores
2. Asegúrate de que `ALLOWED_HOSTS` contenga tu dominio
3. Verifica que las migraciones se ejecutaron correctamente

### Si ves "ModuleNotFoundError":

1. Verifica que el virtualenv esté correctamente configurado
2. Ejecuta: `pip install -r ~/Miespacio/requirements.txt` nuevamente

### Archivos estáticos no cargan (CSS/JS):

En la consola:

```bash
cd ~/Miespacio
python manage.py collectstatic --noinput
```

## Actualizar Código Después

Cuando hagas cambios en GitHub:

```bash
cd ~/Miespacio
git pull origin master
python manage.py migrate  # Si agregaste migraciones
```

Luego recarga la app en el panel de PythonAnywhere.

## Pasar del Plan Gratuito a Pago

Si necesitas:
- Dominio propio (en lugar de pythonanywhere.com)
- Más recursos
- Acceso a bases de datos

Actualiza tu plan en **Account** → **Billing**

---

**¿Necesitas ayuda con algún paso específico?**
