# NewMay2015 
All code contained in tournament.py and tournament.sql were created using sublime build 3083.
"\" used to conform to PEP standards for python code row length exceeding single row character limits.

DESCRIPTION OF CODE: The tournament.sql file creates a database called tournament, with two basic tables called players, and matches. The tournament.py file manages the tournament database by providing the ability to create Swiss Tournament style player pairs, while tracking the number of matches played and wins. The tournament.py file also provides the ability to scrub the database of previous tournament pairings and matches for subsequent Swiss Tournaments. The tournament_test.py file is code that will test the functionality of the tournament.py file, giving a pass or fails status of the code.

How to create the database and run the tournament_test.py file on the tournament.p file.
1. Paste this this link into a web browser to install the necessary VM software. https://www.udacity.com/wiki/ud197/install-vagrant
2. Paste the tournament.py tournament.sql and tournament_test.py files, contained in this github repository, into your USERS/fullstack/vagrant/tournament directory.
3. Open the Git BASH shell and follow the instructions provided in step 1 to open and access PSQL, create the tournament database, and run the tournament_test.py script to test the tournament.py code.
4. All test should pass, if not, then something got corrupted because the code passed FFA(first field application) with no issues :)!
