-- This SQL script lists all shows contained in the database hbtn_0d_tvshows.
-- It displays the show's title and the associated genre's ID.
-- If a show does not have a genre, it displays NULL for genre_id.
-- Results are sorted in ascending order by show title and then by genre ID.
-- The database name (hbtn_0d_tvshows) will be passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0d_tvshows < 11-genre_id_all_shows.sql
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;

