CREATE TABLE
    IS601_ArtistGenres(
        id int auto_increment PRIMARY KEY,
        artist_id INT not null,
        genre_id INT not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY (artist_id, genre_id),
        FOREIGN KEY (artist_id) REFERENCES IS601_Artists(id),
        FOREIGN KEY (genre_id) REFERENCES IS601_Genres(id) 
    );