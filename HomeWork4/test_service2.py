import requests
import pytest
# Проверяем что фильтры отвечают
@pytest.mark.parametrize('filter',['?by_city=san_diego','?by_name=cooper','?by_state=ohio'])
def test_responce_ok_for_filters(service_2_url,filter):
    assert requests.get(service_2_url + filter).ok

#Проверяем что поиск работает для имен компаний
@pytest.mark.parametrize('search_in_name',['Diving Dog Brewhouse','MadTree Brewing'])
def test_search_in_name(service_2_url, search_in_name):
    list_dict = requests.get(service_2_url + '/search?query=' + search_in_name).json()
    for dict in list_dict:
        if str(search_in_name) in str(dict['name']):
            continue
        else:
            assert False
    assert True

#Проверяем что информационные поля соответствуют списку полей по умолчанию
def test_keys(service_2_url):
    keys_default = ['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state', 'county_province', 'postal_code', 'country', 'longitude', 'latitude', 'phone', 'website_url', 'updated_at', 'created_at']
    list_dict = requests.get(service_2_url + '/madtree-brewing-cincinnati').json()
    keysList = list(list_dict.keys())
    assert keys_default == keysList

#Проверка соответствие количества выводимых записей заданному значению для метода ?per_page
@pytest.mark.parametrize('count_of_page',['20','30','50'])
def test_count_of_breweries_on_page(service_2_url, count_of_page):
    list_dict = requests.get(service_2_url + '?per_page=' + count_of_page).json()
    assert str(len(list_dict)) == count_of_page

#Проверка соответствия выводимых типов пивоварен для метода ?by_type=
@pytest.mark.parametrize('brewery_type',['micro','nano','regional','brewpub','large','planning','bar','contract','closed'])
def test_sort_by_breweries_type(service_2_url,brewery_type):
    list_dict = requests.get(service_2_url + '?by_type=' + brewery_type).json()
    for dict in list_dict:
        if ('brewery_type', brewery_type) in dict.items():
             continue
        else:
            assert False
    assert True
