USE db_bank;

-- 1. Insertion des Utilisateurs (10 utilisateurs)
INSERT INTO user (firstname, lastname, email, password, is_admin) VALUES
('Jean', 'Dupont', 'jean.dupont@email.com', 'hash_pass_1', 'False'),
('Marie', 'Curie', 'marie.curie@email.com', 'hash_pass_2', 'False'),
('Luc', 'Skywalker', 'luc.s@force.com', 'hash_pass_3', 'True'),
('Léa', 'Organa', 'lea.o@rebel.org', 'hash_pass_4', 'False'),
('Arthur', 'Pendragon', 'roi.arthur@kaamelott.fr', 'hash_pass_5', 'False'),
('Emma', 'Watson', 'emma.w@cinema.com', 'hash_pass_6', 'False'),
('Thomas', 'Shelby', 't.shelby@peaky.com', 'hash_pass_7', 'False'),
('Sarah', 'Connor', 's.connor@sky.net', 'hash_pass_8', 'False'),
('Bruce', 'Wayne', 'bruce@wayne-ent.com', 'hash_pass_9', 'True'),
('Diana', 'Prince', 'diana@themyscira.gov', 'hash_pass_10', 'False');

-- 2. Insertion des Comptes Bancaires (12 comptes pour varier les plaisirs)
INSERT INTO bank_account (balance) VALUES
(1500.50), (250.00), (50000.00), (10.00), (1200.00),
(3400.75), (890.00), (15000.00), (5.50), (1000000.00),
(450.00), (2200.00);

-- 3. Association User <-> Bank Account (Table de liaison)
-- Rappel des contraintes : 1-3 comptes par user / 1-2 users par compte
INSERT INTO user_bank_account (user_id, bank_account_id) VALUES
-- Jean a 2 comptes (un perso, un joint avec Marie)
(1, 1), (1, 2), 
-- Marie partage le compte 2 et en a un autre
(2, 2), (2, 3),
-- Luc a 1 compte
(3, 4),
-- Léa partage le compte 4 avec Luc et a son propre compte
(4, 4), (4, 5),
-- Arthur a 3 comptes
(5, 6), (5, 7), (5, 8),
-- Emma a 1 compte
(6, 9),
-- Thomas a 2 comptes
(7, 10), (7, 11),
-- Sarah a 1 compte
(8, 11), -- Compte partagé avec Thomas
-- Bruce a 2 comptes
(9, 10), -- Compte partagé avec Thomas (business !)
(9, 12),
-- Diana a 1 compte
(10, 12); -- Compte partagé avec Bruce


-- 1. Dépôts (Salaires et revenus) - 20 transactions
INSERT INTO transaction (account_id, type, date, category, amount) VALUES
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
(4, 'deposit', '2023-11-05 12:00:00', 'Refund', 30.00);

-- 2. Retraits (Dépenses courantes) - 60 transactions
INSERT INTO transaction (account_id, type, date, category, amount) VALUES
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
-- ... (Ajout de répétitions pour atteindre 60)
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
(6, 'withdraw', '2023-11-20 08:00:00', 'Groceries', -75.00);

-- 3. Transferts (Paires équilibrées) - 10 paires (20 transactions)
-- Transfert 1: Compte 1 vers Compte 2 (500€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (1, 'transfer', '2023-10-05 10:00:00', 'Internal', -500.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (2, 'transfer', '2023-10-05 10:00:00', 'Internal', 500.00);

-- Transfert 2: Compte 3 vers Compte 4 (200€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (3, 'transfer', '2023-10-08 14:30:00', 'Savings', -200.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (4, 'transfer', '2023-10-08 14:30:00', 'Savings', 200.00);

-- Transfert 3: Compte 10 vers Compte 9 (1000€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (10, 'transfer', '2023-10-12 09:00:00', 'Investment', -1000.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (9, 'transfer', '2023-10-12 09:00:00', 'Investment', 1000.00);

-- Transfert 4: Compte 7 vers Compte 8 (300€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (7, 'transfer', '2023-10-15 16:00:00', 'Help', -300.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (8, 'transfer', '2023-10-15 16:00:00', 'Help', 300.00);

-- Transfert 5: Compte 5 vers Compte 12 (150€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (5, 'transfer', '2023-10-20 11:00:00', 'Shared Bills', -150.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (12, 'transfer', '2023-10-20 11:00:00', 'Shared Bills', 150.00);

-- Transfert 6: Compte 1 vers Compte 3 (100€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (1, 'transfer', '2023-11-05 10:00:00', 'Pocket Money', -100.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (3, 'transfer', '2023-11-05 10:00:00', 'Pocket Money', 100.00);

-- Transfert 7: Compte 9 vers Compte 10 (2500€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (9, 'transfer', '2023-11-07 14:00:00', 'Business', -2500.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (10, 'transfer', '2023-11-07 14:00:00', 'Business', 2500.00);

-- Transfert 8: Compte 6 vers Compte 5 (400€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (6, 'transfer', '2023-11-10 09:30:00', 'Rent Share', -400.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (5, 'transfer', '2023-11-10 09:30:00', 'Rent Share', 400.00);

-- Transfert 9: Compte 11 vers Compte 12 (50€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (11, 'transfer', '2023-11-12 15:45:00', 'Gift', -50.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (12, 'transfer', '2023-11-12 15:45:00', 'Gift', 50.00);

-- Transfert 10: Compte 2 vers Compte 1 (200€)
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (2, 'transfer', '2023-11-15 10:00:00', 'Reimbursement', -200.00);
INSERT INTO transaction (account_id, type, date, category, amount) VALUES (1, 'transfer', '2023-11-15 10:00:00', 'Reimbursement', 200.00);