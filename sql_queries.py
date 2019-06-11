# DROP TABLES

songplay_table_drop = "drop table songplays"
user_table_drop = "drop table users"
song_table_drop = "drop table songs"
artist_table_drop = "drop table artists"
time_table_drop = "drop table time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays(songplay_id serial, start_time varchar, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar)
""")

user_table_create = ("""create table if not exists users(user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar)
""")

song_table_create = ("""create table if not exists songs(song_id varchar, title varchar, artist_id varchar, year int, duration float)""")

artist_table_create = ("""create table if not exists artists(artist_id varchar, name varchar, location varchar, latitude numeric, longitude numeric)
""")

time_table_create = ("""create table if not exists time(start_time varchar, hour int, day int, week int, month int, year int, weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays(start_time, user_id, level , song_id, artist_id, session_id, location, user_agent) values(%s,%s,%s,%s,%s,%s,%s,%s) 
""")

user_table_insert = ("""insert into users(user_id , first_name , last_name , gender , level) values(%s,%s,%s,%s,%s) 
""")

song_table_insert = ("""insert into songs(song_id, title, artist_id, year, duration) VALUES(%s,%s,%s,%s,%s)""")

artist_table_insert = ("""insert into artists(artist_id, name, location, latitude, longitude) values(%s,%s,%s,%s,%s) 
""")


time_table_insert = ("""insert into time(start_time, hour, day, week, month, year, weekday) values(%s,%s,%s,%s,%s,%s,%s) 
""")

# FIND SONGS

song_select = ("""select a.song_id,b.artist_id
                  from songs as a join artists as b
                  on a.artist_id=b.artist_id
                  where a.title=%s
                  and b.name=%s
                  and a.duration=%s
               """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]