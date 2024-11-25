-- file: borneo-schema.sql
-- authors: Yug Patel
-- last modified: 12 Nov 2024

CREATE TABLE IF NOT EXISTS product(
    ID          VARCHAR(10),
    seller_ID   VARCHAR(10) NOT NULL,
    name        VARCHAR(50) NOT NULL,
    price       FLOAT(2) NOT NULL,
    stars       FLOAT(2),
    description VARCHAR(1000),
    PRIMARY KEY (ID),
    FOREIGN KEY (seller_ID) references seller(ID)
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS bought_by(
    product_ID      VARCHAR(10) NOT NULL,
    buyer_ID      VARCHAR(10) NOT NULL,
    FOREIGN KEY (buyer_ID) references buyer(ID)
        ON DELETE CASCADE,
    FOREIGN KEY (product_ID) references product(ID)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS seller(
    ID VARCHAR(10),
    name VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    stars FLOAT(2),
    phone_number VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(30) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL UNIQUE,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS seller_ph_numbers(
    ID VARCHAR(10),
    phone_number VARCHAR(12) NOT NULL UNIQUE,
    FOREIGN KEY (ID) references seller (ID)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS buyer(
    ID varchar(10),
    name VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(30) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL UNIQUE,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS buyer_ph_numbers(
    ID VARCHAR(10),
    phone_number VARCHAR(12) NOT NULL UNIQUE,
    FOREIGN KEY (ID) references buyer (ID)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS products_offered(
    seller_ID       VARCHAR(10),
    product_ID      VARCHAR(10),
    FOREIGN KEY (seller_ID) REFERENCES seller(ID)
        ON DELETE CASCADE,
    FOREIGN KEY (product_ID) REFERENCES product(ID)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS product_review(
    product_ID      VARCHAR(10),
    buyer_ID        VARCHAR(10),
    description     VARCHAR(5000),
    date_time       DATETIME,
    FOREIGN KEY (product_ID) REFERENCES product(ID)
        ON DELETE CASCADE,
    FOREIGN KEY (buyer_ID) REFERENCES buyer(ID)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS products_bought(
    product_ID      VARCHAR(10),
    buyer_ID        VARCHAR(10),
    product_name    VARCHAR(50) NOT NULL,
    date_time DATETIME,
    payment_method VARCHAR(30),
    FOREIGN KEY (product_ID) REFERENCES product(ID)
        ON DELETE SET NULL,
    FOREIGN KEY (buyer_ID) REFERENCES buyer(ID)
        ON DELETE SET NULL
);

