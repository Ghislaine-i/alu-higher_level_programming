-- This SQL script creates a table named 'id_not_null' in the current database.
-- The database name is expected to be passed as an argument to the mysql command.
-- For example: mysql -hlocalhost -uroot -p <database_name> < 3-id_not_null.sql
-- If 'id_not_null' already exists, the script will not fail due to IF NOT EXISTS.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
