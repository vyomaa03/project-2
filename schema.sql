DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS locations;
CREATE TABLE users(id SERIAL PRIMARY KEY, email TEXT, name TEXT, password_hash TEXT);
CREATE TABLE locations(id SERIAL PRIMARY KEY, email TEXT, name TEXT, latitude INTEGER, longitude INTEGER);