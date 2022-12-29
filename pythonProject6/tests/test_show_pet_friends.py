import pytest
from settings import email, password
from selenium.webdriver.common.by import By

def test_show_pet_friends():
   '''Проверка карточек питомцев'''

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)

   # Вводим эл. почту
   pytest.driver.find_element(By.ID, 'email').send_keys(email)

   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(password)

   # Нажимаем на кнопку "Войти"
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Проверяем, что открылась главная страница пользователя
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(', ')
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
