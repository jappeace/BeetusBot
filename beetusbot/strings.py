'''
Put in this file strings that are meant for simple user notifications
If you have a string that is suposed to change behavior, put it in config.py
'''
POST_CONTENT = """
Other stories from /u/{username}:

{text}

_____
^If ^you ^want ^to ^get ^notified ^as ^soon ^as ^{username} ^posts ^a ^new ^story, [^click ^here](http://www.reddit.com/message/compose/?to=BeetusBot&subject=subscribe&message=subscribe%20/u/{username})^.

^(Hi I'm BeetusBot, for more info about me go to /r/beetusbot)
"""# pls replace the ^'s with one ^() and test it

SUBSCRIPTION_CONTENT = """
Hello there {username}! You are now subscribed to the following users:

{text}

_____
^(To unsubscribe to any of these users, send a message that contains the word unsubscribe and a list of users, for example: unsubscribe /u/username /u/username2)
"""

NEW_STORY_CONTENT = """
Hello {username}!

/u/{writer} just posted a new story called "{title}".

[Click here to read it]({url})

_____
^(To unsubscribe, send a message that contains the word unsubscribe and a list of users, for example: unsubscribe /u/username /u/username2)
"""

FOOTER_TEXT = "Hi im BeetusBot" #not used?
