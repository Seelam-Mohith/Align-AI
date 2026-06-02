import React, { useState } from 'react';
import axios from 'axios';
import SkillChips from '../components/SkillChips';
import './SkillGapAnalyzer.css';

function SkillGapAnalyzer() {
  const [resumeText, setResumeText] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    if (!resumeText.trim() || !jobDescription.trim()) {
      setError('Please fill in both resume and job description');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const response = await axios.post(
        'http://localhost:5000/api/skill-gap/analyze',
        {
          resume_text: resumeText,
          job_description: jobDescription,
        }
      );
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Error analyzing skills');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <div className="content-wrapper">
        <h1 className="page-title">🔄 Skill Gap Analyzer</h1>

        <p className="page-description">
          Compare your resume skills with a job description to identify gaps
          and get personalized recommendations.
        </p>

        <div className="input-section">
          <div className="text-input-group">
            <label htmlFor="resume">Your Resume (Text)</label>
            <textarea
              id="resume"
              value={resumeText}
              onChange={(e) => setResumeText(e.target.value)}
              placeholder="Paste your resume text here..."
              rows="8"
              disabled={loading}
            />
          </div>

          <div className="text-input-group">
            <label htmlFor="job-desc">Job Description</label>
            <textarea
              id="job-desc"
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              placeholder="Paste the job description here..."
              rows="8"
              disabled={loading}
            />
          </div>
        </div>

        <button
          className="btn btn-primary"
          onClick={handleAnalyze}
          disabled={loading}
        >
          {loading ? '⏳ Analyzing...' : '🔍 Analyze Gap'}
        </button>

        {error && (
          <div className="error-message">
            ❌ {error}
          </div>
        )}

        {result && (
          <div className="results-container">
            <h2>Gap Analysis Results</h2>

            <div className="results-grid">
              <div className="result-section">
                <h3>✅ Skills You Have ({result.present.length})</h3>
                <SkillChips skills={result.present} type="matched" />
              </div>

              <div className="result-section">
                <h3>📋 Required Skills ({result.required.length})</h3>
                <SkillChips skills={result.required} type="missing" />
              </div>

              <div className="result-section full-width">
                <h3>⚠️ Skills to Learn ({result.missing.length})</h3>
                <SkillChips skills={result.missing} type="missing" />
              </div>
            </div>

            <div className="recommendations-section">
              <h3>💡 Personalized Recommendations</h3>
              <div className="recommendations-list">
                {result.recommendations.map((rec, index) => (
                  <div key={index} className="recommendation-item">
                    <span className="rec-number">{index + 1}</span>
                    <span className="rec-text">{rec}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default SkillGapAnalyzer;
