# 🖼️ Tesseract-EasyOCR GUI App

A simple desktop application that uses **Tesseract OCR** and **EasyOCR** to extract text from images, with a user-friendly interface built using **Tkinter**. This project allows users to easily compare the results of two popular OCR engines.

---

## 🚀 Features

- User-friendly GUI built with **Tkinter**
- Supports OCR using:
  - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
  - [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- Load and preview images before processing
- View extracted text within the app
- Save recognized text to a `.txt` file

---

## 🛠️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Sickked-C/Tesseract-EasyOCR.git
cd Tesseract-EasyOCR
```
### 2. Install Dependencies
Make sure you have Python 3.7+ installed.

Install required Python packages:

```bash
pip install easyocr pytesseract opencv-python
```
Also, install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and ensure it is added to your system PATH.

### 3. Run the Application
```bash
python ocr_sript.py
```
---
## 🖼️ Usage
Click "Browse" to select an image.

Choose OCR engine: Tesseract or EasyOCR.

Click "Extract Text".

The extracted text will be displayed on the screen.

You can click "Save Text" to export the results to a .txt file.
---
## 🧠 Notes
For Tesseract OCR, make sure it is properly installed and added to your system's PATH.

You can modify the source code to change the language used by EasyOCR (default is English).

---
## 📄 License
This project is licensed under the MIT License.

---
## 🙋‍♂️ Author
Developed by Sickked-C
