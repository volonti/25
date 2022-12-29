import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_there_is_a_photo(open_my_pets):
    '''Поверяем, что на странице со списком питомцев пользователя, хотя бы у половины питомцев есть фото'''

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

    # Сохраняем в переменную statistic элементы статистики
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    # Сохраняем в переменную images элементы с атрибутом img
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Получаем количество питомцев из данных статистики
    quantity = statistic[0].text.split('\n')
    quantity = quantity[1].split(' ')
    quantity = int(quantity[1])

    # Находим половину от количества питомцев
    half = quantity / 2

    # Находим количество питомцев с фотографией
    number_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_photos += 1

    # Проверяем, что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_photos >= half

