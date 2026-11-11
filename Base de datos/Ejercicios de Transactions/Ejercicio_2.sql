DO $$
DECLARE
    v_user_id INTEGER := 1;
    v_bill_id INTEGER;
    v_item RECORD;
    v_stock INTEGER;
    v_unit_price NUMERIC(10, 2);
    v_total NUMERIC := 0;
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM users
        WHERE id = v_user_id
    ) THEN
        RAISE EXCEPTION 'El usuario con ID % no existe.', v_user_id;
    END IF;

    -- Crear la factura para poder asociarle los detalles.
    INSERT INTO bills (user_id, total)
    VALUES (v_user_id, 0)
    RETURNING id INTO v_bill_id;

    -- Cada par representa (ID del producto, cantidad).
    FOR v_item IN
        SELECT cart.product_id, cart.quantity
        FROM (VALUES
            (1, 2),  -- 2 cuadernos
            (2, 3)   -- 3 lapiceros
        ) AS cart(product_id, quantity)
        ORDER BY cart.product_id
    LOOP
        -- Leer el precio y bloquear el producto hasta terminar la compra.
        SELECT p.stock, p.price
        INTO v_stock, v_unit_price
        FROM products AS p
        WHERE p.id = v_item.product_id
        FOR UPDATE;

        IF NOT FOUND THEN
            RAISE EXCEPTION 'El producto con ID % no existe.', v_item.product_id;
        END IF;

        IF v_item.quantity <= 0 THEN
            RAISE EXCEPTION 'La cantidad del producto % debe ser mayor que cero.',
                v_item.product_id;
        END IF;

        IF v_stock < v_item.quantity THEN
            RAISE EXCEPTION 'Stock insuficiente para el producto %. Solicitado: %, disponible: %.',
                v_item.product_id, v_item.quantity, v_stock;
        END IF;

        INSERT INTO bill_details (bill_id, product_id, quantity, unit_price)
        VALUES (v_bill_id, v_item.product_id, v_item.quantity, v_unit_price);

        UPDATE products
        SET stock = stock - v_item.quantity
        WHERE id = v_item.product_id;

        v_total := v_total + (v_item.quantity * v_unit_price);
    END LOOP;

    UPDATE bills
    SET total = v_total
    WHERE id = v_bill_id;

    RAISE NOTICE 'Factura % creada con un total de %.', v_bill_id, v_total;
END;
$$;