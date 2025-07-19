-- This SQL script creates the MySQL server user 'user_0d_1'.
-- The user will have all privileges on the MySQL server.
-- The password for 'user_0d_1' will be 'user_0d_1_pwd'.
-- If the user 'user_0d_1' already exists, the script will not fail
-- due to the 'IF NOT EXISTS' clause in the CREATE USER statement.

-- Create the user if they do not already exist.
-- 'IDENTIFIED BY' sets the password for the user.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and all tables (*.*)
-- to the newly created or existing user 'user_0d_1' when connecting from 'localhost'.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Reload the grant tables to ensure that the new privileges take effect immediately.
FLUSH PRIVILEGES;
