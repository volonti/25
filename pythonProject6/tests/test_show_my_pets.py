import pytest

def test_show_my_pets(open_my_pets):

   # Проверяем что открыта страница "Мои питомцы"
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'
