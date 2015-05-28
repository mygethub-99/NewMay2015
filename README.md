# Project 2 of FullStack Nano degree

***

## Name of Project: Swiss Style Tournament

#### Description: Write a Python module that uses PostgreSQL database to keep track of players and matches in a swiss tournament.
***
#### Required Files

#####tournament.py Contains the python module for the tournament.

#####tournament.sql Contains the sql code that will create the database, tables and views needed to track the players and matches.

#####tournament_test.py Contains the test code to verify that the tournamen.py and tournament.sql are valid.
***
## What is needed to run the tournament module.
1. Install Vagrant. Follow these instructions. [vagrant] (https://www.udacity.com/wiki/ud197/install-vagrant)
2. Clone the project from this Github repository. [project] (https://github.com/udacity/fullstack-nanodegree-vm)
3. Open Git Bash and type in *cd /vagrant/tournament*. Then type in *vagrant up*.
4. After the VM has loaded. Type in *vagrant ssh*. After you see a $ prompt, type in *cd /* then *ls*.
5. You will see a directory called vagrant. Type in *cd /vagrant/tournament*. Type in *ls*.
6. You will see three existing versions of tournament.py, tournament.sql, and tournament_test.py in the tournament directory.
7. Copy and paste the tournament.py, and tournament.sq found in the NewMay2015 repository into the user/fullstack/vagrant/tournament folder on your pc.
8. Now in the Git Bash command shell, type in *psql*.
9. Then type in *\i tournament.sql*. This will create the tournament database and tables.
10. Then type in *\q* to leave psql and return the $ prompt.
11. Now to test the tournament.py module. At the $ prompt in the tournament directory, type in *python tournament_test.py*. 
12. Expected outcome of test is to see *Success! All tests have pass!* If not, then something is not working as expected.
13. You are now ready to track swiss style tournament games.
