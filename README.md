<!-- README.md for PyQt5 Image Processing Application -->

<h1 align="center">🎨 PyQt5 Image Processing Application</h1>

<h3 align="center">
An interactive image editing tool built with Python, PyQt5, and OpenCV
</h3>

<p align="center">
  <img src="https://media.giphy.com/media/llarwdtFqG63IlqUR1/giphy.gif" width="500" alt="Image Processing Animation"/>
</p>

---

## 🧾 Table of Contents
1. [Overview](#-overview)
2. [Features](#-features)
3. [Tech Stack](#-tech-stack)
4. [Installation](#-installation)
5. [Usage](#-usage)
6. [Interface Screenshots](#-interface-screenshots)
7. [Project Structure](#-project-structure)
8. [Future Enhancements](#-future-enhancements)
9. [Author](#-author)
10. [License](#-license)

---

## 🧠 Overview

The **PyQt5 Image Processing Application** is a desktop-based tool that combines the simplicity of **PyQt5 GUI** with the power of **OpenCV**.  
It enables users to perform **real-time image processing**, apply filters, draw on images, toggle themes, and even preview live camera feeds — all through an intuitive interface.

---

## ✨ Features

- 🎞️ **Real-time filters** – blur, grayscale, sharpen, brightness, and more  
- ✏️ **Drawing tools** – adjustable brush color and size  
- 🔄 **Undo / Redo** – easily revert or reapply changes  
- 🌗 **Theme toggle** – switch between light and dark mode  
- 📸 **Webcam support** – capture and edit images from your camera  
- 🖱️ **Drag & drop** – quick image loading into the workspace  
- 🧩 **User-friendly interface** – clean and responsive PyQt5 design  

---

## 🧰 Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Language** | Python |
| **GUI Framework** | PyQt5 |
| **Image Processing** | OpenCV, NumPy |
| **Utilities** | OS, Shutil |

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SayabArshad/PyQt5-Image-Processing-Application.git
cd PyQt5-Image-Processing-Application
### 2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
3️⃣ Activate the environment
For Windows:

bash
Copy code
venv\Scripts\activate
For macOS/Linux:

bash
Copy code
source venv/bin/activate
4️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
▶️ Usage
Run the application using:

bash
Copy code
python main.py
Once launched, you can:

Open an image (via File → Open or drag & drop)

Apply filters or draw on it

Undo/Redo your edits

Switch between light and dark themes

Capture from your webcam in real-time

🖼️ Interface Screenshots
Here’s a preview of the application interface 👇

<p align="center"> <img src="assets/1.png" width="420" alt="Main Window Interface"/> <img src="assets/2.png" width="420" alt="Drawing Mode"/> </p> <p align="center"> <img src="assets/3.png" width="420" alt="Dark Theme Mode"/> </p>
Make sure the images (1.png, 2.png, 3.png) are inside the assets/ folder in your repository for them to appear correctly.

📂 Project Structure
mathematica
Copy code
PyQt5-Image-Processing-Application/
│
├── main.py
├── ui/
│   ├── main_window.ui
│   └── icons/
├── assets/
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
├── utils/
│   ├── filters.py
│   ├── draw.py
│   └── undo_redo.py
├── requirements.txt
└── README.md
🚀 Future Enhancements
🧠 Integrate AI-based auto-enhancement

🎨 Add a custom filter editor

💾 Support multi-format exports (PNG, JPG, PDF)

⌨️ Include keyboard shortcuts for faster editing

👨‍💻 Author
Sayab Arshad Soduzai
🎓 Software Engineer | 🤖 AI & Data Science Enthusiast

<p align="left"> <a href="mailto:sayabarshad789@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a> <a href="https://www.linkedin.com/in/sayab-arshad-soduzai-6138a1252"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> <a href="https://github.com/SayabArshad"><img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white"></a> </p>
📝 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this project for educational or personal purposes.

<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4b6cb7,100:182848&height=100&section=footer"/> </p> ```
