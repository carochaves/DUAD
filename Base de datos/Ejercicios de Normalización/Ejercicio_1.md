# Ejercicio 1: Normalización de pedidos

## 1. Tabla original

| Order ID | Customer Name | Customer Phone | Address | Item ID | Item Name | Price | Quantity | Special Request | Delivery Time |
|---|---|---|---|---|---|---|---|---|---|
| 001 | Alice | 123-456-7890 | 123 Main St | 101 | Cheeseburger | $8 | 2 | No onions | 6:00 PM |
| 001 | Alice | 123-456-7890 | 123 Main St | 102 | Fries | $3 | 1 | Extra ketchup | 6:00 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 103 | Pizza | $12 | 1 | Extra cheese | 7:30 PM |
| 002 | Bob | 987-654-3210 | 4th Avenue | 102 | Fries | $3 | 2 | None | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St | 105 | Salad | $6 | 1 | No croutons | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 106 | Water | $1 | 1 | None | 5:00 PM |

## 2. Observaciones

La dirección de entrega corresponde al pedido completo, por lo que
Address debe almacenarse en Orders.

La dirección del pedido 002 está pendiente de confirmar, porque
en la tabla original aparecen dos direcciones distintas para
el mismo pedido: 456 Elm St y 4th Avenue.

Se conservan los datos originales en la tabla inicial y en 1FN.
A partir de 2FN se utiliza la anotación "Por confirmar" para
ese pedido, sin elegir arbitrariamente una dirección.

Los identificadores de clientes asignados son:

| Customer ID | Customer Name |
|---|---|
| C01 | Alice |
| C02 | Bob |
| C03 | Claire |

### Dependencias funcionales

- Order ID determina Customer ID, Address y Delivery Time.
- Customer ID determina Customer Name y Customer Phone.
- Item ID determina Item Name y Price.
- La combinación Order ID + Item ID determina Quantity y Special Request.

La dependencia Order ID → Address corresponde a la regla del negocio.
Las dos direcciones del pedido 002 representan una inconsistencia
en los datos originales que debe corregirse.

## 3. Primera forma normal (1FN)

La tabla original ya cumple la primera forma normal, porque cada celda contiene un valor individual y cada fila representa un producto dentro de un pedido.

Se establece como clave primaria compuesta:

**(Order ID, Item ID)**

Order ID no puede identificar una fila por sí solo porque un pedido puede contener varios productos.

Item ID tampoco puede identificar una fila por sí solo porque un producto puede aparecer en distintos pedidos.

### Tabla OrderDetails_1NF

| Order ID (PK) | Customer Name | Customer Phone | Address | Item ID (PK) | Item Name | Price | Quantity | Special Request | Delivery Time |
|---|---|---|---|---|---|---|---|---|---|
| 001 | Alice | 123-456-7890 | 123 Main St | 101 | Cheeseburger | 8.00 | 2 | No onions | 6:00 PM |
| 001 | Alice | 123-456-7890 | 123 Main St | 102 | Fries | 3.00 | 1 | Extra ketchup | 6:00 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 103 | Pizza | 12.00 | 1 | Extra cheese | 7:30 PM |
| 002 | Bob | 987-654-3210 | 4th Avenue | 102 | Fries | 3.00 | 2 | None | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St | 105 | Salad | 6.00 | 1 | No croutons | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 106 | Water | 1.00 | 1 | None | 5:00 PM |

### Justificación

Los valores son atómicos y la clave compuesta permite identificar cada fila bajo los supuestos establecidos.

Los precios se representan como números decimales. El símbolo monetario puede agregarse al presentar los datos.

Sin embargo, todavía existen dependencias parciales:

- Los datos del cliente, la dirección y la hora dependen únicamente de Order ID.
- El nombre y el precio del producto dependen únicamente de Item ID.

## 4. Segunda forma normal (2FN)

Se separa la información según sus dependencias:

- Orders_2NF almacena los datos que dependen de Order ID.
- Items_2NF almacena los datos que dependen de Item ID.
- OrderDetails_2NF conserva los datos que dependen de la
  combinación Order ID + Item ID.

Se incorpora Customer ID para identificar a cada cliente.

### Tabla Orders_2NF

| Order ID (PK) | Customer ID | Customer Name | Customer Phone | Address | Delivery Time |
|---|---|---|---|---|---|
| 001 | C01 | Alice | 123-456-7890 | 123 Main St | 6:00 PM |
| 002 | C02 | Bob | 987-654-3210 | Por confirmar | 7:30 PM |
| 003 | C03 | Claire | 555-123-4567 | 789 Oak St | 12:00 PM |
| 004 | C03 | Claire | 555-123-4567 | 464 Georgia St | 5:00 PM |

