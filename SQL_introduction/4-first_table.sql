-- This SQL script creates a table named 'first_table' in the current database.
-- The database name is expected to be passed as an argument to the mysql command.
-- For example: mysql -hlocalhost -uroot -p <database_name> < 4-first_table.sql
-- If 'first_table' already exists, the script will not fail due to IF NOT EXISTS.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
