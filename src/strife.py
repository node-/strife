#!/usr/bin/env python
#
#

from cobe.brain import Brain

def main():
    b = Brain("brains/bible.brain")
    #with open("learning/bible.txt", "r") as bibleFile:
    #    bible = bibleFile.readlines()

    #for line in bible:
    #    b.learn(line)

    print b.reply("Hello cobe")

if __name__ == "__main__":
    main()

