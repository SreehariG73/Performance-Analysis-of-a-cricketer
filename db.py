import sqlite3
conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE Teams (ID INTEGER PRIMARY KEY,name TEXT)')
conn.execute('CREATE TABLE RCB (ID INTEGER PRIMARY KEY,name TEXT)')
conn.execute('CREATE TABLE CSK (ID INTEGER PRIMARY KEY ,name TEXT)')
conn.execute('CREATE TABLE SRH (ID INTEGER PRIMARY KEY ,name TEXT)')
conn.execute('CREATE TABLE MI (ID INTEGER PRIMARY KEY ,name TEXT)')
conn.execute('CREATE TABLE DC (ID INTEGER PRIMARY KEY ,name TEXT)')
conn.execute('CREATE TABLE KKR (ID INTEGER PRIMARY KEY ,name TEXT)')
conn.execute('CREATE TABLE RR (ID INTEGER PRIMARY KEY,name TEXT)')
conn.execute('CREATE TABLE KXIP (ID INTEGER PRIMARY KEY,name TEXT)')

print("Table created successfully")

c = conn.cursor()

Teams = [(1,'Royal Challengers Banglore'),(2,'Chennai Super Kings'),
            (3,'Sunrisers Hyderabad'),(4,'Mumbai Indians'),(5,'Delhi Capitals'),
            (6,'Kolkata Knight Riders'), (7,'Rajastan Royals'),(8,'Kings 11 Punjab')
        ]

c.executemany('INSERT INTO Teams(ID,name) VALUES(?,?);',Teams)
conn.commit()

SRH = ['DA Warner',
 'B Kumar', 'JO Holder', 
'KS Williamson', 'V Shankar', 'Rashid Khan',
'Mohammad Nabi', 'S Kaul', 'CJ Jordan', 'WP Saha', 'MK Pandey',
'Shakib Al Hasan', 'YK Pathan', 'Sandeep Sharma', 'B Stanlake',
'RK Bhui', 'Basil Thampi', 'AD Hales', 'SP Goswami',
'JM Bairstow', 'Abhishek Sharma', 'KK Ahmed',
'MJ Guptill', 'Abdul Samad', 'PK Garg', 'S Nadeem', 'T Natarajan',
'MR Marsh'
]
conn.commit()
i = 1

for row in SRH:
    c.execute('INSERT INTO SRH(ID,name) VALUES(?,?);',(i,row))
    i = i+1
   
c.execute("select * from SRH;")
print(c.fetchall())

Mi =  [ 'SS Tiwary', 'DS Kulkarni',  'AP Tare',  'KA Pollard', 'RG Sharma',  'SA Yadav', 'R Dhawan',
       'JJ Bumrah', 'J Suchith',
       'HH Pandya',
       'MJ McClenaghan',  'KH Pandya', 'TG Southee',
       'MJ Guptill', 'KV Sharma', 'E Lewis', 'Ishan Kishan',
       'BCJ Cutting', 'PJ Sangwan', 'M Markande', 'A Dananjaya',
       'Mustafizur Rahman', 'Q de Kock', 
       'RD Chahar', 'SD Lad', 'AS Joseph', 'BB Sran', 'JL Pattinson',
       'TA Boult']
conn.commit()
i = 1
for row in Mi:
    c.execute('INSERT INTO MI(ID,name) VALUES(?,?);',(i,row))
    i = i+1
   
c.execute("select * from MI;")
print(c.fetchall())


RR = [ 'AM Rahane',
       'SV Samson', 'PV Tambe', 'AM Nayar',
       'R Tewatia','CH Morris', 'J Theron',
       'DJM Short', 'BA Stokes', 'RA Tripathi', 'JC Buttler', 'K Gowtham',
       'S Gopal', 'JD Unadkat', 'B Laughlin', 'H Klaasen', 'JC Archer',
       'MK Lomror', 'P Chopra', 'IS Sodhi', 'Anureet Singh', 'R Parag',
       'LS Livingstone', 'AJ Turner', 'VR Aaron', 'YBK Jaiswal',
       'RV Uthappa', 'TK Curran', 'AJ Tye', 'Kartik Tyagi', 'AS Rajpoot']
conn.commit()
i = 1
for row in RR:
    c.execute('INSERT INTO RR(ID,name) VALUES(?,?);',(i,row))
    i = i+1
   
c.execute("select * from RR;")
print(c.fetchall())


