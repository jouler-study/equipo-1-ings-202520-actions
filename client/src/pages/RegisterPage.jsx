import React, { useState } from 'react'
import { Link } from 'react-router-dom'

const RegisterPage = () => {
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [errorMessage, setErrorMessage] = useState('')

  const handleRegister = () => {
    if (password !== confirmPassword) {
      setErrorMessage('Las contraseñas no coinciden')
      return
    }
    setErrorMessage('')
    // Handle registration logic here
    console.log('Registration successful')
  }

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

      {/* Centered registration form */}
      <div style={{
        flex: 1,
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '20px'
      }}>
        <div style={{
          width: '600px',
          minHeight: '230px',
          backgroundColor: '#F5F5F5',
          border: '1px solid rgba(0, 0, 0, 0.25)',
          boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)',
          borderRadius: '8px',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          padding: '40px 65px'
        }}>
          {/* Page title */}
          <h1 style={{
            fontSize: '48px',
            fontWeight: '600',
            marginBottom: '35px',
            textAlign: 'center',
            lineHeight: '1.2'
          }}>
            <span style={{ color: '#000000' }}>Registrate en </span>
            <span style={{ color: '#4CA772' }}>Plaze</span>
          </h1>

          {/* User icon with background ellipse */}
          <div style={{
            position: 'relative',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            marginBottom: '35px'
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

          {/* Full name input field */}
          <input
            type="text"
            placeholder="Nombre completo"
            style={{
              width: '470px',
              height: '65px',
              backgroundColor: 'rgba(217, 217, 217, 0.5)',
              border: '1px solid #000000',
              borderRadius: '4px',
              padding: '0 15px',
              fontSize: '18px',
              marginBottom: '35px'
            }}
          />

          {/* Email input field */}
          <input
            type="email"
            placeholder="Correo electrónico"
            style={{
              width: '470px',
              height: '65px',
              backgroundColor: 'rgba(217, 217, 217, 0.5)',
              border: '1px solid #000000',
              borderRadius: '4px',
              padding: '0 15px',
              fontSize: '18px',
              marginBottom: '35px'
            }}
          />

          {/* Password input field */}
          <input
            type="password"
            placeholder="Contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={{
              width: '470px',
              height: '65px',
              backgroundColor: 'rgba(217, 217, 217, 0.5)',
              border: '1px solid #000000',
              borderRadius: '4px',
              padding: '0 15px',
              fontSize: '18px',
              marginBottom: '15px'
            }}
          />

          {/* Password requirements */}
          <div style={{
            width: '470px',
            fontSize: '14px',
            color: '#666666',
            marginBottom: '35px',
            lineHeight: '1.5'
          }}>
            La contraseña debe contener mínimo 8 caracteres, una mayúscula, un número y un carácter especial (!@#$%^&*).
          </div>

          {/* Confirm password input field */}
          <input
            type="password"
            placeholder="Repetir contraseña"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            style={{
              width: '470px',
              height: '65px',
              backgroundColor: 'rgba(217, 217, 217, 0.5)',
              border: '1px solid #000000',
              borderRadius: '4px',
              padding: '0 15px',
              fontSize: '18px',
              marginBottom: '20px'
            }}
          />

          {/* Error message */}
          {errorMessage && (
            <div style={{
              color: '#FF0000',
              fontSize: '16px',
              marginBottom: '20px'
            }}>
              {errorMessage}
            </div>
          )}

          {/* Register button */}
          <button
            onClick={handleRegister}
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
              padding: '10px',
              marginTop: '10px',
              boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)'
            }}
          >
            Registrarse
          </button>
        </div>
      </div>
    </div>
  )
}

export default RegisterPage

