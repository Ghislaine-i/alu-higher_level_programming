-- This SQL script lists all records from the 'second_table' in the specified database.
-- It displays the score and name in that order and sorts the results by score in descending order (top first).
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0c_0 < 9-full_creation.sql
SELECT score, name
FROM second_table
ORDER BY score DESC;
