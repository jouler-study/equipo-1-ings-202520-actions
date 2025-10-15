# PLAZE - Frontend Client

Web application for querying product prices in Medellín's market plazas.

## 🚀 Features

### Landing Page
- **Welcome screen**: First point of contact for new visitors
- **Product showcase**: Visual presentation of platform capabilities
- **Interactive CTA**: Animated "Register for Free" button with hover effects
- **About sections**: Information about the platform, team, and data sources
- **Terms and conditions**: Legal information and data transparency

### Application Features
- **Current price queries** (F-01): Search prices by product, city, and plaza
- **Price comparison**: Compare prices between different plazas
- **Intuitive interface**: Usability-focused design (NF-01)
- **Responsive**: Adaptable to different devices
- **Quick search**: With automatic suggestions

## 🛠️ Technologies

- **React 18** - Main framework
- **Vite** - Build tool
- **React Router** - Navigation with page transitions
- **Axios** - HTTP client
- **Lucide React** - Icons
- **CSS3** - Custom styles with animations

---

## 📋 Prerequisites

- **Node.js** (version 16 or higher)
- **npm** (comes with Node.js)
- **Backend server** running on `http://localhost:8000`

---

## 🚀 Installation and Execution

### 1. Install Dependencies
```bash
cd client
npm install
```

### 2. Configure Environment Variables
Create a `.env` file in the `client` folder:
```env
VITE_API_URL=http://localhost:8000/api
```

### 3. Run in Development Mode
```bash
npm run dev
```

### 4. Open in Browser
- URL: http://localhost:3000
- The development server runs on port 3000

---

## 🔧 Available Scripts

- `npm run dev` - Development server with hot reload
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run code linter

---

## 📱 Implemented Features

### ✅ Completed
- [x] Project base structure
- [x] **Landing page** (initial page for new visitors)
- [x] Product search component
- [x] Price results visualization
- [x] Responsive design
- [x] API integration (ready to connect)
- [x] Quick statistics
- [x] Error handling with fallback to sample data
- [x] Login page (NF-01 Usability - User Authentication Frontend)
- [x] Interactive UI animations
- [x] **Page transitions** (smooth fade and slide animations)
- [x] User logout flow (returns to landing page)

### 🔄 In Progress
- [ ] Real server connection
- [ ] Register page
- [ ] Password recovery page
- [ ] Improved error handling
- [ ] Loading states
- [ ] Form validation

### 📝 Pending
- [ ] Price history (F-02)
- [ ] Predictions (F-03)
- [ ] Comparison between plazas (F-04)
- [ ] Backend authentication integration (F-05, F-06)
- [ ] Custom baskets (F-07)

---

## 🏗️ Project Structure

```
client/
├── src/
│   ├── components/              # Reusable components
│   │   ├── Header.jsx           # Application header
│   │   ├── LandingHeader.jsx    # Landing page header
│   │   ├── Footer.jsx           # Footer
│   │   ├── PageTransition.jsx   # Page transition wrapper
│   │   ├── ProductSearch.jsx    # Search form
│   │   ├── PriceResults.jsx     # Price results
│   │   ├── QuickStats.jsx       # Quick statistics
│   │   └── UserMenu.jsx         # User menu with logout
│   ├── pages/                   # Main pages
│   │   ├── LandingPage.jsx      # Landing page (root)
│   │   ├── HomePage.jsx         # Main application page
│   │   ├── LoginPage.jsx        # Login page
│   │   ├── RegisterPage.jsx     # Registration page
│   │   ├── RegisterConfirmationPage.jsx  # Registration success
│   │   └── PasswordRecoveryPage.jsx      # Password recovery
│   ├── styles/                  # Style files
│   │   └── transitions.css      # Page transition animations
│   ├── config/                  # Configuration
│   │   └── api.js               # API services
│   ├── App.jsx                  # Root component with routing
│   ├── main.jsx                 # Entry point
│   └── index.css                # Global styles
├── public/                      # Static files
│   └── client_images/           # Images and SVG icons
├── package.json                 # Dependencies
├── vite.config.js               # Vite configuration
└── index.html                   # Main HTML
```

---

## 🗺️ Routes

The application uses the following route structure:

