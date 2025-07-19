-- This SQL script creates the database hbtn_0d_usa if it doesn't already exist.
-- It then creates the table 'states' within hbtn_0d_usa if it doesn't already exist.

-- Create the database hbtn_0d_usa if it does not exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database for subsequent operations.
USE hbtn_0d_usa;

-- Create the table 'states' if it does not exist.
-- id: INT, unique, auto-generated, cannot be null, and is the primary key.
-- name: VARCHAR(256), cannot be null.
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

