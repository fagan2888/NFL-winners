import psycopg2 
import json
import os

directory = os.fsencode(r'C:\Users\phoki\Documents\Georgetown\Data\stats_data\stats_data')

conn = psycopg2.connect(database='nfl_stats', user='postgres', password ='georgetown', host='localhost', port='5432')

cur = conn.cursor()

cur.execute("""CREATE TABLE player_logs (
    player_id INTEGER, 
    year INTEGER, 
    game_id VARCHAR(255), 
    date DATE, 
    age FLOAT, 
    team VARCHAR(255), 
    game_location VARCHAR(255),
    opponent VARCHAR(255),
    game_won VARCHAR(255),
    player_team_score INTEGER,
    opponent_score INTEGER,
    passing_attempts INTEGER,
    passing_completions INTEGER,
    passing_yards FLOAT,
    passing_rating FLOAT,
    passing_touchdowns INTEGER,
    passing_interceptions INTEGER,
    passing_sacks INTEGER,
    passing_sacks_yards_lost FLOAT,
    rushing_attempts INTEGER,
    rushing_yards FLOAT,
    rushing_touchdowns INTEGER,
    receiving_targets INTEGER,
    receiving_receptions INTEGER,
    receiving_yards FLOAT,
    receiving_touchdowns INTEGER,
    kick_return_attempts INTEGER,
    kick_return_yards FLOAT,
    kick_return_touchdowns INTEGER,
    punt_return_attempts INTEGER,
    punt_return_yards FLOAT,
    punt_return_touchdowns INTEGER,
    defense_sacks INTEGER,
    defense_tackles INTEGER,
    defense_tackle_assists INTEGER,
    defense_interceptions INTEGER,
    defense_interception_yards FLOAT,
    defense_interception_touchdowns INTEGER,
    defense_safeties INTEGER,
    point_after_attempts INTEGER,
    point_after_makes INTEGER,
    field_goal_attempts INTEGER,
    field_goal_makes INTEGER,
    punting_attempts INTEGER,
    punting_yards INTEGER,
    punting_blocked INTEGER);
    """)

fields = [
    'player_id',
    'year',
    'game_id',
    'date',
    'age',
    'team',
    'game_location',
    'opponent',
    'game_won',
    'player_team_score',
    'opponent_score',
    'passing_attempts',
    'passing_completions',
    'passing_yards',
    'passing_rating',
    'passing_touchdowns',
    'passing_interceptions',
    'passing_sacks',
    'passing_sacks_yards_lost',
    'rushing_attempts',
    'rushing_yards',
    'rushing_touchdowns',
    'receiving_targets',
    'receiving_receptions',
    'receiving_yards',
    'receiving_touchdowns',
    'kick_return_attempts',
    'kick_return_yards',
    'kick_return_touchdowns',
    'punt_return_attempts',
    'punt_return_yards',
    'punt_return_touchdowns',
    'defense_sacks',
    'defense_tackles',
    'defense_tackle_assists',
    'defense_interceptions',
    'defense_interception_yards',
    'defense_interception_touchdowns',
    'defense_safeties',
    'point_after_attemps',
    'point_after_makes',
    'field_goal_attempts',
    'field_goal_makes',
    'punting_attempts',
    'punting_yards',
    'punting_blocked'
    ]

for file in os.listdir(directory):

    filepath = os.path.join(directory, os.fsencode(file))

    with open(filepath, 'r') as data_file:
        data = json.load(data_file)

        for item in data:

            my_data = [item[field] for field in fields]

            cur.execute("""INSERT INTO player_logs VALUES(
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,     
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )""",tuple(my_data))
    
cur.close()
conn.commit()
conn.close()