### Public Routes
- **`/`** - Landing page (default entry point for new visitors)
- **`/login`** - User login page
- **`/register`** - User registration page
- **`/register-confirmation`** - Registration confirmation page
- **`/password-recovery`** - Password recovery page

### Protected Routes (require authentication)
- **`/home`** - Main application page with product search and price queries
- More routes will be added for authenticated users

### Route Behavior
- First-time visitors land on **`/`** (Landing Page)
- Landing page includes a call-to-action to register/login
- After authentication, users are redirected to **`/home`**
- Landing page, login, and registration pages have their own custom header and footer
- Application pages (`/home`) use the standard header with user menu

### Landing Page Details
The landing page (`/`) serves as the entry point for new users and includes:
- **Hero section**: Main value proposition with interactive elements
- **Feature showcase**: Images and descriptions of platform capabilities
- **About Plaze**: Mission and value proposition
- **Team information**: Background of the development team
- **Legal sections**: Terms & conditions, and data source information (DANE)
- **Custom header**: Simplified navigation with login/register buttons
- **Interactive animations**: Smooth floating and glow effects on CTA button

---

## 🎬 UI/UX Enhancements

### Page Transitions
The application features smooth CSS-based page transitions for a modern user experience:

- **Fade and Slide animations**: Pages smoothly fade out and slide up when leaving, then fade in and slide up when entering
- **Duration**: 0.3 seconds for quick but visible transitions
- **Timing function**: Cubic-bezier easing for natural motion
- **Landing page special effect**: Subtle scale animation on first load
- **No dependencies**: Pure CSS implementation (no external libraries required)
- **Performance**: Hardware-accelerated transforms for smooth 60fps animations

### Interactive Elements
- **Animated CTA buttons**: Floating and glow effects on primary call-to-action
- **Hover effects**: Smooth transitions on buttons, cards, and interactive elements
- **Smooth scrolling**: Native smooth scroll behavior enabled
- **Card animations**: Subtle lift effect on hover

### User Flow
- **Logout behavior**: Clicking "Cerrar sesión" returns user to landing page
- **Navigation**: Seamless transitions between all routes
- **Loading states**: Pulse animations available for async operations

---

## 🔌 API Endpoints

The client connects to the following server endpoints:

### Price Queries (F-01)
- `GET /api/prices/current` - Current prices
- `GET /api/prices/history` - Price history
- `GET /api/prices/predictions` - Predictions

### Products
- `GET /api/products/search` - Product search
- `GET /api/products/suggestions` - Search suggestions

### Market Plazas
- `GET /api/plazas` - List of plazas
- `GET /api/plazas/{id}` - Plaza details

### Statistics
- `GET /api/stats/quick` - Quick statistics
- `GET /api/stats/variations` - Price variations

---

## 🎨 Design

The design follows Figma specifications and complies with usability requirements (NF-01):

- **Main colors**: Blue (#3b82f6), Green (#10b981)
- **Typography**: Inter (system fonts)
- **Spacing**: 8px system
- **Components**: Consistent cards, buttons, and forms

### Responsive Design
- **Mobile First**: Mobile-optimized design
- **Breakpoints**: 640px, 768px, 1024px
- **Grid System**: CSS Grid and Flexbox

---

## 🔧 Server Configuration

For the client to work correctly, the server must be running on:
- **URL**: http://localhost:8000
- **CORS**: Configured to allow requests from http://localhost:3000

---

## 🐛 Troubleshooting

### Server Connection Error
If the server is unavailable, the frontend will display:
- A warning message
- Sample data for demonstration
- Full functionality in offline mode

### Port in Use
If port 3000 is occupied:
```bash
# Vite will automatically use the next available port
# Or you can specify a different port:
npm run dev -- --port 3001
```

### CORS Issues
Make sure the backend server has CORS configured to allow requests from `http://localhost:3000`.

---

## 🤝 Contributing

1. Create a branch for the new feature
2. Implement changes
3. Test functionality
4. Create a Pull Request

---

## 📞 Support

For issues or questions:
- Check the browser console for errors
- Verify that the backend server is running
- Consult the API documentation on the server

---

## 📄 License

Academic project - Universidad Pontificia Bolivariana

