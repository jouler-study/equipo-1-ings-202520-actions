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

> *Puntos:*
> 5

----

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

> *Puntos:*
> 5

----

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

> *Puntos:*
> 5

----

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

> *Puntos:*
> 1

----

# 📚 NF-05 – Configuración de Google Tag Manager  
## Implementación centralizada de etiquetas y scripts

### Descripción  
El sistema debe contar con la correcta configuración de **Google Tag Manager (GTM)** para facilitar la administración de etiquetas, píxeles de seguimiento y scripts sin necesidad de modificar el código fuente directamente. Esto permitirá un control centralizado, seguro y eficiente de las integraciones de analítica y marketing.  

### 🔎 Criterios de aceptación
- GTM debe estar correctamente configurado en todos los entornos (producción, pruebas).  
- Se debe verificar el correcto disparo de etiquetas mediante la vista previa de GTM.  
- La configuración debe ser documentada y accesible para el equipo de desarrollo y marketing.  
- Solo personal autorizado podrá gestionar las etiquetas en GTM.  

### 📌 Prioridad  
P2  

### 📖 Notas de implementación  
- Usar cuentas y contenedores oficiales de la organización en GTM.  
- Definir un procedimiento para pruebas y despliegues de nuevas etiquetas.  
- Evitar la duplicación de scripts para garantizar rendimiento.  

> **Puntos:**  
3  

----

# 📚 NF-06 – Taggeo del sitio  
## Seguimiento de interacciones clave de los usuarios

### Descripción  
El sitio debe estar correctamente taggeado para recolectar información sobre interacciones clave (clics, búsquedas, navegación, conversiones). Esto permitirá obtener métricas precisas sobre el comportamiento de los usuarios y mejorar la toma de decisiones.  

### 🔎 Criterios de aceptación
- Cada acción relevante (clic en botones principales, consultas, navegación en secciones críticas) debe generar un evento en el sistema de analítica.  
- El taggeo debe ser probado y validado con herramientas como **Google Tag Assistant** o el panel de depuración de GA4.  
- No se deben capturar datos sensibles de los usuarios durante el proceso de taggeo.  
- Los eventos recolectados deben ser visibles en Google Analytics en un plazo máximo de 24 horas.  

### 📌 Prioridad  
P2  

### 📖 Notas de implementación  
- Seguir las recomendaciones de **Google Analytics 4 (GA4)**.  
- Documentar todos los eventos configurados y su propósito.  
- Garantizar cumplimiento con la Ley 1581 de 2012 y normativas de protección de datos.  

> **Puntos:**  
3

----

# 📚 NF-07 – Rendimiento  
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

> *Puntos:*
> 5 

----

# 📚 NF-08 – Disponibilidad  
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

> *Puntos:*
> 3

----

# 📚 NF-09 – Escalabilidad  
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

> *Puntos:*
> 3

----

# 📚 NF-10 – Confiabilidad y calidad de datos  
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

> *Puntos:*
> 2

----
# 📚 NF-11 – Eficiencia en uso de recursos  
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

> *Puntos:*
> 5
