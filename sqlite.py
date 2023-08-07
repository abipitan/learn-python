import sqlite3 

connection = sqlite3.connect("marvel.gb") # making an empty data base.
# when we have established a connection we will need to terminate it\
#  at the end of the code.

release_list = [
    (2008, "Iron Man", "Robert Downey Jr"),
    (2011, "Thor", "Chris Hemsworth" ),
    (2012, "Marvel's First Avengers", "Scarlett Johansen"),
    (2014, "Guardians of the Galaxy", "Chris Pratt"),
    (2015, "Ant Man", "Paul Rudd"),
    (2016, "Doctor Strange", "Benedict Cumberbatch")
    (2018, "Black Panther", "Chadwick Boseman")
]

connection.close()