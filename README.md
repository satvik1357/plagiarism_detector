Here is the **in-depth documentation** for your Plagiarism Detection System project, covering all requested areas:

---

## 📌 **Project Title**

**AI-Powered Multi-File Plagiarism Detection Web Application**

---

## 📄 **Project Description**

This project is a web-based plagiarism detection system designed to evaluate the similarity between multiple files using advanced Natural Language Processing (NLP) techniques and customizable comparison logic. Users can upload text or code documents, specify the group size for combination-based comparison (pairwise, triplets, etc.), or leave it blank to check overall similarity among all uploaded files. The system supports PDF, DOCX, TXT, and code formats like .py, .cpp, .java, etc.

---

## 💡 **Project Idea**

The idea emerged from the need for a **reliable tool** that helps educators, researchers, and developers detect copied or paraphrased content across **multiple files**. Unlike basic pairwise-only checkers, this system allows:

* Group comparisons of *n* files at a time.
* Detection of both literal and paraphrased plagiarism using **BERT-based semantic similarity**.
* Support for various file formats.
* Easy-to-use interface for bulk uploading and flexible group size input.

---

## 🗂️ **Folder Structure**

```plaintext
plagiarism_detector/
│
├── app.py                   # Flask app with routing logic and processing
├── uploads/                 # Temp folder for uploaded files
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
│   └── processor_code.py    # Token/hash-based similarity for code files
│
└── venv/                    # Python virtual environment
```

---

## ⚙️ **Tech Stack**

| Layer       | Tools / Frameworks                             |
| ----------- | ---------------------------------------------- |
| Frontend    | HTML5, CSS3, Bootstrap (optionally), Jinja2    |
| Backend     | Flask                                          |
| NLP Model   | Sentence-BERT (`all-MiniLM-L6-v2`)             |
| Python Libs | `scikit-learn`, `fitz` (PyMuPDF), `docx`, etc. |
| Hosting     | Localhost (can be extended to Render, Heroku)  |

---

## 🔄 **Workflow**

1. **User uploads files** via the browser.
2. Files are saved temporarily in the `uploads/` folder.
3. System detects the file type (text or code).
4. If files are all valid:

   * If group size is provided:

     * Group combinations (size 2, 3, etc.) are created.
     * For each group, pairwise combinations are evaluated, and the average score is computed.
   * Regardless of input, all files are also compared together to compute an overall similarity score.
5. Results are displayed in a structured format showing:

   * Group-wise scores
   * Overall score
6. Files are deleted after processing for security.

---

## ✅ **Advantages**

* 🔁 **Flexible Grouping**: Not restricted to two-file comparisons.
* 🔍 **Semantic Matching**: BERT can catch paraphrased or meaning-preserved changes.
* 🧠 **Smart Code Similarity**: Uses structural/token similarity for source code.
* 🧾 **Multiple Formats**: Handles TXT, DOCX, PDF, and programming files.
* 🖥️ **User-Friendly**: Clean UI and error handling for unsupported formats or mixed types.

---

## 🌟 **What's Special About This Project**

* **Group Comparison Functionality**: Rare in online plagiarism detectors.
* **Hybrid Model Use**:

  * Text: Semantic + N-gram hybrid with weighted scores.
  * Code: Hash/structural analysis for plagiarism detection.
* **Clean Modular Design**: Clear separation of concerns in code (utils, templates, app logic).
* **Auto Cleanup**: Deletes uploaded files after processing to ensure privacy.
* **Scalable**: Can be scaled to accept up to 50 or more files in one go.

---

Would you like a PDF version or README.md for this as well?
