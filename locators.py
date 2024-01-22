from selenium.webdriver.common.by import By


class Locators:
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  #кнопка "Войти в аккаунт" на главной странице
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")               #кнопка "Личный кабинет" на главной странице
    NAME_FIELD_REGISTRATION = (By.XPATH, "(//input[@name= 'name'])[1]")                 #поле для ввода имени с названием "Имя" в форме авторизации
    EMAIL_FIELD_REGISTRATION = (By.XPATH, "(//input[@name= 'name'])[2]")                #поле для ввода mail с названием "Email" в форме авторизации
    PASSWORD_FIELD_REGISTRATION = (By.XPATH, "//input[@name= 'Пароль']")                #поле для ввода пароля с названием "Пароль" в форме авторизации
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")                    #кнопка "Зарегистрироваться" после ввода данных

    BUTTON_LINK_LOGIN = (By.XPATH, ".//a[@href='/login']")           #ссылка на форму авторизации по кнопке "Войти" на /registr
    BUTTON_LINK_REGISTRATION = (By.XPATH, ".//a[@href='/registr']")  #ссылка на форму регистрации по кнопке "Зарегистрироваться" на /login

    EMAIL_AUTHORISATION = (By.XPATH, ".//input[@name='name']")         #поле для ввода email с названием "Email" в форме авторизации
    PASSWORD_AUTHORISATION = (By.XPATH, ".//input[@name='Пароль']")    #поле для ввода пароля с названием "Пароль" в форме авторизации
    BUTTON_ENTER = (By.XPATH, ".//button[text()='Войти']")             #кнопка "Войти" в форме авторизации

    ERROR_REGISTRATION_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")  #сообщение "Некорректный пароль" если был введен невалидный пароль

    BUTTON_LINK_RECOVER_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")     #кнопка со ссылкой на форму восстановления пароля
    BUTTON_RECOVER_PASSWORD = (By.XPATH, "//p[text()='Восстановить']")              #кнопка "Восстановить" на /forgot-password

    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")                 #кнопка с названием "Конструктор"
    BUTTON_LOGO_EMAGE = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')          #кнопка логотипа Stellar Burgers
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")                         #кнопка в личном кабинете с названием "Выход"

    BUTTON_SAUCE = (By.XPATH, ".//span[text()='Соусы']")                        #кнопка "Соусы"
    SECTION_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")                        #отображение раздела с текстом "Соусы"
    BUTTON_FILLING = (By.XPATH, ".//span[text()='Начинки']")                    #кнопка "Начинки"
    SECTION_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']")                    #отображение раздела с текстом "Начинки"
    BUTTON_BUN = (By.XPATH, ".//span[text()='Булки']")                          #кнопка "Булки"
    SECTION_BUNS = (By.XPATH, ".//h2[text()='Булки']")                          #отображение раздела с текстом "Булки"
    CURRENT_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") #переменная текущего состояния (на сайте название текущего раздела подчеркнуто цветом)
