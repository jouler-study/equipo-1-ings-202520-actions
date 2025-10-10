# PLAZE - Frontend Client

Web application for querying product prices in Medellín's market plazas.

## 🚀 Features

- **Current price queries** (F-01): Search prices by product, city, and plaza
- **Price comparison**: Compare prices between different plazas
- **Intuitive interface**: Usability-focused design (NF-01)
- **Responsive**: Adaptable to different devices
- **Quick search**: With automatic suggestions

## 🛠️ Technologies

- **React 18** - Main framework
- **Vite** - Build tool
- **React Router** - Navigation
- **Axios** - HTTP client
- **Lucide React** - Icons
- **CSS3** - Custom styles

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
- [x] Product search component
- [x] Price results visualization
- [x] Responsive design
- [x] API integration (ready to connect)
- [x] Quick statistics
- [x] Error handling with fallback to sample data
- [x] Login page (NF-01 Usability - User Authentication Frontend)

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
│   ├── components/          # Reusable components
│   │   ├── Header.jsx       # Application header
│   │   ├── Footer.jsx       # Footer
│   │   ├── ProductSearch.jsx  # Search form
│   │   ├── PriceResults.jsx   # Price results
│   │   ├── QuickStats.jsx     # Quick statistics
│   │   └── UserMenu.jsx       # User menu
│   ├── pages/               # Main pages
│   │   ├── HomePage.jsx     # Home page
│   │   └── LoginPage.jsx    # Login page
│   ├── config/              # Configuration
│   │   └── api.js           # API services
│   ├── App.jsx              # Root component with routing
│   ├── main.jsx             # Entry point
│   └── index.css            # Global styles
├── public/                  # Static files
│   └── client_images/       # Images and SVG icons
├── package.json             # Dependencies
├── vite.config.js           # Vite configuration
└── index.html               # Main HTML
```

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

## 🎯 Next Steps

1. **Complete authentication pages** (Register, Password Recovery)
2. **Connect with real server** when available
3. **Implement backend authentication** (F-05, F-06)
4. **Add price history** (F-02)
5. **Implement predictions** (F-03)
6. **Add custom baskets** (F-07)

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

