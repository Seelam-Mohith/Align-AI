# roadmap_generator.py - Career Roadmap Generation
from typing import Dict, List
import json

class RoadmapGenerator:
    """
    Generates career roadmaps based on predefined templates
    """
    
    def __init__(self):
        """Initialize with roadmap templates"""
        self.roadmaps = self._create_roadmaps()
    
    def _create_roadmaps(self) -> Dict[str, Dict]:
        """Create predefined roadmaps for different careers"""
        return {
            "web developer": {
                "beginner": [
                    {
                        "title": "HTML & CSS Fundamentals",
                        "description": "Learn the basics of HTML structure and CSS styling",
                        "skills": ["HTML", "CSS", "Responsive Design"],
                        "duration": "4 weeks"
                    },
                    {
                        "title": "JavaScript Basics",
                        "description": "Master JavaScript fundamentals including variables, functions, and DOM manipulation",
                        "skills": ["JavaScript", "DOM", "Events"],
                        "duration": "6 weeks"
                    },
                    {
                        "title": "Git & Version Control",
                        "description": "Learn Git for version control and collaboration",
                        "skills": ["Git", "GitHub", "Branching"],
                        "duration": "2 weeks"
                    }
                ],
                "intermediate": [
                    {
                        "title": "React Fundamentals",
                        "description": "Learn React components, hooks, and state management",
                        "skills": ["React", "JSX", "Hooks", "State Management"],
                        "duration": "8 weeks"
                    },
                    {
                        "title": "Backend Development",
                        "description": "Learn Node.js and Express for backend development",
                        "skills": ["Node.js", "Express", "REST APIs", "Routing"],
                        "duration": "8 weeks"
                    },
                    {
                        "title": "Database Design",
                        "description": "Master MongoDB and SQL databases",
                        "skills": ["MongoDB", "SQL", "Database Design"],
                        "duration": "6 weeks"
                    }
                ],
                "advanced": [
                    {
                        "title": "Full Stack Architecture",
                        "description": "Design and build complete full-stack applications",
                        "skills": ["System Design", "Scalability", "Architecture"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "DevOps & Deployment",
                        "description": "Learn Docker, Kubernetes, and cloud deployment",
                        "skills": ["Docker", "Kubernetes", "AWS", "CI/CD"],
                        "duration": "8 weeks"
                    },
                    {
                        "title": "Performance Optimization",
                        "description": "Optimize web applications for speed and scalability",
                        "skills": ["Performance Tuning", "Caching", "Load Balancing"],
                        "duration": "6 weeks"
                    }
                ]
            },
            "ai engineer": {
                "beginner": [
                    {
                        "title": "Python Fundamentals",
                        "description": "Master Python programming for AI/ML",
                        "skills": ["Python", "Data Types", "Functions", "OOP"],
                        "duration": "6 weeks"
                    },
                    {
                        "title": "Mathematics for AI",
                        "description": "Learn linear algebra, calculus, and probability",
                        "skills": ["Linear Algebra", "Calculus", "Probability", "Statistics"],
                        "duration": "8 weeks"
                    },
                    {
                        "title": "Data Analysis Basics",
                        "description": "Learn NumPy, Pandas, and data visualization",
                        "skills": ["NumPy", "Pandas", "Matplotlib", "Data Cleaning"],
                        "duration": "6 weeks"
                    }
                ],
                "intermediate": [
                    {
                        "title": "Machine Learning Algorithms",
                        "description": "Learn supervised and unsupervised learning algorithms",
                        "skills": ["Scikit-learn", "Classification", "Regression", "Clustering"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "Deep Learning Basics",
                        "description": "Understand neural networks and deep learning frameworks",
                        "skills": ["TensorFlow", "Keras", "PyTorch", "Neural Networks"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "Data Engineering",
                        "description": "Learn data pipeline design and big data tools",
                        "skills": ["SQL", "ETL", "Apache Spark", "Data Warehousing"],
                        "duration": "8 weeks"
                    }
                ],
                "advanced": [
                    {
                        "title": "Advanced Deep Learning",
                        "description": "Master CNNs, RNNs, Transformers, and GANs",
                        "skills": ["CNN", "RNN", "Transformers", "GAN", "Attention"],
                        "duration": "12 weeks"
                    },
                    {
                        "title": "NLP & LLMs",
                        "description": "Learn Natural Language Processing and Large Language Models",
                        "skills": ["NLP", "BERT", "GPT", "Transformers", "LangChain"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "MLOps & Model Deployment",
                        "description": "Deploy and maintain ML models in production",
                        "skills": ["MLOps", "Docker", "Kubernetes", "ML Monitoring"],
                        "duration": "8 weeks"
                    }
                ]
            },
            "data scientist": {
                "beginner": [
                    {
                        "title": "Python for Data Science",
                        "description": "Master Python for data analysis and manipulation",
                        "skills": ["Python", "Pandas", "NumPy", "Jupyter"],
                        "duration": "6 weeks"
                    },
                    {
                        "title": "Statistical Foundations",
                        "description": "Learn statistics, distributions, and hypothesis testing",
                        "skills": ["Statistics", "Distributions", "Hypothesis Testing", "Probability"],
                        "duration": "8 weeks"
                    },
                    {
                        "title": "Data Visualization",
                        "description": "Create compelling visualizations with Matplotlib and Seaborn",
                        "skills": ["Matplotlib", "Seaborn", "Plotly", "Tableau"],
                        "duration": "4 weeks"
                    }
                ],
                "intermediate": [
                    {
                        "title": "Machine Learning Models",
                        "description": "Build and evaluate ML models with Scikit-learn",
                        "skills": ["Scikit-learn", "Model Evaluation", "Feature Engineering", "Cross-validation"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "SQL & Databases",
                        "description": "Master SQL for data querying and analysis",
                        "skills": ["SQL", "Database Design", "Query Optimization", "Joins"],
                        "duration": "6 weeks"
                    },
                    {
                        "title": "A/B Testing & Experimentation",
                        "description": "Design and analyze experiments",
                        "skills": ["A/B Testing", "Statistical Testing", "Experimental Design"],
                        "duration": "5 weeks"
                    }
                ],
                "advanced": [
                    {
                        "title": "Advanced Analytics",
                        "description": "Time series analysis, causal inference, and advanced modeling",
                        "skills": ["Time Series", "Causal Inference", "Bayesian Methods", "Advanced Statistics"],
                        "duration": "12 weeks"
                    },
                    {
                        "title": "Big Data Technologies",
                        "description": "Work with Apache Spark and large-scale data",
                        "skills": ["Apache Spark", "Hadoop", "Hive", "Data Lake"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "Production ML Systems",
                        "description": "Deploy and maintain ML systems at scale",
                        "skills": ["MLOps", "Feature Stores", "Model Monitoring", "Cloud Platforms"],
                        "duration": "8 weeks"
                    }
                ]
            },
            "cybersecurity analyst": {
                "beginner": [
                    {
                        "title": "Networking Fundamentals",
                        "description": "Learn TCP/IP, DNS, HTTP, and networking basics",
                        "skills": ["TCP/IP", "DNS", "HTTP", "Network Protocols"],
                        "duration": "6 weeks"
                    },
                    {
                        "title": "Linux Administration",
                        "description": "Master Linux command line and system administration",
                        "skills": ["Linux", "Command Line", "File Systems", "Permissions"],
                        "duration": "6 weeks"
                    },
                    {
                        "title": "Cybersecurity Basics",
                        "description": "Learn security principles and threats",
                        "skills": ["Security Principles", "Threats", "Risk Management", "Compliance"],
                        "duration": "6 weeks"
                    }
                ],
                "intermediate": [
                    {
                        "title": "Cryptography",
                        "description": "Understand encryption, hashing, and digital signatures",
                        "skills": ["Encryption", "Hashing", "Digital Signatures", "SSL/TLS"],
                        "duration": "8 weeks"
                    },
                    {
                        "title": "Penetration Testing",
                        "description": "Learn ethical hacking and penetration testing techniques",
                        "skills": ["Penetration Testing", "Burp Suite", "Metasploit", "Vulnerability Assessment"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "Incident Response",
                        "description": "Respond to and manage security incidents",
                        "skills": ["Incident Response", "Forensics", "Threat Hunting", "Logging"],
                        "duration": "8 weeks"
                    }
                ],
                "advanced": [
                    {
                        "title": "Advanced Threat Analysis",
                        "description": "Analyze advanced persistent threats and malware",
                        "skills": ["Threat Analysis", "Malware Analysis", "APT", "SIEM"],
                        "duration": "12 weeks"
                    },
                    {
                        "title": "Security Architecture",
                        "description": "Design secure systems and defense strategies",
                        "skills": ["Security Architecture", "Defense Strategy", "Zero Trust", "Cloud Security"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "Compliance & Governance",
                        "description": "Ensure compliance with security standards",
                        "skills": ["Compliance", "GDPR", "ISO 27001", "Governance"],
                        "duration": "6 weeks"
                    }
                ]
            },
            "devops engineer": {
                "beginner": [
                    {
                        "title": "Linux & Command Line",
                        "description": "Master Linux system administration",
                        "skills": ["Linux", "Bash", "Shell Scripting", "System Administration"],
                        "duration": "6 weeks"
                    },
                    {
                        "title": "Networking Basics",
                        "description": "Understand networking concepts and protocols",
                        "skills": ["TCP/IP", "DNS", "Firewalls", "Load Balancing"],
                        "duration": "4 weeks"
                    },
                    {
                        "title": "Version Control",
                        "description": "Master Git and collaborative development",
                        "skills": ["Git", "GitHub", "GitLab", "Branching Strategies"],
                        "duration": "3 weeks"
                    }
                ],
                "intermediate": [
                    {
                        "title": "Docker & Containers",
                        "description": "Learn containerization with Docker",
                        "skills": ["Docker", "Container Architecture", "Docker Compose", "Registries"],
                        "duration": "6 weeks"
                    },
                    {
                        "title": "CI/CD Pipelines",
                        "description": "Build automated deployment pipelines",
                        "skills": ["Jenkins", "GitLab CI", "GitHub Actions", "Automation"],
                        "duration": "8 weeks"
                    },
                    {
                        "title": "Kubernetes Basics",
                        "description": "Learn container orchestration with Kubernetes",
                        "skills": ["Kubernetes", "Pods", "Services", "Deployments"],
                        "duration": "8 weeks"
                    }
                ],
                "advanced": [
                    {
                        "title": "Advanced Kubernetes",
                        "description": "Master complex Kubernetes deployments and management",
                        "skills": ["Helm", "Operators", "Service Mesh", "Advanced Networking"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "Cloud Platforms",
                        "description": "Work with AWS, Azure, or GCP",
                        "skills": ["AWS", "Azure", "GCP", "Cloud Architecture"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "Infrastructure as Code",
                        "description": "Use IaC tools like Terraform and Ansible",
                        "skills": ["Terraform", "Ansible", "CloudFormation", "IaC"],
                        "duration": "8 weeks"
                    }
                ]
            },
            "mobile developer": {
                "beginner": [
                    {
                        "title": "Mobile Development Basics",
                        "description": "Learn mobile development fundamentals",
                        "skills": ["Mobile Design", "UI/UX", "App Architecture", "Mobile OS"],
                        "duration": "4 weeks"
                    },
                    {
                        "title": "React Native or Flutter",
                        "description": "Choose and learn cross-platform mobile framework",
                        "skills": ["React Native", "Flutter", "Dart", "Mobile Components"],
                        "duration": "8 weeks"
                    },
                    {
                        "title": "Mobile APIs & Backend",
                        "description": "Integrate with backend services",
                        "skills": ["REST APIs", "HTTP", "JSON", "Authentication"],
                        "duration": "4 weeks"
                    }
                ],
                "intermediate": [
                    {
                        "title": "Platform-Specific Development",
                        "description": "Deep dive into iOS or Android development",
                        "skills": ["Swift", "Kotlin", "Native Development", "Platform APIs"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "Mobile Databases",
                        "description": "Work with SQLite, Realm, and Firebase",
                        "skills": ["SQLite", "Realm", "Firebase", "Local Storage"],
                        "duration": "5 weeks"
                    },
                    {
                        "title": "Testing & Debugging",
                        "description": "Test and debug mobile applications",
                        "skills": ["Unit Testing", "Integration Testing", "Debugging", "Performance Profiling"],
                        "duration": "6 weeks"
                    }
                ],
                "advanced": [
                    {
                        "title": "Advanced Mobile Architecture",
                        "description": "Build scalable mobile applications",
                        "skills": ["Clean Architecture", "MVVM", "State Management", "Performance Optimization"],
                        "duration": "10 weeks"
                    },
                    {
                        "title": "Mobile Security",
                        "description": "Secure mobile applications",
                        "skills": ["Encryption", "Secure Storage", "Certificate Pinning", "Secure Communication"],
                        "duration": "6 weeks"
                    },
                    {
                        "title": "App Publishing & Monetization",
                        "description": "Publish apps and implement monetization strategies",
                        "skills": ["App Store Publishing", "Analytics", "Monetization", "User Engagement"],
                        "duration": "4 weeks"
                    }
                ]
            }
        }
    
    def generate(self, goal: str) -> Dict:
        """
        Generate roadmap for given career goal
        Returns: {beginner, intermediate, advanced}
        """
        try:
            goal_lower = goal.lower().strip()
            
            # Find matching roadmap
            roadmap = None
            for key in self.roadmaps.keys():
                if key in goal_lower or goal_lower in key:
                    roadmap = self.roadmaps[key]
                    break
            
            if not roadmap:
                # Return default web developer roadmap if no match found
                roadmap = self.roadmaps["web developer"]
                message = f"No specific roadmap found for '{goal}'. Here's a Web Developer roadmap instead."
            else:
                message = f"Personalized roadmap for {goal.title()}"
            
            return {
                "beginner": roadmap.get("beginner", []),
                "intermediate": roadmap.get("intermediate", []),
                "advanced": roadmap.get("advanced", []),
                "goal": goal.title(),
                "message": message,
                "total_duration": "52-78 weeks (1-1.5 years for full track)"
            }
        
        except Exception as e:
            raise Exception(f"Roadmap Generation Error: {str(e)}")
