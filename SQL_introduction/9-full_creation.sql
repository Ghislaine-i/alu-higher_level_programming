-- This SQL script creates a table named 'second_table' in the current database
-- and inserts multiple rows into it.
-- The database name is expected to be passed as an argument to the mysql command.
-- For example: mysql -hlocalhost -uroot -p hbtn_0c_0 < 8-create_second_table.sql

-- Create the table if it does not already exist.
-- The IF NOT EXISTS clause prevents the script from failing if the table exists.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert the specified records into the 'second_table'.
-- Using multiple VALUES clauses in a single INSERT statement for efficiency.
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
