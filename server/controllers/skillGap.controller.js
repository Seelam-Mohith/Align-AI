// controllers/skillGap.controller.js
const axios = require('axios');
const UserHistory = require('../models/UserHistory');

const PYTHON_SERVICE_URL = process.env.PYTHON_SERVICE_URL || 'http://localhost:8000';

/**
 * Analyze skill gap between resume and job description
 * @route POST /api/skill-gap/analyze
 * @param {String} resume_text - Resume text content
 * @param {String} job_description - Job description text
 */
const analyzeSkillGap = async (req, res) => {
  try {
    const { resume_text, job_description } = req.body;

    if (!resume_text || !job_description) {
      return res.status(400).json({
        error: 'Resume text and job description are required',
      });
    }

    // Call Python microservice
    const response = await axios.post(
      `${PYTHON_SERVICE_URL}/skill-gap`,
      {
        resume_text,
        job_description,
      }
    );

    // Save to MongoDB
    await UserHistory.create({
      analysisType: 'skill-gap',
      data: response.data,
      metadata: {
        jobTitle: 'Custom Job Description',
      },
    });

    res.json(response.data);
  } catch (error) {
    console.error('Error in analyzeSkillGap:', error.message);
    res.status(500).json({
      error: error.message || 'Error analyzing skill gap',
    });
  }
};

module.exports = {
  analyzeSkillGap,
};
