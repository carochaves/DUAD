CREATE TABLE `Products`(
    `code` VARCHAR(50) NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `entry_date` DATE NOT NULL,
    `brand` VARCHAR(100) NOT NULL,
    `stock_available` INT NOT NULL,
    PRIMARY KEY(`code`)
);
CREATE TABLE `Invoices`(
    `invoice_number` VARCHAR(50) NOT NULL,
    `purchase_date` DATE NOT NULL,
    `buyer_email` VARCHAR(255) NOT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY(`invoice_number`)
);
CREATE TABLE `Products Per Invoice`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_number` VARCHAR(50) NOT NULL,
    `product_code` VARCHAR(50) NOT NULL,
    `quantity` INT NOT NULL,
    `total_amount` DECIMAL(10, 2) NOT NULL
);
CREATE TABLE `Shopping Cart`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` VARCHAR(255) NOT NULL
);
CREATE TABLE `Products_Per_Cart`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `cart_id` BIGINT NOT NULL,
    `product_code` VARCHAR(50) NOT NULL,
    `quantity` INT NOT NULL
);
ALTER TABLE
    `Products_Per_Cart` ADD CONSTRAINT `products_per_cart_cart_id_foreign` FOREIGN KEY(`cart_id`) REFERENCES `Shopping Cart`(`id`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_product_code_foreign` FOREIGN KEY(`product_code`) REFERENCES `Products`(`code`);
ALTER TABLE
    `Products_Per_Cart` ADD CONSTRAINT `products_per_cart_product_code_foreign` FOREIGN KEY(`product_code`) REFERENCES `Products`(`code`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice_number_foreign` FOREIGN KEY(`invoice_number`) REFERENCES `Invoices`(`invoice_number`);