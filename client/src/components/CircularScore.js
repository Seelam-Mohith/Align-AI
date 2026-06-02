import React from 'react';
import './CircularScore.css';

function CircularScore({ score, strength }) {
  const circumference = 2 * Math.PI * 45;
  const offset = circumference - (score / 100) * circumference;

  const getColor = (strength) => {
    switch (strength) {
      case 'Excellent':
        return '#10b981';
      case 'Strong':
        return '#3b82f6';
      case 'Moderate':
        return '#f59e0b';
      case 'Weak':
        return '#ef4444';
      default:
        return '#6b7280';
    }
  };

  return (
    <div className="score-container">
      <div className="circular-score">
        <svg viewBox="0 0 100 100" className="score-ring">
          <circle cx="50" cy="50" r="45" className="score-ring-bg" />
          <circle
            cx="50"
            cy="50"
            r="45"
            className="score-ring-progress"
            style={{
              strokeDasharray: circumference,
              strokeDashoffset: offset,
              stroke: getColor(strength),
            }}
          />
        </svg>
        <div className="score-text">
          <div className="score-number">{score}</div>
          <div className="score-max">/100</div>
        </div>
      </div>
      <div className="strength-indicator">
        <span
          className="strength-badge"
          style={{ backgroundColor: getColor(strength) }}
        >
          {strength}
        </span>
      </div>
    </div>
  );
}

export default CircularScore;
