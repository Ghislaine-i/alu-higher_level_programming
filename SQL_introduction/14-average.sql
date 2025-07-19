-- This SQL script computes the average score of all records in the 'second_table'.
-- The result column is aliased as 'average'.
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0c_0 < 13-average_score.sql
SELECT AVG(score) AS average
FROM second_table;
