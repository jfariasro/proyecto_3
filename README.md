# 🧠 Plataforma Quiz Interactiva

Una plataforma educativa interactiva desarrollada en Django que permite crear, administrar y participar en quizzes educativos con resultados en tiempo real.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Funcionalidades](#-funcionalidades)
- [API y Vistas](#-api-y-vistas)
- [Comandos Administrativos](#-comandos-administrativos)
- [Despliegue](#-despliegue)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

## ✨ Características

- **🎯 Quizzes Interactivos**: Creación y participación en quizzes educativos
- **⚡ Resultados en Tiempo Real**: Calificación automática e inmediata
- **📊 Panel de Administración**: Gestión completa de quizzes, preguntas y usuarios
- **📁 Carga de Archivos**: Creación masiva de quizzes desde archivos de texto
- **📈 Estadísticas y Reportes**: Seguimiento del progreso y rendimiento
- **🏆 Sistema de Puntuación**: Rankings y tabla de posiciones
- **📱 Diseño Responsivo**: Compatible con dispositivos móviles y desktop
- **🔄 Paginación**: Navegación eficiente en listas grandes
- **📋 Resultados Detallados**: Revisión completa de respuestas correctas e incorrectas

## 🛠 Tecnologías

- **Backend**: Django 5.0.6
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Iconos**: Bootstrap Icons
- **Servidor Web**: Gunicorn (producción)
- **Python**: 3.12.3

## 📋 Requisitos Previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- Git
- Navegador web moderno

## 🚀 Instalación

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd proyecto_3
```

### 2. Crear Entorno Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear Superusuario

```bash
python manage.py createsuperuser
```

### 6. Generar Datos de Ejemplo (Opcional)

```bash
python manage.py generar_quizzes
```

### 7. Ejecutar Servidor de Desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## ⚙️ Configuración

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto (opcional para desarrollo):

```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Configuración de Red Local

Para acceder desde otros dispositivos en la red local:

1. Ejecuta el servidor especificando la IP:
```bash
python manage.py runserver 0.0.0.0:8000
```
## 📖 Uso

### Para Usuarios

1. **Registro**: Crea una cuenta nueva desde `/register/`
2. **Login**: Inicia sesión desde `/login/`
3. **Explorar Quizzes**: Ve los quizzes disponibles en la página principal
4. **Participar**: Haz clic en "Comenzar Quiz" y responde las preguntas
5. **Ver Resultados**: Revisa tus resultados detallados al finalizar
6. **Perfil**: Consulta tu historial y estadísticas en `/profile/`

### Para Administradores

1. **Panel Admin**: Accede a `/admin-panel/` (requiere permisos de staff)
2. **Crear Quizzes**: Usa el formulario web o sube archivos de texto
3. **Gestionar Preguntas**: Agrega/edita preguntas y opciones
4. **Monitorear Participaciones**: Ve estadísticas y reportes
5. **Django Admin**: Acceso completo via `/admin/`

## 🎯 Funcionalidades

### Sistema de Quizzes

- **Creación Manual**: Formularios web intuitivos
- **Carga Masiva**: Desde archivos de texto estructurados
- **Tipos de Pregunta**: Opción múltiple, verdadero/falso
- **Configuración**: Tiempo límite, estado activo/inactivo

### Formato de Archivo para Carga Masiva

```text
Titulo del Quiz: Quiz de Programación
Descripcion: Preguntas básicas de programación

Pregunta: ¿Cuál es la salida de print("Hola")?
A) Hola
B) "Hola" *
C) Error
D) Ninguna

Pregunta: ¿Qué significa HTML?
A) HyperText Markup Language *
B) High Tech Modern Language
C) Home Tool Markup Language
D) Hyper Transfer Markup Language
```

**Reglas del formato:**
- `*` al final de una opción indica que es correcta
- `Titulo del Quiz:` y `Descripcion:` son opcionales
- Cada pregunta debe tener al menos 2 opciones
- Soporta opciones A) B) C) D) E) F)

### Sistema de Usuarios

- **Registro y Autenticación**: Sistema completo de usuarios
- **Perfiles**: Estadísticas personales y historial
- **Roles**: Usuarios normales y administradores (staff)
- **Participaciones**: Registro único por usuario/quiz

### Panel de Administración

- **Dashboard**: Vista general con estadísticas
- **Gestión de Quizzes**: CRUD completo
- **Gestión de Preguntas**: Editor avanzado
- **Gestión de Opciones**: Control detallado
- **Reportes**: Participaciones y estadísticas

## 🔧 API y Vistas

### URLs Principales

