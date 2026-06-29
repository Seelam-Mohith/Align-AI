// routes/roadmap.routes.js
const express = require('express');
const router = express.Router();
const { generateRoadmap } = require('../controllers/roadmap.controller');

/**
 * POST /api/roadmap/generate
 * Generate career roadmap
 */
router.post('/generate', generateRoadmap);

module.exports = router;
