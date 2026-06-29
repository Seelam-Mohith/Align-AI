// models/UserHistory.js
const mongoose = require('mongoose');

const userHistorySchema = new mongoose.Schema(
  {
    userId: {
      type: String,
      default: 'guest',
    },
    analysisType: {
      type: String,
      enum: ['ats', 'skill-gap', 'roadmap'],
      required: true,
    },
    data: {
      type: mongoose.Schema.Types.Mixed,
      required: true,
    },
    metadata: {
      resumeName: String,
      jobTitle: String,
      careerGoal: String,
    },
    createdAt: {
      type: Date,
      default: Date.now,
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model('UserHistory', userHistorySchema);
