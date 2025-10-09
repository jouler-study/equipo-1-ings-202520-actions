import axios from 'axios'

// Base API configuration
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

// Create axios instance with base configuration
const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor to handle errors globally
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error)
    return Promise.reject(error)
  }
)

// API Services
export const productService = {
  // Query current prices (F-01)
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
      throw new Error(`Error querying prices: ${error.message}`)
    }
  },

  // Get price history (F-02)
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
      throw new Error(`Error getting history: ${error.message}`)
    }
  },

  // Get price predictions (F-03)
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
      throw new Error(`Error getting predictions: ${error.message}`)
    }
  },

  // Search products (F-11)
  searchProducts: async (query) => {
    try {
      const response = await api.get('/products/search', {
        params: { q: query.trim() }
      })
      return response.data
    } catch (error) {
      throw new Error(`Error searching products: ${error.message}`)
    }
  },

  // Get search suggestions (F-12)
  getSearchSuggestions: async (query) => {
    try {
      const response = await api.get('/products/suggestions', {
        params: { q: query.trim() }
      })
      return response.data
    } catch (error) {
      throw new Error(`Error getting suggestions: ${error.message}`)
    }
  }
}

export const plazaService = {
  // Get market plazas (F-23)
  getPlazas: async (city = 'Medellín') => {
    try {
      const response = await api.get('/plazas', {
        params: { city }
      })
      return response.data
    } catch (error) {
      throw new Error(`Error getting plazas: ${error.message}`)
    }
  },

  // Get detailed plaza information (F-23)
  getPlazaDetails: async (plazaId) => {
    try {
      const response = await api.get(`/plazas/${plazaId}`)
      return response.data
    } catch (error) {
      throw new Error(`Error getting plaza details: ${error.message}`)
    }
  }
}

export const statsService = {
  // Get quick statistics (F-14)
  getQuickStats: async () => {
    try {
      const response = await api.get('/stats/quick')
      return response.data
    } catch (error) {
      throw new Error(`Error getting statistics: ${error.message}`)
    }
  },

  // Get price variations (F-14)
  getPriceVariations: async (period = 'week') => {
    try {
      const response = await api.get('/stats/variations', {
        params: { period }
      })
      return response.data
    } catch (error) {
      throw new Error(`Error getting variations: ${error.message}`)
    }
  }
}

export default api
