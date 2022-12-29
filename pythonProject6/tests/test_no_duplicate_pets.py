import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_no_duplicate_pets(open_my_pets):
    '''Поверяем что на странице со списком моих питомцев нет дубликатов'''

    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Перебираем данные из переменной, оставляем имя, возраст, породу,  остальное меняем на пустую строку
    # и разделяем по пробелу.
    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    # Склеиваем имя, возраст и породу, получившиеся слова добавляем в строку
    # и между ними вставляем пробел
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    # Получаем список из строки line
    list_line = line.split(' ')

    # Превращаем список в множество
    set_list_line = set(list_line)

    # Находим разницу между количеством элементов списка и множества
    result = len(list_line) - len(set_list_line)

    # Если количество элементов равно 0 - карточки с одинаковыми данными отсутствуют
    assert result == 0