# 🔄 Morphix - Universal File Converter

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Data-Pandas-success?style=for-the-badge\&logo=pandas)
![Pillow](https://img.shields.io/badge/Image-Pillow-orange?style=for-the-badge)
![docx2pdf](https://img.shields.io/badge/Document-docx2pdf-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

### A Python-Based Universal File Conversion Utility Developed Using Pandas, Pillow and docx2pdf

</div>

---

## 📖 Overview

**Morphix** is a lightweight file conversion application developed using **Python**. It provides a unified platform for converting documents, images, and structured data files into different formats.

The application simplifies everyday conversion tasks by allowing users to convert files through a simple command-line interface.

Morphix is designed as an educational project to demonstrate concepts such as:

* File handling in Python
* Data processing using Pandas
* Image manipulation using Pillow
* Document conversion using docx2pdf
* Modular programming
* Command-line application development

---

# ✨ Key Features

### 📄 Document Conversion

* Convert Microsoft Word documents (`.docx`) into PDF files (`.pdf`).
* Automatically generates output filenames.

### 📊 CSV to JSON Conversion

* Converts CSV datasets into JSON format.
* Preserves structured tabular data.

### 🗂️ JSON to CSV Conversion

* Converts JSON files into CSV format.
* Suitable for spreadsheet and data analysis applications.

### 🖼️ Image Conversion

Supports image conversion between formats such as:

* PNG → JPG
* JPG → PNG
* JPEG → PNG
* PNG → JPEG

### ⚡ Interactive Command-Line Interface

* Easy-to-use terminal-based interface.
* Minimal user interaction required.

### 🔄 Automatic File Generation

* Converted files are automatically saved with appropriate extensions.

---

# 🏗️ System Architecture

```text
+----------------+
|    main.py     |
+--------+-------+
         |
         v
+----------------+
|  backend.py    |
+--------+-------+
         |
         +----------------------+
         |                      |
         v                      v
+----------------+    +----------------+
| Data Converter |    | Image Converter|
+----------------+    +----------------+
         |
         v
+----------------+
| PDF Converter  |
+----------------+
```

---

# 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming language |
| Pandas       | CSV and JSON processing   |
| Pillow (PIL) | Image processing          |
| docx2pdf     | Word to PDF conversion    |
| OS Module    | File handling             |
| CLI          | User interaction          |

---

# 📂 Project Structure

```text
Morphix/
│
├── backend.py
├── main.py
├── README.md
│
└── sample_files/
```

---

# 📸 Supported Conversions

| Input Format | Output Format   |
| ------------ | --------------- |
| `.docx`      | `.pdf`          |
| `.csv`       | `.json`         |
| `.json`      | `.csv`          |
| `.png`       | `.jpg`, `.jpeg` |
| `.jpg`       | `.png`          |
| `.jpeg`      | `.png`          |

---

# ⚙️ Installation and Setup

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Morphix.git
```

Move into the project directory:

```bash
cd Morphix
```

---

## Step 2: Install Python Dependencies

Install required libraries using pip:

```bash
pip install pandas pillow docx2pdf
```

Alternatively, install from requirements file:

```bash
pip install -r requirements.txt
```

---

## Step 3: Run the Application

Execute:

```bash
python main.py
```

---

# 🚀 Application Workflow

## Convert a File

1. Launch the application.
2. Enter the file name.
3. Choose the desired output format.
4. Wait for the conversion process to finish.
5. The converted file will be saved automatically.

---

## Example Session

```text
Enter file name to convert: employees.csv
Convert to (pdf/json/csv/png): json

conversion completed
```

---

# 📋 Sample Conversion

## CSV Input

```csv
name,department,salary
Ajith,Development,45000
Arun,Testing,40000
```

## JSON Output

```json
[
    {
        "name":"Ajith",
        "department":"Development",
        "salary":45000
    },
    {
        "name":"Arun",
        "department":"Testing",
        "salary":40000
    }
]
```

---

# 🔒 Error Handling

Morphix includes basic validation mechanisms.

Examples:

* Invalid file name detection
* Unsupported conversion prevention
* Missing file detection
* Invalid format handling

---

# 🌟 Future Enhancements

* [ ] Graphical User Interface (GUI)
* [ ] Batch File Conversion
* [ ] Excel File Support
* [ ] PDF to Word Conversion
* [ ] Drag and Drop Support
* [ ] Cloud Storage Integration
* [ ] Conversion Progress Indicator
* [ ] File Compression Support

---

# 🧪 Testing

Test Cases:

| Test Case              | Expected Result |
| ---------------------- | --------------- |
| Valid DOCX → PDF       | PDF Generated   |
| Valid CSV → JSON       | JSON Generated  |
| Valid JSON → CSV       | CSV Generated   |
| Valid Image Conversion | Image Converted |
| Invalid File           | Error Message   |

---

# 🤝 Contribution

Contributions are welcome.

### Steps:

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push changes.

```bash
git push origin feature-name
```

5. Create a Pull Request.

---

# 👨‍💻 Author

**Ajith P A**

---

# 📄 License

This project is developed for educational and learning purposes.

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a star!

</div>
