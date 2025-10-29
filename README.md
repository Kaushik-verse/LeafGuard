# 🌿 Leaf Disease Detection using AI (Groq + FastAPI + Tailwind)

## 🔍 Overview

The **Leaf Disease Detection** system is an **AI-powered web application** that helps farmers and researchers identify plant leaf diseases from uploaded images. The backend integrates **deep learning** for disease prediction and **Groq’s large language model** to generate detailed, natural-language explanations of results.

The project has two main parts:
1. 🧠 **Backend (AI + FastAPI + Groq)**
2. 💻 **Frontend (TailwindCSS + HTML)**

---

## ⚙️ Tech Stack Breakdown

| Component | Technology Used | Purpose |
|------------|-----------------|----------|
| **Backend Framework** | **FastAPI (Python)** | To build fast REST APIs for prediction and chat explanation |
| **AI Model** | Pre-trained CNN (e.g., MobileNet / Custom Leaf Model) | Detects disease type from uploaded leaf images |
| **LLM Integration** | **Groq API (llama3-8b-8192)** | Generates textual disease descriptions and treatment advice |
| **Frontend Framework** | **HTML + Tailwind CSS** | For responsive and aesthetic user interface |
| **HTTP Requests** | **Fetch API (JavaScript)** | To connect frontend to backend (upload & results) |
| **Server Communication Format** | **JSON** | Data transfer between frontend and backend |
| **Environment** | **Python 3.10+** | To run FastAPI and AI model scripts |
| **Development Tool** | **VS Code / PyCharm** | IDE for development and debugging |

---

## 🧩 System Architecture (End-to-End Flow)

1. **User Interaction (Frontend)** – The user uploads a leaf image via the Tailwind-powered web UI.
2. **FastAPI Backend** – Receives the image, calls the AI model to predict the disease.
3. **Model Prediction** – CNN model identifies the disease class.
4. **Groq API Integration** – Groq’s LLM (llama3-8b-8192) generates detailed textual explanations.
5. **Response Display** – The frontend dynamically shows prediction results with confidence and details.

---

## 📂 Folder Structure

```
Leaf-Disease-Detection/
│
├── backend/
│   ├── main.py                # FastAPI application
│   ├── requirements.txt       # Python dependencies
│   ├── model/
│   │   └── leaf_model.h5      # Pre-trained CNN model
│   ├── utils/
│   │   └── preprocess.py      # Image preprocessing utilities
│
├── frontend/
│   ├── index.html             # Tailwind-based UI
│   ├── app.js                 # Fetch API for backend calls
│   ├── styles.css             # Tailwind compiled styles
│
└── README.md
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<yourusername>/leaf-disease-detection.git
cd leaf-disease-detection/backend
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Groq API Key
Create a `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

### 4️⃣ Run FastAPI Server
```bash
uvicorn main:app --reload
```

Backend runs on: `http://127.0.0.1:8000`

### 5️⃣ Open Frontend
Open `frontend/index.html` in your browser.

---

## 🧠 Example Workflow

1. Upload `tomato_leaf.jpg`  
2. FastAPI → Model predicts → “Tomato Early Blight”  
3. Groq → Generates explanation  
4. Frontend → Displays disease info + treatments  

---

## 🔬 Features

- 🌱 Image Upload & Preview  
- ⚡ Real-time Disease Prediction  
- 🤖 Groq LLM Explanations  
- 🧭 FastAPI REST Backend  
- 💡 Tailwind Modern UI  

---

## 🧭 Future Improvements

- Multi-disease classification  
- Real-time camera capture  
- Database storage for prediction history  
- Confidence visualization graphs  
- Voice output integration  

---

## 🏷️ Credits

- **Frontend:** HTML, Tailwind CSS  
- **Backend:** FastAPI, Python  
- **AI Model:** CNN (MobileNetV2 / Custom trained model)  
- **LLM Explanation:** Groq API (llama3-8b-8192)  
- **Developed by:** Kaushik  
