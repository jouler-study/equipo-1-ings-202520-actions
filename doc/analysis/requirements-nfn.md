# 📚 NF-01 – Usabilidad  
## Interfaz intuitiva para usuarios no técnicos  

### Descripción  
La interfaz del sistema debe ser lo suficientemente clara y fácil de usar para que usuarios sin conocimientos técnicos puedan consultar precios de productos, visualizar tendencias y hacer comparaciones sin requerir ayuda externa. Se busca reducir la curva de aprendizaje y evitar confusiones al navegar por la app.  

### 🔎 Criterios de aceptación  
- El usuario puede consultar el precio de un producto en tres pasos o menos.  
- Los botones principales deben tener íconos representativos y texto descriptivo.  
- Se debe realizar al menos una prueba de usabilidad con usuarios reales y obtener una calificación mínima de 80% de satisfacción.  
- El sistema debe contar con mensajes de retroalimentación claros (por ejemplo: “Producto no encontrado”).  

### 📌 Prioridad  
P0  

### 📖 Notas de implementación  
Se recomienda seguir las pautas de diseño centrado en el usuario:  
1. Participación temprana y activa del usuario.  
2. Identificación de necesidades y requisitos del usuario.  
3. Diseño iterativo con pruebas de prototipo.  
4. Consistencia visual y funcional.  
5. Retroalimentación inmediata y útil.  
6. Medición del impacto mediante satisfacción y comportamiento de usuarios.  

---

# 📚 NF-02 – Compatibilidad  
## Soporte multiplataforma y responsive  

### Descripción  
La aplicación debe poder ejecutarse correctamente en diferentes sistemas operativos (Inicialmente Windows y Android; iOS, Linux en una fase posterior) y adaptarse a distintas resoluciones de pantalla, desde dispositivos móviles hasta pantallas de escritorio. Esto permite que cualquier usuario acceda sin importar su equipo.  

### 🔎 Criterios de aceptación  
- La interfaz se debe ver correctamente en resoluciones desde 360x640 hasta 1920x1080.  
- La app debe funcionar correctamente en navegadores modernos (Chrome, Firefox, Safari, Edge).  

### 📌 Prioridad  
P2  

### 📖 Notas de implementación  
Se recomienda implementar diseño web responsive usando **CSS Grid**, **Flexbox** o frameworks como **Bootstrap**.  

---

# 📚 NF-03 – Seguridad  
## Protección de los datos del usuario  

### Descripción  
Toda la información sensible proporcionada por los usuarios (como nombres y correos) debe ser almacenada de forma segura, aplicando cifrado. Además, la comunicación entre cliente y servidor debe estar protegida mediante el uso de HTTPS para evitar accesos no autorizados.  

### 🔎 Criterios de aceptación  
- Los datos sensibles deben estar cifrados usando un algoritmo seguro (por ejemplo, AES-256).  
- El sistema debe funcionar exclusivamente sobre protocolo HTTPS.  

### 📌 Prioridad  
P1  

### 📖 Notas de implementación  
Usar librerías de cifrado como `cryptography` (en Python) y servicios con **certificados SSL válidos**.  
Si se implementa autenticación, se recomienda:  
- Uso de **tokens JWT**  
- Almacenamiento de contraseñas con **hashing (bcrypt, Argon2)** y sal  

---

# 📚 NF-04 – Mantenibilidad  
## Código limpio y bien documentado  

### Descripción  
El código del proyecto debe seguir buenas prácticas de programación y estándares definidos para facilitar futuras modificaciones, correcciones y ampliaciones. La documentación clara y la estructura organizada aseguran que nuevos desarrolladores puedan entender y continuar el proyecto sin dificultades.  

### 🔎 Criterios de aceptación  
- El código cumple con el estándar **PEP8** (en Python).  
- Se deben incluir **docstrings** para todas las funciones y clases.  
- El proyecto debe estar organizado en módulos separados por funcionalidad.  
- Debe existir un archivo **README.md** con instrucciones para la instalación y uso del sistema.  

### 📌 Prioridad  
P0  

### 📖 Notas de implementación  
Utilizar herramientas como `flake8`, `black` o `pylint` para revisar el estilo del código.  
Para documentar:  
- Usar **Sphinx** o **Markdown**  
- Aplicar control de versiones con **Git** y mantener **commits descriptivos y frecuentes**  

---

# 📚 NF-05 – Trazabilidad de acciones del usuario  
## Registro de eventos y acciones realizadas por los usuarios  

### Descripción  
El sistema debe llevar un registro interno (log) de las acciones relevantes realizadas por los usuarios dentro de la aplicación, como búsquedas de productos, comparaciones entre precios, visualización de predicciones y cambios en configuraciones. Esta trazabilidad permite monitorear el comportamiento del sistema, detectar errores o usos indebidos, y mejorar la toma de decisiones futuras basada en datos reales de uso.  

Además, el sistema debe cumplir con lo establecido por la Ley 1581 de 2012 de protección de datos personales en Colombia (régimen de habeas data), lo cual implica que ningún dato sensible del usuario podrá ser registrado en los logs sin su consentimiento, y se debe garantizar el derecho a conocer, actualizar y eliminar su información personal.  

