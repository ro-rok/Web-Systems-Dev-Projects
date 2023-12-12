CREATE TABLE
    IS601_TrackFeatures(
        id int auto_increment PRIMARY KEY,
        artist_id INT not null,
        track_id INT not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY (artist_id, track_id),
        FOREIGN KEY (artist_id) REFERENCES IS601_Artists(id),
        FOREIGN KEY (track_id) REFERENCES IS601_Tracks(id)
    );