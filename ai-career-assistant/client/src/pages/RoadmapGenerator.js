import React, { useState } from 'react';
import axios from 'axios';
import './RoadmapGenerator.css';

function RoadmapGenerator() {
  const [careerGoal, setCareerGoal] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [expandedLevel, setExpandedLevel] = useState(null);

  const careerOptions = [
    'Web Developer',
    'AI Engineer',
    'Data Scientist',
    'Cybersecurity Analyst',
    'DevOps Engineer',
    'Mobile Developer',
  ];

  const handleGenerate = async () => {
    if (!careerGoal.trim()) {
      setError('Please select or enter a career goal');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const response = await axios.post(
        'http://localhost:5000/api/roadmap/generate',
        { goal: careerGoal }
      );
      setResult(response.data);
      setExpandedLevel(null);
    } catch (err) {
      setError(err.response?.data?.error || 'Error generating roadmap');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const toggleLevel = (level) => {
    setExpandedLevel(expandedLevel === level ? null : level);
  };

  return (
    <div className="page-container">
      <div className="content-wrapper">
        <h1 className="page-title">🗺️ AI Roadmap Generator</h1>

        <p className="page-description">
          Get a personalized career roadmap with structured learning paths for
          your target role.
        </p>

        <div className="goal-selector">
          <label htmlFor="career-input">Select or Enter Career Goal:</label>
          <div className="goal-input-group">
            <input
              id="career-input"
              type="text"
              list="career-options"
              value={careerGoal}
              onChange={(e) => setCareerGoal(e.target.value)}
              placeholder="e.g., Web Developer, AI Engineer..."
              disabled={loading}
            />
            <datalist id="career-options">
              {careerOptions.map((option) => (
                <option key={option} value={option} />
              ))}
            </datalist>
          </div>

          <div className="quick-select">
            {careerOptions.map((option) => (
              <button
                key={option}
                className={`quick-btn ${careerGoal === option ? 'active' : ''}`}
                onClick={() => setCareerGoal(option)}
                disabled={loading}
              >
                {option}
              </button>
            ))}
          </div>
        </div>

        <button
          className="btn btn-primary"
          onClick={handleGenerate}
          disabled={loading}
        >
          {loading ? '⏳ Generating...' : '🚀 Generate Roadmap'}
        </button>

        {error && (
          <div className="error-message">
            ❌ {error}
          </div>
        )}

        {result && (
          <div className="roadmap-container">
            <h2>Your Career Roadmap: {careerGoal}</h2>

            <div className="timeline">
              {['beginner', 'intermediate', 'advanced'].map((level) => (
                <div key={level} className="timeline-item">
                  <div
                    className={`timeline-header ${expandedLevel === level ? 'expanded' : ''}`}
                    onClick={() => toggleLevel(level)}
                  >
                    <span className="timeline-dot" />
                    <h3 className="timeline-title">
                      {level.charAt(0).toUpperCase() + level.slice(1)} Level
                    </h3>
                    <span className="expand-icon">
                      {expandedLevel === level ? '▼' : '▶'}
                    </span>
                  </div>

                  {expandedLevel === level && (
                    <div className="timeline-content">
                      {result[level].map((item, index) => (
                        <div key={index} className="roadmap-card">
                          <div className="card-number">{index + 1}</div>
                          <div className="card-content">
                            <h4>{item.title}</h4>
                            <p>{item.description}</p>
                            {item.skills && item.skills.length > 0 && (
                              <div className="card-skills">
                                {item.skills.map((skill, idx) => (
                                  <span key={idx} className="skill-tag">
                                    {skill}
                                  </span>
                                ))}
                              </div>
                            )}
                            {item.duration && (
                              <p className="card-duration">
                                ⏱️ Duration: {item.duration}
                              </p>
                            )}
                          </div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default RoadmapGenerator;
