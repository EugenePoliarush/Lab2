Лабораторна робота №2

з дисципліни Бази даних і засоби управління
на тему: “ Створення додатку бази даних, орієнтованого на взаємодію з СУБД PostgreSQL”

Сутність	Атрибут	Тип атрибуту
Company - містить дані про компанію	Company_name - унікальний ідентифікатор компанії, тобто її назва
phone – телефон компанії
adress – адреса компанії	character varying (рядок)


character varying (рядок)
character varying (рядок)
Buildilng - містить дані про будинки, якими управляє компанія	id_building - унікальний ідентифікатор будинку
Company_name - назва компанії, яка ним керує
number_of_floors – кількість поверхів у будинку
adress – адреса будинку
number_of_apartments – кількість квартир у будинку	integer (числовий)

character varying (рядок)

integer (числовий)

character varying (рядок)
integer (числовий)
Apartment – містить дані про квартири	id_apartment - унікальний ідентифікатор квартири
id_building – ідентифікатор будинку в якому знаходиться квартира
id_person – ідентифікатор особи, яка володіє квартирою
floor – номер поверху де розташована квартира
number – номер квартири
number_of_rooms – кількість кімнат в квартирі	integer (числовий)

integer (числовий)

integer (числовий)

integer (числовий)

integer (числовий)
integer (числовий)
Person - містить дані про мешканця 	id_person - унікальний ідентифікатор мешканця
Company_name – ідентифікатор компанії
name – Ім’я мешканця
surname – Прізвище мешканця
patronymic – По батькові
phone – телефон мешканця	integer (числовий)

character varying (рядок)

character varying (рядок)
character varying (рядок)
character varying (рядок)
character varying (рядок)

Таблиця 1. Опис структури БД
