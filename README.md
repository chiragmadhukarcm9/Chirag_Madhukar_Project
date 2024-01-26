# YouTube ETL Pipeline for Fidelity
## By Chirag Madhukar

The YouTube ETL Pipeline project leverages Python, YouTube API, Pandas, and Apache Airflow on an AWS EC2 instance to extract, transform, and load data from the Fidelity YouTube channel. The process involves creating a GCP project, obtaining a YouTube API key, and executing the YouTube_ETL.py script to collect video details. Apache Airflow on EC2 manages the workflow through the YouTube_DAG.py file, orchestrating data processing and storage in an Amazon S3 bucket.

This project's versatility extends beyond the Fidelity YouTube channel and can be applied to any YouTube channel, including those of its competitors such as ETrade, Vanguard, Charles Schwab, and BlackRock. By adapting the pipeline for competitors' channels, the project allows for comprehensive analysis and comparison of performance metrics such as views, likes, engagement, and upload frequency. This comparative analysis provides valuable insights into how Fidelity's YouTube presence measures up against its peers in the financial industry. Furthermore, the project can seamlessly integrate with advanced analytics platforms like Databricks and Snowflake, offering opportunities for in-depth analytics and insights. Additionally, the integration with Tableau enables dynamic data visualization for a comprehensive understanding of YouTube channel dynamics across different financial organizations.


