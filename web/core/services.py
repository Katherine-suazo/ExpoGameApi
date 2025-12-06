import requests 


def get_data_from_api(endpoint): 
    try:
        # token = "Autorization: Token asdasdasdasdasd"  <-  ejemplo
        response = requests.get(endpoint) # ,token)     # esta siendo una pregunta con el metodo endpoint
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        return None
    


def post_data_from_api(endpoint, data):
    try:
        # token = "Autorization: Token asdasdasdasdasd"  <-  ejemplo
        response = requests.post(endpoint, json=data) # ,token)     # esta siendo una pregunta con el metodo endpoint
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        return None



    # este es el motodo que se conectara a la api por lo tanto tenemos que pasarle el respons, saber con qeu 

    # -> endpoint pero tambien podri ser
    # -> usuario/clave
    # -> param.
    # -> json


    