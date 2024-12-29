# Lumen

A Perplexity-inspired search and question-answering system that combines Google's Gemini API and Exa's search capabilities to provide enhanced search results and intelligent answers.

## 🌟 Features

- **Intelligent Query Generation**: Uses Gemini to transform natural language questions into optimized search queries
- **Recent News Search**: Fetches news articles from the past week using Exa's search API
- **Smart Summarization**: Automatically summarizes search results using Gemini
- **Related Questions**: Generates relevant follow-up questions based on search results
- **Similar Content Discovery**: Finds related articles based on URL similarity
- **Source Transparency**: Links to original sources for all information
- **YouTube Filtering**: Automatically excludes YouTube results for focused article-based search

## 🚀 Getting Started

### Prerequisites

- Python 3.10
- Active Gemini API key (from Google AI Studio)
- Active Exa API key

### API Keys Setup

You'll need to obtain API keys from:
1. Google AI Studio for Gemini access
2. Exa for search functionality

Set up your environment variables:
```bash
GEMINI_API_KEY=your_gemini_api_key
EXA_API_KEY=your_exa_api_key
```

### Installation

```bash
# Install required packages
pip install exa-py google-generativeai
```

## 💡 Usage

The project consists of three main components:

### 1. News Search (`news.py`)
```python
python news.py
# Enter your question when prompted
```
- Processes your question through Gemini for query optimization
- Searches recent news via Exa API
- Returns summaries and related questions

### 2. Related Questions Generator (`related_questions.py`)
```python
python related_questions.py
```
- Generates contextual follow-up questions
- Specializes in technology and product-related queries

### 3. Similar Content Finder (`similar.py`)
```python
python similar.py
```
- Discovers articles similar to a reference URL
- Provides diverse sources by excluding same-domain content

## 🔄 How It Works

1. User inputs a question
2. Question is processed by Gemini API for optimal search query formation
3. Exa API searches for relevant recent articles
4. Gemini API summarizes the found content
5. System generates related questions
6. All sources are provided for reference

## 🚧 Development Status

This project is under active development. Planned features include:
- Web interface/GUI for easier interaction
- Response caching to reduce API calls
- Customizable search time ranges
- Advanced filtering options
- Enhanced summarization features
- Rate limiting for API calls
- Error handling improvements
