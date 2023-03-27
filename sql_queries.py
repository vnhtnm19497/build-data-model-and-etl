# DROP TABLES

accounts_country_table_drop = "DROP TABLE  IF EXISTS accountscountry"
accounts_data_table_drop = "DROP TABLE IF EXISTS accountsdata"
accounts_series_table_drop = "DROP TABLE IF EXISTS accountsseries"

# CREATE TABLES

accounts_country_table_create = ("""CREATE TABLE IF NOT EXISTS accountscountry(
	country_code VARCHAR PRIMARY KEY,
	short_name VARCHAR,
	table_name VARCHAR,
	long_name VARCHAR,
	currency_unit VARCHAR
)""")

accounts_data_table_create = ("""CREATE TABLE IF NOT EXISTS  accountsdata(
	country_name VARCHAR,
    country_code VARCHAR,
    indicator_name VARCHAR,
    indicator_code VARCHAR,
    year_1995 NUMERIC,
    year_2000 NUMERIC,
    year_2005 NUMERIC,
    year_2010 NUMERIC,
    year_2014 NUMERIC,
)""")

accounts_series_table_create = ("""CREATE TABLE  IF NOT EXISTS accountsseries(
	series_code VARCHAR,
    topic VARCHAR,
    indicator_name VARCHAR,
    short_definition VARCHAR
)""")


# INSERT RECORDS

accounts_country_table_insert = ("""INSERT INTO accountscountry(
    country_code,
    short_name,
    table_name,
    long_name,
    currency_unit
) VALUES (%s, %s, %s, %s, %s)
""")

accounts_data_table_insert = ("""INSERT INTO accountsdata(
    country_name,
    country_code,
    indicator_name,
    indicator_code,
    year_1995,
    year_2000,
    year_2005,
    year_2010,
    year_2014
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")


accounts_series_table_insert = ("""INSERT INTO accountsseries(
    series_code,
    topic,
    indicator_name,
    short_definitio
) VALUES (%s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
    SELECT song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [accounts_country_table_create, accounts_data_table_create, accounts_series_table_create]
drop_table_queries = [accounts_country_table_drop, accounts_data_table_drop, accounts_series_table_drop]