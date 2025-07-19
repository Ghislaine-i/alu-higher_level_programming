-- This SQL script lists all cities of California from the database hbtn_0d_usa.
-- It assumes the 'states' table contains a record where name = 'California'.
-- Results are sorted in ascending order by cities.id.
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0d_usa < 8-cities_of_california.sql

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

