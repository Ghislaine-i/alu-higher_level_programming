-- This SQL script displays the number of records with id = 89 in the 'first_table'.
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0c_0 < 101-safely_divide_by_0.sql
SELECT COUNT(*)
FROM first_table
WHERE id = 89;
