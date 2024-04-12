# Status Report

Our project examines how the recent boycotts against Disney affected the company’s stocks. This topic was chosen because with the recent issues in Palestine, there have been mentions of certain companies (such as Disney) having falling stocks due to boycotts and for many across various platforms to use the tag “BoycottDisney”. We want to see if with social media sentiment, how the stocks of Disney fair and changes were noticeable.

## Changes:

When collecting our data for our research, we were able to get the NASDAQ data on Disney easily through their website. However, we ran into issues attempting to gather the X API Data. Prior to Elon Musk’s acquisition of X, Twitter’s API data was free for academic use. Now, if we were to get our desired historical data we would need to pay for an enterprise license which would be in excess of $10,000 a month. So, we decided to use the Reddit API instead. We chose Reddit because the API is easier to use, and is free to use. Through its subreddit feature, it also hosts a variety of unique communities, so we will be able to access data from a wide variety of perspectives to investigate our topic.
Another change that had been made was to our research question. Upon the initial proposal, the feedback received indicated that the scope of the research questions was broad and should be reduced. Since our intention has been to examine 1 particular company, we will focus on the one. Meaning that our research questions now are:
How do social media sentiments correlate with the stock market performance of the Disney Brand?
What possible factors could contribute to the fluctuations in audience sentiment surrounding Disney’s stocks, if any?

 With the reduced scope of the project, we believe that we would still get a broad examination of social media sentiments as Disney is a popular entertainment brand that many have interacted with and even grew up following. This means that there is huge potential for the Reddit API data to possess polarizing opinions.


### Reddit Data Collection:

Since our NASDAQ data is YTD (January 1st 2024 onward) we used the same timeline when using the Reddit Search API. Our methodology was to find posts containing Disney AND (exclusive AND) Boycott in our desired timeline and then collect the comments for each post. To create a usable dataset, our script creates two csv files, one called `posts.csv` and the other called `comments.csv`. The `posts.csv` file contains the title of the post, its id, its url, and any text inside of the post. The `comments.csv` file contains the comment_id, post_id (for joining the tables), and body which contains the text of the comment. As mentioned previously, the two tables can be joined using the post_id column.
Since posts and comments are both free text submissions, some data cleaning was necessary in order to produce tidy csv files. Most posts and comments contain newline characters and commas which are both used as delimiters in csv files. So, we had to replace newline characters with spaces and use quoting (wrapping the text values in quotes) to produce valid csv files. While this does reduce human readability, it creates tidy datasets for easy computational analysis.

## Disney NASDAQ Stock Data:
With this dataset, it is relatively simple and clear to work with. In other words there is not much cleaning required based on the data.

## Artifacts:

- **reddit_data.py**: A Python script that gathers our research data using the Reddit API and outputs two csv files: `posts.csv` and `comments.csv`
- **comments.csv**: The comments csv file contains the comment_id, post_id (for joining the tables), and body which contains the text of the comment.
- **posts.csv**: The posts csv file contains the title of the post, its id, its url, and any text inside of the post.
- **requirements.txt**: Requirements file for the Python virtual environment to promote computational reproducibility
- **Setup.md**: A documentation file outlining the steps to recreate the Python virtual environment and run the `reddit_data.py` script to collect the data
- **Disney_HIstorical_NASDAQ.csv**: This csv file contains the date, the close, the volume, high, and low of the stock on that particular day.


## Updated Timeline:

**April 12 - April 16 - Data Cleaning and Analysis**
**All Members**: Engage in thorough data cleaning and quality assessment to prepare the data for in-depth analysis and perform exploratory data analysis.
**Member 1**: 
Update the project report with the necessary changes and the current progress of the project. Also discuss with other group members to make sure everyone stays on the same track and make records of meeting notes.
**Member 2 & Member 3**:
Lead the detailed analysis phase, applying statistical or machine learning techniques to address the research questions.
To answer the research questions, members 2 and 3 will perform initial exploratory data analysis to find out what can be acquired/ learned from the data:
This step includes:
- Frequency of like terms
- Basic statistical analysis such as mean and standard deviation

**April 17 - April 23 - Visualization and Finalization of Report**
**All Members**: 
Develop visualizations to represent the analysis findings clearly. This involves selecting appropriate types of charts to represent the data analysis outcomes, such as time series plots showing stock price movements alongside sentiment trend lines and scatter plots illustrating the correlation between sentiment scores and stock performance metrics. Appropriate python packages (such as matplotlib) as well as other means of datavisualization will be used. Everything done in this step should be reproducible, and an automated workflow will be used via Snakemake. 
**Member 1**: 
Finalize the project report, incorporating the analysis results and visualizations, ensuring the narrative is coherent and insightful.
**Member 2 & Member 3**:
Assist in refining the visualizations and contributing to the final sections of the project report. Additionally, the 2 members will use Zenodo Sandbox to properly give the project the correct Metadata it should be labeled as.

**April 24 - April 25 - Submission**
**All Members**: 
Perform a final review of the entire project, including the GitHub repository organization, documentation, code, and the completed project report.
