import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { Filter, X, Store } from 'lucide-react'
import { productService } from '../config/api'

const ProductSearch = () => {
  const navigate = useNavigate()
  const [searchData, setSearchData] = useState({
    product: '',
    plaza: ''
  })
  const [showFilters, setShowFilters] = useState(false)
  const [plazas, setPlazas] = useState([])

  // Fetch available plazas when component mounts
  useEffect(() => {
    const fetchPlazas = async () => {
      try {
        const options = await productService.getOptions()
        setPlazas(options.plazas || [])
      } catch (error) {
        console.error('Error loading plazas:', error)
      }
    }
    fetchPlazas()
  }, [])

  const handleSubmit = (e) => {
    e.preventDefault()
    if (searchData.product.trim()) {
      // Navigate to product detail page with optional plaza parameter
      const productName = searchData.product.trim()
      const params = new URLSearchParams()
      if (searchData.plaza) {
        params.append('plaza', searchData.plaza)
      }
      const queryString = params.toString()
      navigate(`/product/${encodeURIComponent(productName)}${queryString ? `?${queryString}` : ''}`)
    }
  }

  const handleInputChange = (field, value) => {
    setSearchData(prev => ({
      ...prev,
      [field]: value
    }))
  }

  const toggleFilters = () => {
    setShowFilters(!showFilters)
  }

  const clearFilters = () => {
    setSearchData(prev => ({
      ...prev,
      plaza: ''
    }))
  }

  return (
    <div className="bg-white rounded-lg p-10 mx-auto shadow-lg" style={{ width: '1100px' }}>
      <form onSubmit={handleSubmit} className="space-y-8">
        {/* Search Input with Filter Icon */}
        <div className="flex items-center justify-center mb-8">
          <div className="flex items-center" style={{ width: '600px' }}>
            <input
              type="text"
              value={searchData.product}
              onChange={(e) => handleInputChange('product', e.target.value)}
              placeholder="Buscar producto (ej: Tomate, Papa criolla...)"
              className="border border-gray-300 text-xl focus:outline-none focus:ring-2 focus:ring-primary-color focus:border-transparent"
              style={{ 
                borderRadius: '12px 0 0 12px',
                width: '540px',
                flex: 'none',
                paddingLeft: '24px',
                paddingRight: '24px',
                paddingTop: '10px',
                paddingBottom: '10px'
              }}
              required
            />
            <button 
              type="button"
              onClick={toggleFilters}
              className="px-6 border border-l-0 border-gray-300 hover:bg-gray-100 flex items-center justify-center transition-colors"
              style={{ 
                borderRadius: '0 12px 12px 0',
                width: '60px',
                flex: 'none',
                paddingTop: '10px',
                paddingBottom: '10px',
                backgroundColor: showFilters ? '#4CA772' : 'transparent'
              }}
            >
              {showFilters ? (
                <X className="w-7 h-7" style={{ color: 'white' }} />
              ) : (
                <Filter className="w-7 h-7 text-gray-600" />
              )}
            </button>
          </div>
        </div>

        {/* Advanced Filters Section */}
        {showFilters && (
          <div 
            style={{
              backgroundColor: '#f9f9f9',
              borderRadius: '12px',
              padding: '1.5rem',
              marginBottom: '1rem',
              border: '2px solid #4CA772',
              animation: 'slideDown 0.3s ease-out'
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
              <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#4CA772', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Store className="w-5 h-5" />
                Filtros Avanzados
              </h3>
              {searchData.plaza && (
                <button
                  type="button"
                  onClick={clearFilters}
                  style={{
                    fontSize: '0.875rem',
                    color: '#F57C00',
                    textDecoration: 'underline',
                    background: 'none',
                    border: 'none',
                    cursor: 'pointer'
                  }}
                >
                  Limpiar filtros
                </button>
              )}
            </div>

            {/* Plaza Selector */}
            <div style={{ marginBottom: '1rem' }}>
              <label 
                htmlFor="plaza-select"
                style={{ 
                  display: 'block',
                  fontSize: '0.875rem',
                  fontWeight: '500',
                  marginBottom: '0.5rem',
                  color: '#555'
                }}
              >
                Plaza de Mercado (Opcional)
              </label>
              <select
                id="plaza-select"
                value={searchData.plaza}
                onChange={(e) => handleInputChange('plaza', e.target.value)}
                style={{
                  width: '100%',
                  padding: '0.75rem 1rem',
                  border: '1px solid #ddd',
                  borderRadius: '8px',
                  fontSize: '1rem',
                  backgroundColor: 'white',
                  cursor: 'pointer',
                  outline: 'none'
                }}
              >
                <option value="">Todas las plazas</option>
                {plazas.map((plaza) => (
                  <option key={plaza.id} value={plaza.nombre}>
                    {plaza.nombre} - {plaza.ciudad}
                  </option>
                ))}
              </select>
            </div>

            {searchData.plaza && (
              <div 
                style={{
                  padding: '0.75rem',
                  backgroundColor: '#E8F5E9',
                  borderRadius: '8px',
                  fontSize: '0.875rem',
                  color: '#2E7D32',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.5rem'
                }}
              >
                <Store className="w-4 h-4" />
                <span>Buscando en: <strong>{searchData.plaza}</strong></span>
              </div>
            )}
          </div>
        )}

        {/* Search Button */}
        <div className="text-center">
          <button
            type="submit"
            disabled={!searchData.product.trim()}
            className="text-xl font-semibold transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            style={{ 
              backgroundColor: '#D2EDCC',
              color: '#333',
              borderRadius: '25px',
              width: '300px',
              paddingTop: '10px',
              paddingBottom: '10px'
            }}
          >
            Buscar precios
          </button>
        </div>
      </form>

      <style>{`
        @keyframes slideDown {
          from {
            opacity: 0;
            transform: translateY(-10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
      `}</style>
    </div>
  )
}

export default ProductSearch
