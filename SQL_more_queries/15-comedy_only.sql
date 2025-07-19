-- This SQL script lists all Comedy shows from the hbtn_0d_tvshows database.
-- It assumes there is only one genre with the name 'Comedy'.
-- Each record displays the show's title.
-- Results are sorted in ascending order by the show title.
-- The database name (hbtn_0d_tvshows) will be passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0d_tvshows < 15-comedy_shows.sql
SELECT
    tv_shows.title
FROM
    tv_shows
JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE
    tv_genres.name = 'Comedy'
ORDER BY
    tv_shows.title ASC;

