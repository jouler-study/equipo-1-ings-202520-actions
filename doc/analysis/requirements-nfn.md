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
Falta por definir

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
Falta por definir

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
Falta por definir

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
Falta por definir

### Notas de implementación  
Utilizar herramientas como `flake8`, `black` o `pylint` para revisar el estilo del código.  
Para documentar:  
- Usar **Sphinx** o **Markdown**  
- Aplicar control de versiones con **Git** y mantener **commits descriptivos y frecuentes**

----
# NF-005 - Trazabilidad
Por definir

