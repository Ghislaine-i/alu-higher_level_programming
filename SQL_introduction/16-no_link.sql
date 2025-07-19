-- This SQL script lists all records from the 'second_table' that have a name value.
-- It displays the score and name in that order.
-- Records are listed by descending score.
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0c_0 < 100-move_to_top.sql
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
