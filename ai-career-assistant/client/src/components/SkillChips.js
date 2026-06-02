import React from 'react';
import './SkillChips.css';

function SkillChips({ skills, type = 'matched' }) {
  const getChipClass = (type) => {
    return type === 'matched' ? 'chip chip-matched' : 'chip chip-missing';
  };

  return (
    <div className="skills-container">
      <div className="skills-list">
        {skills.map((skill, index) => (
          <span key={index} className={getChipClass(type)}>
            {type === 'matched' ? '✓' : '✕'} {skill}
          </span>
        ))}
      </div>
    </div>
  );
}

export default SkillChips;
