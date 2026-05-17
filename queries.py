
QUERY_TOP_ARTISTS_COUNT = """
SELECT 
    ar.Name AS artist,
    COUNT(t.TrackId) AS track_count
FROM artist ar
JOIN album al ON ar.ArtistId = al.ArtistId
JOIN track t ON al.AlbumId = t.AlbumId
GROUP BY ar.ArtistId
ORDER BY track_count DESC
LIMIT ?
"""

QUERY_TOP_ARTISTS_DURATION = """
SELECT 
    ar.Name AS artist,
    SUM(t.Milliseconds) / 60000.0 AS total_duration
FROM artist ar
JOIN album al ON ar.ArtistId = al.ArtistId
JOIN track t ON al.AlbumId = t.AlbumId
GROUP BY ar.ArtistId
ORDER BY total_duration DESC
LIMIT ?
"""

QUERY_TRACK_DETAILS = """
SELECT
    t.Name AS track,
    ar.Name AS artist,
    al.Title AS album,
    t.Milliseconds / 60000.0 AS minutes
FROM track t
JOIN album al ON t.AlbumId = al.AlbumId
JOIN artist ar ON al.ArtistId = ar.ArtistId
"""

QUERY_TRACK_LENGTH = """
SELECT
    t.Milliseconds / 60000.0 AS minutes
FROM track t
"""

QUERY_TOP_TRACKS_REVENUE = """
SELECT
    t.Name AS Name,
    SUM(il.UnitPrice * il.Quantity) AS revenue
FROM track t
JOIN invoice_line il ON t.TrackId = il.TrackId
GROUP BY t.TrackId
ORDER BY revenue DESC
LIMIT ?
"""