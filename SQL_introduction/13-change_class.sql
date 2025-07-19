-- This SQL script removes all records from the 'second_table' where the score is 5 or less.
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0c_0 < 12-no_cheating.sql
DELETE FROM second_table
WHERE score <= 5;

