-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
INNER JOIN tv_shows_genres
ON tv_shows.id = tv_shows_genres.show id
ORDER BY tv_shows.title ASC, tv_shows genres.genre_id ASC;