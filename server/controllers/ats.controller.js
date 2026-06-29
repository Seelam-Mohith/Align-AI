// controllers/ats.controller.js
const axios = require('axios');
const fs = require('fs');
const path = require('path');
const FormData = require('form-data');
const UserHistory = require('../models/UserHistory');

const PYTHON_SERVICE_URL = process.env.PYTHON_SERVICE_URL || 'http://localhost:8000';

/**
 * Upload and analyze resume
 * @route POST /api/ats/upload
 * @param {File} file - PDF resume file
 */
const uploadResume = async (req, res) => {
  try {
    console.log('=== ATS UPLOAD START ===');
    
    if (!req.file) {
      console.error('❌ No file provided');
      return res.status(400).json({ error: 'No file provided' });
    }

    const filePath = req.file.path;
    const fileName = req.file.originalname;
    
    console.log(`✅ File received: ${fileName}`);
    console.log(`📁 File path: ${filePath}`);
    console.log(`📊 File size: ${req.file.size} bytes`);
    console.log(`📄 MIME type: ${req.file.mimetype}`);

    // Verify file exists
    if (!fs.existsSync(filePath)) {
      console.error('❌ File not found after upload:', filePath);
      return res.status(400).json({ error: 'File upload failed - file not found' });
    }

    // Create FormData to send to Python service
    console.log(`📤 Creating FormData and calling ML service at ${PYTHON_SERVICE_URL}/ats`);
    const formData = new FormData();
    const fileStream = fs.createReadStream(filePath);
    formData.append('file', fileStream, fileName);

    // Call Python microservice
    console.log('⏳ Calling ML service...');
    const response = await axios.post(
      `${PYTHON_SERVICE_URL}/ats`,
      formData,
      {
        headers: formData.getHeaders(),
        timeout: 30000,
      }
    );

    console.log('✅ ML service response received');
    console.log(`📊 Response data:`, JSON.stringify(response.data).substring(0, 200));

    // Save to MongoDB
    try {
      await UserHistory.create({
        analysisType: 'ats',
        data: response.data,
        metadata: {
          resumeName: fileName,
        },
      });
      console.log('💾 Saved to MongoDB');
    } catch (dbErr) {
      console.warn('⚠️  MongoDB save failed (non-critical):', dbErr.message);
    }

    // Clean up uploaded file
    fs.unlink(filePath, (err) => {
      if (err) {
        console.warn('⚠️  Error deleting file:', err.message);
      } else {
        console.log('🗑️  Temp file deleted');
      }
    });

    console.log('=== ATS UPLOAD SUCCESS ===');
    res.json(response.data);
  } catch (error) {
    console.error('❌ ERROR IN ATS UPLOAD');
    console.error('Error type:', error.constructor.name);
    console.error('Error message:', error.message);
    if (error.response) {
      console.error('ML Service response status:', error.response.status);
      console.error('ML Service response data:', error.response.data);
    } else if (error.request) {
      console.error('No response from ML service - request failed');
      console.error('URL attempted:', error.config?.url);
    }
    console.error('Full error:', error);
    
    res.status(500).json({
      error: error.message || 'Error analyzing resume',
      details: error.response?.data || error.message,
    });
  }
};

module.exports = {
  uploadResume,
};
