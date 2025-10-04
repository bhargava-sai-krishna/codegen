# 🚀 **Auto Code Deployer with Daytona Integration**

This project automates the process of deploying backend applications directly to a **Daytona sandbox environment**.
Currently, it supports **Flask-based Python applications**, but will later include support for multiple frameworks and languages such as **Node.js, FastAPI, and Django**.

---

## 📁 **Project Structure**

```
project-root/
│
├── backend/
│   ├── __pycache__/
│   ├── debug.py
│   ├── gemini_client.py
│   ├── main.py
│   ├── utils.py
│
├── checkpoints/
│
├── front_end/         # React frontend
│
├── frontend/          # Plain HTML frontend
│
├── sandbox/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── auto_deployer.py     # Handles automatic deployment
│   ├── daytona.py           # Daytona SDK integration
│   ├── fileParser.py        # Parses project files for upload
│   ├── port_checker.py      # Verifies free ports before deployment
│   ├── sandbox_creator.py   # Creates or retrieves sandbox environments
│
├── venv/                   # Virtual environment
│
├── .env                    # Environment variables
├── .gitignore
├── requirements.txt
```

---

## ⚙️ **Environment Variables**

Your `.env` file should contain the following keys:

```
GEMINI_API_KEY=
LONGCAT_API_KEY=
DAYTONA_API_KEY=
SANDBOX=
```

* **GEMINI_API_KEY** → Used for AI-assisted code generation or enhancement
* **LONGCAT_API_KEY** → Used for LLM or text-based interactions
* **DAYTONA_API_KEY** → Required to authenticate with the Daytona SDK (needs credit card for free credits)
* **SANDBOX** → Optional; existing sandbox ID for faster deployment

---

## 🧠 **Tech Stack**

**Backend:** Python, Flask, Daytona SDK
**Frontend:** React (`front_end/`), Plain HTML (`frontend/`)
**Tools:**

* `dotenv` for environment management
* `daytona` Python SDK for sandbox control
* `pip` for dependency management

---

## 🧩 **How It Works**

1. **File Parsing:**
   All project files are gathered using `fileParser.py`.

2. **Sandbox Management:**
   A Daytona sandbox is either created or reused using `sandbox_creator.py`.

3. **File Upload & Execution:**
   The backend files are uploaded to the sandbox, and Flask is started automatically on port **5000**.

4. **Preview Link:**
   The system prints a live URL to preview your deployed Flask app.

---

## ▶️ **How to Run the Application**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/bhargava-sai-krishna/codegen
cd codegen
```

### **2️⃣ Create and Activate Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**

Create a `.env` file in the root directory and fill in your keys:

```bash
GEMINI_API_KEY=your_gemini_key
LONGCAT_API_KEY=your_longcat_key
DAYTONA_API_KEY=your_daytona_key
SANDBOX=optional_sandbox_id
```

### **5️⃣ Run the Backend**

```bash
cd backend
python main.py
```

### **6️⃣ Run the Frontend**

* For **React**:

  ```bash
  cd front_end
  npm install
  npm start
  ```
* For **Plain HTML**:
  Simply open the files inside `frontend/` in a browser.

---

## 💳 **Daytona Sandbox Setup**

Daytona requires a valid credit card to activate your account, but you’ll receive **free credits** that can be used for deploying your sandbox applications.

---

## 🧭 **Future Enhancements**

* 🌐 Multi-language deployment (Node.js, Django, FastAPI, Go)
* 🧠 Integrated AI model for intelligent deployment recommendations
* 🔁 Real-time build status and sandbox logs
* 🧩 CI/CD pipeline integration

---