# 📚 Arxiv Paper Analyzer
This tool automatically collects, filters, and analyzes recent papers from Arxiv in AI, computational linguistics, machine learning, and software engineering categories. It specifically focuses on papers related to large language models, agents, and LLMs.

### ✨ Features
- Automated paper collection from Arxiv
- Multi-category paper analysis
- Duplicate removal based on titles
- Topic filtering for LLM/Agent related papers
- Title word count visualization
- Top 100 papers ranking
- Asynchronous processing

### 🛠️ How to Get Started?

1. Clone the repository
```bash
git clone [your-repository-url]
cd arxiv-paper-analyzer
```
2.Install the required dependencies
```bash
pip install metagpt
```
3.Run the analyzer
```bash
python arxiv_analyzer.py
```
### 🔧 Technical Components

#### DataInterpreter: Main Analysis Engine
- Handles web scraping  
- Processes paper information  
- Generates visualizations  

#### Web Scraping Tool: Data Collection  
- Fetches paper information from Arxiv  
- Extracts titles and metadata  
- Handles multiple categories  