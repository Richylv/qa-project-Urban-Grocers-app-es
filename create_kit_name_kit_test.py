import sender_stand_request
import data

def get_user_body():
    current_body = data.user_body.copy()

    return current_body

def get_kit_body(name):
    current_bodykit = data.kit_body.copy()
    current_bodykit['name'] = name

    return current_bodykit

def get_new_token():
    user_body = get_user_body()
    user_response = sender_stand_request.post_new_user(user_body)
    token = 'Bearer ' + user_response.json()["authToken"]
    headers_kit = data.headers.copy()
    headers_kit["Authorization"] = token

    return headers_kit

def positive_assert(name):
    user_bodykit = get_kit_body(name)
    headers_kit = get_new_token()
    kit_response = sender_stand_request.post_new_client_kit(user_bodykit, headers_kit)
    assert kit_response.json()["name"] == name
    assert kit_response.status_code == 201

def negative_assert(name):
    user_bodykit = get_kit_body(name)
    headers_kit = get_new_token()
    kit_response = sender_stand_request.post_new_client_kit(user_bodykit, headers_kit)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def negative_assert_body(body):
    user_bodykit = body
    headers_kit = get_new_token()
    kit_response = sender_stand_request.post_new_client_kit(user_bodykit, headers_kit)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# Prueba 1. número permitido de caracteres (1)
def test_create_kit_1_letter_name():
    positive_assert(data.one_letter)

# Prueba 2. El número permitido de caracteres (511)
def test_create_kit_511_letter_name():
    positive_assert(data.letters_511)

# Prueba 3. El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_name():
    negative_assert(data.no_letters)

# Prueba 4. El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_name():
    negative_assert(data.letters_512)

# Prueba 5. Se permiten caracteres especiales
def test_create_kit_special_symbol_name():
    positive_assert(data.special_letters)

# Prueba 6. Se permiten espacios
def test_create_kit_has_space_name():
    positive_assert(data.space_letter)

# Prueba 7. Se permiten números
def test_create_kit_has_numbers_name():
    positive_assert(data.num_name)

# Prueba 8. El parámetro no se pasa en la solicitud
def test_create_kit_no_parameter():
    negative_assert_body(data.no_parameter)

# Prueba 9.
def test_create_kit_has_different_parameter_name():
    header = get_new_token()
    kit_body = get_kit_body(data.num_parameter)
    response = sender_stand_request.post_new_client_kit(kit_body,header)
    assert response.status_code == 400









