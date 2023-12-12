CREATE TABLE
    IS601_Albums (
        id INT PRIMARY KEY AUTO_INCREMENT,
        album_id VARCHAR(50) UNIQUE NOT NULL,
        album_name VARCHAR(255) NOT NULL CHECK (album_name <> ''),
        album_popularity INT CHECK (album_popularity >= 0 AND album_popularity <= 100) DEFAULT 0,
        album_uri VARCHAR(100) CHECK (album_uri <> ''),
        album_img VARCHAR(255) CHECK (album_img <> ''),
        total_tracks INT CHECK (total_tracks >= 0),
        release_date DATE,
        label_name VARCHAR(255),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY (album_id)
    );