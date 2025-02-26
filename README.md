# Youtube Channel Scraper

## Description

This project focus on building a web scraping bot using Scrapy framework to get information about top Vietnamese youtube channel in various categories for further analysis.

## Features

- Data Extraction: Connects to MongoDB using pymongo to extract data on famous musical albums.
- Data Transformation: Utilizes the mrjob framework to perform MapReduce, partitioning data into meaningful datasets, such as Annual top sales, Best sellers in history, etc.
- Data Storage: Loads the transformed data into text-based databases for further analysis.
- Pipeline Report: Generates a report detailing the pipeline designs, key features, and potential improvements.

## Technologies Used

- Python: Core language for data extraction, transformation, and processing.
- MongoDB: NoSQL database for storing and retrieving album data.
- pymongo: Python library for connecting to MongoDB and extracting data.
- mrjob: Framework for running MapReduce jobs in Python.
- json: Python library for json parsing and processing.

## Installation & Setup

### Prerequisites

- Python 3.x installed
- Jupyter Notebook or a Python IDE (VS Code, PyCharm, etc.)
- Virtual environment (optional but recommended)

### Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/TheVinh-Ha-1710/Big-Data-Pipeline-Design.git
   cd Big-Data-Pipeline-Design
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

4. Run the data pipeline scripts:

   ```sh
   chmode +x run_pipelines.sh
   ```

## Folder Structure

```
📂 Diabetes-Predictive-Model
 ├── 📂 youtube_scraper         # Main infrastructure of the scraper
 ├── 📜 .gitignore              # For specifying untracked files
 ├── 📜 README.md               # Project document
 ├── 📜 requirements.txt        # Required frameworks
 ├── 📜 results.csv             # The result CSV file
```
