PRAGMA foreign_keys = ON;

CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    price NUMERIC NOT NULL CHECK (price >= 0),
    entry_date TEXT NOT NULL,
    brand TEXT NOT NULL,
    stock_available INTEGER NOT NULL
        CHECK (stock_available >= 0)
);

CREATE TABLE Invoices (
    id INTEGER PRIMARY KEY,
    invoice_number TEXT NOT NULL UNIQUE,
    purchase_date TEXT NOT NULL,
    buyer_email TEXT NOT NULL,
    total_amount NUMERIC NOT NULL CHECK (total_amount >= 0)
);

CREATE TABLE Products_Per_Invoice (
    id INTEGER PRIMARY KEY,
    invoice_number TEXT NOT NULL,
    product_code TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total_amount NUMERIC NOT NULL CHECK (total_amount >= 0),

    FOREIGN KEY (invoice_number)
        REFERENCES Invoices(invoice_number),

    FOREIGN KEY (product_code)
        REFERENCES Products(code)
);

CREATE TABLE Shopping_Cart (
    id INTEGER PRIMARY KEY,
    buyer_email TEXT NOT NULL
);

CREATE TABLE Products_Per_Cart (
    id INTEGER PRIMARY KEY,
    cart_id INTEGER NOT NULL,
    product_code TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),

    FOREIGN KEY (cart_id)
        REFERENCES Shopping_Cart(id),

    FOREIGN KEY (product_code)
        REFERENCES Products(code)
);

ALTER TABLE Invoices
ADD COLUMN buyer_phone TEXT;

ALTER TABLE Invoices
ADD COLUMN cashier_employee_code TEXT;

PRAGMA table_info(Invoices);

--Obtenga todos los productos almacenados
SELECT *
FROM Products;

--Obtenga todos los productos que tengan un precio mayor a 50000
SELECT *
FROM Products
WHERE price > 50000;

--Obtenga todas las compras de un mismo producto por id.
SELECT pi.*
FROM Products_Per_Invoice AS pi
JOIN Products AS p ON pi.product_code = p.code
WHERE p.id = 1;

--Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT
    p.id,
    p.code,
    p.name,
    SUM(pi.quantity) AS total_quantity
FROM Products_Per_Invoice AS pi
JOIN Products AS p ON pi.product_code = p.code
GROUP BY p.id, p.code, p.name;

--Obtenga todas las facturas realizadas por el mismo comprador
SELECT *
FROM Invoices
WHERE buyer_email = 'cliente@correo.com';

--Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT *
FROM Invoices
ORDER BY total_amount DESC;

--Obtenga una sola factura por número de factura.
SELECT *
FROM Invoices
WHERE invoice_number = 'FAC-001';