# YouTube ETL Pipeline for Fidelity
## By Chirag Madhukar

The YouTube ETL Pipeline project leverages Python, YouTube API, Pandas, and Apache Airflow on an AWS EC2 instance to extract, transform, and load data from the Fidelity YouTube channel. The process involves creating a GCP project, obtaining a YouTube API key, and executing the YouTube_ETL.py script to collect video details. Apache Airflow on EC2 manages the workflow through the YouTube_DAG.py file, orchestrating data processing and storage in an Amazon S3 bucket. The project offers a scalable and automated solution for analyzing YouTube channel metrics, with potential extensions for advanced analytics on platforms like Databricks and Snowflake, and seamless integration with Tableau for dynamic data visualization.
