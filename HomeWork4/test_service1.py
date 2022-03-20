import requests
import pytest
# Проверяем что возврашаемый статус код валидный
def test_responce_ok(service_1_url):
    assert requests.get(service_1_url+'s/list/all').ok

#Проверяем что бульдоги разных пород присутствуют в LIST ALL BREEDS
@pytest.mark.parametrize('bulldog',['boston','english','french'])
def test_check_buldogs(service_1_url, bulldog):
    assert bulldog in requests.get(service_1_url+'s/list/all').json()['message']['bulldog']

#Проверяем что api выдающее случайную картинку возврашает в json статус Success
def test_random_img(service_1_url):
    assert 'success' in ((requests.get(service_1_url+'s/image/random')).json()).values()

#Проверка допустимых расширений файлов изображений для разных пород
@pytest.mark.parametrize('breed',['shiba','akita','shihtzu'])
def test_all_img_extension(service_1_url, breed):
    list_jpg = list(requests.get(service_1_url + '/' + breed + '/images').json().values())
    for jpg in list_jpg[0]:
        if jpg.split('.')[-1] == 'jpg' or jpg.split('.')[-1] == 'jpeg' or jpg.split('.')[-1] == 'JPG' or jpg.split('.')[-1] == 'JPEG':
            continue
        else:
            assert False , 'incorrect file extension'
    assert True

#Проверяем что api выдает заданное количество картинок для разных пород
@pytest.mark.parametrize('count',['1','25','50'])
def test_check_count_img(service_1_url,count):
    assert count == str(len(requests.get(service_1_url + 's/image/random/' + count).json()['message']))
