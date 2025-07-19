-- This SQL script lists all genres of the show 'Dexter' from the hbtn_0d_tvshows database.
-- It assumes there is only one show with the title 'Dexter'.
-- Results are sorted in ascending order by genre name.
-- The database name (hbtn_0d_tvshows) will be passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0d_tvshows < 14-genres_of_dexter.sql
SELECT
    tv_genres.name
FROM
    tv_genres
JOIN
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN
    tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE
    tv_shows.title = 'Dexter'
ORDER BY
    tv_genres.name ASC;

