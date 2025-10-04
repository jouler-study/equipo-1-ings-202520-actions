# 🚀 Instrucciones para Ejecutar PLAZE Frontend

## 📋 Prerrequisitos

- **Node.js** (versión 16 o superior)
- **npm** (viene con Node.js)
- **Servidor backend** ejecutándose en `http://localhost:8000`

## 🛠️ Instalación y Ejecución

### 1. Instalar Dependencias
```bash
cd client
npm install
```

### 2. Configurar Variables de Entorno
Crear archivo `.env` en la carpeta `client`:
```env
VITE_API_URL=http://localhost:8000/api
```

### 3. Ejecutar en Modo Desarrollo
```bash
npm run dev
```

### 4. Abrir en el Navegador
- URL: http://localhost:3000
- El servidor de desarrollo se ejecuta en el puerto 3000

## 🔧 Scripts Disponibles

- `npm run dev` - Servidor de desarrollo con hot reload
- `npm run build` - Construir para producción
- `npm run preview` - Vista previa de la construcción
- `npm run lint` - Ejecutar linter de código

## 📱 Funcionalidades Implementadas

### ✅ Completadas
- **Búsqueda de productos** con filtros por ciudad y plaza
- **Visualización de precios** con tendencias y comparaciones
- **Diseño responsive** para móviles y desktop
- **Integración con API** (preparada para conectar con el servidor)
- **Estadísticas rápidas** del sistema
- **Manejo de errores** con fallback a datos de ejemplo

### 🎨 Características de Diseño
- **Colores**: Azul principal (#3b82f6), Verde secundario (#10b981)
- **Tipografía**: Inter (sistema de fuentes)
- **Componentes**: Cards, botones, formularios consistentes
- **Responsive**: Mobile-first design

## 🔌 Conexión con el Servidor

El frontend está configurado para conectarse con el servidor backend en:
- **URL Base**: `http://localhost:8000/api`
- **Endpoints principales**:
  - `GET /prices/current` - Consulta de precios actuales (F-01)
  - `GET /prices/history` - Historial de precios (F-02)
  - `GET /prices/predictions` - Predicciones (F-03)
  - `GET /products/search` - Búsqueda de productos (F-11)
  - `GET /plazas` - Lista de plazas (F-23)

## 🐛 Solución de Problemas

### Error de Conexión con el Servidor
Si el servidor no está disponible, el frontend mostrará:
- Un mensaje de advertencia
- Datos de ejemplo para demostración
- Funcionalidad completa en modo offline

### Puerto en Uso
Si el puerto 3000 está ocupado:
```bash
# Vite usará automáticamente el siguiente puerto disponible
# O puedes especificar un puerto diferente:
npm run dev -- --port 3001
```

### Problemas de CORS
Asegúrate de que el servidor backend tenga configurado CORS para permitir requests desde `http://localhost:3000`.

## 📁 Estructura del Proyecto

```
client/
├── src/
│   ├── components/          # Componentes reutilizables
│   │   ├── Header.jsx      # Cabecera
│   │   ├── Footer.jsx      # Pie de página
│   │   ├── ProductSearch.jsx  # Búsqueda
│   │   ├── PriceResults.jsx   # Resultados
│   │   └── QuickStats.jsx     # Estadísticas
│   ├── pages/              # Páginas
│   │   └── HomePage.jsx    # Página principal
│   ├── config/             # Configuración
│   │   └── api.js          # Servicios API
│   ├── App.jsx             # Componente raíz
│   ├── main.jsx            # Punto de entrada
│   └── index.css           # Estilos globales
├── public/                 # Archivos estáticos
├── package.json            # Dependencias
├── vite.config.js          # Configuración Vite
└── index.html              # HTML principal
```

## 🎯 Próximos Pasos

1. **Conectar con el servidor real** cuando esté disponible
2. **Implementar autenticación** (F-05, F-06)
3. **Agregar historial de precios** (F-02)
4. **Implementar predicciones** (F-03)
5. **Añadir canastas personalizadas** (F-07)

## 📞 Soporte

Para problemas o preguntas:
- Revisar la consola del navegador para errores
- Verificar que el servidor backend esté ejecutándose
- Consultar la documentación de la API en el servidor
