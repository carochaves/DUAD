# Ejercicio Cars: Normalización de vehículos

## 1. Tabla original

| VIN | Make | Model | Year | Color | Owner ID | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|---|---|---|---|---|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

## 2. Observaciones

La tabla contiene información sobre vehículos, modelos,
propietarios, compañías aseguradoras y pólizas.

El vehículo con VIN 1HGCM82633A aparece con dos propietarios:
Alice y Bob.

Para conservar los datos originales, se asume que un vehículo puede tener varios propietarios y que un propietario puede tener varios vehículos.

Make, Model y Year describen una entrada del catálogo de modelos que puede ser compartida por varios vehículos.

Cada entrada se identificará mediante Model ID y representará una combinación de marca, modelo y año.

Cada póliza pertenece a una compañía y se aplica al vehículo, no al propietario. Una misma póliza puede ser compartida por varios vehículos.

En este ejercicio, Insurance Policy representa un plan de cobertura compartido, no un contrato individual de seguro.

El primer vehículo aparece con dos pólizas diferentes.
Se conservan ambas mediante una tabla de asociación entre vehículos y pólizas, sin vincularlas a personas específicas.

### Dependencias funcionales

- VIN determina Model ID y Color.
- Model ID determina Make, Model y Year.
- Owner ID determina Owner Name y Owner Phone.
- Policy ID determina Policy Name y Company ID.
- Company ID determina Company Name.

Las asociaciones entre vehículos y propietarios se identifican mediante VIN + Owner ID.

Las asociaciones entre vehículos y pólizas se identifican mediante VIN + Policy ID.

## 3. Primera forma normal (1FN)

La tabla original ya cumple la primera forma normal, porque cada celda contiene un valor individual.

Se conserva la tabla original como punto de partida.
En los datos proporcionados, la combinación VIN + Owner ID identifica cada fila.

Esta combinación identifica los registros de origen, pero no se utilizará para vincular pólizas con propietarios en el modelo corregido.

VIN no puede identificar una fila por sí solo porque un vehículo puede tener varios propietarios.

Owner ID tampoco garantiza identificar una fila por sí solo, porque un propietario puede tener varios vehículos, aunque ese caso no aparezca en los datos de ejemplo.

### Tabla CarOwners_1NF

| VIN (PK) | Make | Model | Year | Color | Owner ID (PK) | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|---|---|---|---|---|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

### Justificación

Los valores son atómicos y la clave compuesta permite identificar las filas de origen.

Sin embargo, existen dependencias parciales:

- Make, Model, Year y Color dependen únicamente de VIN.
- Owner Name y Owner Phone dependen únicamente de Owner ID.

Además, se debe corregir la ubicación de los seguros: su asociación corresponde al vehículo, no a la combinación de vehículo y propietario.

Por esta razón, se separan las entidades y sus asociaciones en la siguiente etapa.

## 4. Segunda forma normal (2FN)

Se separa la información según sus dependencias:

- Cars_2NF almacena los datos del vehículo.
- Owners_2NF almacena los datos del propietario.
- CarOwners_2NF relaciona vehículos con propietarios.
- InsurancePolicies_2NF almacena los datos de las pólizas.
- CarPolicies_2NF relaciona vehículos con pólizas.

Se incorporan Model ID, Policy ID y Company ID para identificar las entidades que se separarán durante la normalización.

### Tabla Cars_2NF

| VIN (PK) | Model ID | Make | Model | Year | Color |
|---|---|---|---|---|---|
| 1HGCM82633A | M01 | Honda | Accord | 2003 | Silver |
| 5J6RM4H79EL | M02 | Honda | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | M03 | Chevrolet | Volt | 2015 | Red |

### Tabla Owners_2NF

| Owner ID (PK) | Owner Name | Owner Phone |
|---|---|---|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

### Tabla CarOwners_2NF

| VIN (PK, FK) | Owner ID (PK, FK) |
|---|---|
| 1HGCM82633A | 101 |
| 1HGCM82633A | 102 |
| 5J6RM4H79EL | 103 |
| 1G1RA6EH1FU | 104 |

### Tabla InsurancePolicies_2NF

| Policy ID (PK) | Policy Name | Company ID | Company Name |
|---|---|---|---|
| P01 | Fire & Theft | IC01 | ABC Insurance |
| P02 | Full Cover | IC02 | XYZ Insurance |
| P03 | Collision | IC03 | DEF Insurance |
| P04 | Basic Legal | IC04 | GHI Insurance |

### Tabla CarPolicies_2NF

| VIN (PK, FK) | Policy ID (PK, FK) |
|---|---|
| 1HGCM82633A | P01 |
| 1HGCM82633A | P02 |
| 5J6RM4H79EL | P03 |
| 1G1RA6EH1FU | P04 |

### Justificación

Se eliminaron las dependencias parciales:

- Los datos de cada vehículo se almacenan una sola vez en Cars_2NF.
- Los datos de cada propietario se almacenan una sola vez en Owners_2NF.
- Los datos de cada póliza se almacenan una sola vez en InsurancePolicies_2NF.
- CarOwners_2NF conserva únicamente las asociaciones entre vehículos y propietarios.
- CarPolicies_2NF conserva únicamente las asociaciones entre vehículos y pólizas.

Al separar ambas asociaciones, se elimina la vinculación incorrecta de una póliza con una persona específica.

Todavía existen estas dependencias transitivas:

**VIN → Model ID → Make, Model, Year**

