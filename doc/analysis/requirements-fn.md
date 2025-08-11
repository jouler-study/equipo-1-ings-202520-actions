# ✨ **F-01 – Consulta de precios actuales por producto y ubicación**

---

**📝 Descripción**  
El sistema permitirá a los usuarios consultar el precio actual por kilogramo de productos seleccionados, filtrando por ciudad (por ejemplo, Medellín) y por plaza de mercado específica. Esta funcionalidad busca facilitar la toma de decisiones de compra informadas, ofreciendo precios actualizados según la ubicación.

---

**✅ Criterios de aceptación**

> **Scenario:** Mostrar precio actual de Tomate Chonto en Medellín  
> - **Given** que el usuario ha accedido al sistema  
> - **And** está en la vista de consulta de precios  
> - **When** selecciona el producto *"Tomate Chonto"*  
> - **And** elige la ciudad *"Medellín"*  
> - **And** selecciona la plaza *"Plaza Minorista"*  
> - **Then** el sistema mostrará el precio actual por kilogramo del producto  
> - **And** se indicará la fecha de la última actualización del precio

---

> **📌 Prioridad:**  
> P0

---

# 📊 **F-02 – Visualización de la variación histórica de precios**

---

**📝 Descripción**  
El sistema mostrará cómo ha cambiado el precio de cada producto a lo largo del tiempo. Se presentarán gráficos o tablas que evidencien las tendencias de aumento, disminución o estabilidad del precio, permitiendo al usuario analizar comportamientos pasados.

---

**✅ Criterios de aceptación**

> **Scenario:** Visualizar gráfico histórico de precios de Papa Criolla  
> - **Given** que el usuario ha accedido al sistema  
> - **And** ha consultado el producto *"Papa Criolla"*  
> - **When** hace clic en *"Ver historial de precios"*  
> - **Then** el sistema mostrará un gráfico o tabla con la evolución del precio por kilogramo durante el último año  
> - **And** se indicarán claramente los periodos de aumento, disminución o estabilidad

---

> **📌 Prioridad:**  
> P0

---

# 🔮 **F-03 – Predicción de precios futuros**

---

**📝 Descripción**  
El sistema utilizará modelos de aprendizaje automático entrenados con datos históricos para generar predicciones de precios de los productos. Esto permitirá a los usuarios anticiparse a posibles aumentos o disminuciones de precios en los próximos meses.

---

**✅ Criterios de aceptación**

> **Scenario:** Mostrar predicción de precio para Aguacate Hass  
> - **Given** que el usuario ha accedido al sistema  
> - **And** ha seleccionado el producto *"Aguacate Hass"*  
> - **When** hace clic en *"Ver predicción de precios"*  
> - **Then** el sistema mostrará una estimación del precio por kilogramo para los próximos meses  
> - **And** se indicará el nivel de confianza de la predicción

---

> **📌 Prioridad:**  
> P0

---

# ⚖️ **F-04 – Comparación de precios entre plazas de mercado**

---

**📝 Descripción**  
El sistema permitirá comparar el precio de un mismo producto entre varias plazas de mercado dentro de una misma ciudad, ayudando al usuario a identificar la plaza más económica para hacer su compra.

---

**✅ Criterios de aceptación**

> **Scenario:** Comparar precio de Cebolla Cabezona en Medellín  
> - **Given** que el usuario ha accedido al sistema  
> - **And** ha seleccionado el producto *"Cebolla Cabezona"*  
> - **When** elige la ciudad *"Medellín"*  
> - **Then** el sistema mostrará los precios por kilogramo en todas las plazas de mercado disponibles en esa ciudad  
> - **And** ordenará la información de menor a mayor precio

---

> **📌 Prioridad:**  
> P1

---

# 🔐 F-05 – Registro de usuarios 

---

**📝 Descripción**  
El sistema permitirá a los usuarios registrarse mediante nombre, correo electrónico y contraseña, validando que la información cumpla con los requisitos establecidos. Una vez registrado, el usuario podrá acceder a las funcionalidades del sistema según su rol.

---

**✅ Criterios de aceptación**

> **Scenario:** Registrar un nuevo usuario con correo electrónico  
> - **Given** que el usuario accede a la pantalla de registro  
> - **When** el usuario ingresa nombre, correo y contraseña válidos  
> - **Then** el sistema crea una nueva cuenta y muestra un mensaje de bienvenida  

> **Scenario:** Validar correo existente en el registro  
> - **Given** que el usuario ingresa un correo que ya está registrado  
> - **When** intenta completar el registro  
> - **Then** el sistema muestra un mensaje indicando que el correo ya está en uso  

> **Scenario:** Validar formato de contraseña  
> - **Given** que el usuario ingresa una contraseña  
> - **When** la contraseña no cumple con los requisitos mínimos  
> - **Then** el sistema muestra un mensaje indicando las reglas de seguridad  

---

> **📌 Prioridad:**  
> P0

---

# 🔑 F-06 – Inicio de sesión

---

