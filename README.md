# 💇‍♀️ Web de Peluquería – Backend en Django

Este proyecto es el backend completo de una web de peluquería, desarrollado íntegramente con Django. Está diseñado para integrarse con una plantilla frontend ya existente en HTML/CSS/JS, proporcionando funcionalidades administrativas y de gestión de datos.

## ✨ Funcionalidades principales

- Panel de administración de Django para:
  - Añadir y editar empleados
  - Gestionar precios y horarios
- Gestión de correos electrónicos (confirmaciones, notificaciones, etc.)
- Integración con plantilla frontend 
- Estructura escalable y segura para despliegue en producción

## ⚙️ Requisitos

- Python 3.8+
- Django 4.x
- Base de datos SQLite (no incluida)
- Entorno virtual recomendado

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/web-peluqueria-backend.git
   cd web-peluqueria-backend

2. Crea y activa un entorno virtual:
```bash
  python -m venv env
  source env/bin/activate  # En Windows: env\Scripts\activate
```
3. Instala las dependencias:
```bash
   pip install -r requirements.txt
```
4. Crea el archivo settings.py dentro del directorio del proyecto Django.
⚠️ Importante: Por motivos de seguridad, el archivo settings.py no se incluye en este repositorio.
 Debes crearlo manualmente, configurando tus claves secretas, parámetros de correo electrónico y base de datos.
 (En mi proyecto usé MailTrap).

5. Realiza las migraciones:
```bash
   python manage.py makemigrations
   python manage.py migrate
```
6. Crea un superusuario para acceder al panel de administración:
```bash
   python manage.py createsuperuser
```
7. Ejecuta el servidor:
```bash
  python manage.py runserver
```

# 📬 Gestión de correos
El proyecto incluye lógica para el envío de correos electrónicos (por ejemplo, confirmaciones de citas).
Recuerda configurar los parámetros SMTP en tu settings.py:

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.tuservidor.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tuemail@dominio.com'
EMAIL_HOST_PASSWORD = 'tucontraseña'
```

# 📄 Licencia de Uso – Backend Web de Peluquería

Este proyecto ha sido desarrollado por **Jobab Hacomar Izquier Torres** y se distribuye bajo los siguientes términos:

## ✅ Permisos concedidos

Se permite:

- Usar el código fuente del backend para fines personales, educativos o de mejora técnica.
- Modificar el código para adaptarlo a otros proyectos no comerciales.
- Compartir el proyecto con otros desarrolladores, siempre que se mantenga esta licencia y se respete la atribución.

## ❌ Restricciones

No se permite:

- Utilizar este proyecto con fines comerciales o lucrativos.
- Vender, sublicenciar o distribuir el código como parte de un producto o servicio comercial.
- Eliminar, modificar u ocultar la atribución al autor original del backend (**Jobab Hacomar Izquier Torres**).
- Utilizar el frontend incluido (plantilla HTML/CSS/JS) sin respetar la licencia de sus creadores originales.

## 📌 Atribución

Toda copia, modificación o redistribución del backend debe incluir una referencia clara al autor original:

> Backend desarrollado por **Jobab Hacomar Izquier Torres** – Proyecto Web de Peluquería

## 📦 Sobre el frontend

# 📄 Licencia de Uso – Plantilla HTML del Proyecto Web de Peluquería

La plantilla HTML utilizada en este proyecto ha sido desarrollada por **HTML Codex** y se encuentra licenciada bajo la **Creative Commons Attribution 4.0 International License**.
Esto implica que **no está permitido eliminar el enlace de atribución al autor original** sin adquirir una licencia
especial.

Al utilizar esta plantilla, se aceptan las siguientes condiciones:

---

## ✅ ESTÁ PERMITIDO

1. Usar la plantilla para fines personales y comerciales.
2. Modificar o personalizar el diseño según tus necesidades.
3. Adaptar la plantilla para su uso en cualquier CMS.
4. Compartir o distribuir la plantilla bajo el nombre de marca **HTML Codex**.
5. Publicar capturas de pantalla o enlaces en blogs, redes sociales u otros sitios web.

---

## ❌ NO ESTÁ PERMITIDO

1. Eliminar el enlace de atribución al autor (backlink) sin adquirir la [Licencia de Eliminación de Créditos](https://htmlcodex.com/credit-removal).
2. Vender, revender, alquilar, licenciar o sublicenciar la plantilla.
3. Subir la plantilla a sitios de recopilación de plantillas o terceros sin autorización expresa de HTML Codex.

---

## ⚠️ Terminación de la Licencia

Esta licencia puede ser revocada si se incumple cualquiera de las condiciones mencionadas.

Para cualquier duda o consulta sobre el uso de la plantilla, puedes contactar directamente con HTML Codex:  
👉 [https://htmlcodex.com/contact](https://htmlcodex.com/contact)

---

## 🛡️ Garantía

Este software se proporciona "tal cual", sin garantías de ningún tipo.
El autor no se hace responsable de posibles daños derivados del uso del código.

---

Si deseas utilizar este proyecto en un contexto comercial o tienes dudas sobre los términos,
puedes contactar directamente con el autor para discutir posibles acuerdos.

Gracias por respetar el trabajo y el esfuerzo invertido en este desarrollo.





