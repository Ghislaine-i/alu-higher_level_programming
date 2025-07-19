-- This SQL script creates the MySQL server user 'user_0d_1'.
-- The user will have all privileges on the MySQL server.
-- The password for 'user_0d_1' will be 'user_0d_1_pwd'.
-- If the user already exists, the script will not fail due to the IF NOT EXISTS clause.

-- Create the user if they don't already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply the privilege changes.
FLUSH PRIVILEGES;
