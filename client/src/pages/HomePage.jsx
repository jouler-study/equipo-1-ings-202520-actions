import React from 'react'
import ProductSearch from '../components/ProductSearch'

const HomePage = () => {

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <section className="py-16 bg-gray-50">
        <div className="container flex justify-center">
          {/* Main Hero Card */}
          <div className="mb-8" style={{ 
            width: '1200px', 
            height: '1000px', 
            backgroundColor: 'rgba(248, 231, 176, 0.54)',
            borderRadius: '20px',
            padding: '50px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center'
          }}>
            {/* Title */}
            <h1 className="text-6xl font-bold mb-8" style={{ 
              color: '#4CA772',
              textShadow: '2px 2px 4px rgba(0, 0, 0, 0.3)'
            }}>
              PLAZE
            </h1>

            {/* Subtitle */}
            <h2 className="text-xl font-semibold mb-12 text-black">
              Compra mejor con información real
            </h2>

            {/* Content Card */}
            <div className="mb-8" style={{
              width: '1100px',
              height: '350px',
              backgroundColor: 'rgba(247, 224, 147, 0.7)',
              borderRadius: '20px',
              display: 'flex',
              alignItems: 'center',
              padding: '40px',
              position: 'relative'
            }}>
              {/* Left Half - Image */}
              <div className="w-1/2 pr-8" style={{ position: 'relative', zIndex: 1 }}>
                <img 
                  src="/client_images/Plaze-hero-background.jpg" 
                  alt="Plaze Hero Background" 
                  style={{
                    width: '90%',
                    height: '320px',
                    objectFit: 'cover',
                    borderRadius: '16px',
                    boxShadow: '0 8px 32px rgba(0, 0, 0, 0.15)',
                    position: 'relative',
                    zIndex: 2
                  }}
                />
              </div>

              {/* Right Half - Text */}
              <div className="w-1/2 pl-8" style={{ paddingLeft: '60px', position: 'relative', zIndex: 1 }}>
                <p className="text-white text-lg leading-relaxed" style={{ maxWidth: '400px' }}>
                  Consulta precios actualizados de productos agrícolas en las principales plazas de mercado de Medellín.
                </p>
                <br />
                <p className="text-white text-lg leading-relaxed" style={{ maxWidth: '400px' }}>
                  Busca tu producto y obtén información para tomar las mejores decisiones de compra.
                </p>
              </div>
            </div>

            {/* Search Component */}
            <div className="w-full">
              <ProductSearch />
            </div>
          </div>
        </div>
      </section>

    </div>
  )
}

export default HomePage
