BeetusBot
=========
Source code for BeetusBot

## Installation
Note: $ means you can execute as a user, # means you need to execute as root (sudo)

clone the repository:

	$ git clone https://github.com/Bakkes/BeetusBot.git

make sure you have the required python dependecies with pip

	# pip install praw
	# pip install mysql-python

Now go to "start the bot" to learn how to start it

### Compatibility
The bot was written in Python 2.7. Make sure you have this installed and set as the system default.
If you don't know how to change the system default, type in Google: "python set systemdefault <distro name>".

## Start the bot

### Manually
To start the bot manually go to the directory you cloned BeetusBot in and type:

	$ ./start.sh

if it doesn't work, make sure you have execute permissions on this file.

### Cron
To start the bot as a cron job use

	$ start.sh bot

to start the subscription service use

	$ start.sh subscription

to start them both use

	$ start.sh both

### Log output

The output of the bot is stored in `beetuslog/log-<currentdate>.log`. You can follow the output with:

	$ tail -f beetuslog/log-<currentdate>.log

### Testing

To test the beetusbot you need to put up a test account for the bot. A test subreddit and a local datatbase.

#### Test account
Go to https://www.reddit.com/login and create a new one.
Put your new login credentials in config.py
#### Sub reddit
Go to https://www.reddit.com/subreddits/create
Fill out the form, congrats, you're now an moderator. (well your bot is)
put this into the subreddit var in config.py

#### Database
Install mysql (if you did not do this already) now type

	$ mysql -u root -p

##### Error help
If you see `ERROR 2002, cant connect to ... socket`, it means you need to start the mysql deamon.
If your distrobution uses systemd (most should, if not you should upgrade) type:

	# systemctl start mysqld

try the mysql command again. If you still don't get a connection type:

	# tail -f /var/log/mysql/mysql.err

it will probably complain about some configuration error in /etc/mysql/my.cnf (in my case I tried to bind to a wrong ip adress)

##### Creating database credentials
you now should be logged into your local database as root.
create a new database with

	mysql> create database <databasename> \G

note I usualy keep the database name the same as the user name, now verify the creation with

	mysql> SHOW DATABASES\G

now to create the user type (or copy)

	mysql> CREATE USER '<user>'@'localhost' IDENTIFIED BY '<pass>'
	mysql> GRANT SELECT,INSERT,UPDATE,DELETE ON <databasename>.* TO '<user>'@'localhost'

the first line creates, the second line grants the privelages, the last line logs you out.
##### Create the tables
make sure your working directory is in the root of the beetusbot project.
beetusbot is currently not smart enough to create its own tables so we have to do that for him.

	mysql> use <databasename>
	mysql> \. createdb.sql
	mysql>SHOW TABLES\g

the last line should return somthing like:

	+------------------+
	| Tables_in_       |
	+------------------+
	| notifications    |
	| repliedto        |
	| subscriptions    |
	+------------------+

##### updating config.py
The final step is to update config.py with your new credentials.

## TODO
Rewrite everything
