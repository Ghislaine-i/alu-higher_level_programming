-- This SQL script creates the database hbtn_0d_usa if it doesn't already exist.
-- It then creates the table 'cities' within hbtn_0d_usa if it doesn't already exist.

-- Create the database hbtn_0d_usa if it does not exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database for subsequent operations.
USE hbtn_0d_usa;

-- Create the table 'cities' if it does not exist.
-- id: INT, unique, auto-generated, cannot be null, and is the primary key.
-- state_id: INT, cannot be null, and is a FOREIGN KEY referencing the 'id' of the 'states' table.
-- name: VARCHAR(256), cannot be null.
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
