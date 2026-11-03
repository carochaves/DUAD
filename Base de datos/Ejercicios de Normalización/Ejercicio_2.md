# Ejercicio Cars: Normalización de vehículos

## 1. Tabla original

| VIN | Make | Model | Year | Color | Owner ID | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|---|---|---|---|---|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

## 2. Observaciones

La tabla contiene información sobre vehículos, propietarios
y seguros asociados a cada propietario de un vehículo.

El vehículo con VIN 1HGCM82633A aparece con dos propietarios:
Alice y Bob.

Para conservar los datos originales, se asume que un vehículo puede tener varios propietarios y que un propietario puede tener varios vehículos.

### Dependencias funcionales

- VIN determina Make, Model, Year y Color.
- Owner ID determina Owner Name y Owner Phone.
- La combinación VIN + Owner ID determina Insurance Company
  e Insurance Policy.

## 3. Primera forma normal (1FN)

La tabla original ya cumple la primera forma normal, porque cada celda contiene un valor individual y cada fila representa la asociación entre un vehículo y un propietario.

Se establece como clave primaria compuesta:

**(VIN, Owner ID)**

VIN no puede identificar una fila por sí solo porque un vehículo
puede tener varios propietarios.

Owner ID tampoco garantiza identificar una fila por sí solo,
porque un propietario puede tener varios vehículos, aunque
ese caso no aparezca en los datos de ejemplo.

### Tabla CarOwners_1NF

| VIN (PK) | Make | Model | Year | Color | Owner ID (PK) | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|---|---|---|---|---|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

### Justificación

Los valores son atómicos y la clave compuesta permite identificar
cada fila bajo los supuestos establecidos.

Sin embargo, existen dependencias parciales:

- Make, Model, Year y Color dependen únicamente de VIN.
- Owner Name y Owner Phone dependen únicamente de Owner ID.

Por esta razón, la tabla todavía no cumple la segunda forma normal.

## 4. Segunda forma normal (2FN)

Se separa la información según sus dependencias:

- Cars_2NF almacena los datos que dependen de VIN.
- Owners_2NF almacena los datos que dependen de Owner ID.
- CarOwners_2NF conserva los datos que dependen de la combinación
  VIN + Owner ID.

### Tabla Cars_2NF

| VIN (PK) | Make | Model | Year | Color |
|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red |

### Tabla Owners_2NF

| Owner ID (PK) | Owner Name | Owner Phone |
|---|---|---|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

### Tabla CarOwners_2NF

| VIN (PK, FK) | Owner ID (PK, FK) | Insurance Company | Insurance Policy |
|---|---|---|---|
| 1HGCM82633A | 101 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | 102 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | 103 | DEF Insurance | Collision |
| 1G1RA6EH1FU | 104 | GHI Insurance | Basic Legal |

### Justificación

Se eliminaron las dependencias parciales:

- Los datos de cada vehículo se almacenan una sola vez en Cars_2NF.
- Los datos de cada propietario se almacenan una sola vez en Owners_2NF.
- Insurance Company e Insurance Policy dependen de la combinación completa de VIN y Owner ID.

La información del seguro se conserva en la tabla intermedia, porque corresponde a un propietario asociado a un vehículo específico.

## 5. Tercera forma normal (3FN)

Se revisan las tablas obtenidas en la segunda forma normal para identificar posibles dependencias transitivas.

Bajo los supuestos establecidos, no existen dependencias transitivas que requieran nuevas separaciones:

- En Cars, los atributos dependen de VIN.
- En Owners, los atributos dependen de Owner ID.
- En CarOwners, los datos del seguro dependen de la clave
  compuesta VIN + Owner ID.

Por lo tanto, las tablas obtenidas en 2FN también cumplen la 3FN y conservan su estructura.

### Tabla final Cars

| VIN (PK) | Make | Model | Year | Color |
|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red |

### Tabla final Owners

| Owner ID (PK) | Owner Name | Owner Phone |
|---|---|---|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

### Tabla final CarOwners

| VIN (PK, FK) | Owner ID (PK, FK) | Insurance Company | Insurance Policy |
|---|---|---|---|
| 1HGCM82633A | 101 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | 102 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | 103 | DEF Insurance | Collision |
| 1G1RA6EH1FU | 104 | GHI Insurance | Basic Legal |

### Justificación

Las tablas cumplen la tercera forma normal porque no presentan dependencias parciales ni transitivas bajo las reglas establecidas.

No es necesario crear otra tabla en cada etapa de normalización si las tablas existentes ya cumplen sus requisitos.

No se separan Insurance Company e Insurance Policy en una tabla con una dependencia entre ellas, porque el enunciado no establece que una determine a la otra.

Tampoco se asume que Model determine Make: el nombre de un modelo
no garantiza ser único entre todas las marcas.

## 6. Claves y relaciones

### Significado de las claves

- PK: clave primaria. Identifica cada registro.
- FK: clave foránea. Hace referencia a una clave de otra tabla.
- En CarOwners, VIN y Owner ID forman una única clave primaria
  compuesta. Cada columna también es una clave foránea.

### Claves foráneas

| Tabla | Clave foránea | Referencia |
|---|---|---|
| CarOwners | VIN | Cars.VIN |
| CarOwners | Owner ID | Owners.Owner ID |

### Relaciones

| Tablas | Relación | Explicación |
|---|---|---|
| Cars → CarOwners | 1:N | Un vehículo puede aparecer en varias asociaciones con propietarios. |
| Owners → CarOwners | 1:N | Un propietario puede aparecer en varias asociaciones con vehículos. |

Cars y Owners tienen una relación muchos a muchos (N:N), resuelta mediante la tabla intermedia CarOwners.