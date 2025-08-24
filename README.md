# 💇‍♀️ Web de Peluquería – Backend en Django

Este proyecto es el backend completo de una web de peluquería, desarrollado íntegramente con Django. Está diseñado para integrarse con una plantilla frontend ya existente en HTML/CSS/JS, proporcionando funcionalidades administrativas y de gestión de datos.

## ✨ Funcionalidades principales

- Panel de administración de Django para:
  - Añadir y editar empleados
  - Gestionar precios y horarios
  - Gestionar otra información que se muestra en la web
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
```
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

# 📄 Licencia – Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

Este proyecto de backend ha sido desarrollado por **Jobab Hacomar Izquier Torres** y se encuentra bajo la licencia **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

## ✅ Permisos otorgados

Puedes:

- **Compartir**: copiar y redistribuir el material en cualquier medio o formato.
- **Adaptar**: remezclar, transformar y construir a partir del material.

Siempre que:

- Se dé **crédito adecuado** al autor original.
- Se incluya un enlace a esta licencia.
- Se indique si se han realizado cambios.

## ❌ Restricciones

No puedes:

- Usar el material con **fines comerciales**.
- Aplicar restricciones legales o tecnológicas que impidan a otros hacer lo que permite esta licencia.

## 📌 Atribución

Ejemplo recomendado de atribución:

> Backend desarrollado por **Jobab Hacomar Izquier Torres** – Licencia CC BY-NC 4.0  
> [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

## 🔗 Enlace oficial

Consulta los términos completos de la licencia en el sitio oficial de Creative Commons:  
👉 [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

---

Este archivo cubre exclusivamente el backend desarrollado por **Jobab Hacomar Izquier Torres**. La plantilla HTML utilizada en el frontend tiene su propia licencia independiente, detallada a continuación.

Gracias por respetar esta licencia y por reconocer el trabajo del autor original.

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

## ❓ Preguntas Frecuentes sobre Licencias

**¿Puedo usar este proyecto para fines comerciales?**  
- **Frontend**: Sí, bajo la licencia CC BY 4.0 de HTML Codex, manteniendo la atribución requerida.  
- **Backend**: No, sin permiso explícito del autor, debido a la licencia CC BY-NC 4.0.

**¿Cómo atribuir correctamente?**  
- **Backend**: `"Backend desarrollado por Jobab Hacomar Izquier Torres – CC BY-NC 4.0" - https://github.com/JobabHIzquierTorres`.
- **Frontend**: Sigue los requisitos específicos de HTML Codex (ver `LICENSE - HTML Codex.txt`).

**¿Necesitas uso comercial o tienes otras preguntas?**  
Contacta al autor del backend en: [https://www.linkedin.com/in/jhizquier/](https://www.linkedin.com/in/jhizquier/)


## 🛡️ Garantía

Este software se proporciona "tal cual", sin garantías de ningún tipo.
El autor no se hace responsable de posibles daños derivados del uso del código.

---
