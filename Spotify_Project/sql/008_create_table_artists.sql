CREATE TABLE
    IS601_Artists (
        id INT PRIMARY KEY AUTO_INCREMENT,
        artist_id VARCHAR(50) UNIQUE NOT NULL,
        artist_name VARCHAR(255) NOT NULL CHECK (artist_name <> ''),
        artist_popularity INT CHECK (artist_popularity >= 0 AND artist_popularity <= 100) DEFAULT 0,
        followers_total INT CHECK (followers_total >= 0),
        artist_uri VARCHAR(100) CHECK (artist_uri <> ''),
        artist_img VARCHAR(255) CHECK (artist_img <> ''),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY (artist_id)
    );