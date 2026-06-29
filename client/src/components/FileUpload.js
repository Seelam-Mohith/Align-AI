import React from 'react';
import './FileUpload.css';

function FileUpload({ onFileSelect, loading }) {
  const handleChange = (e) => {
    const file = e.target.files[0];
    if (file && file.type === 'application/pdf') {
      onFileSelect(file);
    } else {
      alert('Please select a PDF file');
    }
  };

  return (
    <div className="file-upload-container">
      <label htmlFor="file-input" className="file-upload-label">
        <div className="upload-box">
          <span className="upload-icon">📄</span>
          <p className="upload-text">Drag and drop your PDF resume here</p>
          <p className="upload-subtext">or click to browse</p>
        </div>
        <input
          id="file-input"
          type="file"
          accept=".pdf"
          onChange={handleChange}
          disabled={loading}
          className="file-input"
        />
      </label>
    </div>
  );
}

export default FileUpload;
