-- This SQL script updates the score of the record where the name is 'Bob' to 10
-- in the 'second_table' of the specified database.
-- It specifically uses the 'name' field for identification, as required.
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0c_0 < 11-update_bob_score.sql
UPDATE second_table
SET score = 10
WHERE name = 'Bob';

