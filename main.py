import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector
import time


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
worksheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Dz73RpnRghC6LCpL1-39VDAIRf4BC4-3G6ZfuhGvR2c/edit#gid=2042640543').sheet1


conn = mysql.connector.connect(
    host="132.148.72.171",
    user="tps_test",
    password="Pacific23!",
    database="tps_test"
)

cursor = conn.cursor()
print("db Connected")

create_table_sql = """
    CREATE TABLE IF NOT EXISTS diamonds_final (
        ID INT PRIMARY KEY,
        Stock_id VARCHAR(255),
        ReportNo VARCHAR(255),
        Shape VARCHAR(255),
        Carats FLOAT,
        color VARCHAR(255),
        clarity VARCHAR(255),
        cut VARCHAR(255),
        polish VARCHAR(255),
        symmetry VARCHAR(255),
        flou VARCHAR(255),
        length FLOAT,
        width FLOAT,
        height FLOAT,
        depth FLOAT,
        `table` INT,
        lab VARCHAR(255),
        video VARCHAR(255),
        image VARCHAR(255),
        Price FLOAT,
        Currency VARCHAR(255)
    );
"""


cursor.execute(create_table_sql)
conn.commit()

def sync_data():
    
    sheet_data = worksheet.get_all_records()

  

    cursor.execute("SELECT ID FROM diamonds_final")
    sd=cursor.fetchall()
 
    #chnaged 
    for i in sd:
        nf=True
        for j in sheet_data :
            if i[0] == j["ID"] :
                nf=False
                break 
        if nf :
            cursor.execute(f"delete FROM diamonds_final where ID={i[0]}")

    sql = f"""
            INSERT INTO diamonds_final (ID, Stock_id, ReportNo, Shape, Carats, color, clarity, cut, polish, symmetry, flou, length, width, height, depth, `table`, lab, video, image, Price, Currency)
<<<<<<< HEAD
            VALUES (%(ID)s, %(Stock id)s, %(ReportNo)s, %(Shape)s, %(Carats)s, %(color)s, %(clarity)s, %(cut)s, %(polish)s, %(symmetry)s, %(flou)s, %(length)s, %(width)s, %(height)s, %(depth)s, %(table)s, %(lab)s, %(video)s, %(image)s, %(Price)s, %(Currency)s)
            ON DUPLICATE KEY UPDATE
                Stock_id = VALUES(Stock_id),
                ReportNo = VALUES(ReportNo),
                Shape = VALUES(Shape),
                Carats = VALUES(Carats),
                color = VALUES(color),
                clarity = VALUES(clarity),
                cut = VALUES(cut),
                polish = VALUES(polish),
                symmetry = VALUES(symmetry),
                flou = VALUES(flou),
                length = VALUES(length),
                width = VALUES(width),
                height = VALUES(height),
                depth = VALUES(depth),
                `table` = VALUES(`table`),
                lab = VALUES(lab),
                video = VALUES(video),
                image = VALUES(image),
                Price = VALUES(Price),
                Currency = VALUES(Currency);
        """

    cursor.executemany(sql,sheet_data)
    conn.commit()
    print(f"data synced [{time.time()}]")
while True:
    sync_data() 
    time.sleep(10)  
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector
import time


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
worksheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Dz73RpnRghC6LCpL1-39VDAIRf4BC4-3G6ZfuhGvR2c/edit#gid=2042640543').sheet1


conn = mysql.connector.connect(
    host="132.148.72.171",
    user="tps_test",
    password="Pacific23!",
    database="tps_test"
)

cursor = conn.cursor()
print("db Connected")

create_table_sql = """
    CREATE TABLE IF NOT EXISTS diamonds_final (
        ID INT PRIMARY KEY,
        Stock_id VARCHAR(255),
        ReportNo VARCHAR(255),
        Shape VARCHAR(255),
        Carats FLOAT,
        color VARCHAR(255),
        clarity VARCHAR(255),
        cut VARCHAR(255),
        polish VARCHAR(255),
        symmetry VARCHAR(255),
        flou VARCHAR(255),
        length FLOAT,
        width FLOAT,
        height FLOAT,
        depth FLOAT,
        `table` INT,
        lab VARCHAR(255),
        video VARCHAR(255),
        image VARCHAR(255),
        Price FLOAT,
        Currency VARCHAR(255)
    );
"""


cursor.execute(create_table_sql)
conn.commit()

def sync_data():
    
    sheet_data = worksheet.get_all_records()

  

    cursor.execute("SELECT ID FROM diamonds_final")
    sd=cursor.fetchall()
 
    #chnaged 
    for i in sd:
        nf=True
        for j in sheet_data :
            if i[0] == j["ID"] :
                nf=False
                break 
        if nf :
            cursor.execute(f"delete FROM diamonds_final where ID={i[0]}")

    sql = f"""
            INSERT INTO diamonds_final (ID, Stock_id, ReportNo, Shape, Carats, color, clarity, cut, polish, symmetry, flou, length, width, height, depth, `table`, lab, video, image, Price, Currency)
=======
>>>>>>> origin/main
            VALUES (%(ID)s, %(Stock id)s, %(ReportNo)s, %(Shape)s, %(Carats)s, %(color)s, %(clarity)s, %(cut)s, %(polish)s, %(symmetry)s, %(flou)s, %(length)s, %(width)s, %(height)s, %(depth)s, %(table)s, %(lab)s, %(video)s, %(image)s, %(Price)s, %(Currency)s)
            ON DUPLICATE KEY UPDATE
                Stock_id = VALUES(Stock_id),
                ReportNo = VALUES(ReportNo),
                Shape = VALUES(Shape),
                Carats = VALUES(Carats),
                color = VALUES(color),
                clarity = VALUES(clarity),
                cut = VALUES(cut),
                polish = VALUES(polish),
                symmetry = VALUES(symmetry),
                flou = VALUES(flou),
                length = VALUES(length),
                width = VALUES(width),
                height = VALUES(height),
                depth = VALUES(depth),
                `table` = VALUES(`table`),
                lab = VALUES(lab),
                video = VALUES(video),
                image = VALUES(image),
                Price = VALUES(Price),
                Currency = VALUES(Currency);
        """

    cursor.executemany(sql,sheet_data)
    conn.commit()
    print(f"data synced [{time.time()}]")
while True:
    sync_data() 
    time.sleep(10)  
