# Udacity Data Engineering - Project 1 
### Postgres: Data-Modelling
<br/>
A fictional Startup called Sparkify is trying to analize the data they've been collecting on songs and user activity. The only problem is that this data is being stored into JSON formats. <br/>
To solve this problem they hired a data engineer to help them storing this data in sql using postgres, so they can easily query and analyse the data. 


As the data engineer we have "to create a star schema optimized for queries on song play analysis. This includes the following tables.

Fact Table <br/>
<b>songplays</b> - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
<br/>
Dimension Tables
<br/>
<b>users</b> - users in the app
user_id, first_name, last_name, gender, level
<br/>
<b>songs</b> - songs in music database
song_id, title, artist_id, year, duration
<br/>
<b>artists</b> - artists in music database
artist_id, name, location, latitude, longitude
<br/>
<b>time</b> - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday"
<br/>
<br/>
## Project Steps - From Udacity
Below are steps you can follow to complete the project:
<br/>
Create Tables<br/>
Write CREATE statements in sql_queries.py to create each table.<br/>
Write DROP statements in sql_queries.py to drop each table if it exists.<br/>
Run create_tables.py to create your database and tables.<br/>
Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.<br/>
Build ETL Processes<br/>
Follow instructions in the etl.ipynb notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run test.ipynb to confirm that records were successfully inserted into each table. Remember to rerun create_tables.py to reset your tables before each time you run this notebook.
<br/>
Build ETL Pipeline<br/>
Use what you've completed in etl.ipynb to complete etl.py, where you'll process the entire datasets. Remember to run create_tables.py before running etl.py to reset your tables. Run test.ipynb to confirm your records were successfully inserted into each table.
<br/>
Document Process<br/>
Do the following steps in your README.md file.
<br/>
Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.<br/>
State and justify your database schema design and ETL pipeline.<br/>
[Optional] Provide example queries and results for song play analysis.<br/>
Here's a guide on Markdown Syntax."<br/>
 
