-- This SQL script lists all shows and their linked genres from the hbtn_0d_tvshows database.
-- If a show does not have a genre, it displays NULL in the genre column.
-- Each record displays the show's title and the genre's name.
-- Results are sorted in ascending order by show title and then by genre name.
-- The database name (hbtn_0d_tvshows) will be passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0d_tvshows < 16-shows_by_genre.sql
SELECT
    tv_shows.title,
    tv_genres.name
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY
    tv_shows.title ASC,
    tv_genres.name ASC;

