import axios from 'axios'

// Configuración base de la API
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

// Crear instancia de axios con configuración base
const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor para manejar errores globalmente
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error)
    return Promise.reject(error)
  }
)

// Servicios de la API
export const productService = {
  // Consultar precios actuales (F-01)
  getCurrentPrices: async (product, city, plaza = '') => {
    try {
      const params = {
        product: product.trim(),
        city: city || 'Medellín',
        ...(plaza && { plaza })
      }
      
      const response = await api.get('/prices/current', { params })
      return response.data
    } catch (error) {
      throw new Error(`Error al consultar precios: ${error.message}`)
    }
  },

  // Obtener historial de precios (F-02)
  getPriceHistory: async (product, city, plaza = '', months = 12) => {
    try {
      const params = {
        product: product.trim(),
        city: city || 'Medellín',
        months,
        ...(plaza && { plaza })
      }
      
      const response = await api.get('/prices/history', { params })
      return response.data
    } catch (error) {
      throw new Error(`Error al obtener historial: ${error.message}`)
    }
  },

  // Obtener predicciones de precios (F-03)
  getPricePredictions: async (product, city, plaza = '', months = 3) => {
    try {
      const params = {
        product: product.trim(),
        city: city || 'Medellín',
        months,
        ...(plaza && { plaza })
      }
      
      const response = await api.get('/prices/predictions', { params })
      return response.data
    } catch (error) {
      throw new Error(`Error al obtener predicciones: ${error.message}`)
    }
  },

  // Buscar productos (F-11)
  searchProducts: async (query) => {
    try {
      const response = await api.get('/products/search', {
        params: { q: query.trim() }
      })
      return response.data
    } catch (error) {
      throw new Error(`Error al buscar productos: ${error.message}`)
    }
  },

  // Obtener sugerencias de búsqueda (F-12)
  getSearchSuggestions: async (query) => {
    try {
      const response = await api.get('/products/suggestions', {
        params: { q: query.trim() }
      })
      return response.data
    } catch (error) {
      throw new Error(`Error al obtener sugerencias: ${error.message}`)
    }
  }
}

export const plazaService = {
  // Obtener plazas de mercado (F-23)
  getPlazas: async (city = 'Medellín') => {
    try {
      const response = await api.get('/plazas', {
        params: { city }
      })
      return response.data
    } catch (error) {
      throw new Error(`Error al obtener plazas: ${error.message}`)
    }
  },

  // Obtener información detallada de una plaza (F-23)
  getPlazaDetails: async (plazaId) => {
    try {
      const response = await api.get(`/plazas/${plazaId}`)
      return response.data
    } catch (error) {
      throw new Error(`Error al obtener detalles de la plaza: ${error.message}`)
    }
  }
}

export const statsService = {
  // Obtener estadísticas rápidas (F-14)
  getQuickStats: async () => {
    try {
      const response = await api.get('/stats/quick')
      return response.data
    } catch (error) {
      throw new Error(`Error al obtener estadísticas: ${error.message}`)
    }
  },

  // Obtener variaciones de precios (F-14)
  getPriceVariations: async (period = 'week') => {
    try {
      const response = await api.get('/stats/variations', {
        params: { period }
      })
      return response.data
    } catch (error) {
      throw new Error(`Error al obtener variaciones: ${error.message}`)
    }
  }
}

export default api