```python
# Usuarios
/                          # Lista de quizzes
/quiz/<id>/               # Detalle del quiz
/quiz/<id>/submit/        # Envío de respuestas
/quiz/results/<id>/       # Resultados detallados
/profile/                 # Perfil del usuario
/leaderboard/            # Tabla de posiciones

# Administración
/admin-panel/                              # Dashboard admin
/admin-panel/quizzes/                     # Lista de quizzes
/admin-panel/quiz/create/                 # Crear quiz
/admin-panel/quiz/<id>/edit/              # Editar quiz
/admin-panel/upload-quiz/                 # Subir archivo
/admin-panel/download-example/            # Descargar ejemplo
```

### Modelos de Datos

- **Quiz**: Título, descripción, fecha, estado, tiempo límite
- **Pregunta**: Texto de la pregunta, relación con quiz
- **Opcion**: Texto de opción, marca si es correcta
- **Participacion**: Usuario, quiz, puntaje, tiempo, estado
- **Respuesta**: Relación participación-pregunta-opción

## 🎮 Comandos Administrativos

### Generar Datos de Ejemplo

```bash
python manage.py generar_quizzes
```

### Cargar Quiz desde Archivo

```bash
python manage.py cargar_quiz_archivo archivo.txt --titulo "Mi Quiz" --descripcion "Descripción" --tiempo 30
```

### Otros Comandos Útiles

```bash
# Colectar archivos estáticos
python manage.py collectstatic

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Shell interactivo
python manage.py shell
```

## 🌐 Despliegue

### Heroku

1. Instala Heroku CLI
2. Crea app: `heroku create mi-app-quiz`
3. Configura variables: `heroku config:set SECRET_KEY=...`
4. Deploy: `git push heroku main`

### Servidor Local

1. Configura Gunicorn: `gunicorn plataforma_quiz_interactiva.wsgi`
2. Usa nginx como proxy reverso
3. Configura SSL/HTTPS para producción

### Docker (Opcional)

```dockerfile
FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "plataforma_quiz_interactiva.wsgi"]
```

## 📂 Estructura del Proyecto

```
proyecto_3/
├── manage.py                          # Comando principal de Django
├── requirements.txt                   # Dependencias Python
├── runtime.txt                       # Versión de Python
├── Procfile                          # Configuración Heroku
├── ejemplo_quiz.txt                  # Archivo de ejemplo
├── plataforma_quiz_interactiva/      # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py                   # Configuración Django
│   ├── urls.py                       # URLs principales
│   └── wsgi.py                       # WSGI para producción
└── quizzes/                          # Aplicación principal
    ├── __init__.py
    ├── admin.py                      # Configuración admin Django
    ├── apps.py                       # Configuración de la app
    ├── models.py                     # Modelos de datos
    ├── views.py                      # Vistas y lógica
    ├── forms.py                      # Formularios
    ├── urls.py                       # URLs de la app
    ├── utils.py                      # Utilidades
    ├── management/commands/          # Comandos personalizados
    ├── migrations/                   # Migraciones de BD
    ├── templates/                    # Plantillas HTML
    └── templatetags/                 # Tags personalizados
```

## 🎨 Características de la Interfaz

- **Diseño Moderno**: Bootstrap 5 con gradientes y animaciones
- **Responsive**: Compatible con móviles y tablets
- **Iconografía**: Bootstrap Icons para mejor UX
- **Paginación**: Navegación eficiente en listas grandes
- **Feedback Visual**: Alertas, modales y estados de carga
- **Temas**: Paleta de colores consistente
- **Accesibilidad**: Etiquetas ARIA y navegación por teclado

## 🐛 Solución de Problemas

### Errores Comunes

1. **ModuleNotFoundError**: Verifica que el entorno virtual esté activado
2. **Error de migración**: Ejecuta `python manage.py migrate`
3. **Error 500**: Revisa `DEBUG=True` en settings.py para desarrollo
4. **Archivos estáticos**: Ejecuta `python manage.py collectstatic`

### Logs y Debugging

```python
# En settings.py para desarrollo
DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit: `git commit -am 'Agrega nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

### Estándares de Código

- Seguir PEP 8 para Python
- Documentar funciones y clases
- Escribir tests para nuevas funcionalidades
- Usar nombres descriptivos para variables y funciones

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

- **Documentación**: Este README
- **Issues**: Usa el sistema de issues de GitHub

## 🔄 Changelog

### v1.0.0 (2025-06-28)
- ✅ Sistema completo de quizzes
- ✅ Panel de administración
- ✅ Carga masiva desde archivos
- ✅ Resultados detallados
- ✅ Paginación en todas las vistas
- ✅ Diseño responsivo
- ✅ Sistema de usuarios y autenticación

---

⭐ **¡Dale una estrella si te gusta el proyecto!** ⭐
