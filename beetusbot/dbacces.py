import MySQLdb
import config
'''
SHOULD PROBABLY CHANGE THIS TO SOME NICE ORM AND STUFF
PLS FIX
'''
def connect(): #connecting for every query? wow..
    db_connection = MySQLdb.connect(config.DATABASE_HOST, config.DATABASE_USER, config.DATABASE_PASS, config.DATABASE_DB)
    return db_connection

def get_post_in_thread(id):
    db_connection = connect()
    cursor = db_connection.cursor()
    cursor.execute("SELECT replied_id FROM repliedto  WHERE reddit_id='%s'" % id)
    id = cursor.fetchone()
    db_connection.close()
    return False if id is None else id[0]

def add_notification_request(reddit_id):
    db_connection = connect()
    cursor = db_connection.cursor()
    cursor.execute('INSERT INTO notifications(reddit_id, done) VALUES("%s", "%d")' % (reddit_id, 0))
    db_connection.commit()
    db_connection.close()

def get_new_stories():
    db_connection = connect()
    cursor = db_connection.cursor()
    cursor.execute("SELECT reddit_id FROM notifications WHERE done=0")
    items = cursor.fetchall()
    db_connection.close()
    return [item[0] for item in items]

def mark_checked(id):
    db_connection = connect()
    cursor = db_connection.cursor()
    cursor.execute("UPDATE notifications SET done=1 WHERE reddit_id='%s'" % id)
    db_connection.commit()
    db_connection.close
    return

def add_post(parent, user, reply_id):
    db_connection = connect()
    cursor = db_connection.cursor()
    try:
        cursor.execute('INSERT INTO repliedto(reddit_id, user, replied_id) VALUES("%s", "%s", "%s")' % (parent, user, reply_id))
        db_connection.commit()
    except:
        print "Something went wrong when adding to the database!"
        db_connection.rollback()
    db_connection.close()

def get_subscriptions(subscriber):
    db_connection = connect()
    cursor = db_connection.cursor()
    cursor.execute('SELECT subscribed_to FROM subscriptions WHERE subscriber="%s"' % subscriber)
    items = cursor.fetchall()
    db_connection.close()
    return items

def get_subscribers(writer):
    db_connection = connect()
    cursor = db_connection.cursor()
    cursor.execute('SELECT subscriber FROM subscriptions WHERE subscribed_to="%s"' % writer)
    items = cursor.fetchall()
    db_connection.close()
    return items

def remove_subscription(writer, subscriber):
    db_connection = connect()
    cursor = db_connection.cursor()
    try:
        cursor.execute('DELETE FROM subscriptions WHERE subscribed_to="%s" AND subscriber="%s" AND subreddit="fatpeoplestories"' % (writer, subscriber))
        db_connection.commit()
    except:
        print "Something went wrong when removing subscription to the database. Subscription possibly doesn't exists."
        db_connection.rollback()
    db_connection.close()

def add_subscription(writer, subscriber):
    db_connection = connect()
    cursor = db_connection.cursor()
    try:
        cursor.execute('INSERT INTO subscriptions(subscribed_to, subscriber, subreddit) VALUES("%s", "%s", "FatPeopleStories")' % (writer, subscriber))
        db_connection.commit()
    except:
        print "Something went wrong when adding subscription to the database. Subscription possibly already exists."
        db_connection.rollback()
    db_connection.close()
