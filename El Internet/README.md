# Fundamentos de Internet 

## 1. Del Cliente al Servidor

Cuando escribo www.youtube.com en el navegador, ocurre lo siguiente:
1. El cliente inicia la solicitud.
   El navegador es el cliente: interpreta la dirección y comienza a buscar cómo conectarse a YouTube.
2. El DNS busca la dirección IP.
   El DNS funciona como una agenda: traduce el nombre www.youtube.com a una dirección IP, que identifica un servidor al que el navegador puede conectarse. Si esa información ya está guardada en caché, puede reutilizarla.
3. El navegador se conecta usando la IP.
   Con esa dirección IP, el navegador establece una conexión con el servidor. Como YouTube utiliza HTTPS, también establece una conexión cifrada para proteger la información que se intercambia.
4. El cliente envía una petición HTTPS.
   El navegador solicita la página de YouTube. HTTP define cómo se realizan las peticiones y respuestas entre cliente y servidor; HTTPS añade protección mediante cifrado.
5. El servidor procesa la petición y responde.
   El servidor recibe la solicitud y devuelve los recursos necesarios, como HTML, CSS, JavaScript e imágenes. Estos permiten construir la página, darle estilo y hacerla interactiva.
6. El navegador muestra la página.
   El navegador interpreta los archivos recibidos y presenta la interfaz de YouTube. A medida que necesita más recursos, realiza nuevas peticiones.
7. Se solicita y reproduce el video.
   Cuando seleccionas un video —o comienza uno automáticamente—, el navegador solicita sus datos. Normalmente llegan en pequeños segmentos desde servidores de distribución de contenido. El reproductor guarda algunos temporalmente, decodifica el audio y las imágenes y los reproduce en pantalla mientras sigue descargando los siguientes.

## 2. Frontend y Backend en acción

Frontend: es la parte que el usuario ve y utiliza en el navegador. Incluye el formulario para solicitar una cita, el calendario de horarios disponibles y los botones para confirmar o cancelar.
Tres tecnologías posibles:
- HTML: estructura el contenido y los formularios.
- CSS: define colores, tamaños y diseño.
- JavaScript: permite la interacción y envía solicitudes al backend.
Backend: es la parte que se ejecuta en el servidor. Valida los datos, consulta la disponibilidad del médico y guarda o cancela las citas en una base de datos.
Tres tecnologías posibles:
- Python con Django.
- JavaScript con Node.js y Express.
- C# con ASP.NET Core.
¿Cómo se comunican?
El frontend se comunica con el backend mediante una API, que define las operaciones disponibles, como consultar horarios o registrar una cita. Utiliza HTTP, normalmente protegido mediante HTTPS, para intercambiar solicitudes y respuestas (request/response).

## 3. REST vs SOAP vs GraphQL

|Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
-------------------------------------------------------------------------------------------------------------------------------
| REST       | JSON / XML             |        Media          |            Baja              |            Alta                  | 
| SOAP       | XML                    |        Baja           |            Alta              |            Baja                  |
| GraphQL    | Consultas GraphQL;     |        Alta           |            Media-Alta        |            Media                 |
               respuestas en JSON 
               habitualmente

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**
En mi opinión, REST es la mejor opción para un startup moderna ya que es sencilla de implementar, cuenta con muchas herramientas y permite crear, consultar, actualizar y hacer cancelaciones 
mediant métodos HTTP como POST, GET, PATH y DELETE. 

## 4. Explorando APIs con Postman

### 4.1 Selección de la API

-***Nombre de la API:** JSONPlaceholder
-**Descripción:** API REST pública que ofrece datos ficticios de usuarios, publicaciones, comentarios y tareas para practicar solicitudes HTTP. Devuelve información en formato JSON.

### 4.2 Configuración en Postman
-**Nombre de la colección:** JSONPlaceholder
-**Solicitudes agregadas:**
 - GET - https://jsonplaceholder.typicode.com/posts/1 — Obtener una publicación.
 - POST - https://jsonplaceholder.typicode.com/posts — Simular la creación de una publicación.
 - DELETE - https://jsonplaceholder.typicode.com/posts/1 — Simular la eliminación de una publicación.

### 4.3 Ejecución y análisis

| Solicitud           | Método | Endpoint | Código de estado | Notas                                                       |
|Obtener publicación  |GET     |posts/1   |200               |Devuelve un JSON con userId, id, title y body.               |
|Crear publicación    |POST    |posts     |201               |Devuelve los datos enviados y un id. La creación es simulada.|
|Eliminar publicación |DELETE  |posts/1   |200               |Devuelve {}. La eliminación es simulada.                     |

### 4.4 Explicación técnica
JSONPlaceholder es una API REST pública y gratuita que ofrece datos ficticios de publicaciones, usuarios, comentarios y tareas. Permite practicar solicitudes HTTP sin autenticación. Los datos se intercambian en formato JSON y las operaciones de creación, actualización y eliminación son simuladas.

#### [Obtener publicación]

- **Método HTTP:** GET
- **Endpoint:** /posts/1
- **Parámetros / body:** Parámetro de ruta: 1, identificador de la publicación. Sin cuerpo.
- **Descripción de la respuesta:** Devuelve la publicación con sus campos userId, id, title y body. Estado esperado: 200 OK.

#### [Crear publicación]

- **Método HTTP:** POST
- **Endpoint:** /posts
- **Parámetros / body:** Cuerpo JSON con title, body y userId.
- **Descripción de la respuesta:** Devuelve los datos enviados y un identificador asignado. Estado esperado: 201 Created.

#### [Eliminar publicación]

- **Método HTTP:** DELETE  
- **Endpoint:** /posts/1
- **Parámetros / body:** Parámetro de ruta: 1, identificador de la publicación. Sin cuerpo.
- **Descripción de la respuesta:** Devuelve un objeto vacío {}. Estado esperado: 200 OK.

Ejemplos:

POST
{
  "title": "Mi primera publicación",
  "body": "Estoy practicando solicitudes con Postman.",
  "userId": 1
}

jemplo de respuesta JSON
La solicitud GET /posts/1 devolvió:
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}

**¿Qué aprendiste del proceso?** Aprendí a utilizar Postman para organizar y ejecutar solicitudes a una API REST. Comprendí cómo GET permite consultar información, POST enviar datos y DELETE eliminar un recurso. También aprendí a identificar endpoints, enviar un cuerpo en formato JSON, revisar códigos de estado y headers, y guardar las respuestas en una colección. 

### 4.5 Reflexión final
Aprendí que las APIs permiten que distintas aplicaciones se comuniquen mediante solicitudes y respuestas. El cliente envía una solicitud a un endpoint y el servidor la procesa y devuelve una respuesta. También comprendí el uso de los métodos GET, POST y DELETE, el formato JSON y los códigos de estado para interpretar el resultado de cada operación.
Postman me ayudó a entender esta comunicación porque pude actuar como cliente, enviar solicitudes y observar las respuestas del servidor. Al revisar el cuerpo de la respuesta, los headers y los códigos de estado, pude relacionar los conceptos teóricos con ejemplos prácticos, sin tener que programar una aplicación completa.