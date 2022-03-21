import requests
import pytest
import cerberus
from jsonschema import validate
#Проверяем что присутствуют все элементы в posts
@pytest.mark.parametrize('elements',['userId','id','title','body'])
def test_post_elements(service_3_url,elements):
    list_dict = requests.get(service_3_url + 'posts').json()
    for dict in list_dict:
        if elements in dict.keys():
            continue
        else:
            assert False
    assert True

#Проверем схем json коментариев с помощью валидатора цербер
def test_json_schema_coments(service_3_url):
    res = requests.get(service_3_url + 'comments/1').json()

    schema = {
        "postId": {"type": "number"},
        "id": {"type": "number"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"},
    }

    v=cerberus.Validator()
    assert v.validate(res, schema)

#Проверяем что значение Server в headers соответствует ожидаемому
def test_header_server(service_3_url):
    list_dict = requests.get(service_3_url + 'posts')
    assert list_dict.headers['Server']=='cloudflare'

#Проверем схем json todos с помощью валидатора из jsonschema
def test_json_schema_todos(service_3_url):
    res = requests.get(service_3_url + 'todos/1').json()

    schema = {
        "type": "object",
        "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
        },
        "required":["userId", "id", "title", "completed"]
    }

    validate(instance=res, schema=schema)

def test_json_schema(service_3_url):
    res = requests.get(service_3_url + 'todos/1').json()

#Проверем схем json albums с помощью валидатора из jsonschema перебераем несколько
@pytest.mark.parametrize('number',['1','2','3','4'])
def test_json_schema_albums(service_3_url,number):
    res = requests.get(service_3_url + 'albums/' + number).json()

    schema = {
        "type": "object",
        "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        },
        "required":["userId", "id", "title"]
    }

    validate(instance=res, schema=schema)
