CREATE TABLE
    IS601_ArtistAlbums(
        id int auto_increment PRIMARY KEY,
        artist_id INT not null,
        album_id INT not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY (artist_id, album_id),
        FOREIGN KEY (artist_id) REFERENCES IS601_Artists(id),
        FOREIGN KEY (album_id) REFERENCES IS601_Albums(id)
    );