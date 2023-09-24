CREATE DATABASE web_scraping_db;

GRANT ALL PRIVILEGES ON DATABASE web_scraping_db TO postgres;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS supercasa_house(
    HouseID uuid NOT NULL DEFAULT gen_random_uuid(),
    Link VARCHAR(255),
    Title VARCHAR(255),
    Price VARCHAR(255),
    HouseLocation VARCHAR(255),
    Features TEXT,
    Highlights TEXT,
    DescriptionText TEXT
);

