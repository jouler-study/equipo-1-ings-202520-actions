import React, { useState, useRef, useEffect } from 'react'
import { User, LogOut, ChevronDown } from 'lucide-react'

const UserMenu = ({ userName = "Usuario" }) => {
  const [isOpen, setIsOpen] = useState(false)
  const menuRef = useRef(null)

  // Close menu when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }

    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const handleLogout = () => {
    console.log('Cerrando sesión...')
    // TODO: Implement logout logic with backend
    setIsOpen(false)
  }

  const handleProfile = () => {
    console.log('Ir a información personal...')
    // TODO: Navigate to profile page
    setIsOpen(false)
  }

  return (
    <div className="flex items-center" style={{ gap: '12px', position: 'relative' }} ref={menuRef}>
      {/* User Greeting (static text with icon) */}
      <div className="flex items-center" style={{ gap: '8px' }}>
        <User className="w-5 h-5" style={{ color: '#333' }} />
        <span className="text-sm font-medium" style={{ color: '#333' }}>
          Hola, {userName}
        </span>
      </div>

      {/* Dropdown Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center justify-center px-3 py-3 border border-black transition-all hover:shadow-md"
        style={{
          backgroundColor: '#D2EDCC',
          boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
          borderRadius: '8px',
          position: 'relative'
        }}
      >
        <ChevronDown 
          className="w-5 h-5 transition-transform" 
          style={{ 
            transform: isOpen ? 'rotate(180deg)' : 'rotate(0deg)' 
          }} 
        />
      </button>

      {/* Dropdown Menu */}
      {isOpen && (
        <div
          className="bg-white border border-gray-200 shadow-lg"
          style={{
            position: 'absolute',
            top: '100%',
            right: '0',
            marginTop: '8px',
            width: '224px',
            borderRadius: '8px',
            zIndex: 9999
          }}
        >
          <div className="py-1">
            {/* Profile Option */}
            <button
              onClick={handleProfile}
              className="w-full text-left px-4 py-3 text-sm text-gray-700 hover:bg-gray-100 flex items-center transition-colors"
              style={{ gap: '12px' }}
            >
              <User className="w-4 h-4" />
              <span>Información personal</span>
            </button>

            {/* Divider */}
            <div className="border-t border-gray-200 my-1"></div>

            {/* Logout Option */}
            <button
              onClick={handleLogout}
              className="w-full text-left px-4 py-3 text-sm text-red-600 hover:bg-red-50 flex items-center transition-colors"
              style={{ gap: '12px' }}
            >
              <LogOut className="w-4 h-4" />
              <span>Cerrar sesión</span>
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

export default UserMenu
