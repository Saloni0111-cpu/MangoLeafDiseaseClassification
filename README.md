# 🍃 Mango Leaf Disease Classification

This project is a **Deep Learning-based image classification application** that detects and classifies mango leaf diseases using **CNN**.  
It helps farmers and researchers quickly identify plant health issues for better crop management.  

---

## 📌 Features
- ✅ Classifies **6 types** of mango leaf conditions:
  - Anthracnose  
  - Bacterial Canker  
  - Die Back  
  - Healthy  
  - Powdery Mildew  
  - Sooty Mould  
- ✅ Built with **TensorFlow & Keras (CNN)**  
- ✅ Dataset preprocessing with **ImageDataGenerator**  
- ✅ Training & Validation split (80/20)  
- ✅ Accuracy and loss visualization with **Matplotlib**  
- ✅ Saves trained model (`.h5`) for future use  
- ✅ Compatible with **Google Colab + Google Drive integration**  
- ✅ Can be integrated with **Streamlit frontend** for real-time predictions  

---

## 🗂️ Project Structure
📦 Mango-Leaf-Disease-Classification
┣ 📂 MangoLeafBD_Dataset/ # Original dataset (not uploaded to GitHub)
┣ 📂 MangoLeafBD_Train/ # Training split (auto-generated)
┣ 📂 MangoLeafBD_Val/ # Validation split (auto-generated)
┣ 📜 app.py # Streamlit app for prediction
┣ 📜 train_model.ipynb # Google Colab training notebook
┣ 📜 mango_leaf_disease_model.h5 # Saved trained model
┣ 📜 convert_model.py # Script to convert models (if needed)
┣ 📜 requirements.txt # Project dependencies
┣ 📜 README.md # Project documentation
┗ 📜 .gitignore # Ignored files (dataset, models, etc.)



---

## ⚙️ Installation & Setup

### 🔹 1. Clone the Repository

git clone https://github.com/your-username/mango-leaf-disease-classification.git
cd mango-leaf-disease-classification  

### 🔹2. Install Dependencies
pip install -r requirements.txt

### 🔹3. Run the Streamlit App
streamlit run app.py

---

👩‍💻 Developed by Saloni Zade
---
🔗 LinkedIn: https://www.linkedin.com/in/saloni-zade-7aa816257/
     | GitHub: https://github.com/Saloni0111-cpu
     | Email: saronisan09@gmail.com
