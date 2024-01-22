@sprint_5

Тестирование сервиса Stellar Burgers.

Основа для написания автотестов — фреймворк pytest.

Команда для запуска — pytest -v

1. test_registration_user.py 
Тестируем регистрацию пользователя с использованием валидных и невалидных рандомных данных


2. test_authorisation_user.py
Тестирование авторизации пользователя с разных частей страницы:

    test_authorisation_user_button_enter_account - вход по кнопке «Войти в аккаунт» на главной
    test_authorisation_user_button_personal_account - вход через кнопку «Личный кабинет»
    test_authorisation_user_button_link_login_form - вход через кнопку в форме регистрации
    test_authorisation_user_button_password_recovery_form - вход через кнопку в форме восстановления пароля


3. test_transfer_in_personal_account.py
Тестирование перехода в Личный кабинет авторизованного пользователя


4. test_transfer_from_personal_account.py
Тестирование перехода из Личного кабинета в Конструктор: 
test_transition_authorized_user_from_personal_account_in_constructor - переход по кнопке Конструктор
test_clicking_logo_button_from_personal_account - переход через лого Stellar Burgers


5. test_logout_personal_account.py
Тестирование выхода по кнопке «Выйти» в личном кабинете


6. test_constructor.py
Тестирование перехода по разделам конструктора на главной:
test_constructor_section_fillings - клик на раздел "Начинки"
test_constructor_section_sauce - клик на раздел "Соусы"
test_constructor_section_buns - клик на раздел "Булки" из раздела "Начинки"
