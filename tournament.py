#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
	"""Connect to the PostgreSQL database.  Returns a database connection."""
	return psycopg2.connect("dbname=tournament")
	

def deleteMatches():
	"""Remove all the match records from the database."""
	DB = connect()
	c = DB.cursor()
	c.execute("DELETE FROM matches")
	DB.commit()
	DB.close()


def deletePlayers():
	"""Remove all the player records from the database."""
	DB = connect()
	c = DB.cursor()
	c.execute("DELETE FROM players")
	# Resets prim key players&matches tables.
	c.execute("ALTER SEQUENCE players_id_seq restart with 1")
	c.execute("ALTER SEQUENCE matches_id_seq restart with 1")
	DB.commit()
	DB.close()
	

def countPlayers():
	"""Returns the number of players currently registered."""
	DB = connect()
	c = DB.cursor()
	c.execute("SELECT count (*) from players;")
	pcount = c.fetchall() [0][0]
	DB.close()
	return pcount
	

def registerPlayer(name):
	"""Adds a player to the tournament database.
  
	The database assigns a unique serial id number for the player.  (This
	should be handled by your SQL database schema, not in your Python code.)
  
	Args:
	  name: the player's full name (need not be unique).
	"""
	DB = connect()
	c = DB.cursor()
	c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
	DB.commit()
	DB.close()


def playerStandings():
	"""Returns a list of the players and their win records, sorted by wins.

	The first entry in the list should be the player in first place, or a player
	tied for first place if there is currently a tie.

	Returns:
	  A list of tuples, each of which contains (id, name, wins, matches):
		id: the player's unique id (assigned by the database)
		name: the player's full name (as registered)
		wins: the number of matches the player has won
		matches: the number of matches the player has played
	"""
	DB = connect()
	c = DB.cursor()
	c.execute("SELECT num_matches.id, num_matches.name, num_wins.wins, \
		num_matches.matches from num_matches, num_wins where num_matches.id = \
		num_wins.id group by num_matches.id, num_matches.name, \
		num_matches.matches, num_wins.wins order by num_matches.id asc")
	outp1 = c.fetchall()
	DB.close()
	return outp1
	

def reportMatch(winner, loser):
	"""Records the outcome of a single match between two players.

	Args:
	  winner:  the id number of the player who won
	  loser:  the id number of the player who lost
	"""
	DB = connect()
	c = DB.cursor()
	# Inserts the winner and loser into matches table.
	c.execute("INSERT INTO matches (p1, p2) VALUES (%s, %s)", (winner, loser))
	# Updates the winner column in the matches table.
	c.execute("update matches set winner = p1")
	DB.commit()
	DB.close()
 
 
def swissPairings():
	"""Returns a list of pairs of players for the next round of a match.
  
	Assuming that there are an even number of players registered, each player
	appears exactly once in the pairings.  Each player is paired with another
	player with an equal or nearly-equal win record, that is, a player adjacent
	to him or her in the standings.
  
	Returns:
	  A list of tuples, each of which contains (id1, name1, id2, name2)
		id1: the first player's unique id
		name1: the first player's name
		id2: the second player's unique id
		name2: the second player's name
	"""
	DB = connect()
	c = DB.cursor()
	# Query to pull a fresh look at tournament standings for pairings test.
	c.execute("SELECT num_matches.id, num_matches.name, num_matches.matches, \
		num_wins.wins from num_matches, num_wins where num_matches.id = \
		num_wins.id group by num_matches.id, num_matches.name, \
		num_matches.matches, num_wins.wins order by num_wins.wins desc")
	output = c.fetchall()
	swiss_group = []
	
	# Uses range and len to build pairings list tuple.
	for i in range(0, (len(output)) -1, 2):
		make_list = (output[i][0], output[i][1], output[i + 1][0], \
			output[i + 1][1])
		swiss_group.append(make_list)
		
	DB.close()
	return swiss_group
