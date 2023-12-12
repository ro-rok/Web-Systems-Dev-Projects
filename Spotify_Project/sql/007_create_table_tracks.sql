CREATE TABLE
    IS601_Tracks (
        id INT PRIMARY KEY AUTO_INCREMENT,
        track_id VARCHAR(50) UNIQUE NOT NULL,
        album_id VARCHAR(50) NOT NULL,
        track_name VARCHAR(255) NOT NULL CHECK (track_name <> ''),
        track_popularity INT CHECK (track_popularity >= 0 AND track_popularity <= 100) DEFAULT 0,
        preview_url VARCHAR(255) CHECK (preview_url <> ''),
        track_number INT CHECK (track_number >= 0),
        track_uri VARCHAR(100) CHECK (track_uri <> ''),
        track_img VARCHAR(255) CHECK (track_img <> ''),
        duration_ms INT CHECK (duration_ms >= 0),
        is_explicit BOOLEAN DEFAULT FALSE,
        release_date DATE,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (album_id) REFERENCES IS601_Albums(album_id),
        UNIQUE KEY (track_id)
    );