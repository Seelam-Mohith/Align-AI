import React, { useState } from 'react';
import axios from 'axios';
import FileUpload from '../components/FileUpload';
import CircularScore from '../components/CircularScore';
import SkillChips from '../components/SkillChips';
import './ATSChecker.css';

function ATSChecker() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFileSelect = (selectedFile) => {
    setFile(selectedFile);
    setError(null);
  };

  const handleAnalyze = async () => {
    if (!file) {
      setError('Please select a PDF file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setLoading(true);
      setError(null);
      const response = await axios.post(
        'http://localhost:5000/api/ats/upload',
        formData,
        {
          headers: { 'Content-Type': 'multipart/form-data' },
        }
      );
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Error analyzing resume');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <div className="content-wrapper">
        <h1 className="page-title">📄 Resume ATS Score Checker</h1>

        <p className="page-description">
          Upload your PDF resume to get an ATS score based on keyword matching,
          skills alignment, and industry standards.
        </p>

        <FileUpload onFileSelect={handleFileSelect} loading={loading} />

        {file && (
          <div className="file-info">
            <p>Selected: <strong>{file.name}</strong></p>
            <button
              className="btn btn-primary"
              onClick={handleAnalyze}
              disabled={loading}
            >
              {loading ? '⏳ Analyzing...' : '🔍 Analyze Resume'}
            </button>
          </div>
        )}

        {error && (
          <div className="error-message">
            ❌ {error}
          </div>
        )}

        {result && (
          <div className="results-container">
            <h2>Your ATS Analysis</h2>

            <CircularScore score={result.score} strength={result.strength} />

            <div className="results-grid">
              <div className="result-section">
                <h3>✅ Matched Skills ({result.matched.length})</h3>
                <SkillChips skills={result.matched} type="matched" />
              </div>

              <div className="result-section">
                <h3>⚠️ Missing Skills ({result.missing.length})</h3>
                <SkillChips skills={result.missing} type="missing" />
              </div>
            </div>

            <div className="recommendations">
              <h3>💡 Recommendations</h3>
              <ul>
                <li>Add missing technical skills to improve your ATS score</li>
                <li>Use industry-standard keywords relevant to your target role</li>
                <li>Include quantifiable achievements in your bullet points</li>
                <li>Ensure proper formatting for better parsing</li>
              </ul>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default ATSChecker;
