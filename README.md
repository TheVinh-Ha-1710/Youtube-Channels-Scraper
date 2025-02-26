# Youtube Channels Scraper

## Description

This project utilizes Scrapy to build a web scraping bot that collects data on top Vietnamese YouTube channels across various categories for analysis.

## Features

- Scrapes Top Vietnamese YouTube Channels: Collects data on leading YouTube channels across multiple categories.
- Automated Data Extraction: Uses Scrapy to efficiently extract channel names, subscriber counts, total views, and more.
- Customizable Categories: Allows modification of scraping targets based on user-defined categories.
- CSV Export: Saves the extracted data into a structured CSV file for further analysis.
- Error Handling & Logging: Implements basic error handling and logging to ensure smooth execution.
- Lightweight & Fast: Optimized for quick and efficient data retrieval.

## Technologies Used

- Python: main programming language.
- Scrapy: Python library for web scraping.
- csv: File format of the results.

## Installation & Setup

### Prerequisites

- Python 3.x installed
- Jupyter Notebook or a Python IDE (VS Code, PyCharm, etc.)
- Virtual environment (optional but recommended)

### Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/TheVinh-Ha-1710/Youtube-Channels-Scraper.git
   cd Youtube-Channels-Scraper
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the web scraping bot:

   ```sh
   cd youtube_scraper
   scrapy crawl youtube_spider -o ../results.csv
   ```

## Folder Structure

```
📂 Youtube-Channels-Scraper
 ├── 📂 youtube_scraper         # Main infrastructure of the scraper
 ├── 📜 .gitignore              # For specifying untracked files
 ├── 📜 README.md               # Project document
 ├── 📜 requirements.txt        # Required frameworks
 ├── 📜 results.csv             # The result CSV file
```
