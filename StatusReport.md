# Status Report

Our project examines how the recent boycotts against Disney regarding Palestine affected the company’s stocks.

## Changes:

When collecting our data for our research, we were able to get the NASDAQ data on Disney easily through their website. However, we ran into issues attempting to gather the X API Data. Prior to Elon Musk’s acquisition of X, Twitter’s API data was free for academic use. Now, if we were to get our desired historical data we would need to pay for an enterprise license which would be in excess of $10,000 a month. So, we decided to use the Reddit API instead. We chose Reddit because the API is easier to use, and is free to use. Through its subreddit feature, it also hosts a variety of unique communities, so we will be able to access data from a wide variety of perspectives to investigate our topic.

### Reddit Data Collection:

Since our NASDAQ data is YTD (January 1st 2024 onward) we used the same timeline when using the Reddit Search API. Our methodology was to find posts containing Disney AND (exclusive AND) Boycott in our desired timeline and then collect the comments for each post. To create a usable dataset, our script creates two csv files, one called `posts.csv` and the other called `comments.csv`. The `posts.csv` file contains the title of the post, its id, its url, and any text inside of the post. The `comments.csv` file contains the comment_id, post_id (for joining the tables), and body which contains the text of the comment. As mentioned previously, the two tables can be joined using the post_id column.
Since posts and comments are both free text submissions, some data cleaning was necessary in order to produce tidy csv files. Most posts and comments contain newline characters and commas which are both used as delimiters in csv files. So, we had to replace newline characters with spaces and use quoting (wrapping the text values in quotes) to produce valid csv files. While this does reduce human readability, it creates tidy datasets for easy computational analysis.

## Artifacts:

- **reddit_data.py**: A Python script that gathers our research data using the Reddit API and outputs two csv files: `posts.csv` and `comments.csv`
- **comments.csv**: The comments csv file contains the comment_id, post_id (for joining the tables), and body which contains the text of the comment.
- **posts.csv**: The posts csv file contains the title of the post, its id, its url, and any text inside of the post.
- **requirements.txt**: Requirements file for the Python virtual environment to promote computational reproducibility
- **Setup.md**: A documentation file outlining the steps to recreate the Python virtual environment and run the `reddit_data.py` script to collect the data

## Updated Timeline:

**April 12 - April 16 - Data Cleaning and Analysis**
- **All Members**: Engage in thorough data cleaning and quality assessment to prepare the data for in-depth analysis and perform exploratory data analysis.
- **Member 1**: Update the project report with findings from the data cleaning process and initial analyses.
- **Member 2 & Member 3**: Lead the detailed analysis phase, applying statistical or machine learning techniques to address the research questions.

**April 17 - April 23 - Visualization and Finalization of Report**
- **All Members**: Develop visualizations to represent the analysis findings clearly. This involves selecting appropriate types of charts to represent the data analysis outcomes, such as time series plots showing stock price movements alongside sentiment trend lines and scatter plots illustrating the correlation between sentiment scores and stock performance metrics.
- **Member 1**: Finalize the project report, incorporating the analysis results and visualizations, ensuring the narrative is coherent and insightful.
- **Member 2 & Member 3**: Assist in refining the visualizations and contributing to the final sections of the project report.

**April 24 - April 25 - Submission**
- **All Members**: Perform a final review of the entire project, including the GitHub repository organization, documentation, code, and the completed project report.