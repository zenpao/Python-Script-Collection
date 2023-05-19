firstNoun = str(input("Enter 1st noun:")).upper()
secondNoun = str(input("Enter 2nd noun:")).upper()
firstAdj = str(input("Enter 1st adjective:")).upper()
secondAdj = str(input("Enter 2nd adjective:")).upper()

lyrics = """
What do you want? 'Cause you've been keeping me awake
Are you here to distract me so I make a big mistake?
Or are you someone out there who's a little bit like me?
Who knows deep down I'm not where I'm meant to be?
Every day's a little harder as I feel your power grow
Don't you know there's part of me that longs to go...
\n"""

lyricsReplaced = lyrics.replace("someone",firstNoun).replace("who", secondNoun).replace("mistake", firstAdj).replace("power", secondAdj)

print(" \n===================Original Lyrics===================\n")

print(lyrics)

print(" ===================Replaced Lyrics===================\n")

print(lyricsReplaced)
