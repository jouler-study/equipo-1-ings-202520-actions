import React from 'react'
import { Link } from 'react-router-dom'

const PasswordRecoveryPage = () => {
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

      {/* Main content centered */}
      <div style={{
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '20px',
        gap: '40px'
      }}>
        {/* Page title */}
        <h1 style={{
          fontSize: '48px',
          fontWeight: '600',
          textAlign: 'center',
          lineHeight: '1.2',
          marginTop: '100px',
          color: '#000000'
        }}>
          Recuperar contraseña
        </h1>

        {/* Message box with mail icon */}
        <div style={{
          position: 'relative',
          width: '800px',
          height: '250px',
          backgroundColor: '#D2EDCC',
          borderRadius: '8px',
          display: 'flex',
          alignItems: 'center',
          padding: '40px 60px'
        }}>
          {/* Mail icon container (positioned at top-left corner of green box) */}
          <div style={{
            position: 'absolute',
            top: '0',
            left: '0',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            transform: 'translate(-50%, -50%)'
          }}>
            {/* Rectangle background */}
            <img 
              src="/client_images/Rectangle-mail.svg" 
              alt="Mail Background" 
              style={{
                width: 'auto',
                height: 'auto'
              }}
            />
            {/* Mail icon on top */}
            <img 
              src="/client_images/Mail-icon.svg" 
              alt="Mail Icon" 
              style={{
                position: 'absolute',
                width: 'auto',
                height: 'auto'
              }}
            />
          </div>

          {/* Message text */}
          <div style={{
            flex: 1,
            color: '#000000',
            fontSize: '18px',
            lineHeight: '1.6'
          }}>
            <p style={{ marginBottom: '16px' }}>
              <strong>Instrucciones enviadas a tu correo.</strong>
            </p>
            <p style={{ marginBottom: '16px' }}>
              Hemos enviado un enlace para restablecer tu contraseña a tu email.
            </p>
            <p>
              Revisa tu bandeja de entrada y sigue los pasos para crear una nueva contraseña.
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default PasswordRecoveryPage

