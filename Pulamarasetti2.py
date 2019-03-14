# Import Needed Libraries
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os.path
import sqlite3
conn = sqlite3.connect("Pulamarasetti.db")
cur=conn.cursor()

#define functions
def CreateTables():
    cur.execute("Drop Table if Exists Sales")
    cur.execute("create table Sales (TrxId int not null,DoY int,StoreID int,SoupId int,PromoId int,Sales number);")
    cur.execute("Drop Table if Exists Days")
    cur.execute("create table Days (DoY int not null,DoW text,Holiday int,Weather text);")
    cur.execute("drop table if exists Managers")
    cur.execute("create table Managers (MgrId int not null,MgrName text,Grade text,Years int);")
    cur.execute("Drop table if exists Promotions")
    cur.execute("create table Promotions (PromoId int not null,Medium text,Target text,Interval text);")
    cur.execute("drop table if exists Soups")
    cur.execute("create table Soups (SoupId int not null,Type text,Vendor text,Mode text,Style text);")
    cur.execute("drop table if exists Stores")
    cur.execute("create table Stores (StoreId int not null,Location text,Size text,Elevation text,MgrId int);")
    print "Tables Created"
   
def InsertSales(record):
    TrxId = int(record[0])
    DoY = int(record[1])
    StoreId = int(record[5])
    SoupId = int(record[13])
    PromoId = int(record[18])
    Sales = float(record[22])
    row = [TrxId,DoY,StoreId,SoupId,PromoId,Sales]
    cur.execute("Insert or ignore into Sales values(?,?,?,?,?,?)",row)
def InsertDays(record):
    DoY = int(record[1])
    DoW = str(record[2])
    Holiday = int(record[3])
    Weather = str(record[4])
    row = [DoY,DoW,Holiday,Weather]
    cur.execute("Insert or ignore into Days values(?,?,?,?)",row)
def InsertManagers(record):
    MgrId = int(record[9])
    MgrName = str(record[10])
    Grade = str(record[11])
    Years = str(record[12])
    row = [MgrId,MgrName,Grade,Years]
    cur.execute("Insert or ignore into Managers values(?,?,?,?)",row)
def InsertPromotions(record):
    PromoId = int(record[18])
    Medium = str(record[19])
    Target = str(record[20])
    Interval = str(record[21])
    row = [PromoId,Medium,Target,Interval]
    cur.execute("Insert or ignore into Promotions values(?,?,?,?)",row)
def InsertSoups(record):
    SoupId = int(record[13])
    Type = str(record[14])          
    Vendor = str(record[15])
    Mode = str(record[16])
    Style = str(record[17])
    row = [SoupId,Type,Vendor,Mode,Style]
    cur.execute("Insert or ignore into Soups values(?,?,?,?,?)",row)
def InsertStores(record):
    StoreId = int(record[5])
    Location = str(record[6])            
    Size = str(record[8])
    Elevation = str(record[7])            
    MgrId = int(record[9])
    row = [StoreId,Location,Size,Elevation,MgrId]
    cur.execute("Insert or ignore into Stores values(?,?,?,?,?)",row)

def WhoAmI():
    return "Shanmukha Pulamarasetti"

def CurrentSemester():
    return "F2018"

def LoadFile(fileName):
    f = open(fileName,"r")
    global linecount
    linecount = 0
    line = f.readline()
    while line != "" and linecount < 100:
        linecount = linecount + 1
        line = line.replace("\n","")
        linelist = line.split("\t")
        InsertSales(linelist)
        InsertDays(linelist)
        InsertManagers(linelist)
        InsertPromotions(linelist)
        InsertSoups(linelist)
        InsertStores(linelist)
        line = f.readline()
    conn.commit()
    f.close()
    return "File Parsed"

def RowCount():
    return linecount

def TableRowCount(tableName):
    cur.execute("Select Count(*) from {}".format(tableName))
    tablerowcount = str(cur.fetchall()[0][0])
    return tablerowcount

def ListTable(tableName1):
    cur.execute("Select * from {}".format(tableName1))
    output = cur.fetchall()
    for row in output:
        print (row)

def CustomSQL(query):
    cur.execute(str(query))
    output1 = cur.fetchall()
    for row in output1:
        print (row)

def DistinctValues(input1):
    global input2
    global output2
    input2 = input1.split(",")
    cur.execute("Select count(distinct {0}) from {1}".format(input2[1],input2[0]))
    output2 = str(cur.fetchall()[0][0])
    return output2    

