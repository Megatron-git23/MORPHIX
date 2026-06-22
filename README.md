# 🔄 Morphix - Universal File Converter




\

### A Lightweight Python-Based Universal File Conversion Utility

---

## 📖 Overview

**Morphix** is a desktop-based command-line file conversion utility developed using Python. The application enables users to convert files between various formats quickly and efficiently.

Morphix simplifies everyday file conversion tasks by providing a single interface for handling document, image, and data format conversions.

This project demonstrates concepts such as:

* File Handling in Python
* Data Processing using Pandas
* Image Processing using Pillow
* Document Conversion using docx2pdf
* Modular Programming
* Command-Line Application Development

---

# ✨ Key Features

### 📄 Document Conversion

* Convert **Word Documents (.docx)** to **PDF (.pdf)**.
* Automatically generates output filenames.

### 📊 CSV to JSON Conversion

* Converts CSV datasets into JSON format.
* Preserves structured tabular data.

### 🗂️ JSON to CSV Conversion

* Converts JSON files into CSV format.
* Useful for data analysis and spreadsheet applications.

### 🖼️ Image Format Conversion

Supports image conversions such as:

* PNG → JPG
* JPG → PNG
* JPEG → PNG
* PNG → JPEG

### ⚡ Simple Command-Line Interface

* Easy-to-use interactive terminal interface.
* Minimal user input required.

### 🔄 Automatic Output Generation

* Output files are automatically named based on the input filename.

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
         +-----------------------+
         |                       |
         v                       v
+----------------+      +----------------+
| Document Tools |      | Image Tools    |
+----------------+      +----------------+
         |                       |
         v                       v
docx2pdf Library         Pillow Library

         |
         v

+----------------+
| Data Tools     |
+----------------+
         |
         v
Pandas Library
```

---

# 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core Programming Language |
| Pandas       | CSV and JSON Processing   |
| Pillow (PIL) | Image Processing          |
| docx2pdf     | Word to PDF Conversion    |
| OS Module    | File Handling             |
| CLI          | User Interaction          |

---

# 📂 Project Structure

```text
Morphix/
│
├── backend.py
├── main.py
├── README.md
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

## Step 2: Install Required Libraries

Install all dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas pillow docx2pdf
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
3. Select the desired output format.
4. Wait for the conversion to complete.
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

Morphix validates file formats before conversion.

Examples:

* Invalid file name detection
* Unsupported conversion prevention
* Missing file detection

---

# 🌟 Future Enhancements

* [ ] Graphical User Interface (GUI)
* [ ] Drag and Drop Support
* [ ] Batch File Conversion
* [ ] Excel File Support
* [ ] PDF to Word Conversion
* [ ] File Compression Support
* [ ] Cloud Integration
* [ ] Conversion Progress Indicator

---

# 🧪 Testing

| Test Case              | Expected Result       |
| ---------------------- | --------------------- |
| Valid DOCX → PDF       | PDF Created           |
| Valid CSV → JSON       | JSON Created          |
| Valid JSON → CSV       | CSV Created           |
| Valid Image Conversion | Converted Image Saved |
| Invalid File           | Error Message         |

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

## ⭐ If you found this project useful, consider giving it a star!

### 🔄 Morphix — One Tool, Endless Transformations.
