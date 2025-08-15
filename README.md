# Text-to-SQL Query Generator

A powerful Natural Language to SQL query converter built with Streamlit and Google Gemini AI. This application allows users to query a college admission database using plain English questions and automatically generates and executes the corresponding SQL queries.

## 🚀 Features

- **Natural Language Processing**: Convert English questions to SQL queries using Google Gemini AI
- **Interactive Web Interface**: Built with Streamlit for a user-friendly experience
- **Database Integration**: Seamlessly connects to SQLite databases
- **Real-time Query Execution**: Instant results from database queries
- **Smart Schema Understanding**: AI-powered database schema interpretation
- **Educational Database**: Pre-configured with college admission data (ACPC 2017)

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit UI  │───▶│  Google Gemini   │───▶│  SQLite DB     │
│                 │    │      AI Model    │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
   User Interface         Query Generation         Data Retrieval
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Gemini 2.5 Pro
- **Database**: SQLite
- **Language**: Python 3.x
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.7 or higher
- Google AI API key
- SQLite database file

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Text_To_SQL
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Setup
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_google_ai_api_key_here
```

### 5. Database Setup
Ensure your SQLite database file (`JustKidding_Admission.s3db`) is in the project root directory.

## 🎯 Usage

### Starting the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### How to Use

1. **Input Your Question**: Type your question in natural language in the input field
   - Example: "Show me all colleges in Ahmedabad with their branch names"
   - Example: "List top 5 colleges with lowest open cutoff scores"

2. **Submit Query**: Click the "Ask the question" button

3. **View Results**: The application will:
   - Generate the corresponding SQL query using AI
   - Execute the query against the database
   - Display the results in a formatted manner

## 🗄️ Database Schema

The application is configured to work with the following database structure:

### Tables
- **ADMI_CollegeBranch**: College-branch relationships and cutoff scores
- **MST_Branch**: Branch information
- **MST_College**: College details and metadata
- **MST_CollegeType**: College type classifications
- **MST_University**: University information
- **MST_HelpCenter**: Help center details
- **UseFulWebsite**: Useful website links

### Key Relationships
- College-Branch relationships through foreign keys
- College-University associations
- College type classifications

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google AI API key for Gemini access

### Database Configuration
- Default database: `JustKidding_Admission.s3db`
- Database path can be modified in `app.py`

## 📁 Project Structure

```
Text_To_SQL/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore patterns
├── JustKidding_Admission.s3db  # SQLite database
├── student.db           # Additional database file
├── sql.py              # SQL utilities (placeholder)
└──README.md           # This file

```



## 🔒 Security Considerations

- **API Key Protection**: Never commit your `.env` file to version control
- **Database Access**: Ensure proper database permissions and access controls
- **Input Validation**: The application processes user input - consider implementing input sanitization for production use

## 🚧 Limitations

- Requires active internet connection for Google Gemini AI
- Limited to SQLite database compatibility
- Query complexity depends on AI model understanding
- Database schema must be properly documented for optimal results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



---

**Note**: This application is designed for educational and demonstration purposes. For production use, consider implementing additional security measures, error handling, and performance optimizations.