### 🔎 Criterios de aceptación  
* Cada acción del usuario debe generar un evento registrado con: ID del usuario (si está autenticado), tipo de acción, fecha y hora.  
* Los registros deben almacenarse en un archivo de log o base de datos con acceso restringido al administrador del sistema.  
* El sistema debe contar con una función de consulta de logs para propósitos de auditoría interna.  
* No se deben registrar datos sensibles (como contraseñas, números de identificación, correos personales, etc.) en los logs.  
* El usuario debe poder solicitar la eliminación de su historial de acciones de acuerdo con la normativa de habeas data.  
* Los registros deben conservarse por un período no mayor a 30 días salvo justificación técnica o legal.  

### 📌 Prioridad  
P3  

### 📖 Notas de implementación  
Se recomienda el uso de un sistema de logging como `logging` en Python. Para cumplir con la Ley 1581 de 2012, se deben establecer políticas claras sobre el tratamiento de datos personales, visibles en la plataforma. Los logs deben estar protegidos y ser accesibles solo por personal autorizado. Si se escala el sistema, considerar el uso de servicios como AWS CloudWatch, ELK Stack o herramientas de auditoría con encriptación.  

---

# 📚 NF-06 – Rendimiento  
## Respuesta rápida en consultas y generación de gráficas  

### Descripción  
El sistema debe garantizar que las consultas de datos y la generación de gráficas se realicen en menos de 3 segundos en condiciones normales de uso, optimizando el rendimiento mediante estrategias de indexación, caché y procesamiento eficiente.  

### 🔎 Criterios de aceptación  
- El tiempo máximo de respuesta para consultas y gráficos debe ser ≤ 5 segundos.  
- Bajo condiciones de estrés (100 usuarios concurrentes) el tiempo no debe superar los 5 segundos.  
- Deben ejecutarse pruebas de rendimiento periódicas para verificar el cumplimiento.  

### 📌 Prioridad  
P1  

### 📖 Notas de implementación  
- Utilizar técnicas de caché para datos consultados con frecuencia.  
- Implementar consultas SQL optimizadas y estructuras de datos adecuadas.  
- Usar paginación en listados grandes para reducir carga.  

---

# 📚 NF-07 – Disponibilidad  
## Alta disponibilidad del servicio  

### Descripción  
El sistema debe estar disponible y accesible al menos el 99 % del tiempo, excluyendo periodos de mantenimiento programado, para garantizar la continuidad del servicio a los usuarios.  

### 🔎 Criterios de aceptación  
- El uptime mensual debe ser ≥ 99 %.  
- Los mantenimientos programados deben notificarse con al menos 48 horas de anticipación.  
- Implementación de redundancia y balanceo de carga para reducir caídas.  

### 📌 Prioridad  
P1  

### 📖 Notas de implementación  
- Usar infraestructura en la nube con redundancia geográfica.  
- Configurar monitoreo y alertas en tiempo real.  

---

# 📚 NF-08 – Escalabilidad  
## Capacidad de crecimiento sin interrupciones  

### Descripción  
La arquitectura debe permitir aumentar la capacidad de almacenamiento y procesamiento sin interrumpir el servicio, soportando al menos un 100 % de crecimiento de datos en un año.  

### 🔎 Criterios de aceptación  
- El sistema soporta duplicar la carga de datos y usuarios sin caída de rendimiento.  
- No se requieren cambios de arquitectura para escalar horizontal o verticalmente.  

### 📌 Prioridad  
P2  

### 📖 Notas de implementación  
- Utilizar arquitectura basada en microservicios.  
- Base de datos escalable (sharding o replicación).  

---

# 📚 NF-09 – Confiabilidad y calidad de datos  
## Información verificada y actualizada  

### Descripción  
Toda la información mostrada debe provenir de fuentes verificadas y estar actualizada para garantizar que las decisiones de los usuarios se basen en datos confiables.  

### 🔎 Criterios de aceptación  
- El 100 % de los datos provienen de fuentes oficiales (ej. DANE, SIPSA).  
- Los datos se actualizan según el calendario oficial de publicación.  
- El sistema valida y registra la fecha de la última actualización.  

### 📌 Prioridad  
P4  

### 📖 Notas de implementación  
- Integración directa con APIs oficiales.  
- Mecanismos de validación de integridad de datos.  

---

# 📚 NF-10 – Eficiencia en uso de recursos  
## Optimización de CPU y memoria  

### Descripción  
El sistema debe mantener un uso de CPU por debajo del 70 % y de memoria por debajo del 75 % incluso en condiciones de carga máxima, evitando cuellos de botella y degradación del servicio.  

### 🔎 Criterios de aceptación  
- CPU ≤ 70 % en condiciones de máxima carga.  
- Memoria ≤ 75 % en condiciones de máxima carga.  
- Monitoreo en tiempo real del uso de recursos.  

### 📌 Prioridad  
P3  

### 📖 Notas de implementación  
- Uso de consultas y algoritmos eficientes.  
- Implementar escalado automático cuando se detecte sobrecarga.  

