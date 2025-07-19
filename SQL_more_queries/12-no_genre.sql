-- This SQL script lists all shows from the 'hbtn_0d_tvshows' database
-- that do NOT have any genre linked.
-- It displays the show's title and the associated genre's ID (which will be NULL).
-- Results are sorted in ascending order by show title and then by genre ID.
-- The database name (hbtn_0d_tvshows) will be passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0d_tvshows < 12-no_genre.sql
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE
    tv_show_genres.genre_id IS NULL
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;

