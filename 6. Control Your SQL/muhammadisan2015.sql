SELECT albums.Title, artists.Name, tracks.Name track
FROM albums, artists, tracks
WHERE albums.ArtistId = artists.ArtistId
AND albums.AlbumId = tracks.AlbumId
AND (
		(
			artists.Name = 'AC/DC' 
			AND albums.Title = 'Let There Be Rock'
		)
		OR artists.Name = 'Aerosmith'
	);