CREATE TABLE
    IS601_TrackPlaylist(
        id int auto_increment PRIMARY KEY,
        user_id INT not null,
        track_id INT not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY (user_id, track_id),
        FOREIGN KEY(user_id) REFERENCES IS601_Users(id),
        FOREIGN KEY (track_id) REFERENCES IS601_Tracks(id)
    );
    