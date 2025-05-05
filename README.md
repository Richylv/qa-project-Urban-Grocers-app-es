![image](https://github.com/user-attachments/assets/8a527faa-993e-4fcd-bb96-058a3ceb4549)

<em> Proyecto para hacer solicitudes al servidor de una tienda </em> 
En este proyecto se trabajo pruebas en la lista de comprobación: positivas y negativas mediante métodos GET, POST, PUT y DELETE. 

## :hammer:Funcionalidades del proyecto
Se escriben pruebas automatizadas que cubran el proceso de pedir un taxi:
- `Funcionalidad 1`:Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
- `Funcionalidad 2`:Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Autorization
- `Funcionalidad 3`:Lista de comprobación de pruebas
  - El número permitido de caracteres
  - Se permiten caracteres especiales
  - El parámetro no se pasa en la solicitud
  - Se ha pasado un tipo de parámetro diferente
- `Funcionalidad 4`:uso de métodos GET, POST, PUT y DELETE 

## 🛠 tecnologias usadas
- PYTHON
- Pytest
- Github
 
## Notas
- data.py: contiene los datos para la prueba
- configuration.py: contiene los links 
- sender_stand_request.py: contiene los metodos para la creacion de usuario y kit
- create_kit_name_test.py:contiene las funciones para ejecutar las pruebas 
