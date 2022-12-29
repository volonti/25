import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_name_different(open_my_pets):
   '''Поверяем, что на странице со списком моих питомцев, у всех питомцев разные имена'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную элементы с данными о питомцах
   data_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Перебираем данные из переменной, оставляем имя, возраст, породу, остальное меняем на пустую строку
   # и разделяем по пробелу.Выбираем имена и добавляем их в список pets_name.
   pets_name = []
   for i in range(len(data_pets)):
      data_pet = data_pets[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      pets_name.append(split_data_pet[0])

   # Перебираем имена и если имя повторяется, то прибавляем к счетчику единицу.
   # Проверяем, если n == 0 то повторяющихся имен нет
   n = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         n += 1
   assert n == 0
   print(n)
   print(pets_name)
