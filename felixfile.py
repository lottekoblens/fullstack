import mysql.connector

def methodenaam(eengegeven):
    print(eengegeven+": van felix")
    mydb = mysql.connector.connect(
    host="mijndatabaselotte.mysql.database.azure.com",  #port erbij indien mac
    port=3306,
    user="ikalsadmin",
    password="abcd1234ABCD!@#$",
    database="onzedatabase"
    )

    mycursor = mydb.cursor()
    gaan = eengegeven
    sql = "INSERT INTO Vakantiebestemming (naam, prijs) VALUES (%s, %s)"
    val = (gaan, 2100)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return "dit is de methode van felix : " + str(mycursor.rowcount)