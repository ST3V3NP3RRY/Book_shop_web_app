DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS author;


CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    title VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    isbn INT,
    author_id INT NOT NULL REFERENCES author(id)
);