import sqlite3
conn = sqlite3.connect('libr.db')
c= conn.cursor()
print('success')
# conn.execute('''CREATE TABLE ADMIN
#              (ID INTEGER PRIMARY KEY     NOT NULL,
#               NAME    TEXT    NOT NULL,
#                PASSWORD   TEXT  NOT NULL);''')
# print("Admin Table created successfully")

# conn.execute('''CREATE TABLE USER
#              (TITLE  TEXT NOT NULL,
#               NAME    TEXT    NOT NULL,
#               SURNAME   TEXT,
#               PHONE  TEXT   PRIMARY KEY  NOT NULL,
#               ADDRESS1  TEXT,
#               ADDRESS2   TEXT,
#               ADDRESS3   TEXT,
#               POSTCODE   INTEGER,
#               BOOKTITLE  TEXT  NOT NULL,
#               DATEBORROWED NUMERIC NOT NULL,
#               DOL   INTEGER,
#               MEMBERTYPE TEXT NOT NULL);''')
#print("User Table created successfully")

# conn.execute('''CREATE TABLE BOOKS
#             (BOOKTITLE  TEXT NOT NULL,
#              BOOKID TEXT  PRIMARY KEY     NOT NULL,
#              AUTHERNAME   TEXT  NOT NULL,
#              PRICE INT NOT NULL);''')
# print("Books Table created successfully")
#conn.close()
ListOfBooks = [('Software Quality', 'ISBN 9870001203709', 'Rajender Singh Chhillar', 600),
               ('Computer Graphics', 'ISBN 9870001203710', 'James D', 600),
               ('Computer Fundamental', 'ISBN 9870001203711', 'abc', 600),
               ('Database System', 'ISBN 9870001203712', 'Pardeep', 600),
               ('Operating System', 'ISBN 9870001203713', 'Korth', 600),
               ('Data Communication', 'ISBN 9870001203714', 'Korth', 600),
               ('Artifical Intelligence', 'ISBN 9870001203715', 'Korth', 600),
               ('Soft Computing', 'ISBN 9870001203716', 'Korth', 600),
               ('Art of UNIX', 'ISBN 9870001203717', 'Korth', 600),
               ('Programming With Java', 'ISBN 9870001203718', 'Korth', 600),
               ('Python Book', 'ISBN 9870001203719', 'Korth', 600),
               ('Bioinformatics', 'ISBN 9870001203720', 'Korth', 600),
               ('Anlysis And Design', 'ISBN 9870001203721', 'Korth', 600),
               ('Computer Security', 'ISBN 9870001203722', 'Korth', 600),
               ('Object Technology', 'ISBN 9870001203723', 'Korth', 600),
               ('Matlab', 'ISBN 9870001203724', 'Korth', 600),
               ('Internet of Thing', 'ISBN 9870001203725', 'Korth', 600),
               ('Web design', 'ISBN 9870001203726', 'Korth', 600),
               ('PC Software', 'ISBN 9870001203727', 'Korth', 600),
               ('Pattern Of Software', 'ISBN 9870001203728', 'Korth', 600),
               ('Logical Organisation', 'ISBN 9870001203729', 'Korth', 600),
               ('Programming In C#', 'ISBN 9870001203730', 'Korth', 600)
               ]
# c.execute("INSERT INTO ADMIN (ID, NAME, PASSWORD) VALUES (001, 'user', '1234')")
# conn.commit()
# conn.close()
 
 
#conn = sqlite3.connect('libr.db')

# c.executemany("INSERT INTO BOOKS (BOOKTITLE,BOOKID,AUTHERNAME,PRICE) VALUES (?,?,?,?)", ListOfBooks)
# conn.commit()
# conn.close()#
a = c.execute("select * from ADMIN").fetchone()
#a = c.fetchall()
print(a)
# for i in a:
#     username= i[1]
#     passw=i[2]

# print(username,passw)
#          self.MTypeDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
#          self.MTypeDetail.grid(row=1, column=0)
#          self.RnoDetails=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
#          self.RnoDetails.grid(row=1, column=1)
#         self.NameDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
#         self.NameDetail.grid(row=1, column=2)
#         self.AddDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
#         self.AddDetail.grid(row=1, column=3)
#         self.MnoDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
#         self.MnoDetail.grid(row=1, column=4)
#         self.PcodeDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
#         self.PcodeDetail.grid(row=1, column=5)
#         self.BtitleDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
#         self.BtitleDetail.grid(row=1, column=6)
#         self.DborrowedDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
#         self.DborrowedDetail.grid(row=, column=7)
#         self.DolDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
#         self.DolDetail.grid(row=1, column=8)