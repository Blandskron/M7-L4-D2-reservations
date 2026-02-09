# Sistema de Reservas con Reestructuración de Modelo (Django)

Proyecto Django enfocado en **la evolución controlada del esquema de base de datos** mediante migraciones.  
El sistema parte con un modelo de reservas simple y avanza por múltiples etapas donde el esquema cambia de forma deliberada: nuevos campos, renombres, restricciones, índices y reglas de obligatoriedad.

El valor del proyecto está en **cómo se gestionan esos cambios**, no en la complejidad funcional.

---

## Objetivo

Demostrar de forma práctica cómo Django resuelve problemas reales de:

- Desfase entre modelo y base de datos
- Cambios frecuentes de requerimientos
- Versionado del esquema
- Despliegues consistentes entre entornos
- Reproducibilidad total del estado de la base de datos

---

## Problema que resuelven las migraciones

En un sistema real, el modelo de datos **evoluciona constantemente**:

- Se agregan campos nuevos
- Se renombran columnas
- Se cambian tipos de datos
- Se agregan índices por rendimiento
- Se endurecen reglas de obligatoriedad

Sin migraciones:
- cada cambio requiere SQL manual
- los entornos se desincronizan
- los despliegues fallan
- no existe trazabilidad

Las migraciones de Django funcionan como un **sistema de control de versiones del esquema**, permitiendo avanzar y retroceder de forma segura.

---

## Qué es una migración en Django

Una migración es un archivo versionado que describe **cómo transformar el esquema** desde un estado conocido a otro.

Características clave:
- Se aplican en orden
- Son reversibles
- Quedan registradas en la base de datos
- Permiten reconstruir el esquema desde cero

Django mantiene el historial en la tabla interna `django_migrations`.

---

## Estructura relevante del proyecto

```text
reservations/
├── admin.py
├── models.py
├── views.py
└── migrations/
    ├── 0001_initial.py
    ├── 0002_add_contact_and_status.py
    ├── 0003_rename_and_constraints.py
    └── 0004_constraints_and_indexes.py
````

Cada archivo de migración representa **una etapa real de evolución del sistema**.

---

## Evolución del modelo (resumen)

### Etapa 1 — Modelo base

* Reserva con código, nombre y fecha
* Estructura mínima

### Etapa 2 — Nuevos requerimientos

* Email de contacto
* Estado de la reserva
* Cantidad de personas
* Defaults para compatibilidad

### Etapa 3 — Reglas y semántica

* Renombre de campos
* Estados controlados (`choices`)
* Índice por fecha

### Etapa 4 — Endurecimiento del esquema

* Campos obligatorios
* Índices adicionales
* Timestamp de actualización

Cada cambio genera **una migración independiente**.

---

## Comandos del proyecto (flujo completo)

### 1. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 2. Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install django
pip install psycopg2-binary
```

---

### 3. Crear proyecto y app

```bash
django-admin startproject core .
python manage.py startapp reservations
```

Registrar la app en `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "reservations",
]
```

---

## Configuración PostgreSQL (básica, directa)

```python
# settings.py

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "reservations_db",
        "USER": "reservations_user",
        "PASSWORD": "strong_password",
        "HOST": "localhost",
        "PORT": "5432",
        "CONN_MAX_AGE": 60,
    }
}
```

---

## Migraciones — ciclo real de trabajo

### Generar migraciones

```bash
python manage.py makemigrations
```

Django:

* detecta cambios en `models.py`
* genera archivos de migración incrementales
* no toca la base de datos

---

### Aplicar migraciones

```bash
python manage.py migrate
```

Django:

* ejecuta migraciones pendientes
* sincroniza esquema real con el modelo
* registra cada ejecución

---

### Flujo típico tras cada cambio de modelo

```bash
python manage.py makemigrations reservations
python manage.py migrate
```

---

## Comandos de control y auditoría

Ver estado de migraciones:

```bash
python manage.py showmigrations
```

Ver SQL generado por una migración:

```bash
python manage.py sqlmigrate reservations 0003
```

Aplicar migraciones hasta un punto específico:

```bash
python manage.py migrate reservations 0002
```

Rollback completo de la app:

```bash
python manage.py migrate reservations zero
```

---

## Administración y verificación

Crear usuario administrativo:

```bash
python manage.py createsuperuser
```

Ejecutar servidor:

```bash
python manage.py runserver
```

Panel administrativo:

```
http://127.0.0.1:8000/admin
```

---

## Comentarios de base de datos

El modelo utiliza `db_comment` para documentar el esquema directamente en PostgreSQL.

Ejemplo:

```python
status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    db_comment="Estado controlado de la reserva"
)
```

Esto se traduce a comentarios reales a nivel de columna en la base de datos.
