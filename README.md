<br><br>
Посилання на розгорнутий проект<br>
https://boiling-atoll-35275.herokuapp.com/

<br><br>
Базу можна звантажити тут: https://edu.postgrespro.ru/demo-small.zip
Описание Таблиц БД<br>
https://postgrespro.ru/docs/postgrespro/11/apjs04
<br><br>
<h2>REST API:</h2>
<h3>1. Create user</h3>
POST .../api-auth/users/ <br>
body example: <br>

```
{
    "user": {
        "username": "airlines",
        "email": "airlines@air.lines",
        "password": "airlines"
    }
}
```
<br>
Response example:

```
{
    "user": {
        "email": "airlines@air.lines",
        "username": "airlines"
    }
}
```
<br>
Response example if user exist:

```
{
    "errors": {
        "email": [
            "user with this email already exists."
        ],
        "username": [
            "user with this username already exists."
        ]
    }
}
```
<h3>2. Login user</h3>
POST .../api-auth/users/login/

```
{
    "user": {
        "username": "user2",
        "email": "user2@user.user",
        "password": "qweasdzxc"
    }
}
```
<br>
Response example:

```
{
    "user": {
        "email": "airlines@air.lines",
        "username": "airlines",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjUwMjg5Nzk2fQ.bbyMdQan7igWflnenMrg0Hd5_kT0-n5d-flCvkaTQa8"
    }
}
```

<h3>3. User information </h3>
GET .../api-auth/user/ -H 'Authorization: Token {Token from previous response}<br>
Response example:

```
{
    "user": {
        "email": "airlines@air.lines",
        "username": "airlines",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjUwMjkxNjU1fQ.b86jDnSh6UktvClY3G6tsvdGTLXitn6r_ugzUX7mDKI"
    }
}
```


<h3>4. Aircraft get information</h3>
Need be authorized as in previous paragraph: GET .../api/aircrafts
<br>
Filter and ordering fields:

```
['aircraft_code', 'range']
```
Example for filter:

```
.../api/aircrafts?range=3000
```
Example for ordering:

```
.../api/aircrafts?ordering=range
```

<br><br>
JWT Аутентифікацію узяв з ресурсу: <br> 
https://habr.com/ru/post/538040/


<p>Що не вийшло зробити:</p>
<p>1. Не зміг зробити PointField, не має в базовой моделі в Django, додаткову бібліотеку встановити не вийшло, є 
помилки.</p>
<p>2. PRIMARY KEY для декількох полів Django не підтримує, зовнишня біблбіотека нормально не працює.</p>
<p>3. Розгорнути усю базу даних на ресурсі heroku, тому що є обмеження ресурсу до 10 000 строк бази.</p>
<p>4. Сортування та фільтрація по полю JSONField, потрібно описувати розгортання в кожному випадку.</p>
<p>5. Тести </p>