# Define Form as a Class
class Form( QDialog):
    # Form Constructor
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        cryptokey = 50
        self.pbuttonName = QPushButton("Developer's Name")
        self.lineeditName = QLineEdit("")
        self.pbuttonSemester = QPushButton("Current Semester")
        self.lineeditSemester = QLineEdit("")
        self.pbutton0 = QPushButton("Load File")
        self.lineedit0 = QLineEdit(" Enter Input File Name")
        self.pbutton1 = QPushButton("Show Input Row Count")
        self.lineedit1 = QLineEdit("Total Input Rows Parsed")
        self.pbutton2 = QPushButton("Table Rows Count")
        self.lineedit2 = QLineEdit("Enter Table Name")
        self.pbutton3 = QPushButton("List Table")
        self.lineedit3 = QLineEdit("Enter Table Name")
        self.pbutton4 = QPushButton("Custom SQL")
        self.lineedit4 = QLineEdit("Enter Custom SQL")
        self.pbutton5 = QPushButton("Distinct Values")
        self.lineedit5 = QLineEdit("Enter Tablename, ColumnName")
        self.pbuttonQuit = QPushButton("Quit")
        layout = QVBoxLayout()
        layout.addWidget(self.pbuttonName)
        layout.addWidget(self.lineeditName)
        layout.addWidget(self.pbuttonSemester)
        layout.addWidget(self.lineeditSemester)       
        layout.addWidget(self.pbutton0)
        layout.addWidget(self.lineedit0)
        layout.addWidget(self.lineedit0)
        layout.addWidget(self.pbutton1)
        layout.addWidget(self.lineedit1)
        layout.addWidget(self.pbutton2)
        layout.addWidget(self.lineedit2)
        layout.addWidget(self.pbutton3)
        layout.addWidget(self.lineedit3)
        layout.addWidget(self.pbutton4)
        layout.addWidget(self.lineedit4)
        layout.addWidget(self.pbutton5)
        layout.addWidget(self.lineedit5)
        layout.addWidget(self.pbuttonQuit)
        self.setLayout(layout)
        ck = cryptokey
        self.lineeditName.setFocus()
        self.connect(self.pbuttonName, SIGNAL("clicked()"),self.buttonNamePressed)
        self.connect(self.pbuttonSemester, SIGNAL("clicked()"),self.buttonSemesterPressed)
        self.connect(self.pbutton0, SIGNAL("clicked()"),self.button0Pressed)
        self.connect(self.pbutton1, SIGNAL("clicked()"),self.button1Pressed)
        self.connect(self.pbutton2, SIGNAL("clicked()"),self.button2Pressed)
        self.connect(self.pbutton3, SIGNAL("clicked()"),self.button3Pressed)
        self.connect(self.pbutton4, SIGNAL("clicked()"),self.button4Pressed)
        self.connect(self.pbutton5, SIGNAL("clicked()"),self.button5Pressed)
        self.connect(self.pbuttonQuit, SIGNAL("clicked()"),self.buttonQuitPressed)
        s = chr(ck + 20) + chr(ck) + chr(ck-2) +chr(ck-1)+chr(ck+6)
        self.setWindowTitle(s)
    # Form Methods
    
    def buttonNamePressed(self):
        Name = WhoAmI()
        self.lineeditName.setText(Name)
        
    def buttonSemesterPressed(self):
        Sem = CurrentSemester()
        self.lineeditSemester.setText(Sem)
        
    def button0Pressed(self):
        CreateTables()
        global fileName
        fileName = self.lineedit0.text()
        text = LoadFile(fileName)     
        self.lineedit0.setText(text) 
        
    def button1Pressed(self):
        rowcount = RowCount()           
        self.lineedit1.setText(str(rowcount))
        
    def button2Pressed(self):
        tableName = self.lineedit2.text()
        TRcount = TableRowCount(tableName)        
        self.lineedit2.setText(str(TRcount))
        
    def button3Pressed(self):
        tableName1= self.lineedit3.text()
        tableList=ListTable(tableName1)            
        self.lineedit3.setText("View Python IDLE shell")
        
    def button4Pressed(self):
        query = self.lineedit4.text()
        customSQL = CustomSQL(query)
        self.lineedit4.setText("View Python IDLE shell")
        
    def button5Pressed(self):
        input1 = self.lineedit5.text()
        dValues = DistinctValues(input1)
        self.lineedit5.setText(output2 + " unique values")
        
    def buttonQuitPressed(self):
        self.done(1)
        app.quit()
# End of Form Class Definition

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
