<h2 align="center">Сканирование сети с помощью Nmap и настройка UFW на Ubuntu 25.04</h2>

Конфигурация сети на первой виртуальной машине (VM1)
<br><br>
  <img width="775" height="486" alt="image" src="https://github.com/user-attachments/assets/f38910cb-789d-4f5b-a98f-c0636154a108" />

Конфигурация сети на второй виртуальной машине (VM2)
<br><br>
<img width="789" height="434" alt="image" src="https://github.com/user-attachments/assets/9cae8049-b1e3-4fc5-b7c7-01b5a53760c4" />
<br><br>
<h3 align="center">Шаг 1: Установка и настройка сервисов на VM2</h3>
1. Обновляю пакеты системы
<br><br>
 <img width="689" height="28" alt="image" src="https://github.com/user-attachments/assets/bffb5ebb-0590-41fb-9de0-9f955258ac24" />
<br><br>
2. Устанавливаю nginx
<br><br>
<img width="974" height="683" alt="image" src="https://github.com/user-attachments/assets/50bcaa6d-acf1-4a07-9780-aa2ed08ffb66" />
<br><br>
3. Устанавливаю SSH-сервер
<br><br>
<img width="974" height="917" alt="image" src="https://github.com/user-attachments/assets/dc930965-fee5-4c4a-8733-6c33216a1236" />
<br><br>
4. Проверяю, что сервисы запущены
<br><br>
 <img width="974" height="343" alt="image" src="https://github.com/user-attachments/assets/ee085cb2-1c01-4bba-8839-b9b80ecb8411" />
 <img width="974" height="185" alt="image" src="https://github.com/user-attachments/assets/ccc5d9ba-b524-478c-b660-10ad7a718be0" />
<br><br>
5. Проверяю доступность сервисов с VM1
<br><br>
 <img width="974" height="957" alt="image" src="https://github.com/user-attachments/assets/0d0b7514-54e6-4e4d-b2c4-826b52903a16" />
 <img width="867" height="727" alt="image" src="https://github.com/user-attachments/assets/a91a68d7-1a61-401b-96b1-76bd635cafb1" />
<br><br>
<h3 align="center">Шаг 2: Сканирование VM2 с помощью Nmap на VM1</h3>
1. Устанавливаю Nmap на VM1
<br><br>
 <img width="505" height="34" alt="image" src="https://github.com/user-attachments/assets/f59a3867-817b-44b0-87f8-e2a637f281f1" />
<br><br>
2. Выполняю сканирование портов
<br><br>
 <img width="830" height="286" alt="image" src="https://github.com/user-attachments/assets/4b53e6a2-5001-4c23-99d3-f3e9378d3dc2" />
<br><br>
3. Выполняю сканирование с определением операционной системы и версий сервисов
<br><br>
 <img width="974" height="349" alt="image" src="https://github.com/user-attachments/assets/0bf977d1-2687-418f-a617-6914e340cde4" />
<br><br>
4. Использую TCP SYN сканирование
<br><br>
 <img width="824" height="311" alt="image" src="https://github.com/user-attachments/assets/aca87b47-cb23-4f7c-ac31-ad11e204615c" />
<br><br>
5. Выполните UDP сканирование
<br><br>
 <img width="903" height="623" alt="image" src="https://github.com/user-attachments/assets/4d5db1d5-c186-46f1-89ae-f1b33b0b832a" />
<br><br>
6. Пробую сканирование скрытых портов
<br><br>
 <img width="828" height="339" alt="image" src="https://github.com/user-attachments/assets/024104f8-7c01-4edb-b3b1-f42c637f93ac" />
<br><br>
7. (Надо бы проанализировать результаты каждого сканирования и отметьте открытые порты и обнаруженные сервисы)
<br><br>
<h3 align="center">Шаг 3: Настройка брандмауэра UFW на VM2</h3>
1. Активирую UFW
<br><br>
 <img width="614" height="88" alt="image" src="https://github.com/user-attachments/assets/14b2d9b9-4af7-4190-a05b-91ee477972da" />
<br><br>
2. По умолчанию разрешаю входящие подключения на необходимые порты
<br><br>
 <img width="438" height="86" alt="image" src="https://github.com/user-attachments/assets/40b51b6c-aeec-4000-98b6-a0e09ff405b4" />
<br>
 <img width="450" height="83" alt="image" src="https://github.com/user-attachments/assets/db049f29-62f8-4a5b-8d07-8e9181f25f79" />
<br><br>
3. Запрещаю доступ к VM2 с IP-адреса VM1 (192.168.56.101)
<br><br>
 <img width="627" height="61" alt="image" src="https://github.com/user-attachments/assets/9c6be4cb-e203-4ecf-a8cd-9ec154e0bed3" />
<br><br>
4. Проверяю статус UFW
<br><br>
 <img width="774" height="370" alt="image" src="https://github.com/user-attachments/assets/9e7dfc54-c795-4b7f-a8df-f321d45d4d7a" />
<br><br>
5. Пытаюсь получить доступ к nginx и SSH с VM1
<br><br>
 <img width="953" height="677" alt="image" src="https://github.com/user-attachments/assets/5c94b558-5d1f-4b35-991f-4a80c210f50b" />
 <img width="819" height="533" alt="image" src="https://github.com/user-attachments/assets/1e47341d-70fc-41c0-babb-b1d3353eb827" />
<br><br>
Доступ не запрещен, потому что порядок запретов и разрешений неверный. Исправляю.
<br><br>
 <img width="741" height="763" alt="image" src="https://github.com/user-attachments/assets/268d7906-096f-453b-b442-8826608aaca3" />
 <img width="974" height="92" alt="image" src="https://github.com/user-attachments/assets/c8e24e0a-4b10-4226-8394-735f1dd53630" />
<br><br>
6. Сканирую VM2 с VM1 с помощью Nmap и убеждаюсь, что порты недоступны
<br><br>
 <img width="974" height="112" alt="image" src="https://github.com/user-attachments/assets/c640138c-9cc7-4166-9de9-a4ba6156ac11" />
<br><br>
<h3 align="center">Шаг 4: Открытие порта 80 на VM2</h3>
1. Разрешаю входящие подключения на порт 80 для всех IP
<br><br>
 <img width="428" height="147" alt="image" src="https://github.com/user-attachments/assets/ddc59ec7-a36c-401d-9bc4-988c4e279a13" />
<br><br>
2. Пытаюсь снова получить доступ к nginx с VM1
<br>
3. Повторно сканирую VM2 с VM1 с помощью Nmap
<br><br>
 <img width="955" height="958" alt="image" src="https://github.com/user-attachments/assets/f1ca60ae-5161-449b-926a-0e2232924ad4" />
<br><br>
Контрольные вопросы (позже надо ответить)
<br>
1. Какие методы сканирования Nmap вы использовали и в чем их особенности?
<br>
2. Как UFW блокирует трафик и как это отражается на результатах сканирования Nmap?
<br>
3. Почему после открытия порта 80 сервис nginx стал снова доступен с VM1?
<br>
4. Какие еще методы защиты можно использовать для обеспечения безопасности сервера?

