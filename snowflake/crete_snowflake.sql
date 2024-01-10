DROP DATABASE IF EXISTS fifa_football;
CREATE DATABASE fifa_football;
// Create schema
CREATE SCHEMA football_schema;
// Create Table
CREATE OR REPLACE TABLE fifa_football.football_schema.stadium (
rank INT,
stadium STRING,
capacity INT,
region STRING,
country STRING,
city STRING,
images STRING,
home_team STRING
);

SELECT * FROM fifa_football.football_schema.stadium


// Create file format object
CREATE SCHEMA file_format_schema;
CREATE OR REPLACE file format fifa_football.file_format_schema.format_csv
    type = 'CSV'
    field_delimiter = ','
    RECORD_DELIMITER = '\n'
    skip_header = 1
    
    
// Create staging schema
CREATE SCHEMA external_stage_schema;

// Create staging
CREATE OR REPLACE STAGE fifa_football.external_stage_schema.stadium_ext_stage_yml 
    url="s3://stadium-football-zone-yml/"
    credentials=(aws_key_id=''
    aws_secret_key='')
    FILE_FORMAT = fifa_football.file_format_schema.format_csv;

list @fifa_football.external_stage_schema.stadium_ext_stage_yml;