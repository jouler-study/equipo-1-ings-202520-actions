# Decisiones Backend 

## 🌐 Frameworks Backend considerados

### 🏃🏽 FastAPI (Python)

Framework moderno y ligero de alto rendimiento para Python, diseñado específicamente para crear APIs rápidas y eficientes, con tipado automático y documentación interactiva. Es creciente en proyectos de análisis y machine learning.

> Ventajas
-  **Sintaxis sencilla**, muy rápido de aprender.
- **Compatibilidad nativa** con librerías como pandas, numpy, TensorFlow y librerías de predicción como scikit-learn, esto es ideal para exponer modelos de Machine learning en endpoints REST.
- **Altamente eficiente**, ya que es uno de los frameworks más rápidos para Python, porque usa ASGI, que da soporte a la programación asíncrona y maneja eficientemente aplicaciones con alta concurrencia. 
- **Genera automáticamente documentación**, puede ser en OpenAPI o Swagger.
- Soporte completo para **type hints** de Python, reduciendo errores.
- **Validación de datos** de entrada y salida automática.
- Muy **flexible** para trabajar con bases SQL (PostgreSQL, SQLAlchemy) o NoSQL (MongoDB).

> Desventajas
- **Menor cantidad de recursos y plugins comparado con Django**.
- Requiere entendimiento de **conceptos async/await**.
- Necesita **integración con ORMs** (Mapeo Objeto-Relacional).
- Hay que **configurar autenticación, admin, etc. por separado**.

---
### 🐍 Django (Python)

Framework backend completo de alto nivel, basado en el patrón MTV (Model-Template-View). Usado mucho en aplicaciones que requieren manejo de bases de datos, autenticación, seguridad y panel de administración. También sigue el principio "batteries included", proporcionando una solución completa para desarrollo web.

> Ventajas
- **Protección integrada contra ataques comunes**, como SQL Injection, XSS y CSRF
- Incluye **ORM propio**, fácil de usar con bases SQL como Postgres y MySQL.
- **Documentación muy completa y comunidad grande**.
- Tiene **admin panel integrado**, para la gestión de datos.
- **Compatible con librerías de ciencia de datos**.

> Desventajas
- Puede ser **excesivo para APIs simples**. Puede sentirse pesado para proyectos pequeños o muy livianos.
- **Estructura más rígida**, siguiendo convenciones estrictas.
- **Menor rendimiento** comparado con FastAPI para APIs puras.
- Curva de aprendizaje un poco alta al inicio, ya que hay **muchos conceptos y patrones por aprender**.

---
### 🚅 Express.js (Node.js)

Framework web minimalista y flexible para Node.js, ampliamente utilizado para crear APIs REST y aplicaciones web, en general, para proyectos que necesitan escalabilidad en tiempo real.

> Ventajas
- Rápido y ligero, **posee mucha flexibilidad altamente configurable y personalizable**.
- Acceso a **gran cantidad de paquetes y librerías** (NPM).
- Puede **combinarse con bases NoSQL y SQL**.
- **Manejo natural de JSON**.
- Muy usado en la industria, lo que asegura **soporte y recursos de aprendizaje**.
- Ideal cuando se realiza **frontend en React/Angular/Vue**.

> Desventajas
- **Requiere configurar muchos aspectos manualmente**.
- Es **menos amigable para integrar modelos de ciencia de datos**, tiene limitadas opciones para ML/análisis estadístico.
- Tiene **tipado débil**, JavaScript no tipado puede generar errores en runtime
- **No trae un ORM oficial**.
- La **seguridad no es tan robusta por defecto**, depende de configuraciones adicionales.

---
### 🌼 Spring Boot (Java)

Framework que simplifica el desarrollo de aplicaciones Java, proporcionando configuración automática y un enfoque de convención sobre configuración.

> Ventajas
- Gran cantidad de **librerías y herramientas**.
- Excelente para **sistemas de gran escala**.
- **Documentación extensa**.
- **Buen rendimiento y optimización**.

> Desventajas
- **Alta curva de aprendizaje**.
- **Código más extenso** comparado con otros frameworks.
- Puede requerir **mucha configuración inicial**.
- **Menos integrado con ciencia de datos**, tiene limitadas opciones nativas para Machine learning.