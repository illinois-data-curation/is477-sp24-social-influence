rule all:
    input:
        "data/reddit.csv",
        "data/Lows per day (DISNEY).png",
        "data/Highs per day (DISNEY).png",
        "data/Closing Stock to Comment Sentiment.png",
        "data/Closing Stock to Post Sentiment.png"

rule reddit_data:
    output:
        posts = "data/posts.csv",
        comments = "data/comments.csv"
    shell:
        "python reddit_data.py"

rule run_analysis:
    input:
        posts = "data/posts.csv",
        comments = "data/comments.csv"
    output:
        analysis = "data/reddit.csv", 
        lows_plot = "data/Lows per day (DISNEY).png",
        highs_plot = "data/Highs per day (DISNEY).png",
        sentiment_plot = "data/Closing Stock to Comment Sentiment.png",
        post_sentiment_plot = "data/Closing Stock to Post Sentiment.png"
    shell:
        "python analysis.py"
