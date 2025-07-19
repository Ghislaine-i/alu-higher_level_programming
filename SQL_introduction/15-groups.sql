-- This SQL script lists the number of records for each unique score in 'second_table'.
-- It displays the score and the count of records for that score, labeled as 'number'.
-- The results are sorted by the 'number' of records in descending order.
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0c_0 < 14-group_by_score.sql
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
