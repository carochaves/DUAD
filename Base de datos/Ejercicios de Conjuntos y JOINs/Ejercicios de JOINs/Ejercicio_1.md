La instrucción SELECT permite consultar datos de una o varias tablas. Se puede combinar con cláusulas para ordenar, limitar, agrupar y relacionar los datos.

Los ejemplos utilizan las tablas ficticias:
- clientes: id, nombre.
- pedidos: id, cliente_id, total.

## Tabla informativa

| Funcionalidad | Descripción | Cómo se utiliza | Ejemplo |
| --- | --- | --- | --- |
| ORDER BY | Ordena los resultados según una o varias columnas. | ASC ordena de forma ascendente y DESC de forma descendente. Por defecto se utiliza ASC. | `SELECT id, total FROM pedidos ORDER BY total DESC, id ASC;` |
| LIMIT | Limita la cantidad de filas que devuelve una consulta. | Se indica el número máximo de filas. Se combina con ORDER BY para obtener resultados en un orden predecible. | `SELECT id, total FROM pedidos ORDER BY total DESC, id ASC LIMIT 5;` |
| GROUP BY | Agrupa filas que tienen el mismo valor en una o varias columnas. | Se puede combinar con funciones como COUNT(), SUM() y AVG() para calcular resultados por grupo. | `SELECT cliente_id, COUNT(*) AS cantidad FROM pedidos GROUP BY cliente_id;` |
| INNER JOIN | Devuelve únicamente las combinaciones de filas que coinciden en ambas tablas. | Se utiliza ON para indicar la condición que relaciona las tablas. | `SELECT c.nombre, p.id FROM clientes AS c INNER JOIN pedidos AS p ON c.id = p.cliente_id;` |
| LEFT JOIN | Devuelve todos los registros de la tabla izquierda y sus coincidencias en la tabla derecha. | Si no existe una coincidencia, las columnas de la tabla derecha contienen NULL. | `SELECT c.nombre, p.id FROM clientes AS c LEFT JOIN pedidos AS p ON c.id = p.cliente_id;` |
| RIGHT JOIN | Devuelve todos los registros de la tabla derecha y sus coincidencias en la tabla izquierda. | Si no existe una coincidencia, las columnas de la tabla izquierda contienen NULL. | `SELECT c.nombre, p.id FROM clientes AS c RIGHT JOIN pedidos AS p ON c.id = p.cliente_id;` |

## Aclaraciones

- Los alias c y p representan las tablas clientes y pedidos.
- ON establece la condición de unión entre las tablas.
- NULL representa un valor desconocido o ausente.
- Un cliente con varios pedidos puede aparecer en varias filas del resultado de un JOIN.
- GROUP BY agrupa los datos, pero no garantiza que el resultado esté ordenado. Para ordenarlo se utiliza ORDER BY.

## Fuentes consultadas

Documentación oficial de PostgreSQL:

- [SELECT](https://www.postgresql.org/docs/current/sql-select.html)
- [ORDER BY](https://www.postgresql.org/docs/current/queries-order.html)
- [LIMIT y OFFSET](https://www.postgresql.org/docs/current/queries-limit.html)
- [JOIN y GROUP BY](https://www.postgresql.org/docs/current/queries-table-expressions.html)