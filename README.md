AI-Powered Multi-File Plagiarism Detection Web Application
📄 Project Description
This web-based plagiarism detection system evaluates similarity across multiple files using advanced Natural Language Processing (NLP) and customizable comparison logic. Users can upload text or code documents, specify group sizes for combination-based comparisons (e.g., pairwise, triplets), or check overall similarity among all files. Supported formats include PDF, DOCX, TXT, and code files (.py, .cpp, .java, etc.).
💡 Project Idea
The tool was designed to address the need for a reliable plagiarism detector for educators, researchers, and developers. Unlike traditional pairwise checkers, it offers:

Group comparisons of n files.
Detection of literal and paraphrased plagiarism using BERT-based semantic similarity.
Support for diverse file formats.
A user-friendly interface for bulk uploads and flexible group size inputs.

🗂️ Folder Structure
plagiarism_detector/
│
├── app.py                   # Flask app with routing and processing logic
├── uploads/                 # Temporary folder for uploaded files
│
├── static/                  # Static files (CSS)
│   └── style.css            # Custom styling for the site
│
├── templates/               # HTML templates
│   ├── index.html           # File upload and configuration form
│   └── result.html          # Displays similarity results
│
├── utils/                   # Utility logic
│   ├── processor_text.py    # NLP-based similarity checks for text
│   └── processor_code.py    # Token/hash-based similarity for code
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

⚙️ Tech Stack



Layer
Tools/Frameworks



Frontend
HTML5, CSS3, Bootstrap (optional), Jinja2


Backend
Flask


NLP Model
Sentence-BERT (all-MiniLM-L6-v2)


Python Libs
scikit-learn, fitz (PyMuPDF), python-docx, etc.


Hosting
Localhost (extendable to cloud platforms)


🔄 Workflow

Users upload files via the browser.
Files are saved temporarily in the uploads/ folder.
The system detects file types (text or code).
If files are valid:
If a group size is specified:
Creates group combinations (size 2, 3, etc.).
Computes pairwise similarity within groups and averages scores.


Computes overall similarity across all files.


Results display group-wise and overall similarity scores.
Files are deleted post-processing for security.

✅ Advantages

Flexible Grouping: Supports comparisons beyond pairwise checks.
Semantic Matching: BERT detects paraphrased or meaning-preserved content.
Smart Code Similarity: Uses structural/token analysis for code.
Multiple Formats: Handles TXT, DOCX, PDF, and code files.
User-Friendly: Clean UI with robust error handling.

🌟 What's Special

Group Comparison: Rare in plagiarism detection tools.
Hybrid Model:
Text: Combines semantic and N-gram analysis.
Code: Uses hash/structural similarity.


Modular Design: Clear separation of concerns.
Auto Cleanup: Deletes files post-processing for privacy.
Scalable: Supports up to 50+ files.

🚀 Getting Started
Prerequisites

Python 3.8+
Git
Virtual environment (recommended)

Installation

Clone the repository:
git clone https://github.com/your-username/plagiarism_detector.git
cd plagiarism_detector


Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:
pip install -r requirements.txt


Run the application:
python app.py


Access the app at http://localhost:5000.


Sample requirements.txt
flask==2.0.1
sentence-transformers==2.2.2
scikit-learn==1.0.2
PyMuPDF==1.19.6
python-docx==0.8.11
gunicorn==20.1.0

📝 Usage

Open the web app in your browser (http://localhost:5000).
Upload multiple files (TXT, DOCX, PDF, or code files like .py, .cpp, .java).
Optionally specify a group size for comparisons (e.g., 2 for pairwise, 3 for triplets).
Submit to view similarity scores, including group-wise and overall results.
Results are displayed in a clear, tabular format.

📚 Limitations

Memory Usage: BERT models are resource-intensive; deployment may require lighter models.
File Size: Large files (>10 MB) may slow processing or exceed hosting limits.
Language Support: BERT model (all-MiniLM-L6-v2) is optimized for English; other languages may need different models.

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make changes and commit (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

📧 Contact
For questions or feedback, open an issue or contact [your-email@example.com].
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
