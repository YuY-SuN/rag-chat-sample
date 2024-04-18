-- user テーブルの作成
CREATE TABLE user (
    id TEXT PRIMARY KEY
);

-- history テーブルの作成
CREATE TABLE history (
    userid TEXT,
    talkid TEXT,
    talknum INTEGER,
    text TEXT,
    PRIMARY KEY (userid, talkid),
    FOREIGN KEY (userid) REFERENCES user(id)
);

