import React from 'react'
import { Link } from 'react-router-dom'

const LoginPage = () => {
  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#FFFFFF',
      display: 'flex',
      flexDirection: 'column',
      position: 'relative'
    }}>
      {/* Logo in top left corner */}
      <div style={{
        position: 'absolute',
        top: '10px',
        left: '40px'
      }}>
        <Link to="/">
          <img 
            src="/client_images/Plaze-Logo.png" 
            alt="Plaze Logo" 
            style={{
              height: '220px',
              width: 'auto',
              objectFit: 'contain',
              cursor: 'pointer'
            }}
          />
        </Link>
      </div>

      {/* Centered login form */}
      <div style={{
        flex: 1,
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '20px'
      }}>
        <div style={{
          width: '680px',
          height: '750px',
          backgroundColor: '#F5F5F5',
          border: '1px solid rgba(0, 0, 0, 0.25)',
          boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)',
          borderRadius: '8px',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          padding: '60px 80px'
        }}>
          {/* Page title */}
          <h1 style={{
            fontSize: '48px',
            fontWeight: '600',
            marginBottom: '55px',
            textAlign: 'center',
            lineHeight: '1.2'
          }}>
            <span style={{ color: '#000000' }}>Inicia sesión en </span>
            <span style={{ color: '#4CA772' }}>Plaze</span>
          </h1>

          {/* User icon with background ellipse */}
          <div style={{
            position: 'relative',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            marginBottom: '40px'
          }}>
            {/* Background ellipse */}
            <img 
              src="/client_images/Ellipse-user-auth.svg" 
              alt="User Background" 
              style={{
                width: 'auto',
                height: 'auto'
              }}
            />
            {/* User icon on top */}
            <img 
              src="/client_images/User-icon.svg" 
              alt="User Icon" 
              style={{
                position: 'absolute',
                width: 'auto',
                height: 'auto'
              }}
            />
          </div>

          {/* Username input field */}
          <input
            type="text"
            placeholder="Nombre de usuario"
            style={{
              width: '350px',
              height: '60px',
              backgroundColor: 'rgba(217, 217, 217, 0.5)',
              border: '1px solid #000000',
              borderRadius: '4px',
              padding: '0 12px',
              fontSize: '18px',
              marginBottom: '32px'
            }}
          />

          {/* Password input field */}
          <input
            type="password"
            placeholder="Contraseña"
            style={{
              width: '350px',
              height: '60px',
              backgroundColor: 'rgba(217, 217, 217, 0.5)',
              border: '1px solid #000000',
              borderRadius: '4px',
              padding: '0 12px',
              fontSize: '18px',
              marginBottom: '32px'
            }}
          />

          {/* Login button */}
          <button
            style={{
              width: '200px',
              height: '50px',
              backgroundColor: '#D2EDCC',
              border: 'none',
              borderRadius: '20px',
              color: '#000000',
              fontSize: '24px',
              fontWeight: '500',
              cursor: 'pointer',
              marginTop: '10px',
              boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)'
            }}
          >
            Iniciar Sesión
          </button>

          {/* Forgot password link */}
          <div style={{
            marginTop: '20px',
            fontSize: '16px',
            textAlign: 'center'
          }}>
            <span style={{ color: '#000000' }}>¿Olvidaste tu contraseña? </span>
            <Link 
              to="/recuperar-contrasena" 
              style={{
                color: '#4CA772',
                textDecoration: 'underline',
                cursor: 'pointer'
              }}
            >
              Recuperar contraseña
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}

export default LoginPage

