# NF-001 – Usabilidad  
## Interfaz intuitiva para usuarios no técnicos

### Descripción  
La interfaz del sistema debe ser lo suficientemente clara y fácil de usar para que usuarios sin conocimientos técnicos puedan consultar precios de productos, visualizar tendencias y hacer comparaciones sin requerir ayuda externa. Se busca reducir la curva de aprendizaje y evitar confusiones al navegar por la app.

### Criterios de aceptación
- El usuario puede consultar el precio de un producto en tres pasos o menos.  
- Los botones principales deben tener íconos representativos y texto descriptivo.  
- Se debe realizar al menos una prueba de usabilidad con usuarios reales y obtener una calificación mínima de 80% de satisfacción.  
- El sistema debe contar con mensajes de retroalimentación claros (por ejemplo: “Producto no encontrado”).

### Prioridad  
P0

### Notas de implementación  
Se recomienda seguir las pautas de diseño centrado en el usuario:  
1. Participación temprana y activa del usuario.  
2. Identificación de necesidades y requisitos del usuario.  
3. Diseño iterativo con pruebas de prototipo.  
4. Consistencia visual y funcional.  
5. Retroalimentación inmediata y útil.  
6. Medición del impacto mediante satisfacción y comportamiento de usuarios.

----

# NF-002 – Compatibilidad  
## Soporte multiplataforma y responsive

### Descripción  
La aplicación debe poder ejecutarse correctamente en diferentes sistemas operativos (Inicialmente Windows y Android; iOS, Linux en una fase posterior) y adaptarse a distintas resoluciones de pantalla, desde dispositivos móviles hasta pantallas de escritorio. Esto permite que cualquier usuario acceda sin importar su equipo.

### Criterios de aceptación
- La interfaz se debe ver correctamente en resoluciones desde 360x640 hasta 1920x1080.  
- La app debe funcionar correctamente en navegadores modernos (Chrome, Firefox, Safari, Edge).

### Prioridad  
P2

### Notas de implementación  
Se recomienda implementar diseño web responsive usando **CSS Grid**, **Flexbox** o frameworks como **Bootstrap**.

----

# NF-003 – Seguridad  
## Protección de los datos del usuario

### Descripción  
Toda la información sensible proporcionada por los usuarios (como nombres y correos) debe ser almacenada de forma segura, aplicando cifrado. Además, la comunicación entre cliente y servidor debe estar protegida mediante el uso de HTTPS para evitar accesos no autorizados.

### Criterios de aceptación
- Los datos sensibles deben estar cifrados usando un algoritmo seguro (por ejemplo, AES-256).  
- El sistema debe funcionar exclusivamente sobre protocolo HTTPS.

### Prioridad  
P1

### Notas de implementación  
Usar librerías de cifrado como `cryptography` (en Python) y servicios con **certificados SSL válidos**.  
Si se implementa autenticación, se recomienda:  
- Uso de **tokens JWT**  
- Almacenamiento de contraseñas con **hashing (bcrypt, Argon2)** y sal  


----

# NF-004 – Mantenibilidad  
## Código limpio y bien documentado

### Descripción  
El código del proyecto debe seguir buenas prácticas de programación y estándares definidos para facilitar futuras modificaciones, correcciones y ampliaciones. La documentación clara y la estructura organizada aseguran que nuevos desarrolladores puedan entender y continuar el proyecto sin dificultades.

### Criterios de aceptación
- El código cumple con el estándar **PEP8** (en Python).  
- Se deben incluir **docstrings** para todas las funciones y clases.  
- El proyecto debe estar organizado en módulos separados por funcionalidad.  
- Debe existir un archivo **README.md** con instrucciones para la instalación y uso del sistema.

### Prioridad  
P0

### Notas de implementación  
Utilizar herramientas como `flake8`, `black` o `pylint` para revisar el estilo del código.  
Para documentar:  
- Usar **Sphinx** o **Markdown**  
- Aplicar control de versiones con **Git** y mantener **commits descriptivos y frecuentes**

----
# NF-005 – Trazabilidad de acciones del usuario
## Registro de eventos y acciones realizadas por los usuarios

### Descripción  
El sistema debe llevar un registro interno (log) de las acciones relevantes realizadas por los usuarios dentro de la aplicación, como búsquedas de productos, comparaciones entre precios, visualización de predicciones y cambios en configuraciones. Esta trazabilidad permite monitorear el comportamiento del sistema, detectar errores o usos indebidos, y mejorar la toma de decisiones futuras basada en datos reales de uso.

Además, el sistema debe cumplir con lo establecido por la Ley 1581 de 2012 de protección de datos personales en Colombia (régimen de habeas data), lo cual implica que ningún dato sensible del usuario podrá ser registrado en los logs sin su consentimiento, y se debe garantizar el derecho a conocer, actualizar y eliminar su información personal.

### Criterios de aceptación
* Cada acción del usuario debe generar un evento registrado con: ID del usuario (si está autenticado), tipo de acción, fecha y hora.

* Los registros deben almacenarse en un archivo de log o base de datos con acceso restringido al administrador del sistema.

* El sistema debe contar con una función de consulta de logs para propósitos de auditoría interna.

* No se deben registrar datos sensibles (como contraseñas, números de identificación, correos personales, etc.) en los logs.

* El usuario debe poder solicitar la eliminación de su historial de acciones de acuerdo con la normativa de habeas data.

* Los registros deben conservarse por un período no mayor a 30 días salvo justificación técnica o legal.

### Prioridad 
P3

### Notas de implementación  
Se recomienda el uso de un sistema de logging como logging en Python. Para cumplir con la Ley 1581 de 2012, se deben establecer políticas claras sobre el tratamiento de datos personales, visibles en la plataforma. Los logs deben estar protegidos y ser accesibles solo por personal autorizado. Si se escala el sistema, considerar el uso de servicios como AWS CloudWatch, ELK Stack o herramientas de auditoría con encriptación.