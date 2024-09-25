# Tax-CRM version #1

## Функціональні потреби

### Функціональні блоки

* Аутентифікація
* Авторизація
* Редагування профілю
* Редагування профілю зі сторони адміна

### Типи користувачів

* Гість (анонімний користувач у якого є тільки часткові права на перегляд).
* Системний адміністратор (користувач із найвищою категорією прав).
* Компанія (профіль із найвищими правами для користувача). Компанія може створювати підкористувачів, які будуть членами цієї компанії.
* Співробітник компанії (права визначаються під час створення профілю компанією-батьком).

### Інтерфейси системи

1. Домашня сторінка (home / dashboard):
	- Сьогоднішня дата у форматі (Tuesday, September 10, 2024).
	- Фото, ім'я та прізвище профілю користувача (якщо це співробітник, то показати назву компанії-батька).
	- Показати статистику профілю (к-сть лідів / непрочитаних повідомлень / завдань).
	- Маленький dashboard для Leads.
	- Маленький dashboard для Tasks.
	- Маленький dashboard для Calendar.
	- Маленький dashboard для Unread messages.
	- Поля для створення нового ліда / контакта / Tasks.

2. Профіль користувача (My Account):
	- Фото профілю
	- Account Info (Full Name *, Email Address *, Job Title, Phone Number, Personal Address)/
	- Change Password
	- Security Phone Number

3. Профіль користувача (company, тільки перегляд, якщо співробітник та редагування+перегляд, якщо адміністратор чи компанія):
	- Поле для редагування інформації (назва компанії, Company Type, Company Email, Phone Number, Company Website).
	- Поле для редагування Company smart file theme:
		- MAIN FONT AND COLORS; 
		- BUTTON font, color text, background color, size, border-radius
		- QUESTIONS font, color text, background color, size, border-radius, input fill, warning text color 
	- Brand elements (Main logo, Secondary logo, Brand color).
	- Email signature (персоналізований підпис, який буде з'являтися під кожним email від компанії).
	- About your company:
		- one line
		- Paragraph
	- Spread the word (посилання на соціальні мережі)
	- More info (Street Address, City, Postal Code, Country, Province, Currency, Timezone)

4. Профіль користувача (Company, вкладка TEAM)
	- Team members (Only editable by company owner)

5. Сторінка Contacts:
	- All contacts / Clients / Leads
	- Фільтрвання (поки порожньо)
	- Добавити контакт / ліда
		- Full name * 0/100
		- Email address *
		- Phone number
		- Organization
		- Job title
		- More details (Mailing address, Private comments (only visible to you))
	- Можна обрати певний перелік контактів (чи лідів) і виконати з ними такі дії:
		- видалити
		- надіслати email

6. Сторінка конкретного контакту:
	- Можливість редагувати Фото, повне ім'я
	- Добавити тег до контакта
	- вкладка Activity - показано хронологічну історію цього контакта у вигляді:
		- дата-час
		- що зролено (яка активність)
		- яким користувачем у CRM зроблена (повне ім'я)
	- вкладка Details (доступ до редагування усіх інших полів контакта)
	- вкладка Communication (можна надіслати лист користувачу)
