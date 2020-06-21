# Udacity Data Engineering - Project 1 
### Postgres: Data-Modelling

A fictional Startup called Sparkify is trying to analize the data they've been collecting on songs and user activity. The only problem is that this data is being stored into JSON formats.
To solve this problem they hired a data engineer to help them storing this data in sql using postgres, so they can easily query and analyse the data. 


As the data engineer we have "to create a star schema optimized for queries on song play analysis. This includes the following tables.

Fact Table
<b>songplays</b> - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
Dimension Tables
<b>users</b> - users in the app
user_id, first_name, last_name, gender, level
<b>songs</b> - songs in music database
song_id, title, artist_id, year, duration
<b>artists</b> - artists in music database
artist_id, name, location, latitude, longitude
<b>time</b> - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday"


##"Project Steps
Below are steps you can follow to complete the project:

Create Tables
Write CREATE statements in sql_queries.py to create each table.
Write DROP statements in sql_queries.py to drop each table if it exists.
Run create_tables.py to create your database and tables.
Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.
Build ETL Processes
Follow instructions in the etl.ipynb notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run test.ipynb to confirm that records were successfully inserted into each table. Remember to rerun create_tables.py to reset your tables before each time you run this notebook.

Build ETL Pipeline
Use what you've completed in etl.ipynb to complete etl.py, where you'll process the entire datasets. Remember to run create_tables.py before running etl.py to reset your tables. Run test.ipynb to confirm your records were successfully inserted into each table.

Document Process
Do the following steps in your README.md file.

Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
State and justify your database schema design and ETL pipeline.
[Optional] Provide example queries and results for song play analysis.
Here's a guide on Markdown Syntax."
 
