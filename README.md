# AI Scraper Project

## **Overview**
AI Scraper is a Python-based project designed to fetch articles from the web, generate titles and summaries using a large language model (LLM), and save the results for further analysis. This project demonstrates modular design, abstraction, and unit testing for scalable and maintainable code.

---

## **Features**
- Fetch articles from any given URL using web scraping techniques.
- Generate titles and summaries using OpenAI's LLMs.
- Save generated results to a text file for easy access.
- Modular design with separation of concerns for better maintainability.
- Comprehensive unit testing for all critical modules.

---

## **Project Structure**
```plaintext
AI-scraper/
├── config/                    # Configuration files and setup
│   ├── __init__.py
│   ├── config.py              # Global settings
│   ├── logger_setup.py        # Logger configuration
│
├── core/                      # Core business logic
│   ├── __init__.py
│   ├── article_fetcher.py     # Fetch articles from the web
│   ├── summarizer.py          # Generate summaries and titles
│   ├── file_manager.py        # File operations for saving results
│   ├── process_article.py     # Main processing logic
│
├── prompts/                   # Prompt templates for LLM
│   ├── __init__.py
│   ├── prompts.py             # Templates for article processing
│
├── utils/                     # Utility modules
│   ├── __init__.py
│   ├── output_manager.py      # Console output management
│
├── tests/                     # Unit tests for the project
│   ├── test_article_fetcher.py
│   ├── test_file_manager.py
│   ├── test_process_article.py
│   ├── test_summarizer.py
│
├── .env                       # Environment file for API keys
├── app.log                    # Log file for application events
├── requirements.txt           # Python dependencies
├── main.py                    # Entry point for the program
└── result.txt                 # File for storing generated results
```

## Prerequisites
Python 3.8 or higher
An OpenAI API key
A virtual environment (optional, but recommended)

1. Clone the Repository
    git clone https://github.com/GeorgiLukanov87/ai-scraper.git
    cd ai-scraper
2. Create a Virtual Environment
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies - Install the required Python libraries:
    pip install -r requirements.txt
4. Configure the Environment - Create a .env file in the root directory and add your OpenAI API key:
    OPENAI_API_KEY=your_openai_api_key
5. Run the Application - Execute the main.py file to start the application:
    python main.py

## Usage
Provide a URL in main.py for the article you want to process.
The application will:
Fetch the article.
Generate a title and summary using OpenAI's LLM.
Print the results in the console.
Save the results to result.txt.

## Unit Testing
The project includes comprehensive unit tests for all critical modules. To run the tests:
    python -m unittest discover tests

## Key Modules
1. config/
config.py: Stores global configurations, like file names and API keys.
logger_setup.py: Sets up the logger for tracking application events.
2. core/
article_fetcher.py: Handles fetching articles from URLs.
summarizer.py: Interfaces with OpenAI's LLM to generate summaries and titles.
file_manager.py: Saves results (titles, summaries, and URLs) to a text file.
process_article.py: Combines all functionalities to process articles end-to-end.
3. prompts/
prompts.py: Contains reusable prompt templates for generating titles and summaries.
4. utils/
output_manager.py: Manages console output, including error and result messages.

## Logging
The project logs all key events to app.log:

Errors (e.g., network failures, API issues)
Successful operations (e.g., article fetched, results saved)

## Result File
    ========================================
    The application saves all generated results to result.txt.
    Each entry is structured as:
    Record <N>:
    URL: <Article URL>
    Generated Title: <Title>
    Generated Summary: <Summary>
    ========================================

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.