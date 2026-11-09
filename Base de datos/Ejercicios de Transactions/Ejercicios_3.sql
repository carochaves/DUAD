DO $$
DECLARE
    v_bill_id INTEGER := 2;
    v_status VARCHAR(20);
BEGIN
    -- Verificar que la factura exista y bloquearla durante la devolución.
    SELECT status INTO v_status
    FROM bills
    WHERE id = v_bill_id
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'La factura % no existe.', v_bill_id;
    END IF;

    IF v_status = 'Retornada' THEN
        RAISE EXCEPTION 'La factura % ya fue retornada.', v_bill_id;
    END IF;

    -- Reponer las cantidades registradas en la compra.
    UPDATE products AS p
    SET stock = p.stock + d.quantity
    FROM bill_details AS d
    WHERE d.bill_id = v_bill_id
      AND d.product_id = p.id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'La factura % no tiene productos para devolver.', v_bill_id;
    END IF;

    -- Marcar la factura como retornada.
    UPDATE bills
    SET status = 'Retornada'
    WHERE id = v_bill_id;

    RAISE NOTICE 'La factura % fue retornada.', v_bill_id;
END;
$$;
