-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop tournament if old one exists
DROP DATABASE IF EXISTS tournament;

-- Drop any old tables
DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS matches CASCADE;

-- Create a new tournament database
create database tournament;

-- Connect to the database
 \c tournament

 --Create the players table
	create table players (
		id SERIAL PRIMARY KEY,
		name text);

--Create matches table with references to players table
	create table matches (
		id SERIAL PRIMARY KEY,
		p1 INTEGER REFERENCES players,
		p2 INTEGER REFERENCES players,
		winner INTEGER REFERENCES players
		);

--Create a view of player id, name, and matches.
	CREATE VIEW num_matches as select players.id, players.name, 
	count (matches.id) as matches from players left join matches 
	on  players.id = matches.p1 or players.id = matches.p2 
	group by players.id;

--Create a view of player id and number of wins.
	CREATE VIEW num_wins as SELECT players.id, count(matches.winner) 
	as wins FROM players left join matches on players.id = matches.winner 
	GROUP by players.id order by wins desc;
