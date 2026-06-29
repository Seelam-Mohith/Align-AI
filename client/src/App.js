import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ATSChecker from './pages/ATSChecker';
import SkillGapAnalyzer from './pages/SkillGapAnalyzer';
import RoadmapGenerator from './pages/RoadmapGenerator';
import './App.css';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<ATSChecker />} />
        <Route path="/ats-checker" element={<ATSChecker />} />
        <Route path="/skill-gap" element={<SkillGapAnalyzer />} />
        <Route path="/roadmap" element={<RoadmapGenerator />} />
      </Routes>
    </Router>
  );
}

export default App;
