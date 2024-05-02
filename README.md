# Social Influence: How Social Media Can Affect the Stock Markets

## Contributors:
- Jackson Clark (GitHub username: JacksonArthurClark)
- Trishla Nair (GitHub username: tanair2)
- Ziwei Wang (GitHub username: IlinoisZiwei)

## Link to Archival Record:
- [Zenodo Record](https://zenodo.org/records/11099989)
- DOI: 10.5281/zenodo.11099988

## Summary

In the digital age, companies are more than just global entities reliant on the traditional success metrics. However, they are also increasingly subject to the court of public opinion on platforms such as Twitter, Facebook, and Reddit. Stocks can be seen as the "lifeblood" of a company as they can dictate what a company does, and they can be significantly influenced by social media, where a single viral tweet can either bolster or batter a company's stock value.

In October of 2023, Israel declared war against Hamas because Hamas attacked Israel. This in turn led to Israel attacking those in Palestine. Many have died and are still dying on either side of the war. Protests around the world in support of Palestine and a ceasefire, as well as in support of Israel, are occurring. As of recently in the United States, many university students are holding their own protests, condemning the US and asking the government to help the Palestinians.

In response, however, a form of online boycott has appeared, and many companies' stocks have been hurt because of their ties with Israel or because a major individual within the company holds beliefs that support Israel or have done something to support Israel. Against this backdrop, our research looks into how social media sentiments correlate with a company's stock market performance and identifies factors that can influence the relationship between how consumers view a company.

The main question on our minds was how do social media sentiments correlate with the stock market performance of various companies. To solve this, we decided to use a social media platform, refine our search to posts and comments referring to boycotts from October onwards, and using python, we conducted sentiment analysis and compared those values to the company’s stocks from the same time and looked for any correlation.

The company chosen for this project was Disney. Disney is a large entertainment company and with the rise of Disney+ during COVID, the company became even more popular. According to the Hollywood Reporter, Disney has donated money to help Israel, hence why many have called for a boycott against the company.

Originally, the media chosen for this project was X (formally known as Twitter before Elon Musk bought the company). With X, trends can appear when certain “hashtags” are used and it is easier to access the API data and look into tweets specifically using the hashtag. However, another platform had to be chosen because X will only allow users to get the data if they pay cash. This led us to use Reddit instead. Reddit is a social media platform that is built like an open forum and they have less restrictions to get the API Data.

After doing the intended analysis, we found only a handful of posts and comments from October 2023 onwards discussing the boycott of Disney. Based on the sentiment analysis, the texts were mostly either neutral or skewed negatively. Combining the stock data with the sentiment analysis, however, depicted no real correlation between the 2 due to bias from minimal data.

## Data Profile
Stock Market Data (Non-API Data from Nasdaq.com): This dataset will include historical stock price data from Nasdaq. This dataset is set to offer an extensive examination of how various companies' stocks have performed over the previous year. To further answer our research questions, Our approach involves divide the stock data into segments before and after each event and look for patterns. Specifically, we aim to investigate whether there is a noticeable increase in stock prices subsequent to positive social media buzz surrounding events like film releases. Those data will be critical in establishing a correlation with social media sentiment trends.

In conducting our research, we have adhered strictly to the terms set forth by NASDAQ for the use of its data. According to the licensing agreement, NASDAQ grants a limited, non-exclusive, non-transferable license for the use of data for internal business purposes, which encompasses academic research such as ours. Our project does not involve the redistribution of raw data nor does it allow reverse engineering or decompilation of the data. Furthermore, any derived data created during our analysis, such as statistical interpretations or aggregated findings, does not disclose the underlying NASDAQ data in a manner that could be reverse-engineered. We have ensured that our use of NASDAQ data is in full compliance with the license terms, focusing solely on educational and research purposes within the prescribed guidelines

To acquire our dataset, navigate to the following page: https://www.nasdaq.com/market-activity/stocks/dis/historical?page=1&rows_per_page=10&timeline=ytd and press the download button. Save the csv file as Disney_Stocks_NASDAQ.csv in the data folder. Sadly, we are unable to use the API as NASDAQ charges for use of their API.

NASDAQ publishes historical data on Disney's stock price ($DIS). This data is aggregated from EDGAR, the Electronic Data Gathering, Analysis, and Retrieval system which is provided by the SEC. Publicly traded companies are required to register their financials (such as balance sheets and earnings) through EDGAR. EDGAR also makes certain stock price data publicly available and free to use by the general public (About EDGAR). Since the data is free for the public to use, our use of the stock price data from EDGAR is fully compliant with their licensing.

The specific dataset we're using contains up to 10 years of historical data. We will be using data from 3/18/2023 until 3/19/2024 specifically. The dataset is a CSV file containing the following columns: Date (M/D/Y), Close/Last (Price the stock closed at in dollars), Volume (Shares traded that day), Open (Opening price in dollars), High (Highest price a share was sold for that day in dollars), and Low (Lowest price a share was sold for that day in dollars).

## Findings
Prior to exploring our main goal, we wanted to extrapolate some things from the datasets to better understand them. From the stock dataset, we examined the Lows and Highs of the days. Comparing the 2 line plots side by side, they looked nearly identical. This indicates to us that there was a minimal difference between the Highs and Lows of each day.

Another thing we also examined was with the reddit data and that was how much overlap was there between the comments and the posts. In other words, How many comments were there with the posts we found related to boycotting data. By joining the dataframes, we found that 5 of the 11 posts found had comments related to the boycotting of Disney. The post with the most comments had 105 comments and the post discussed boycotting Disney in the UK. The posts with the fewest comments only had 1 that was connected to the comments dataframe. 

Using the Textblob package, we began to examine the sentiment analysis of all the texts. The average sentiment from the comments was 0.05824079880986023. This indicates that on reddit the sentiment was neutral amongst the comments. As for the posts.the mean sentiment was 0.15833333333333333. While still being fairly neutral, the sentiment of the posts is more positive compared to the comments.

Using numpy, we looked into the correlation coefficients and examined linear regression. From the correlation coefficient, we see the correlation between the Last stock of the day and the comment’s sentiment analysis as -0.38190184. This indicates that the correlation is a bit weak but negative. However with the posts, we see the correlation as -0.95915213. This indicates that there is a strong correlation between the sentiment and the last stock of the day that is negative.

While it can be concluded that there is a strong correlation, the plots tell us a different story. From the respective regression plots of comments and posts, many points share very similar sentiment ratings and also share similar Closing stock values. Additionally, because of how few points there are when it comes to the number of posts, it would be biased to conclude that the connection is strong. Therefore, the data can be said to be inconclusive.

What this also indicates is that using data from Reddit alone is not enough. While reddit is split into forums called subreddits, these forums are constantly moderated, so there are some posts and comments that potentially were more polarizing that were possibly removed. Hence, other data sources should be examined as well.

## Future Work
Lessons learned:

Our datasets’ sizes are relatively small, with one data having 2516 rows and the other having 201 rows. The potential limitation of working with a small dataset is that we cannot make statistically significant conclusions because it does not represent large trends. Although we did see a strong correlation between the two datasets we worked with, our conclusion might not apply to similar studies but to large datasets. So, in the future, we can use a large dataset to redo a similar analysis to validate or refute our findings.

One of the major lessons learned is the complexity of analyzing sentiments from social media. Text data from Reddit can sometimes be difficult to categorize because the data can include sarcasm and slang. For example, a statement like "Great job, as always" could be sarcastic in context but might be interpreted as positive by basic sentiment analysis tools. In addition, our analysis of Reddit comments can be challenging because they mainly contain short text, and we might not have enough context to help determine sentiment. The most important lesson we learned is to consider privacy and ethical issues. Because the data we use is from social media, it is essential to pay attention to that data and ensure that there is not any potential violation of privacy.

Potential future work:

In this project, we are focusing on comments on Reddit. In the future, more comments can be acquired through various platforms like Instagram and LinkedIn. By analyzing comments from different social media platforms, we can have a more comprehensive view of social sentiment from diverse demographics. For example, Instagram is predominantly used by younger demographics, and it is highly visual. Analyzing sentiment on Instagram could provide insights into how these images and videos influence consumer perceptions and further change stock performance. Another example is LinkedIn. It is a professional networking platform whose users include professionals, business leaders, and industry experts. Content on LinkedIn is more formal and business-oriented. From the sentiment analysis on LinkedIn, we can understand how professional comments impact the market perception of a company's worth. By analyzing the two platforms above, we can capture a broader spectrum of public opinion that may not be fully represented on a single platform like Reddit. Also, the speed at which information spreads on various platforms differs, so it is essential to include a slightly broader time spectrum to analyze the influence between people's comments and stock market performance from multiple platforms.

For future work, we also want to look into what factors could contribute to the fluctuations in audience sentiment surrounding stocks. Company news might play a critical role in influencing the stock market, and that news might include earnings announcements and product launches. Earnings reports reflect the company's financial health. Positive earnings reports can lead to stock price surges, while adverse earnings reports can lead to declines in stock prices. The announcement of launching new products can also influence a company's stock. For instance, the impact of a product launch like the Apple Vision Pro on Apple's stock price can vary widely based on social media sentiment and the perceived success of the product. Therefore, we can explore fluctuations in audience sentiment surrounding stocks by analyzing the company's earnings reports and news regarding product launches.

## Reproducing the Analysis
### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- `credentials.json` file with Reddit API credentials, the steps to acquire this are below

Get Reddit API credentials:
1. First, create a Reddit account if you don’t have one already.
2. Navigate to [https://ssl.reddit.com/prefs/apps/](https://ssl.reddit.com/prefs/apps/).
3. Click the 'create app' button.
4. Name your app, the name doesn’t matter. Give it a description as well.
5. Select the ‘script’ option.
6. For the redirect URL, use the following: `http://localhost:8080`.
7. Press the ‘create app button’.
8. Fill out the following JSON template:

```
{
    "client_id": "{The string under ‘personal use script’ under your app name}",
    "client_secret": "{Your secret key, do not share this!}",
    "user_agent": "{your-app-name}”
}
```
	- Save this as credentials.json in your workspace
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

### Run Snakemake
Run the Snakemade workflow with the following command:
```snakemake --cores 1```

Be sure to not delete the Disney_Stocks_NASDAQ.csv data file, you can delete and reproduce any of the other files in data using the Snakemake workflow.

## References

- **Reddit API Documentation** - [api - reddit.com](https://www.reddit.com/wiki/api/). (2023, November 28). Reddit. Retrieved May 1, 2024.
- **Documentation for Visual Studio Code** - [Visual Studio Code Docs](https://code.visualstudio.com/docs). (n.d.). Retrieved May 1, 2024.
- **Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... Oliphant, T. E.** (2020). Array programming with NumPy. *Nature*, 585, 357–362. [DOI](https://doi.org/10.1038/s41586-020-2649-2).
- **J. D. Hunter** - "Matplotlib: A 2D Graphics Environment," in *Computing in Science & Engineering*, vol. 9, no. 3, pp. 90-95, May-June 2007. [DOI: 10.1109/MCSE.2007.55](https://doi.org/10.1109/MCSE.2007.55).
- **Köster, J.** - Sustainable data analysis with Snakemake. (n.d.). Retrieved May 1, 2024, from [F1000Research](https://f1000research.com/articles/10-33/v1).
- **Loria, S.** (2018). textblob Documentation. Release 0.15, 2.
- **Mackintosh, P.** (2024, May 1). Walt Disney Company (The) Common Stock (DIS) Historical Data. Nasdaq. Retrieved May 1, 2024, from [Nasdaq](https://www.nasdaq.com/market-activity/stocks/dis/historical).
- **McKinney, W., & others.** (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51–56).
- **Rahman, A., & Lassner, E.** (2023, October 12). Disney Donates $2M to Support Humanitarian Relief in Israel After Hamas Attack. *The Hollywood Reporter*. Retrieved May 1, 2024, from [The Hollywood Reporter](https://www.hollywoodreporter.com/news/general-news/disney-donates-2m-humanitarian-relief-israel-1235617427/).
- **Van Rossum, G., & Drake, F. L.** (2009). Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.

