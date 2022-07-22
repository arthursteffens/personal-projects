-- Create a schema called realty

DROP SCHEMA IF EXISTS realty;

CREATE SCHEMA realty;

-- Use the new schema
USE realty;


-- Create table SALES
DROP TABLE IF EXISTS sales;

-- Create tables SALES
CREATE TABLE sales (
    property_id VARCHAR(12),
    prop_type VARCHAR(20),
    prop_status VARCHAR(20),
    price INT,
    baths INT,
    beds FLOAT,
    address_city VARCHAR(50),
    address_line VARCHAR(200),
    address_state_code CHAR(2),
    address_state VARCHAR(50),
    address_county VARCHAR(50),
    addres_lat DOUBLE,
    address_lon DOUBLE,
    address_neighborhood_name VARCHAR(50)
);


-- Create table RENTS
DROP TABLE IF EXISTS rents;

-- Create table RENTS
CREATE TABLE rents (
    property_id VARCHAR(12),
    prop_type VARCHAR(20),
    prop_status VARCHAR(20),
    year_built INT,
    address_city VARCHAR(50),
    address_line VARCHAR(200),
    address_state_code CHAR(2),
    address_state VARCHAR(50),
    address_county VARCHAR(50),
    address_lat DOUBLE,
    address_lon DOUBLE,
    address_neighborhood_name VARCHAR(50),
    community_price_max INT,
    community_price_min INT
);


-- Create table SOLD
DROP TABLE IF EXISTS sold;

-- Create table SOLD
CREATE TABLE sold (
    property_id VARCHAR(12),
    prop_type VARCHAR(20),
    prop_status VARCHAR(20),
    year_built INT,
    price INT,
    baths INT,
    beds FLOAT,
    address_city VARCHAR(50),
    address_line VARCHAR(200),
    address_state_code CHAR(2),
    address_state VARCHAR(50),
    address_county VARCHAR(50),
    address_lat DOUBLE,
    address_lon DOUBLE,
    address_neighborhood_name VARCHAR(50)
);