**Policy ID → Company ID → Company Name**

Por esta razón, es necesario aplicar la tercera forma normal.

## 5. Tercera forma normal (3FN)

Se revisan las tablas obtenidas en la segunda forma normal para identificar posibles dependencias transitivas.

Se crea VehicleModels para almacenar Make, Model y Year.
Cars conserva Model ID como clave foránea y el color del vehículo específico.

También se crea InsuranceCompanies para almacenar los datos de las compañías aseguradoras.

InsurancePolicies conserva el nombre de la póliza y Company ID como clave foránea.

Owners, CarOwners y CarPolicies conservan la estructura obtenida en 2FN.

### Tabla final VehicleModels

| Model ID (PK) | Make | Model | Year |
|---|---|---|---|
| M01 | Honda | Accord | 2003 |
| M02 | Honda | CR-V | 2014 |
| M03 | Chevrolet | Volt | 2015 |

Cada Model ID representa una combinación de Make, Model y Year.
Esta combinación debe ser única en el catálogo.

### Tabla final Cars

| VIN (PK) | Model ID (FK) | Color |
|---|---|---|
| 1HGCM82633A | M01 | Silver |
| 5J6RM4H79EL | M02 | Blue |
| 1G1RA6EH1FU | M03 | Red |

### Tabla final Owners

| Owner ID (PK) | Owner Name | Owner Phone |
|---|---|---|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

### Tabla final CarOwners

| VIN (PK, FK) | Owner ID (PK, FK) |
|---|---|
| 1HGCM82633A | 101 |
| 1HGCM82633A | 102 |
| 5J6RM4H79EL | 103 |
| 1G1RA6EH1FU | 104 |

### Tabla final InsuranceCompanies

| Company ID (PK) | Company Name |
|---|---|
| IC01 | ABC Insurance |
| IC02 | XYZ Insurance |
| IC03 | DEF Insurance |
| IC04 | GHI Insurance |

### Tabla final InsurancePolicies

| Policy ID (PK) | Policy Name | Company ID (FK) |
|---|---|---|
| P01 | Fire & Theft | IC01 |
| P02 | Full Cover | IC02 |
| P03 | Collision | IC03 |
| P04 | Basic Legal | IC04 |

Para este catálogo, la combinación Company ID + Policy Name se considera única. El nombre de una póliza puede repetirse en distintas compañías.

### Tabla final CarPolicies

| VIN (PK, FK) | Policy ID (PK, FK) |
|---|---|
| 1HGCM82633A | P01 |
| 1HGCM82633A | P02 |
| 5J6RM4H79EL | P03 |
| 1G1RA6EH1FU | P04 |

### Justificación

Se eliminaron las dependencias transitivas:

- Make, Model y Year dependen de Model ID en VehicleModels.
- Model ID y Color dependen de VIN en Cars.
- Owner Name y Owner Phone dependen de Owner ID en Owners.
- Policy Name y Company ID dependen de Policy ID
  en InsurancePolicies.
- Company Name depende de Company ID en InsuranceCompanies.

Si existen 500 Honda Accord 2003, todos pueden utilizar Model ID M01 sin repetir la marca, el modelo y el año en Cars.

Si una misma póliza se aplica a 300 vehículos, sus datos
se almacenan una sola vez en InsurancePolicies.
CarPolicies registra las asociaciones con esos vehículos.

Las tablas cumplen la tercera forma normal bajo las reglas establecidas.

No se asume que el nombre del modelo por sí solo determine la marca o el año. Model ID identifica la combinación completa almacenada en el catálogo.

## 6. Claves y relaciones

### Significado de las claves

- PK: clave primaria. Identifica cada registro.
- FK: clave foránea. Hace referencia a una clave de otra tabla.
- En CarOwners, VIN y Owner ID forman una única clave primaria
  compuesta. Cada columna también es una clave foránea.
- En CarPolicies, VIN y Policy ID forman una única clave primaria
  compuesta. Cada columna también es una clave foránea.

### Claves foráneas

| Tabla | Clave foránea | Referencia |
|---|---|---|
| Cars | Model ID | VehicleModels.Model ID |
| CarOwners | VIN | Cars.VIN |
| CarOwners | Owner ID | Owners.Owner ID |
| InsurancePolicies | Company ID | InsuranceCompanies.Company ID |
| CarPolicies | VIN | Cars.VIN |
| CarPolicies | Policy ID | InsurancePolicies.Policy ID |

### Relaciones

| Tablas | Relación | Explicación |
|---|---|---|
| VehicleModels → Cars | 1:N | Una entrada del catálogo puede corresponder a varios vehículos. |
| Cars → CarOwners | 1:N | Un vehículo puede aparecer en varias asociaciones con propietarios. |
| Owners → CarOwners | 1:N | Un propietario puede aparecer en varias asociaciones con vehículos. |
| InsuranceCompanies → InsurancePolicies | 1:N | Una compañía puede ofrecer varias pólizas. |
| Cars → CarPolicies | 1:N | Un vehículo puede tener varias pólizas asociadas. |
| InsurancePolicies → CarPolicies | 1:N | Una póliza puede aplicarse a varios vehículos. |

Cars y Owners tienen una relación muchos a muchos (N:N), resuelta mediante la tabla intermedia CarOwners.

Cars e InsurancePolicies tienen una relación muchos a muchos (N:N), resuelta mediante la tabla intermedia CarPolicies.

Las pólizas se relacionan con los vehículos, no con sus propietarios.