// routes/skillGap.routes.js
const express = require('express');
const router = express.Router();
const { analyzeSkillGap } = require('../controllers/skillGap.controller');

/**
 * POST /api/skill-gap/analyze
 * Analyze skill gap
 */
router.post('/analyze', analyzeSkillGap);

module.exports = router;
