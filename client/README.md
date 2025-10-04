# PLAZE - Cliente Frontend

Aplicación web para consulta de precios de productos en plazas de mercado de Medellín.

## 🚀 Características

- **Consulta de precios actuales** (F-01): Busca precios por producto, ciudad y plaza
- **Comparación de precios**: Compara precios entre diferentes plazas
- **Interfaz intuitiva**: Diseño centrado en la usabilidad (NF-01)
- **Responsive**: Adaptable a diferentes dispositivos
- **Búsqueda rápida**: Con sugerencias automáticas

## 🛠️ Tecnologías

- **React 18** - Framework principal
- **Vite** - Herramienta de construcción
- **React Router** - Navegación
- **Axios** - Cliente HTTP
- **Lucide React** - Iconos
- **CSS3** - Estilos personalizados

## 📦 Instalación

1. **Instalar dependencias:**
   ```bash
   npm install
   ```

2. **Configurar variables de entorno:**
   Crear archivo `.env` en la raíz del proyecto:
   ```env
   VITE_API_URL=http://localhost:8000/api
   ```

3. **Ejecutar en modo desarrollo:**
   ```bash
   npm run dev
   ```

4. **Abrir en el navegador:**
   http://localhost:3000

## 🏗️ Estructura del Proyecto

```
src/
├── components/          # Componentes reutilizables
│   ├── Header.jsx      # Cabecera de la aplicación
│   ├── Footer.jsx      # Pie de página
│   ├── ProductSearch.jsx  # Formulario de búsqueda
│   ├── PriceResults.jsx   # Resultados de precios
│   └── QuickStats.jsx     # Estadísticas rápidas
├── pages/              # Páginas principales
│   └── HomePage.jsx    # Página principal
├── config/             # Configuración
│   └── api.js          # Servicios de API
├── App.jsx             # Componente raíz
├── main.jsx            # Punto de entrada
└── index.css           # Estilos globales
```

## 🔌 API Endpoints

El cliente se conecta con los siguientes endpoints del servidor:

### Consulta de Precios (F-01)
- `GET /api/prices/current` - Precios actuales
- `GET /api/prices/history` - Historial de precios
- `GET /api/prices/predictions` - Predicciones

### Productos
- `GET /api/products/search` - Búsqueda de productos
- `GET /api/products/suggestions` - Sugerencias de búsqueda

### Plazas de Mercado
- `GET /api/plazas` - Lista de plazas
- `GET /api/plazas/{id}` - Detalles de plaza

### Estadísticas
- `GET /api/stats/quick` - Estadísticas rápidas
- `GET /api/stats/variations` - Variaciones de precios

## 🎨 Diseño

El diseño sigue las especificaciones de Figma y cumple con los requisitos de usabilidad (NF-01):

- **Colores principales**: Azul (#3b82f6), Verde (#10b981)
- **Tipografía**: Inter (sistema de fuentes)
- **Espaciado**: Sistema de 8px
- **Componentes**: Cards, botones, formularios consistentes

## 📱 Responsive Design

- **Mobile First**: Diseño optimizado para móviles
- **Breakpoints**: 640px, 768px, 1024px
- **Grid System**: CSS Grid y Flexbox

## 🚀 Scripts Disponibles

- `npm run dev` - Servidor de desarrollo
- `npm run build` - Construcción para producción
- `npm run preview` - Vista previa de producción
- `npm run lint` - Linter de código

## 🔧 Configuración del Servidor

Para que el cliente funcione correctamente, el servidor debe estar ejecutándose en:
- **URL**: http://localhost:8000
- **CORS**: Configurado para permitir requests desde http://localhost:3000

## 📋 Funcionalidades Implementadas

### ✅ Completadas
- [x] Estructura base del proyecto
- [x] Componente de búsqueda de productos
- [x] Visualización de resultados de precios
- [x] Diseño responsive
- [x] Integración con API (preparada)

### 🔄 En Progreso
- [ ] Conexión real con el servidor
- [ ] Manejo de errores mejorado
- [ ] Loading states
- [ ] Validación de formularios

### 📝 Pendientes
- [ ] Historial de precios (F-02)
- [ ] Predicciones (F-03)
- [ ] Comparación entre plazas (F-04)
- [ ] Autenticación de usuarios (F-05, F-06)
- [ ] Canastas personalizadas (F-07)

## 🤝 Contribución

1. Crear una rama para la nueva funcionalidad
2. Implementar los cambios
3. Probar la funcionalidad
4. Crear un Pull Request

## 📄 Licencia

Proyecto académico - Universidad Pontificia Bolivariana
