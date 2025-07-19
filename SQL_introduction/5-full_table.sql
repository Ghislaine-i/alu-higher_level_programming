-- This SQL script prints the full description of the table 'first_table'
-- from the database specified as an argument to the mysql command.
-- It queries the information_schema to retrieve column details.
--
-- Example usage:
-- mysql -hlocalhost -uroot -p hbtn_0c_0 < 5-full_table.sql
SELECT
    COLUMN_NAME AS Field,
    COLUMN_TYPE AS Type,
    IS_NULLABLE AS Null,
    COLUMN_KEY AS Key,
    COLUMN_DEFAULT AS Default,
    EXTRA AS Extra
FROM
    information_schema.COLUMNS
WHERE
    TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';
