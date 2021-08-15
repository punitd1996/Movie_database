
#connecting a sqlite database:----->

import sqlite3

#Creating New Database:----->

conn = sqlite3.connect('moviesdatabase.db')
#print("successfully created database")

#Creating Cursor
c = conn.cursor()




#Creating Movies Table in a database:----->

#c.execute("""CREATE TABLE movies(
          #movie_name text,
          #actor_name text,
          #actress_name text,
          #year of release integer,
          #director_name)""")
#print("Movies Table Created")





# Inserting Data in movies table:----->

#many_details = [
               # ('Raees','Shahrukh Khan','Mahira Khan', 2017 ,'Rahul Dholakia'),
               # ('Raazi','Vicky Kaushal','Alia Bhatt', 2018 ,'Meghna Gulzar'),
               # ('Shershaah','Sidharth Malhotra','Kiara Advani', 2021 ,'Vishnuvardhan'),
               # ('Dabangg','Salman Khan','Sonakshi Sinha', 2010 ,'Abhinav Kashyap'),
               # ('PK','Aamir Khan','Anushka Sharma', 2014 ,'Rajkumar Hirani'),
                #]
#c.executemany("INSERT INTO movies VALUES(?,?,?,?,?)",many_details)
#print("Data inserted in a movies table")




#Querying the data from the movies Table:----->

#Select all details from movie table:

#c.execute("SELECT * FROM movies")
#items = c.fetchall()
#for item in items:
    #print(item)


#Select all rows from movies table using PRIMARY KEY:

#c.execute("SELECT rowid, * FROM movies ")
#items = c.fetchall()
#for item in items:
    #print(item)


#Select movies name based on actor name:

#c.execute("SELECT movie_name FROM movies WHERE actor_name='Salman Khan'")
#items = c.fetchall()
#for item in items:
    #print(item)



conn.commit()
conn.close()
