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
> Por definir

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
> Por definir

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
> Por definir

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
> Por definir

---

# 🔐 **F-05 – Registro e inicio de sesión de usuarios con historial**

---

**📝 Descripción**  
El sistema permitirá a los usuarios registrarse y autenticarse para acceder a una funcionalidad adicional: guardar un historial de los productos que han consultado, facilitando su seguimiento en el tiempo.

---

**✅ Criterios de aceptación**

> **Scenario:** Registro de usuario y consulta del historial  
> - **Given** que el usuario no tiene cuenta  
> - **When** ingresa sus datos personales y una contraseña válida  
> - **And** hace clic en *"Registrarse"*  
> - **Then** el sistema creará una cuenta y redirigirá al usuario a su perfil  
> - **Given** que el usuario ha iniciado sesión  
> - **When** consulta el producto *"Frijol Cargamanto"*  
> - **Then** ese producto será agregado al historial de consultas  
> - **And** el usuario podrá ver una lista de los productos consultados recientemente

---

> **📌 Prioridad:**  
> Por definir

---
