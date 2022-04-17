<br><br>
Ссылка на развернутый проект<br>
https://boiling-atoll-35275.herokuapp.com/

<br><br>
Базу можна звантажити тут: https://edu.postgrespro.ru/demo-small.zip
Описание Таблиц БД<br>
https://postgrespro.ru/docs/postgrespro/11/apjs04
<br><br>
REST API:
<p>1. Create user: POST .../api/users/ <br>
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
</p>
<p>2. Login user: POST .../api/users/login/

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
</p>
<p>3. User information: GET .../api/user/ -H 'Authorization: Token {Token from previous response}<br>
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

</p>
<br><br>
JWT Аутентифікацію узяв з ресурсу: <br> 
https://habr.com/ru/post/538040/


<p>Що не вийшло зробити:</p>
<p>1. Не зміг зробити PointField, не має в базовой моделі в Django, додаткову бібліотеку встановити не вийшло, є 
помилки.</p>
<p>2. PRIMARY KEY для декількох полів Django не підтримує, зовнишня біблбіотека нормально не працює.</p>
<p>3. Розгорнути усю базу даних на ресурсі heroku, тому що є обмеження ресурсу до 10 000 строк бази.</p>
<p>4. Тести </p>