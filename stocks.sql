-- Step 1: Create the database
CREATE DATABASE stocks;

-- Step 2: Use the new database
USE stock_management;

-- Step 3: Create the stocks table
CREATE TABLE stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
