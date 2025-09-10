## Installation & Setup

### Step 1: Clone the Repository
```bash
cd backend
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Get API Keys

#### Google Gemini API Key:
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the generated key

### Step 5: Create Environment File
Create a `.env` file in the project root directory:
```bash
# Create .env file
touch .env  # On macOS/Linux
# or create manually on Windows
```

Add your API keys to the `.env` file:
```env
DATABASE_URL=sqlite:///./databse.db

API_PREFIX=/api
DEBUG=True

ALLOWED_ORIGINS=https://localhost:3000,https://localhost:5173
GEMINI_API_KEY=your_gemini_api_key_here
```


## Running the Application

### Start the Flask Server
```bash
python main.py
```

###You can run the backend in one terminal and switch to another terminal to run the frontend.

