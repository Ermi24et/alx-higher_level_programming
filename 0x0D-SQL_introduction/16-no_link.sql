-- a script that lists all records of the second_table
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
