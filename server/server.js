// server.js - Main Express server
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');
const path = require('path');
const axios = require('axios');

// Load environment variables
dotenv.config();

// Import routes
const atsRoutes = require('./routes/ats.routes');
const skillGapRoutes = require('./routes/skillGap.routes');
const roadmapRoutes = require('./routes/roadmap.routes');

// Initialize Express app
const app = express();

// CORS Configuration
const corsOrigin = process.env.CORS_ORIGIN || 'http://localhost:3000';
app.use(cors({
  origin: corsOrigin,
  credentials: true
}));

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// MongoDB Connection
const connectDB = async () => {
  try {
    const mongoURI = process.env.MONGODB_URI || 'mongodb://localhost:27017/ai-career-assistant';
    await mongoose.connect(mongoURI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('✅ MongoDB connected successfully');
  } catch (err) {
    console.error('❌ MongoDB connection error:', err.message);
    console.warn('⚠️  Continuing without MongoDB. History persistence is disabled.');
  }
};

connectDB();

// Logging middleware
app.use((req, res, next) => {
  console.log(`📨 ${req.method} ${req.path} - ${new Date().toLocaleTimeString()}`);
  next();
});

// Routes
app.use('/api/ats', atsRoutes);
app.use('/api/skill-gap', skillGapRoutes);
app.use('/api/roadmap', roadmapRoutes);

// Health check route
app.get('/api/health', (req, res) => {
  res.json({ status: 'Server is running' });
});

// Unified health endpoint for quick local verification
app.get('/api/health/all', async (req, res) => {
  const checks = [
    {
      name: 'backend',
      url: 'http://localhost:5000/api/health',
    },
    {
      name: 'frontend',
      url: 'http://localhost:3000',
    },
    {
      name: 'ml_service',
      url: process.env.PYTHON_SERVICE_URL
        ? `${process.env.PYTHON_SERVICE_URL}/health`
        : 'http://localhost:8000/health',
    },
  ];

  const results = await Promise.all(
    checks.map(async (check) => {
      try {
        const response = await axios.get(check.url, { timeout: 2500 });
        return {
          status: 'up',
          status_code: response.status,
          url: check.url,
        };
      } catch (error) {
        return {
          status: 'down',
          status_code: error.response?.status || null,
          url: check.url,
          error: error.code || error.message,
        };
      }
    })
  );

  const services = checks.reduce((acc, check, index) => {
    acc[check.name] = results[index];
    return acc;
  }, {});

  const allUp = Object.values(services).every((service) => service.status === 'up');

  res.status(allUp ? 200 : 503).json({
    overall_status: allUp ? 'up' : 'degraded',
    services,
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(err.status || 500).json({
    error: err.message || 'Internal server error'
  });
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});
