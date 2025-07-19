-- This SQL script creates a table named 'unique_id' in the current database.
-- The database name is expected to be passed as an argument to the mysql command.
-- For example: mysql -hlocalhost -uroot -p <database_name> < 4-unique_id.sql
-- If 'unique_id' already exists, the script will not fail due to IF NOT EXISTS.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
