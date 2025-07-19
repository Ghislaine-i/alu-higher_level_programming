-- This SQL script lists all records from the 'second_table' where the score is 10 or greater.
-- It displays the score and name in that order and sorts the results by score in descending order (top first).
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0c_0 < 10-top_score.sql
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

