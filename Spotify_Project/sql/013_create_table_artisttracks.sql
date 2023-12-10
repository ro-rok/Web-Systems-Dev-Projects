CREATE TABLE
    IS601_ArtistTracks(
        id int auto_increment PRIMARY KEY,
        artist_id VARCHAR(60) not null,
        track_id VARCHAR(60) not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY (artist_id, track_id),
        FOREIGN KEY (artist_id) REFERENCES IS601_Artists(artist_id),
        FOREIGN KEY (track_id) REFERENCES IS601_Tracks(track_id)
    );