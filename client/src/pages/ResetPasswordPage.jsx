import React, { useState } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import { authService } from '../config/api'

const ResetPasswordPage = () => {
  // State for password, confirm password, error and success messages
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const navigate = useNavigate()

  // Get token from URL query string
  const query = new URLSearchParams(useLocation().search)
  const token = query.get('token')

  // Handle password reset form submission
  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setMessage('')
    setIsLoading(true)

    // Basic validations
    if (!password || !confirmPassword) {
      setError('Por favor completa todos los campos')
      setIsLoading(false)
      return
    }
    if (password !== confirmPassword) {
      setError('Las contraseñas no coinciden')
      setIsLoading(false)
      return
    }

    // Validate password requirements
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/
    if (!passwordRegex.test(password)) {
      setError('La contraseña no cumple con los requisitos mínimos')
      setIsLoading(false)
      return
    }

    try {
      // Call backend API to reset password
      await authService.resetPassword(token, password)
      setMessage('¡Contraseña restablecida exitosamente!')
    } catch (err) {
      console.error('Reset password error:', err)
      const errorMsg = err.message || 'Ocurrió un error al restablecer la contraseña'
      
      // User-friendly error messages
      if (errorMsg.includes('inválido')) {
        setError('El enlace de recuperación es inválido o ya fue usado')
      } else if (errorMsg.includes('expirado')) {
        setError('El enlace de recuperación ha expirado. Solicita uno nuevo.')
      } else if (errorMsg.includes('contraseña')) {
        setError('La contraseña no cumple con los requisitos de seguridad')
      } else {
        setError(errorMsg)
      }
    } finally {
      setIsLoading(false)
    }
  }

  // Navigate back to login page
  const handleBackToLogin = () => {
    navigate('/login')
  }

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#FFFFFF',
      display: 'flex',
      flexDirection: 'column',
      position: 'relative'
    }}>
      {/* Logo */}
      <div style={{ position: 'absolute', top: '10px', left: '40px' }}>
        <Link to="/">
          <img
            src="./client_images/Plaze-Logo.png"
            alt="Plaze Logo"
            style={{ height: '220px', width: 'auto', objectFit: 'contain', cursor: 'pointer' }}
          />
        </Link>
      </div>

      {/* Main content */}
      <div style={{
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '20px',
        gap: '40px'
      }}>
        <h1 style={{
          fontSize: '48px',
          fontWeight: '600',
          textAlign: 'center',
          lineHeight: '1.2',
          marginTop: '100px',
          color: '#000000'
        }}>
          Restablecer contraseña
        </h1>

        {!message ? (
          <div style={{
            width: '600px',
            backgroundColor: '#F5F5F5',
            border: '1px solid rgba(0, 0, 0, 0.25)',
            boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)',
            borderRadius: '8px',
            padding: '50px 60px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center'
          }}>
            <p style={{
              fontSize: '18px',
              color: '#000000',
              textAlign: 'center',
              marginBottom: '30px',
              lineHeight: '1.6'
            }}>
              Ingresa tu nueva contraseña para restablecer tu cuenta.
            </p>

            <form onSubmit={handleSubmit} style={{ width: '100%' }}>
              {/* New password input */}
              <input
                type="password"
                placeholder="Nueva contraseña"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                disabled={isLoading}
                style={{
                  width: '100%',
                  height: '65px',
                  backgroundColor: 'rgba(217, 217, 217, 0.5)',
                  border: '1px solid #000000',
                  borderRadius: '4px',
                  padding: '0 15px',
                  fontSize: '18px',
                  marginBottom: '10px',
                  opacity: isLoading ? 0.6 : 1
                }}
              />
              {/* Password requirements */}
              <p style={{
                fontSize: '14px',
                color: '#555',
                marginBottom: '20px',
                lineHeight: '1.4'
              }}>
                La contraseña debe tener al menos 8 caracteres, incluir una letra mayúscula, un número y un carácter especial (!@#$%^&*).
              </p>

              {/* Confirm password input */}
              <input
                type="password"
                placeholder="Confirmar contraseña"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                disabled={isLoading}
                style={{
                  width: '100%',
                  height: '65px',
                  backgroundColor: 'rgba(217, 217, 217, 0.5)',
                  border: '1px solid #000000',
                  borderRadius: '4px',
                  padding: '0 15px',
                  fontSize: '18px',
                  marginBottom: '20px',
                  opacity: isLoading ? 0.6 : 1
                }}
              />

              {/* Error message */}
              {error && (
                <div style={{
                  color: '#D32F2F',
                  backgroundColor: '#FFEBEE',
                  padding: '12px 20px',
                  borderRadius: '4px',
                  fontSize: '14px',
                  marginBottom: '20px',
                  textAlign: 'center',
                  border: '1px solid #EF5350'
                }}>
                  {error}
                </div>
              )}

              {/* Submit button */}
              <div style={{ display: 'flex', justifyContent: 'center' }}>
                <button
                  type="submit"
                  disabled={isLoading}
                  style={{
                    width: '200px',
                    height: '50px',
                    backgroundColor: isLoading ? '#A8E88D' : '#D2EDCC',
                    border: '1px solid #000000',
                    borderRadius: '20px',
                    color: '#000000',
                    fontSize: '24px',
                    fontWeight: '500',
                    cursor: isLoading ? 'not-allowed' : 'pointer',
                    marginTop: '10px',
                    boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)',
                    opacity: isLoading ? 0.7 : 1
                  }}
                >
                  {isLoading ? 'Cambiando...' : 'Cambiar'}
                </button>
              </div>
            </form>
          </div>
        ) : (
          // Success message
          <div style={{
            position: 'relative',
            width: '800px',
            minHeight: '250px',
            backgroundColor: '#D2EDCC',
            borderRadius: '8px',
            display: 'flex',
            alignItems: 'center',
            padding: '40px 60px',
            flexDirection: 'column',
            justifyContent: 'center',
            textAlign: 'center',
            gap: '20px'
          }}>
            <p style={{ 
              fontSize: '24px', 
              fontWeight: '600',
              color: '#000000',
              marginBottom: '10px'
            }}>
              {message}
            </p>
            <p style={{ 
              fontSize: '18px', 
              color: '#000000',
              lineHeight: '1.6'
            }}>
              Tu contraseña ha sido actualizada correctamente. Ahora puedes iniciar sesión con tu nueva contraseña.
            </p>
            <button
              onClick={handleBackToLogin}
              style={{
                width: '250px',
                height: '50px',
                backgroundColor: '#FFFFFF',
                border: '1px solid #000000',
                borderRadius: '20px',
                color: '#000000',
                fontSize: '18px',
                fontWeight: '500',
                cursor: 'pointer',
                padding: '10px 20px',
                boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)',
                marginTop: '10px'
              }}
            >
              Ir a Inicio de sesión
            </button>
          </div>
        )}
      </div>
    </div>
  )
}

export default ResetPasswordPage

