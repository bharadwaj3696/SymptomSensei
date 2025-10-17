# SymptomSensei 🏥

An AI-powered symptom checker that helps users understand their symptoms and get educational health information using Google's Gemini AI.

![AI Symptom Checker](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-blue)
![Python](https://img.shields.io/badge/Python-3.11-green)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal)

## ⚠️ Disclaimer

**This application is for educational purposes only and does not provide medical advice.** Always consult with a qualified healthcare professional for medical concerns. This tool should not be used as a substitute for professional medical diagnosis or treatment.

## 🌟 Features

- **AI-Powered Analysis**: Uses Google's Gemini 2.5 Flash model to analyze symptoms
- **Detailed Suggestions**: Provides three probable conditions with recommended next steps for each
- **Clean UI**: Modern, responsive interface with gradient purple design
- **Real-time Results**: Fast API responses with loading indicators
- **Privacy-Focused**: No data storage, completely stateless application
- **Medical Disclaimer**: Every response includes a clear educational disclaimer

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SymptomSensei.git
   cd SymptomSensei
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn google-genai
   ```
   
   Or using uv (recommended):
   ```bash
   uv sync
   ```

3. **Set up your API key**
   
   Create a `.env` file in the root directory or set an environment variable:
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5000
   ```

5. **Open your browser**
   
   Navigate to `http://localhost:5000` to use the application

## 🏗️ Project Structure

```
SymptomSensei/
├── main.py           # FastAPI backend with Gemini integration
├── index.html        # Frontend UI
├── pyproject.toml    # Python project configuration
├── uv.lock          # Dependency lock file
├── .gitignore       # Git ignore rules
├── replit.md        # Project documentation
└── README.md        # This file
```

## 🔧 How It Works

1. **User Input**: Users describe their symptoms in the text area
2. **API Request**: Frontend sends symptoms to the `/check_symptoms` endpoint
3. **AI Processing**: Gemini AI analyzes symptoms with a medical-focused prompt
4. **Response**: Three probable conditions with recommendations are displayed
5. **Disclaimer**: Every response includes a medical disclaimer

## 💻 API Documentation

### POST `/check_symptoms`

Analyzes user symptoms and returns probable conditions.

**Request Body:**
```json
{
  "symptoms": "headache, fever, and sore throat for 2 days"
}
```

**Response:**
```json
{
  "response": "IMPORTANT EDUCATIONAL DISCLAIMER: ...\n\nBased on your symptoms...\n\n1. Common Cold...\n2. Influenza...\n3. Strep Throat..."
}
```

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **AI Model**: Google Gemini 2.5 Flash
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Server**: Uvicorn (ASGI)

## 🔐 Security

- API keys are stored as environment variables (never in code)
- Server-side error logging keeps sensitive data out of client responses
- CORS is configured (restrict origins for production use)
- Input validation prevents empty or malicious requests

## 🚢 Deployment

### Deploy on Replit
1. Import this repository to Replit
2. Add `GEMINI_API_KEY` to Replit Secrets
3. Click "Run" - the app will start automatically

### Deploy Elsewhere
1. Set the `GEMINI_API_KEY` environment variable
2. Run `uvicorn main:app --host 0.0.0.0 --port 5000`
3. Ensure port 5000 is accessible

## 📝 Configuration

The application uses these environment variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source.

## 🙏 Acknowledgments

- Google Gemini AI for powering the symptom analysis
- FastAPI for the excellent Python web framework
- The open-source community

## 📧 Support

If you have any questions or need help, please open an issue in the GitHub repository.

---

**Remember**: This is an educational tool. Always consult healthcare professionals for medical advice.