**📝 Descripción**  
El sistema permitirá a los usuarios iniciar sesión en su cuenta mediante correo electrónico y contraseña válidos. Contará con mecanismos de seguridad para bloqueo temporal por múltiples intentos fallidos y ofrecerá la opción de recuperación de contraseña a través de correo electrónico.  

---

**✅ Criterios de aceptación**  

> **Scenario:** Iniciar sesión con credenciales válidas  
> - **Given** que el usuario está en la pantalla de inicio de sesión  
> - **When** ingresa su correo y contraseña correctos  
> - **Then** el sistema permite el acceso a su cuenta  

> **Scenario:** Bloqueo por múltiples intentos fallidos  
> - **Given** que el usuario ingresa una contraseña incorrecta tres veces seguidas  
> - **When** intenta iniciar sesión nuevamente  
> - **Then** el sistema bloquea temporalmente la cuenta y envía un correo de recuperación  

> **Scenario:** Recuperación de contraseña  
> - **Given** que el usuario olvidó su contraseña  
> - **When** solicita recuperación  
> - **Then** el sistema envía un enlace de restablecimiento al correo registrado  

---

> **📌 Prioridad:** 
P0  

---

# 🍎 F-07 – Creación y cálculo del valor mensual de la canasta personalizada

---

**📝 Descripción**  
El sistema permitirá a los usuarios crear canastas personalizadas con diferentes alimentos y cantidades definidas, asignándoles un nombre para su identificación. Adicionalmente, el sistema calculará el valor total mensual de la canasta con base en los precios actualizados de cada alimento en el mes seleccionado, permitiendo una estimación precisa de gastos.  

---

**✅ Criterios de aceptación**  

> **Scenario:** Crear canasta personalizada  
> - **Given** que el usuario ha iniciado sesión  
> - **When** el usuario selecciona varios alimentos y sus cantidades  
> - **Then** el sistema guarda la canasta con un nombre definido por el usuario  

> **Scenario:** Calcular valor mensual de la canasta  
> - **Given** que el usuario tiene una canasta personalizada guardada  
> - **When** el usuario solicita el valor total mensual  
> - **Then** el sistema calcula el precio sumando el valor actual de cada alimento en el mes seleccionado  

---

> **📌 Prioridad:** 
P2  

---

# 🛠️ F-08 – Gestión de perfil de usuario

---

**📝 Descripción**  
El sistema permitirá a los usuarios autenticados modificar sus datos personales y cambiar su contraseña, garantizando que la información actualizada se almacene correctamente y que los cambios de contraseña sean confirmados por correo electrónico como medida de seguridad.  

---

**✅ Criterios de aceptación**  

> **Scenario:** Editar información personal  
> - **Given** que el usuario ha iniciado sesión  
> - **When** modifica su nombre o datos de contacto  
> - **Then** el sistema guarda los cambios y confirma la actualización  

> **Scenario:** Cambiar contraseña  
> - **Given** que el usuario está autenticado  
> - **When** solicita cambiar su contraseña e ingresa la actual y la nueva  
> - **Then** el sistema actualiza la contraseña y envía confirmación al correo  

---

> **📌 Prioridad:** 
P1  

---

# 📂 F-09 – Administración de datos

---

**📝 Descripción**  
El sistema permitirá a los administradores gestionar la información de precios de los alimentos, incluyendo la carga de datos desde archivos, la edición manual de precios y la eliminación de registros incorrectos. Estas acciones garantizarán que la información disponible para los usuarios sea precisa y actualizada.  

---

**✅ Criterios de aceptación**  

> **Scenario:** Cargar datos de precios manualmente  
> - **Given** que el administrador ha iniciado sesión  
> - **When** carga un archivo con datos de precios  
> - **Then** el sistema valida el formato y actualiza la base de datos  

> **Scenario:** Editar precio de un alimento  
> - **Given** que el administrador está en el panel de gestión  
> - **When** selecciona un alimento y modifica su precio  
> - **Then** el sistema guarda los cambios y registra la fecha de actualización  

> **Scenario:** Eliminar registro de precio erróneo  
> - **Given** que el administrador detecta un dato incorrecto  
> - **When** solicita eliminarlo  
> - **Then** el sistema lo elimina y actualiza las consultas de precios  

---

> **📌 Prioridad:** 
P2  

---

# 📈 F-10 – Evolución histórica y predicción del valor de la canasta personalizada

---

**📝 Descripción**  
El sistema permitirá a los usuarios visualizar la evolución del valor mensual de su canasta personalizada en un rango de tiempo definido, así como obtener una predicción estimada de su valor en meses futuros, apoyándose en datos históricos y modelos de proyección.  

---

**✅ Criterios de aceptación**  

> **Scenario:** Mostrar evolución del valor mensual de la canasta  
> - **Given** que el usuario tiene una canasta personalizada  
> - **When** el usuario selecciona un rango de meses  
> - **Then** el sistema muestra cómo ha variado el valor total de la canasta por mes  

> **Scenario:** Predecir valor mensual futuro de la canasta  
> - **Given** que el usuario tiene una canasta personalizada  
> - **When** el usuario solicita la predicción  
> - **Then** el sistema muestra el valor estimado de la canasta para meses futuros  

---

> **📌 Prioridad:** 
P3  

---
