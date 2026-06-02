// routes/ats.routes.js
const express = require('express');
const router = express.Router();
const upload = require('../middleware/upload');
const { uploadResume } = require('../controllers/ats.controller');

/**
 * POST /api/ats/upload
 * Upload and analyze resume
 */
router.post('/upload', upload.single('file'), uploadResume);

module.exports = router;
