import mysql.connector
import os

# BEFORE BEGINNING EXECUTE IN YOUR POWERSHELL THIS COMMAND:
# setx DB_PASSWORD 'your_password'
# THE COMMAND WILL BE EFFECTIVE AFTER CLOSING ALL YOUR TERMINAL AND VSCODE WINDOWS
# YOU CAN CHECK IT WITH $env:DB_PASSWORD IN YOUR POWERSHELL OR IMPORT os IN TEST PAGE AND PRINT os.getenv('DB_PASSWORD')
db_password = os.getenv('DB_PASSWORD')

# CREATE MYSQL_USER IN YOUR MY SQL WITH ROOT PRIVILEGE
# USE YOUR ROOT PASSWORD DELETED IT AFTER THE USE
mydb =mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = ""
)
# CREATE CURSOR 
cursor = mydb.cursor()
# CREATE DB_BANK
cursor.execute("CREATE DATABASE IF NOT EXISTS db_bank")

# CREATE USER
cursor.execute(f"""CREATE USER IF NOT EXISTS 'u_bank_admin'@'localhost'
    IDENTIFIED BY '{db_password}'
""")
# GRANT PRIVILEGES
cursor.execute("""GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES
    ON db_bank.*
    TO 'u_bank_admin'@'localhost'
""")

# With an account management statement like GRANT,
# the database will reload the grant tables immediately
# into memory, meaning that the FLUSH PRIVILEGES command
# isn’t necessary in our case.
# On the other hand, running it won’t have any negative
# effect on the system.
cursor.execute("FLUSH PRIVILEGES")

# CLOSE CURSOR AND DB
cursor.close()
mydb.close()

#----------------------------------------#
# CONNECT TO DB 
mydb =mysql.connector.connect(
    host = "localhost",
    user = "u_bank_admin",
    password = f"{db_password}",
    database = "db_bank"
)
# CREATE CURSOR
cursor = mydb.cursor()

# CREATE TABLE USER
cursor.execute("""CREATE TABLE IF NOT EXISTS user(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    is_admin ENUM('True', 'False') DEFAULT 'False',
    firstname VARCHAR(70),
    lastname VARCHAR(70),
    email VARCHAR(70) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)""")

# CREATE TABLE BANK_ACCOUNT
cursor.execute("""CREATE TABLE IF NOT EXISTS bank_account(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    balance DECIMAL 
)""")

# CREATE TABLE USER_BANK_ACCOUNT
cursor.execute("""CREATE TABLE IF NOT EXISTS user_bank_account(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    bank_account_id INT NOT NULL,
    user_id INT NOT NULL 
)""")

# ADD FOREIGN KEY BANK_ACCOUNT_ID AND USER_ID
# IN USER_BANK_ACCOUNT
cursor.execute("""ALTER TABLE user_bank_account 
               ADD FOREIGN KEY (bank_account_id) 
               REFERENCES bank_account(id)""")
cursor.execute("""ALTER TABLE user_bank_account 
               ADD FOREIGN KEY (user_id) 
               REFERENCES user(id)""")

# CREATE TABLE TRANSACTION
cursor.execute("""CREATE TABLE IF NOT EXISTS transaction(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    type ENUM('withdraw','deposit','transfer'),
    date DATETIME,
    category VARCHAR(30),
    amount DECIMAL NOT NULL
)""")

# ADD FOREIGN KEY ACCOUNT_ID
cursor.execute("""ALTER TABLE transaction 
               ADD FOREIGN KEY (account_id) 
               REFERENCES bank_account(id)""")

cursor.execute("SHOW TABLES")
result = cursor.fetchall()

print(result)
cursor.close()
mydb.close()
