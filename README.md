# ETL Pipeline with Airflow on AWS

Overview
This project demonstrates the creation of an ETL (Extract, Transform, Load) pipeline using Apache Airflow on an AWS EC2 instance. The pipeline is designed to crawl data from multiple sources on Wikipedia, perform data transformation and cleaning, and store the processed data in Amazon S3. Further analysis can be performed using AWS Athena, and the data can be loaded into a Snowflake database using Snowpipe for automated updates. Finally, Tableau is utilized for data visualization, connecting directly to Snowflake.

Technologies Used
AWS EC2
Apache Airflow
AWS S3
AWS Athena
Snowflake
Tableau
Setup Instructions
AWS Setup

Launch an EC2 instance on AWS to host the Airflow server.
Set up S3 buckets for storing raw and processed data.
Configure AWS Athena for querying data stored in S3.
Create a Snowflake account and set up a database for data loading.
Airflow Setup

Install Airflow on the EC2 instance.
Create a virtual environment for Airflow and install required dependencies.
Configure Airflow connections for AWS and Snowflake.
DAG Configuration

Define Airflow DAG tasks for crawling data from Wikipedia, transforming, and storing it in S3.
Schedule the DAG to run at specified intervals.
Data Transformation

Implement data transformation and cleaning scripts within the DAG tasks.
Ensure that the transformed data is stored in the designated S3 bucket.
AWS Athena Integration

Set up Athena tables to query data stored in the S3 bucket.
Implement SQL queries within the DAG tasks to interact with Athena.
Snowflake Data Loading

Configure Snowflake connection in Airflow.
Create tasks within the DAG for loading data into Snowflake using Snowpipe triggers.
Tableau Integration

Connect Tableau to Snowflake for data visualization.
Build dashboards and reports in Tableau based on the Snowflake data.
Running the Pipeline
Start the Airflow web server on the EC2 instance.

bash
Copy code
airflow webserver --port 8080
Trigger the DAG to run manually or set up a schedule for automatic execution.

Additional Notes
Make sure to replace placeholders in the configuration files with your AWS and Snowflake credentials.
Monitor Airflow logs and AWS/Snowflake consoles for any issues during the pipeline execution.
Contributors
[Ming5499]
License
This project is licensed under the MIT License.
