-- Create schema for snowpipe
CREATE OR REPLACE SCHEMA fifa_football.snowpipe_schema;

// Create Pipe
CREATE OR REPLACE PIPE fifa_football.snowpipe_schema.stadium_snowpipe
auto_ingest = TRUE
AS 
COPY INTO fifa_football.football_schema.stadium
FROM @fifa_football.external_stage_schema.stadium_ext_stage_yml;

DESC PIPE fifa_football.snowpipe_schema.stadium_snowpipe;