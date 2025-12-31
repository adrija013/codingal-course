CREATE TABLE IF NOT EXISTS nomnoms (
 NAME TEXT,
 NEIGHBOURHOOD TEXT,
 CUISINE TEXT,
 REVIEW REAL,
 PRICE TEXT,
 HEALTH TEXT
 );

 INSERT INTO nomnoms (NAME, NEIGHBOURHOOD ,CUISINE ,REVIEW ,PRICE ,HEALTH) VALUES
('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
('Pocha', 'Midtown', 'Pizza', 4, '$$$', 'B'),
('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$$', 'A'),
('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');

SELECT * FROM nomnoms;

SELECT DISTINCT NEIGHBOURHOOD FROM nomnoms;

SELECT DISTINCT CUISINE FROM nomnoms;

SELECT * FROM nomnoms WHERE CUISINE = 'Chinese';

SELECT * FROM nomnoms WHERE REVIEW >= 4;

SELECT * FROM nomnoms WHERE CUISINE = 'Italian' AND PRICE = '$$$';

SELECT * FROM nomnoms WHERE NAME LIKE '%Candy%';

SELECT * FROM nomnoms
WHERE NEIGHBOURHOOD IN ('Midtown', 'Downtown','Chinatown');

SELECT * FROM nomnoms;
SELECT * FROM nomnoms ORDER BY REVIEW DESC LIMIT 4;

SELECT * FROM nomnoms;
SELECT * FROM nomnoms LIMIT 5 OFFSET 2; 



