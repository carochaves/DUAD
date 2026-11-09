INSERT INTO users (name, email)
VALUES ('Ana Mora', 'ana@example.com')
RETURNING id, name;

INSERT INTO products (name, price, stock)
VALUES
    ('Cuaderno', 1500.00, 10),
    ('Lapicero', 500.00, 5)
RETURNING id, name, price, stock;

DO $$
DECLARE
    v_user_id INTEGER := 1;
	v_bill_id INTEGER;
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM users
        WHERE id = v_user_id
    ) THEN
        RAISE EXCEPTION 'El usuario con ID % no existe.', v_user_id;
    END IF;

	IF NOT EXISTS (
    SELECT 1
    FROM products
    WHERE id = 1 AND stock >= 2
) THEN
    RAISE EXCEPTION 'El cuaderno no existe o no tiene stock suficiente.';
END IF;

IF NOT EXISTS (
    SELECT 1
    FROM products
    WHERE id = 2 AND stock >= 3
) THEN
    RAISE EXCEPTION 'El lapicero no existe o no tiene stock suficiente.';
END IF;

RAISE NOTICE 'Hay stock suficiente para ambos productos.';

    RAISE NOTICE 'El usuario con ID % existe.', v_user_id;
	INSERT INTO bills (user_id, total)
VALUES (v_user_id, 4500.00)
RETURNING id INTO v_bill_id;
INSERT INTO bill_details (bill_id, product_id, quantity, unit_price)
VALUES
    (v_bill_id, 1, 2, 1500.00),
    (v_bill_id, 2, 3, 500.00);
	UPDATE products AS p
SET stock = p.stock - d.quantity
FROM bill_details AS d
WHERE d.bill_id = v_bill_id
  AND d.product_id = p.id;
END;
$$;
