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

# 🔐 **F-05 – Registro de usuarios **

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
