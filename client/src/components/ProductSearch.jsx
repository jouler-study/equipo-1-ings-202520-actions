import React, { useState } from 'react'
import { Filter } from 'lucide-react'

const ProductSearch = () => {
  const [searchData, setSearchData] = useState({
    product: ''
  })

  const handleSubmit = (e) => {
    e.preventDefault()
    if (searchData.product.trim()) {
      console.log('Búsqueda realizada:', searchData.product)
      // Aquí se conectará con la base de datos en el futuro
    }
  }

  const handleInputChange = (field, value) => {
    setSearchData(prev => ({
      ...prev,
      [field]: value
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
              className="px-8 py-5 border border-gray-300 text-xl focus:outline-none focus:ring-2 focus:ring-primary-color focus:border-transparent"
              style={{ 
                borderRadius: '12px 0 0 12px',
                width: '540px',
                flex: 'none'
              }}
              required
            />
            <button 
              type="button"
              className="px-6 py-5 border border-l-0 border-gray-300 hover:bg-gray-100 flex items-center justify-center"
              style={{ 
                borderRadius: '0 12px 12px 0',
                width: '60px',
                flex: 'none'
              }}
            >
              <Filter className="w-7 h-7 text-gray-600" />
            </button>
          </div>
        </div>

        {/* Search Button */}
        <div className="text-center">
          <button
            type="submit"
            disabled={!searchData.product.trim()}
            className="py-5 text-xl font-semibold transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            style={{ 
              backgroundColor: '#D2EDCC',
              color: '#333',
              borderRadius: '12px',
              width: '300px'
            }}
          >
            Buscar precios
          </button>
        </div>
      </form>
    </div>
  )
}

export default ProductSearch
