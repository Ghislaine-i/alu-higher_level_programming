-- This SQL script lists all cities contained in the database hbtn_0d_usa.
-- Each record displays the city's ID, city's name, and the corresponding state's name.
-- Results are sorted in ascending order by cities.id.
-- The database name is passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0d_usa < 9-cities_by_state_join.sql
SELECT
    cities.id,
    cities.name,
    states.name
FROM
    cities
JOIN
    states ON cities.state_id = states.id
ORDER BY
    cities.id ASC;

