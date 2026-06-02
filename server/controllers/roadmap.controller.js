// controllers/roadmap.controller.js
const axios = require('axios');
const UserHistory = require('../models/UserHistory');

const PYTHON_SERVICE_URL = process.env.PYTHON_SERVICE_URL || 'http://localhost:8000';

/**
 * Generate career roadmap based on goal
 * @route POST /api/roadmap/generate
 * @param {String} goal - Career goal (e.g., "Web Developer")
 */
const generateRoadmap = async (req, res) => {
  try {
    const { goal } = req.body;

    if (!goal) {
      return res.status(400).json({
        error: 'Career goal is required',
      });
    }

    // Call Python microservice
    const response = await axios.post(
      `${PYTHON_SERVICE_URL}/roadmap`,
      { goal }
    );

    // Save to MongoDB
    await UserHistory.create({
      analysisType: 'roadmap',
      data: response.data,
      metadata: {
        careerGoal: goal,
      },
    });

    res.json(response.data);
  } catch (error) {
    console.error('Error in generateRoadmap:', error.message);
    res.status(500).json({
      error: error.message || 'Error generating roadmap',
    });
  }
};

module.exports = {
  generateRoadmap,
};
