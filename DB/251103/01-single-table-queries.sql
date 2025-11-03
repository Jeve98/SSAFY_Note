-- 01. Querying data
SELECT LastName
FROM employees;

SELECT LastName, FirstName
FROM employees;

SELECT *
FROM employees;

SELECT FirstName AS '이름'
FROM employees;

SELECT Name, Milliseconds / 60000 AS '재생시간'
FROM tracks;

-- 02. Sorting data
SELECT FirstName
From employees
ORDER BY FirstName ASC;

SELECT Country, City
From customers
ORDER BY Country DESC, City ASC;

SELECT Name, Milliseconds / 60000 AS '재생시간'
FROM tracks
ORDER BY "Milliseconds" DESC;

-- NULL 정렬 예시
SELECT ReportsTo
FROM employees
ORDER BY "ReportsTo";

-- 03. Filtering data
SELECT DISTINCT Country, City
FROM customers
ORDER BY "Country" ASC;

SELECT LastName, FirstName, City
FROM customers
WHERE City = 'Prague';

SELECT LastName, FirstName, City
FROM customers
WHERE City != 'Prague';

SELECT LastName, FirstName, Company, Country
FROM customers
WHERE Company IS Null AND Country = 'USA';

SELECT LastName, FirstName, Company, Country
FROM customers
WHERE Company IS Null OR Country = 'USA';

SELECT Name, Bytes
FROM tracks
WHERE Bytes BETWEEN 10000 AND 500000
-- WHERE 10000 <= Bytes and Bytes <= 500000
ORDER BY "Bytes" ASC;

SELECT LastName, FirstName, Country
FROM customers
WHERE Country IN ('Canada', 'Germany', 'France');
-- WHERE Country = 'Canada' OR Country = 'Germany' OR Country = 'France'

SELECT LastName, FirstName, Country
FROM customers
WHERE Country NOT IN ('Canada', 'Germany', 'France');

SELECT LastName, FirstName
FROM customers
WHERE LastName LIKE '%son';

SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY "Bytes" DESC
-- LIMIT 7;
LIMIT 1, 7;
-- LIMIT 7 OFFSET 1;

-- 04. Grouping data
SELECT Country
FROM customers
GROUP BY "Country";

SELECT Country, COUNT(*)
FROM customers
GROUP BY "Country";

SELECT Composer, AVG(Bytes) AS avgByte
FROM tracks
GROUP BY "Composer"
ORDER BY avgByte DESC;