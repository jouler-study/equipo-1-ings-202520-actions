import React from 'react'

const Footer = () => {
  return (
    <footer className="py-12" style={{ backgroundColor: 'rgba(76, 167, 114, 0.7)' }}>
      <div className="container">
        <div className="flex justify-center flex-wrap gap-12">
          {/* Enlaces del footer */}
          <a 
            href="#" 
            className="text-white text-lg font-medium hover:text-gray-200 transition-colors px-6 py-3 border-2 border-white border-opacity-50 rounded-xl hover:bg-white hover:bg-opacity-20 shadow-lg"
            style={{ minWidth: '200px', textAlign: 'center', flex: '0 0 auto' }}
          >
            Sobre el proyecto
          </a>
          <a 
            href="#" 
            className="text-white text-lg font-medium hover:text-gray-200 transition-colors px-6 py-3 border-2 border-white border-opacity-50 rounded-xl hover:bg-white hover:bg-opacity-20 shadow-lg"
            style={{ minWidth: '200px', textAlign: 'center', flex: '0 0 auto' }}
          >
            Quiénes somos
          </a>
          <a 
            href="#" 
            className="text-white text-lg font-medium hover:text-gray-200 transition-colors px-6 py-3 border-2 border-white border-opacity-50 rounded-xl hover:bg-white hover:bg-opacity-20 shadow-lg"
            style={{ minWidth: '200px', textAlign: 'center', flex: '0 0 auto' }}
          >
            Términos y condiciones
          </a>
          <a 
            href="#" 
            className="text-white text-lg font-medium hover:text-gray-200 transition-colors px-6 py-3 border-2 border-white border-opacity-50 rounded-xl hover:bg-white hover:bg-opacity-20 shadow-lg"
            style={{ minWidth: '200px', textAlign: 'center', flex: '0 0 auto' }}
          >
            Información de los datos
          </a>
        </div>

        <div className="border-t border-white border-opacity-30 mt-8 pt-8 text-center">
          <p className="text-white text-sm">
            © 2025 PLAZE. Todos los derechos reservados.
          </p>
        </div>
      </div>
    </footer>
  )
}

export default Footer
