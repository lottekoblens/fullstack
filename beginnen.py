import mysql.connector

def mijnmethode () :
    print("ik ben een tekst")
    return "bla bla bla"

def database (dier) :
    mydb = mysql.connector.connect(
    host="mijndatabaselotte.mysql.database.azure.com",  #port erbij indien mac
    port=3306,
    user="ikalsadmin",
    password="abcd1234ABCD!@#$",
    database="onzedatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM Vakantiebestemming")

    myresult = mycursor.fetchall()

    returnString = ""

    for x in myresult:
        print(x[1])
        returnString += x[1] + " dit zijn de return values <br>"
    return returnString
database("dier")