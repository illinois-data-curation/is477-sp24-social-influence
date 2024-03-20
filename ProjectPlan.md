# Overview

In the digital age, companies are more than just global entities reliant on traditional success metrics. However, they are also increasingly subject to the court of public opinion on platforms such as Twitter, Facebook, and Reddit. Stocks can be seen as the "lifeblood" of a company as they can dictate what a company does, and they can be significantly influenced by social media, where a single viral tweet can either bolster or batter a company's stock value. Recently, however, a form of online boycott has appeared, and many companies' stocks have been hurt. Against this backdrop, our research looks into how social media sentiments correlate with a company's stock market performance and identifies factors that can influence the relationship between how consumers view a company.

## Research Questions

- How do social media sentiments correlate with the stock market performance of various companies?
- What possible factors could contribute to the fluctuations in audience sentiment surrounding stocks?

## Team

We have integrated the specific roles and responsibilities of our team members with a detailed timeline, which is shown in the timeline section. This approach ensures that we have a clear understanding of the tasks each member is accountable for at different stages of the project.

## Datasets

### Social Media Sentiment Data (API Data)

We will collect data on tweets before and after the release of a few products and examine the overall sentiment of the product. For example, we will select high-profile Disney movie releases, such as those from the Marvel or Star Wars franchises. These movies typically generate a lot of buzz on social media. Another Disney product we are going to look at is theme park openings or new attractions. The opening of new parks typically has a significant impact on Disney's stock price. To collect data for each chosen Disney product, we will identify the launch dates and compile a list of associated keywords and hashtags. Then, we will use the Twitter API to collect tweets that mention those identified keywords and hashtags. 

### Stock Market Data (Non-API Data from Nasdaq.com)

This dataset will include historical stock price data from Nasdaq. This dataset is set to offer an extensive examination of how various companies' stocks have performed over the previous year. To further answer our research questions, Our approach involves dividing the stock data into segments before and after each event and looking for patterns. Specifically, we aim to investigate whether there is a noticeable increase in stock prices subsequent to positive social media buzz surrounding events like film releases. Those data will be critical in establishing a correlation with social media sentiment trends.

## Jackson Stock Data Writeup

NASDAQ publishes historical data on Disney's stock price ($DIS). This data is aggregated from EDGAR, the Electronic Data Gathering, Analysis, and Retrieval system which is provided by the SEC. Publicly traded companies are required to register their financials (such as balance sheets and earnings) through EDGAR. EDGAR also makes certain stock price data publicly available and free to use by the general public (About EDGAR). Since the data is free for the public to use, our use of the stock price data from EDGAR is fully compliant with their licensing.

The specific dataset we're using contains up to 10 years of historical data. We will be using data from 3/18/2023 until 3/19/2024 specifically. The dataset is a CSV file containing the following columns: Date (M/D/Y), Close/Last (Price the stock closed at in dollars), Volume (Shares traded that day), Open (Opening price in dollars), High (Highest price a share was sold for that day in dollars), and Low (Lowest price a share was sold for that day in dollars).

## Timeline

### March 20 - March 26 - Data Identification and Preliminary Research
- **Member 1:** Begin drafting the project report in Markdown, focusing on a detailed overview and refinement of the research questions.
- **Member 2:** Research and document potential APIs for acquiring social media sentiment data, including initial tests and data structure analysis.
- **Member 3:** Identify sources for stock market data, focusing on data availability, format, syntaxes, and licensing requirements.

### March 27 - April 2 - Data Acquisition
- **Member 1:** Assist in evaluating data sources and documenting the data acquisition process, including any challenges or initial findings.
- **Member 2:** Lead the acquisition of social media sentiment data via selected APIs, ensuring data integrity checks are in place.
- **Member 3:** Acquire stock market data, paying close attention to ensuring the data meets the project's diversity requirements in format, syntax, and license.

### April 3 - April 9 - Data Integration and Initial Analysis
- **All Members:** Collaborate on integrating the acquired datasets using Python/Pandas or SQL, ensuring smooth and logical merging of disparate data sources.
- **Member 1:** Document the integration process in detail within the project report.
- **Member 2 & Member 3:** Begin preliminary analysis to explore the datasets, identifying patterns or discrepancies that could influence later stages

### April 10 - April 16 - Data Cleaning and Detailed Analysis
- **All Members:** Engage in thorough data cleaning and quality assessment to prepare the data for in-depth analysis.
- **Member 1:** Update the project report with findings from the data cleaning process and initial analyses.
- **Member 2 & Member 3:** Lead the detailed analysis phase, applying statistical or machine learning techniques to address the research questions.

### April 17 - April 23 - Visualization and Finalization of Report
- **All Members:** Develop visualizations to represent the analysis findings clearly. This involves selecting appropriate types of charts to represent the data analysis outcomes, such as time series plots showing stock price movements alongside sentiment trend lines and scatter plots illustrating the correlation between sentiment scores and stock performance metrics. 
- **Member 1:** Finalize the project report, incorporating the analysis results and visualizations, ensuring the narrative is coherent and insightful.
- **Member 2 & Member 3:** Assist in refining the visualizations and contributing to the final sections of the project report.

### April 24 - April 25 - Submission
- **All Members:** Perform a final review of the entire project, including the GitHub repository organization, documentation, code, and the completed project report.