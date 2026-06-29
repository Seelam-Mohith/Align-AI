import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <img src="/logo.svg" alt="AlignAI Logo" className="navbar-logo-img" />
          <span className="navbar-logo-text">AlignAI</span>
        </Link>
        <ul className="nav-menu">
          <li className="nav-item">
            <Link to="/ats-checker" className="nav-link">
              ATS Checker
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/skill-gap" className="nav-link">
              Skill Gap
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/roadmap" className="nav-link">
              Roadmap
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
