-- MySQL script for tracking D&D deaths
CREATE DATABASE IF NOT EXISTS dnd_deaths;
USE dnd_deaths;

CREATE TABLE IF NOT EXISTS deaths (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    race VARCHAR(100),
    class VARCHAR(100),
    cause_of_death TEXT NOT NULL,
    location VARCHAR(255),
    date_of_death DATE,
    notes TEXT,
    buried_in INT DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (buried_in) REFERENCES graveyard(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS graveyard (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    caretaker VARCHAR(255),
    established_year INT
);
