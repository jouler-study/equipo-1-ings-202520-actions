import React from 'react'
import { Search, User, UserPlus } from 'lucide-react'

const Header = () => {
  return (
    <header className="sticky top-0 z-50" style={{ backgroundColor: 'rgba(76, 167, 114, 0.7)' }}>
      <div className="container">
        <div className="flex items-center justify-between py-6">
          {/* Logo */}
          <div className="flex items-center">
            <img 
              src="/client_images/Plaze-Logo.png" 
              alt="Plaze Logo" 
              style={{ 
                height: '80px', 
                width: 'auto',
                maxHeight: '80px',
                objectFit: 'contain'
              }}
            />
          </div>

          {/* Search Bar - Centered */}
          <div className="flex-1 max-w-md mx-0">
            <div className="flex items-center">
              <input
                type="text"
                placeholder="Buscar un producto"
                className="px-4 border border-gray-300 rounded-l-md text-base focus:outline-none focus:ring-2 focus:ring-primary-color focus:border-transparent"
                style={{ width: '250px', height: '40px' }}
              />
              <button className="px-4 border border-l-0 border-gray-300 rounded-r-md hover:bg-gray-100 flex items-center justify-center" style={{ height: '40px' }}>
                <Search className="w-5 h-5 text-gray-600" />
              </button>
            </div>
          </div>

          {/* User Actions */}
          <div className="flex items-center" style={{ gap: '50px' }}>
            <button 
              className="px-6 py-3 border border-black text-sm font-medium transition-all flex items-center"
              style={{ 
                backgroundColor: '#D2EDCC',
                boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
                minWidth: '140px',
                gap: '8px',
                borderRadius: '8px'
              }}
            >
              <User className="w-4 h-4" />
              Iniciar Sesión
            </button>
            <button 
              className="px-6 py-3 border border-black text-sm font-medium transition-all flex items-center"
              style={{ 
                backgroundColor: '#D2EDCC',
                boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
                minWidth: '140px',
                gap: '8px',
                borderRadius: '8px'
              }}
            >
              <UserPlus className="w-4 h-4" />
              Registrarse
            </button>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header