### Tabla Items_2NF

| Item ID (PK) | Item Name | Price |
|---|---|---|
| 101 | Cheeseburger | 8.00 |
| 102 | Fries | 3.00 |
| 103 | Pizza | 12.00 |
| 105 | Salad | 6.00 |
| 106 | Water | 1.00 |

### Tabla OrderDetails_2NF

| Order ID (PK, FK) | Item ID (PK, FK) | Quantity | Special Request |
|---|---|---|---|
| 001 | 101 | 2 | No onions |
| 001 | 102 | 1 | Extra ketchup |
| 002 | 103 | 1 | Extra cheese |
| 002 | 102 | 2 | None |
| 003 | 105 | 1 | No croutons |
| 004 | 106 | 1 | None |

### Justificación

Se eliminaron las dependencias parciales:

- La información del pedido se almacena una sola vez por pedido.
- La información del producto se almacena una sola vez por producto.
- Address se almacena en Orders_2NF porque depende de Order ID.
- Quantity y Special Request dependen de la combinación
  completa de Order ID e Item ID.

Sin embargo, Orders_2NF todavía contiene una dependencia transitiva:

**Order ID → Customer ID → Customer Name, Customer Phone**

El nombre y el teléfono corresponden al cliente. Por ejemplo, los datos de Claire se repiten en los pedidos 003 y 004.

Por esta razón, es necesario aplicar la tercera forma normal.

## 5. Tercera forma normal (3FN)

Se crea Customers para almacenar los datos propios de cada cliente.

Orders conserva el identificador del cliente como clave foránea, además del identificador del pedido, su dirección y su hora de entrega.

Items y OrderDetails conservan la estructura obtenida en 2FN.

### Tabla final Customers

| Customer ID (PK) | Customer Name | Customer Phone |
|---|---|---|
| C01 | Alice | 123-456-7890 |
| C02 | Bob | 987-654-3210 |
| C03 | Claire | 555-123-4567 |

### Tabla final Orders

| Order ID (PK) | Customer ID (FK) | Address | Delivery Time |
|---|---|---|---|
| 001 | C01 | 123 Main St | 6:00 PM |
| 002 | C02 | Por confirmar | 7:30 PM |
| 003 | C03 | 789 Oak St | 12:00 PM |
| 004 | C03 | 464 Georgia St | 5:00 PM |

### Tabla final Items

| Item ID (PK) | Item Name | Price |
|---|---|---|
| 101 | Cheeseburger | 8.00 |
| 102 | Fries | 3.00 |
| 103 | Pizza | 12.00 |
| 105 | Salad | 6.00 |
| 106 | Water | 1.00 |

### Tabla final OrderDetails

| Order ID (PK, FK) | Item ID (PK, FK) | Quantity | Special Request |
|---|---|---|---|
| 001 | 101 | 2 | No onions |
| 001 | 102 | 1 | Extra ketchup |
| 002 | 103 | 1 | Extra cheese |
| 002 | 102 | 2 | None |
| 003 | 105 | 1 | No croutons |
| 004 | 106 | 1 | None |

### Justificación

Se eliminó la dependencia transitiva de los datos del cliente:

- Customer Name y Customer Phone dependen de Customer ID
  en Customers.
- Customer ID, Address y Delivery Time dependen de Order ID en Orders.
- Item Name y Price dependen de Item ID en Items.
- Quantity y Special Request dependen de la clave
  compuesta de OrderDetails.

Bajo los supuestos establecidos, las tablas cumplen la tercera forma normal.

## 6. Claves y relaciones

### Significado de las claves

- PK: clave primaria. Identifica cada registro.
- FK: clave foránea. Hace referencia a una clave de otra tabla.
- En OrderDetails, Order ID e Item ID forman una única clave
  primaria compuesta. Cada columna también es una clave foránea.

### Claves foráneas

| Tabla | Clave foránea | Referencia |
|---|---|---|
| Orders | Customer ID | Customers.Customer ID |
| OrderDetails | Order ID | Orders.Order ID |
| OrderDetails | Item ID | Items.Item ID |

### Relaciones

| Tablas | Relación | Explicación |
|---|---|---|
| Customers → Orders | 1:N | Un cliente puede realizar varios pedidos. |
| Orders → OrderDetails | 1:N | Un pedido puede tener varios detalles. |
| Items → OrderDetails | 1:N | Un producto puede aparecer en varios detalles de pedidos. |

Orders e Items tienen una relación muchos a muchos (N:N), resuelta mediante la tabla intermedia OrderDetails.