DC =  [
        'R Ashwin',
        'PP Shaw', 'LE Plunkett',
       'Abhishek Sharma', 'SS Iyer', 'CA Ingram', 'RR Pant',
       'KMA Paul', 'AR Patel', 
       'HV Patel', 'Avesh Khan', 'K Rabada', 'S Lamichhane', 'C Munro',
       'A Mishra', 'SE Rutherford', 'J Suchith', 'TA Boult', 'I Sharma',
       'SO Hetmyer', 'MP Stoinis', 'R Ashwin', 'A Nortje', 'AM Rahane',
       'TU Deshpande', 'AT Carey', 'P Dubey', 'DR Sams']
conn.commit()
i = 1
for row in DC:
    c.execute('INSERT INTO DC(ID,name) VALUES(?,?);',(i,row))
    i = i+1
   
c.execute("select * from DC;")
print(c.fetchall())

Kxip =  [
       'DA Miller', 'KL Rahul', 'MA Agarwal', 'KK Nair', 'AJ Finch',
       'R Ashwin', 'AJ Tye', 'Mujeeb Ur Rahman', 'CH Gayle', 'BB Sran',
       'MK Tiwary', 'AS Rajpoot', 'AD Nath', 'SN Khan', 'N Pooran',
       'SM Curran', 'GC Viljoen', 'M Ashwin', 'Mohammed Shami',
       'Harpreet Brar', 'P Simran Singh', 'K Gowtham', 'CJ Jordan',
       'DJ Hooda', 'JDS Neesham', 'Ravi Bishnoi', 'SS Cottrell',
       'Arshdeep Singh']
conn.commit()
i = 1
for row in Kxip:
    c.execute('INSERT INTO KXIP(ID,name) VALUES(?,?);',(i,row))
    i = i+1
   
c.execute("select * from KXIP;")
print(c.fetchall())

Kkr =  ['KD Karthik',
       'EJG Morgan', 'Shakib Al Hasan',  'SP Narine',  'AD Russell',  'C de Grandhomme', 
       'Kuldeep Yadav', 'DM Bravo', 'SP Jackson',  'IR Jaggi',
       'AS Rajpoot', 'N Rana', 'KD Karthik', 'RK Singh', 'TK Curran',
       'Shubman Gill', 'Shivam Mavi', 'MG Johnson', 'M Prasidh Krishna',
       'JPR Scantlebury-Searles', 'NS Naik', 'HF Gurney', 'JL Denly',
       'CR Brathwaite', 'Y Prithvi Raj', 'KC Cariappa', 'RA Tripathi',
       'T Banton', 'LH Ferguson', 'KL Nagarkoti', 'CV Varun']
conn.commit()
i = 1
for row in Kkr:
    c.execute('INSERT INTO KKR(ID,name) VALUES(?,?);',(i,row))
    i = i+1
   
c.execute("select * from KKR;")
print(c.fetchall())

Csk =  [ 'MS Dhoni', 'SK Raina',
        'M Vijay',  'DJ Bravo','MM Ali',
       'F du Plessis', 'RA Jadeja', 
       'SR Watson', 'AT Rayudu', 'KM Jadhav', 'DL Chahar',
       'Harbhajan Singh', 'MA Wood', 'Imran Tahir', 'SW Billings',
       'DR Shorey', 'SN Thakur', 'MJ Santner', 'SM Curran', 'RD Gaikwad',
       'N Jagadeesan']
conn.commit()
i = 1
for row in Csk:
    c.execute('INSERT INTO CSK(ID,name) VALUES(?,?);',(i,row))
    i = i+1
   
c.execute("select * from CSK;")
print(c.fetchall())

Rcb =  [ 'V Kohli',  'AB de Villiers',  
       'HV Patel', 
       'DT Christian', 'PA Patel',
       
       'YS Chahal', 
       'KW Richardson', 'Sachin Baby', 
       'Washington Sundar',  'UT Yadav', 'Mohammed Siraj',
        'C de Grandhomme',  
        'S Dube', 'NA Saini', 'P Ray Barman', 'MP Stoinis',
       'AD Nath', 'H Klaasen', 'Gurkeerat Singh', 'D Padikkal',
       'AJ Finch', 'JR Philippe', 'CH Morris', 'I Udana', 'Shahbaz Ahmed']
conn.commit()
i = 1
for row in Rcb:
    c.execute('INSERT INTO RCB(ID,name) VALUES(?,?);',(i,row))
    i = i+1
   
c.execute("select * from RCB;")
print(c.fetchall())

conn.commit()
conn.close()