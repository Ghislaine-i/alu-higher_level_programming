-- This SQL script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- It only displays genres that have at least one show linked.
-- The results are sorted in descending order by the number of shows.
-- The database name (hbtn_0d_tvshows) will be passed as an argument to the mysql command.
-- Example usage: mysql -hlocalhost -uroot -p hbtn_0d_tvshows < 13-count_shows_by_genre.sql
SELECT
    tv_genres.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM
    tv_genres
JOIN
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY
    tv_genres.name
ORDER BY
    number_of_shows DESC;

