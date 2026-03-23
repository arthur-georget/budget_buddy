import mysql.connector
import os
import bcrypt
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
cursor.execute("""GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, TRIGGER, REFERENCES
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

######################
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
# CREATE TABLE TRANSACTION
cursor.execute("""CREATE TABLE IF NOT EXISTS transaction(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    type ENUM('withdraw','deposit','transfer'),
    date DATETIME,
    category VARCHAR(30),
    amount DECIMAL NOT NULL
)""")

cursor.execute("SHOW TABLES")
result = cursor.fetchall()

test_1 = 'hash_pass_1'
test_2 = 'hash_pass_2'
test_3 = 'hash_pass_3'
test_4 = 'hash_pass_4'
test_5 = 'hash_pass_5'
test_6 = 'hash_pass_6'
test_7 = 'hash_pass_7'
test_8 = 'hash_pass_8'
test_9 = 'hash_pass_9'
test_10 = 'hash_pass_10'

test_1 = bcrypt.hashpw(test_1.encode(), bcrypt.gensalt())
test_2 = bcrypt.hashpw(test_2.encode(), bcrypt.gensalt())
test_3 = bcrypt.hashpw(test_3.encode(), bcrypt.gensalt())
test_4 = bcrypt.hashpw(test_4.encode(), bcrypt.gensalt())
test_5 = bcrypt.hashpw(test_5.encode(), bcrypt.gensalt())
test_6 = bcrypt.hashpw(test_6.encode(), bcrypt.gensalt())
test_7 = bcrypt.hashpw(test_7.encode(), bcrypt.gensalt())
test_8 = bcrypt.hashpw(test_8.encode(), bcrypt.gensalt())
test_9 = bcrypt.hashpw(test_9.encode(), bcrypt.gensalt())
test_10= bcrypt.hashpw(test_10.encode(), bcrypt.gensalt())

sql = ("""INSERT INTO user (firstname, lastname, email, password, is_admin) VALUES
                ('Jean', 'Dupont', 'jean.dupont@email.com',        %s, 'False'),
                ('Marie', 'Curie', 'marie.curie@email.com',        %s, 'False'),
                ('Luc', 'Skywalker', 'luc.s@force.com',            %s, 'True'),
                ('Léa', 'Organa', 'lea.o@rebel.org',               %s, 'False'),
                ('Arthur', 'Pendragon', 'roi.arthur@kaamelott.fr', %s, 'False'),
                ('Emma', 'Watson', 'emma.w@cinema.com',            %s, 'False'),
                ('Thomas', 'Shelby', 't.shelby@peaky.com',         %s, 'False'),
                ('Sarah', 'Connor', 's.connor@sky.net',            %s, 'False'),
                ('Bruce', 'Wayne', 'bruce@wayne-ent.com',          %s, 'True'),
                ('Diana', 'Prince', 'diana@themyscira.gov',        %s, 'False')
               """)
cursor.execute(sql,(test_1, test_2, test_3, test_4, test_5, test_6, test_7, test_8, test_9, test_10))
mydb.commit()
# BANK ACCOUNT
cursor.execute("""INSERT INTO bank_account (balance) VALUES
(1500.50), (250.00), (50000.00), (10.00), (1200.00),
(3400.75), (890.00), (15000.00), (5.50), (1000000.00),
(450.00), (2200.00)""")
mydb.commit()
#
cursor.execute("""INSERT INTO user_bank_account (user_id, bank_account_id) VALUES
(1, 1), (1, 2), 
(2, 2), (2, 3),
(3, 4),
(4, 4), (4, 5),
(5, 6), (5, 7), (5, 8),
(6, 9),
(7, 10), (7, 11),
(8, 11),
(9, 10),(9, 12),
(10, 12)""")
mydb.commit()

# DEPOSIT
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES
(1, 'deposit', '2023-10-01 09:00:00', 'Salary', 2500.00),
(2, 'deposit', '2023-10-01 10:30:00', 'Salary', 1800.00),
(3, 'deposit', '2023-10-02 08:15:00', 'Dividend', 500.00),
(4, 'deposit', '2023-10-05 12:00:00', 'Refund', 45.50),
(5, 'deposit', '2023-10-01 09:00:00', 'Salary', 3200.00),
(6, 'deposit', '2023-10-01 09:00:00', 'Salary', 2100.00),
(7, 'deposit', '2023-10-01 09:00:00', 'Salary', 2800.00),
(8, 'deposit', '2023-10-10 14:00:00', 'Gift', 150.00),
(9, 'deposit', '2023-10-01 09:00:00', 'Salary', 4500.00),
(10, 'deposit', '2023-10-01 09:00:00', 'Salary', 12000.00),
(11, 'deposit', '2023-10-01 09:00:00', 'Salary', 1900.00),
(12, 'deposit', '2023-10-01 09:00:00', 'Salary', 3000.00),
(1, 'deposit', '2023-10-15 11:00:00', 'Selling', 120.00),
(3, 'deposit', '2023-10-20 10:00:00', 'Bonus', 1000.00),
(5, 'deposit', '2023-10-25 16:30:00', 'Refund', 22.00),
(7, 'deposit', '2023-11-01 09:00:00', 'Salary', 2800.00),
(9, 'deposit', '2023-11-01 09:00:00', 'Salary', 4500.00),
(10, 'deposit', '2023-11-01 09:00:00', 'Salary', 12000.00),
(2, 'deposit', '2023-11-01 10:30:00', 'Salary', 1800.00),
(4, 'deposit', '2023-11-05 12:00:00', 'Refund', 30.00)""")
mydb.commit()
# WITHDRAW
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES
(1, 'withdraw', '2023-10-02 14:20:00', 'Shopping', -55.30),
(1, 'withdraw', '2023-10-03 19:45:00', 'Restaurant', -42.00),
(1, 'withdraw', '2023-10-05 08:10:00', 'Refuel', -65.00),
(2, 'withdraw', '2023-10-02 12:00:00', 'Rent', -850.00),
(2, 'withdraw', '2023-10-10 15:30:00', 'Groceries', -120.45),
(3, 'withdraw', '2023-10-04 10:00:00', 'Leisure', -200.00),
(3, 'withdraw', '2023-10-12 18:00:00', 'Shopping', -350.00),
(4, 'withdraw', '2023-10-02 09:00:00', 'Rent', -600.00),
(4, 'withdraw', '2023-10-06 20:00:00', 'Restaurant', -35.00),
(5, 'withdraw', '2023-10-03 14:00:00', 'Shopping', -110.00),
(5, 'withdraw', '2023-10-15 10:00:00', 'Refuel', -70.00),
(5, 'withdraw', '2023-10-20 12:00:00', 'Groceries', -95.00),
(6, 'withdraw', '2023-10-02 08:30:00', 'Rent', -750.00),
(6, 'withdraw', '2023-10-05 17:00:00', 'Shopping', -45.99),
(7, 'withdraw', '2023-10-03 11:00:00', 'Groceries', -150.00),
(7, 'withdraw', '2023-10-08 21:00:00', 'Restaurant', -80.00),
(8, 'withdraw', '2023-10-15 09:00:00', 'Refuel', -55.00),
(9, 'withdraw', '2023-10-05 14:00:00', 'Investment', -2000.00),
(10, 'withdraw', '2023-10-10 10:00:00', 'Luxury', -5000.00),
(10, 'withdraw', '2023-10-20 15:00:00', 'Travel', -1200.00),
(11, 'withdraw', '2023-10-02 10:00:00', 'Rent', -700.00),
(12, 'withdraw', '2023-10-05 11:00:00', 'Shopping', -85.00),
(1, 'withdraw', '2023-10-20 18:30:00', 'Leisure', -30.00),
(2, 'withdraw', '2023-10-25 14:20:00', 'Groceries', -65.00),
(4, 'withdraw', '2023-10-28 09:15:00', 'Refuel', -40.00),
(5, 'withdraw', '2023-10-30 20:00:00', 'Restaurant', -120.00),
(7, 'withdraw', '2023-11-02 10:00:00', 'Rent', -900.00),
(9, 'withdraw', '2023-11-03 15:00:00', 'Shopping', -250.00),
(10, 'withdraw', '2023-11-04 12:00:00', 'Groceries', -400.00),
(3, 'withdraw', '2023-11-05 14:00:00', 'Refuel', -80.00),
# ... (Ajout de répétitions pour atteindre 60)
(1, 'withdraw', '2023-11-06 08:00:00', 'Coffee', -4.50),
(2, 'withdraw', '2023-11-06 12:30:00', 'Lunch', -15.00),
(3, 'withdraw', '2023-11-07 10:00:00', 'Online Store', -120.00),
(4, 'withdraw', '2023-11-07 16:45:00', 'Parking', -10.00),
(5, 'withdraw', '2023-11-08 19:00:00', 'Cinema', -25.00),
(6, 'withdraw', '2023-11-08 09:00:00', 'Gym', -40.00),
(7, 'withdraw', '2023-11-09 11:30:00', 'Groceries', -88.00),
(8, 'withdraw', '2023-11-09 15:00:00', 'Medical', -50.00),
(9, 'withdraw', '2023-11-10 13:00:00', 'Subscription', -15.99),
(10, 'withdraw', '2023-11-10 20:00:00', 'Restaurant', -250.00),
(11, 'withdraw', '2023-11-11 10:00:00', 'Groceries', -110.00),
(12, 'withdraw', '2023-11-11 14:00:00', 'Leisure', -60.00),
(1, 'withdraw', '2023-11-12 09:00:00', 'Refuel', -70.00),
(2, 'withdraw', '2023-11-12 17:00:00', 'Shopping', -45.00),
(3, 'withdraw', '2023-11-13 18:00:00', 'Restaurant', -65.00),
(4, 'withdraw', '2023-11-13 12:00:00', 'Lunch', -12.50),
(5, 'withdraw', '2023-11-14 08:30:00', 'Groceries', -40.00),
(6, 'withdraw', '2023-11-14 15:00:00', 'Shopping', -32.00),
(7, 'withdraw', '2023-11-15 19:30:00', 'Leisure', -15.00),
(8, 'withdraw', '2023-11-15 10:00:00', 'Refuel', -55.00),
(9, 'withdraw', '2023-11-16 11:00:00', 'Pharmacy', -22.50),
(10, 'withdraw', '2023-11-16 14:00:00', 'Charity', -100.00),
(11, 'withdraw', '2023-11-17 09:00:00', 'Coffee', -5.00),
(12, 'withdraw', '2023-11-17 12:30:00', 'Lunch', -18.00),
(1, 'withdraw', '2023-11-18 10:00:00', 'Groceries', -130.00),
(2, 'withdraw', '2023-11-18 16:00:00', 'Shopping', -90.00),
(3, 'withdraw', '2023-11-19 19:00:00', 'Restaurant', -45.00),
(4, 'withdraw', '2023-11-19 11:00:00', 'Refuel', -60.00),
(5, 'withdraw', '2023-11-20 15:00:00', 'Shopping', -25.00),
(6, 'withdraw', '2023-11-20 08:00:00', 'Groceries', -75.00)""")
mydb.commit()
# TRANSFERS
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (1, 'transfer', '2023-10-05 10:00:00', 'Internal', -500.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (2, 'transfer', '2023-10-05 10:00:00', 'Internal', 500.00)""")
mydb.commit()

cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (3, 'transfer', '2023-10-08 14:30:00', 'Savings', -200.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (4, 'transfer', '2023-10-08 14:30:00', 'Savings', 200.00)""")
mydb.commit()

cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (10, 'transfer', '2023-10-12 09:00:00', 'Investment', -1000.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (9, 'transfer', '2023-10-12 09:00:00', 'Investment', 1000.00)""")
mydb.commit()

cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (7, 'transfer', '2023-10-15 16:00:00', 'Help', -300.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (8, 'transfer', '2023-10-15 16:00:00', 'Help', 300.00)""")
mydb.commit()

cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (5, 'transfer', '2023-10-20 11:00:00', 'Shared Bills', -150.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (12, 'transfer', '2023-10-20 11:00:00', 'Shared Bills', 150.00)""")
mydb.commit()

cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (1, 'transfer', '2023-11-05 10:00:00', 'Pocket Money', -100.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (3, 'transfer', '2023-11-05 10:00:00', 'Pocket Money', 100.00)""")
mydb.commit()

cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (9, 'transfer', '2023-11-07 14:00:00', 'Business', -2500.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (10, 'transfer', '2023-11-07 14:00:00', 'Business', 2500.00)""")
mydb.commit()

cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (6, 'transfer', '2023-11-10 09:30:00', 'Rent Share', -400.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (5, 'transfer', '2023-11-10 09:30:00', 'Rent Share', 400.00)""")
mydb.commit()

cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (11, 'transfer', '2023-11-12 15:45:00', 'Gift', -50.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (12, 'transfer', '2023-11-12 15:45:00', 'Gift', 50.00)""")
mydb.commit()

cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (2, 'transfer', '2023-11-15 10:00:00', 'Reimbursement', -200.00)""")
mydb.commit()
cursor.execute("""INSERT INTO transaction (account_id, type, date, category, amount) VALUES (1, 'transfer', '2023-11-15 10:00:00', 'Reimbursement', 200.00)""")
mydb.commit()

# ADD FOREIGN KEY BANK_ACCOUNT_ID AND USER_ID
# IN USER_BANK_ACCOUNT
cursor.execute("""ALTER TABLE user_bank_account 
               ADD FOREIGN KEY (bank_account_id) 
               REFERENCES bank_account(id)""")
cursor.execute("""ALTER TABLE user_bank_account 
               ADD FOREIGN KEY (user_id) 
               REFERENCES user(id)""")


# ADD FOREIGN KEY ACCOUNT_ID
cursor.execute("""ALTER TABLE transaction 
               ADD FOREIGN KEY (account_id) 
               REFERENCES bank_account(id)""")

#ALTER TABLE user_bank_account
#DROP FOREIGN KEY user_bank_account_ibfk_2;
#
#ALTER TABLE user_bank_account
#ADD CONSTRAINT user_bank_account_ibfk_2
#    FOREIGN KEY (user_id)
#    REFERENCES user(id)
#    ON DELETE CASCADE;
#
#
#-- TRANSACTION TABLE
#ALTER TABLE transaction
#DROP FOREIGN KEY transaction_ibfk_1;
#
#ALTER TABLE transaction
#ADD CONSTRAINT transaction_ibfk_1
#    FOREIGN KEY (account_id)
#    REFERENCES bank_account(id)
#    ON DELETE CASCADE;
#
#-- TRIGGER SQL
#
#CREATE TRIGGER delete_orphan_accounts
#AFTER DELETE ON user_bank_account
#FOR EACH ROW
#BEGIN
#    -- Check if account had user
#    IF (SELECT COUNT(*) 
#        FROM user_bank_account
#        WHERE bank_account_id = OLD.bank_account_id) = 0 THEN
#        
#        -- Suppr orphan account
#        DELETE FROM bank_account
#        WHERE id = OLD.bank_account_id;
#    END IF;
#END

cursor.close()
mydb.close()
