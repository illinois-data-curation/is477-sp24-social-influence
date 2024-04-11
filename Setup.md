# Reddit Data Scraper

This Python script uses the PRAW (Python Reddit API Wrapper) to scrape data from Reddit.

## Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- `credentials.json` file with Reddit API credentials. Ask Jackson or use your own.

### Create virtual environment
Create a virtual environment named 'venv': `python3 -m venv venv`

### Activate virtual environment
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  .\venv\Scripts\activate
  ```

### Install dependencies
Install the required dependencies from the `requirements.txt` file: 

```pip install -r requirements.txt```


### Running the Script

After setting up the environment and installing the dependencies, you can run the script with the following command: 

```python reddit_data.py```