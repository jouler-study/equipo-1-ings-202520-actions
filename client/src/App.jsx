import React from 'react'
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom'
import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import Header from './components/Header'
import Footer from './components/Footer'

/**
 * AppContent Component
 * Handles the main content layout with conditional header and footer display
 * Header and Footer are hidden on authentication pages (login, register, password recovery)
 */
function AppContent() {
  const location = useLocation()
  
  // Hide header and footer on login page
  const showHeader = location.pathname !== '/login'
  const showFooter = location.pathname !== '/login'

  return (
    <div className="min-h-screen flex flex-col">
      {showHeader && <Header />}
      <main className="flex-1">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </main>
      {showFooter && <Footer />}
    </div>
  )
}

/**
 * App Component
 * Root component that wraps the application with React Router
 */
function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  )
}

export default App
