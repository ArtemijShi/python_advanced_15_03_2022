"""
http-протокол://www.google.com-домен(может быть числовой): 88-порт -полная адресная часть/ - путь(адрес ресурса)
?-набор параметров&&text='nnn'&name='ar'
https:// 196.201.45.1 - айпи адрес:77 - порт
ftp
Методы:
GET - запрос содержимого с сервера, содержит тело
POST - запрос для отправки данных на сервер
HEAD - аналог метода ГЕТ, содержит только заголовок
PUT - загрузка данных на сервер
PATCH - для обновления фрагмента каких то данных на сервере
DELETE - для удаления какого то ресурса
TRACE - для получения информации о промежуточных серверах, которые между клиен  и сервером
CONNECT - применяется когда создается тоннель(типа впн)


Status code:
1xx(100-199) - информационные коды для передачи информации, запрос принят для обработки.
2хх(200-299) - успешность обработки запросов, данные валидные можно юзать
3хх(300-399) - в случае если запрос переадресовывается сервером на другие серверы
4хх(400-499) - ошибки клиента, запрос клиентом является не валидным
5хх(500-599) - ошибки сервера, запрос не обработан сервером по внутренним прроблемам


Headers:
General - могут добавлены в клиентский запрос и в запрос серве
Requests - включаются только в клиентский запрос
Response - заголовки ответа, только в ответах сервиса.
Entity - в ответ либоо запрос и сопровожждать каждый обьект в этом запросе, описывать сущность пересылаемоего сообщения


Body:

HTML
JSON / XML
binary

"""