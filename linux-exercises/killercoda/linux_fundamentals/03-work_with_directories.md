<h1>Урок 3. Работа с каталогами</h1>


<br>
<h2>1. Создание каталогов</h2>
<pre>
Для начала давайте посмотрим, что у нас есть в текущем каталоге.

<img width="377" height="74" alt="image" src="https://github.com/user-attachments/assets/fc2e22eb-706b-4cd3-ad9e-548188ce4f2f" />

Чтобы создать каталог, нам нужно использовать команду mkdir .

Хорошо, давайте создадим структуру.

mkdir myfirstdirectory создает каталог с указанным именем.

<img width="411" height="103" alt="image" src="https://github.com/user-attachments/assets/ddef7ba3-0765-4498-b188-1a9c286fda6e" />

Теперь представьте, что мы хотим создать несколько каталогов с похожими именами. 
Мы можем создавать каталоги, последовательно выполняя одну команду, и повторить это несколько раз. 
Но есть способы получше.

Давайте создадим 10 каталогов, начиная с testdir1 и заканчивая testdir10. 
Как сделать это с помощью одной команды?

<img width="408" height="273" alt="image" src="https://github.com/user-attachments/assets/a4213614-4734-46aa-abad-52d536e3aa08" />

С помощью этого синтаксиса мы можем создать 10 каталогов с именами, содержащими числа от 1 до 10. Очень удобно.

ок, другой подход.

<img width="458" height="325" alt="image" src="https://github.com/user-attachments/assets/3c9052ca-bde9-4a7f-985f-8d39d68153f3" />

Так мы создали три разных каталога.

Хорошо, давайте создадим что-нибудь посложнее. 
Чтобы создать более глубокую структуру, нам нужно использовать аргумент -p. 
Это позволяет нам создать всю структуру, не создавая родительский каталог в качестве первого шага.

mkdir -p parentdir/childdir{01..100}

Что мы здесь делаем? С помощью -p мы позволили системе создать родительский каталог, а вторую часть мы уже знаем. 
В каталоге parentdir мы создали 100 файлов, от childdir001 до childdir100. 
Обратите внимание, как красиво это отформатировала система!
Мы указали 01, но система создала каталоги с тремя цифрами, как в childdir100.

Итак, мы создали структуру. Что у нас есть в parentdir? Как это проверить? 
Мы узнаем об этом больше в следующем разделе, а пока давайте посмотрим parentdir

<img width="373" height="1244" alt="image" src="https://github.com/user-attachments/assets/ccfe06fc-bd06-4699-8390-72b6be77968d" />

Таким образом мы можем вывести список файлов в другом каталоге.
</pre>


<br>
<h2>2. Перемещение между каталогами</h2>
<br>
<pre>
Мы уже знаем, что находится внутри parentdir. Давайте перейдем туда. 
Чтобы сменить каталог, нам нужно использовать команду cd . 
Как и следовало ожидать, она называется Change Directory .

<img width="819" height="257" alt="image" src="https://github.com/user-attachments/assets/14f72cd7-62d8-44ab-a5f1-df02a59ff6d4" />

Есть еще одна команда, которая позволяет узнать, где мы находимся в данный момент pwd . 
Эта команда показывает ваш текущий рабочий каталог.

<img width="209" height="54" alt="image" src="https://github.com/user-attachments/assets/61a8b8c6-7547-49be-973f-ff449c2d5f72" />

Мы можем вернуться в предыдущий каталог, набрав cd .. 

<img width="219" height="70" alt="image" src="https://github.com/user-attachments/assets/09fa5cd6-732d-476b-af08-f1c3cc32fbc9" />

Надеюсь, вы помните из предыдущего урока, что означает .. . 
Это родительский каталог по отношению к текущему.

Давайте спустимся еще ниже

<img width="290" height="37" alt="image" src="https://github.com/user-attachments/assets/1b9bf246-b4f4-430d-bde9-8239aae89c54" />

Где мы сейчас?

<img width="292" height="57" alt="image" src="https://github.com/user-attachments/assets/1eb40ebd-5727-448a-9cfb-606d9a0400cb" />

Как видите, мы можем перемещаться по множеству каталогов, используя / в качестве разделителя.

Как это работает? Это будет объяснено на следующей странице.

Если мы хотим перейти в домашний каталог (тот, с которого мы начали), 
мы можем сделать это уже известным способом: cd .. и снова cd .., но это не очень удобно. 
Мы можем объединить .. так же, как мы заходим в этот каталог:

<img width="323" height="70" alt="image" src="https://github.com/user-attachments/assets/dfa9b08f-e140-4ef4-a62d-750e2e914f05" />

Ну вот, мы снова здесь.

Хорошо, теперь перейдем к другой теме, но сначала создадим еще один каталог

<img width="200" height="36" alt="image" src="https://github.com/user-attachments/assets/32c148c6-e211-4bcd-b651-a9a8121c6305" />

Мы создали каталог root . Теперь перейдем в него

<img width="182" height="41" alt="image" src="https://github.com/user-attachments/assets/371b9b45-11c6-443c-b046-9f59ba1ad730" />

Пожалуйста, посмотрите, где мы находимся:

<img width="168" height="57" alt="image" src="https://github.com/user-attachments/assets/6c20a773-fe77-4a7a-976c-956553e7a63f" />

У нас такая структура: /root/root.

Хорошо, теперь вернемся

<img width="184" height="38" alt="image" src="https://github.com/user-attachments/assets/575f5452-6a88-440b-986c-33e37740eb3f" />

Теперь сделаем почти то же самое

<img width="172" height="41" alt="image" src="https://github.com/user-attachments/assets/15281ac7-14ac-4a70-a6f5-b4edcc5a403a" />

Где мы сейчас?

<img width="141" height="56" alt="image" src="https://github.com/user-attachments/assets/1e4856d8-2164-4bfc-a543-462d66402e1f" />

В чем разница? Очевидно, вы заметили символ / . Что все это значит?

В файловых системах Linux корень, «первая точка», — это root каталог. 
Этот корневой каталог представлен символом /. 
Все, что находится на верхнем уровне файловой системы, находится в каталоге / .

Давайте посмотрим на картинку ниже.

<img width="1500" height="780" alt="directories" src="https://github.com/user-attachments/assets/305e5291-daff-4ed2-97dd-0cd6fdd6483f" />

Предположим, я нахожусь в каталоге /home/user2/dir1 . 
Если я хочу перейти в каталог /var/log/nginx , я могу сделать это несколькими способами.

cd ../../../var/log/nginx
cd /var/log/nginx

В чем разница? Во втором варианте мы используем путь absolute . 
Мы ссылаемся на journey through directories в главной, центральной точке системы — root, /. 
Когда мы ставим / в начале пути, это сообщает системе, что мы хотим использовать абсолютный путь.

В первом примере мы используем путь relative . Это просто означает, что мы перемещаемся из текущей позиции.

Таким образом, если мы находимся в нашем домашнем каталоге, который является корневым... 
Что ж, не удивляйтесь. Мы вошли в систему как пользователь root. 
root Пользователь — самая важная сущность во всей системе Linux, и его домашний каталог находится по адресу /root. 
У других пользователей домашние каталоги находятся по адресу /home. 
Таким образом, когда вы находитесь в каталоге /root, то при вводе cd /root результат будет отличаться от cd root.

</pre>


<br>
<h2>3. Возвращаемся домой!</h2>
<br>
<pre>
Где бы мы ни находились в системе Linux, у нас есть несколько способов вернуться домой. 
Кто-то говорит, что все дороги ведут в Рим, и в Linux это почти так :)

Итак, во-первых, если вы помните свой домашний каталог, используйте его

<img width="222" height="124" alt="image" src="https://github.com/user-attachments/assets/b5611138-fd40-439a-aa25-4e39e75d6183" />

но это не самый удобный способ.

Есть встроенная переменная $HOME. Эта переменная содержит путь к домашнему каталогу текущего пользователя.

<img width="226" height="123" alt="image" src="https://github.com/user-attachments/assets/08b97e78-bed2-477d-b953-5e097dede22b" />

Кстати, мы можем вывести значение этой переменной, используя echo $HOME

<img width="187" height="58" alt="image" src="https://github.com/user-attachments/assets/4ffc8f61-88f6-407b-9cd0-69702b5d8176" />

Но $HOME — это слишком длинно. Можно использовать что-нибудь покороче — ~

<img width="201" height="126" alt="image" src="https://github.com/user-attachments/assets/ae012d60-b640-4bdb-a0ba-92bbfa20bd29" />

И наконец, самый короткий вариант...

<img width="191" height="125" alt="image" src="https://github.com/user-attachments/assets/4e15b87a-b7b8-4e73-a52c-30a67ec28ec6" />

Да, достаточно просто cd , чтобы вернуться в домашний каталог.
</pre>


<br>
<h2>4. Удаление каталогов</h2>
<br>
<pre>
Сначала удалим каталог root.

<img width="423" height="378" alt="image" src="https://github.com/user-attachments/assets/23d36fd1-bd5c-4f5d-a0b3-115b92e5b0a8" />

Теперь удалим все каталоги testdir.

<img width="430" height="205" alt="image" src="https://github.com/user-attachments/assets/6b1a5456-cb7a-4947-aa9f-8c4fa9b48633" />

Да, мы можем использовать тот же синтаксис, что и при создании этих каталогов :)

Хорошо, теперь удалим каталог parentdir.

<img width="403" height="56" alt="image" src="https://github.com/user-attachments/assets/08b56649-ab75-4717-8d73-2524e185c5a3" />

Хм. Не получается. Каталог не пуст. Хорошо, у нас есть способ. 
Помните аргумент -p команды mkdir?

<img width="403" height="53" alt="image" src="https://github.com/user-attachments/assets/5ddfbd70-d1de-441e-b74b-1e6458917d56" />

Нет.

У нас есть каталог под названием maindir, давайте заглянем внутрь

<img width="187" height="56" alt="image" src="https://github.com/user-attachments/assets/d6050105-d925-425d-a1f9-80a958e8b4c6" />

Итак, мы можем удалить родительский каталог, только если он пуст. Тогда это сработает

<img width="420" height="222" alt="image" src="https://github.com/user-attachments/assets/4984f430-3785-4d46-8555-fdbaa6b273c5" />

Чтобы удалить весь parentdir каталог, нам нужно выполнить другую команду, rm. 
Эта команда работает с файлами. А поскольку в Linux все является файлами, она должна работать и с каталогами.

<img width="331" height="57" alt="image" src="https://github.com/user-attachments/assets/d7096e2a-83b4-47f7-b2cf-8ed9c2bcbca6" />

Но... это не.

Хорошо, давайте... сделаем это

<img width="232" height="71" alt="image" src="https://github.com/user-attachments/assets/1d99c9f9-49fa-4833-8ab1-1fab5cd63d82" />

Хм... Если вам кажется, что это не похоже на то, как должен работать умный Linux...

Вы правы.

У нас есть anotherparentdir с такой же структурой. 
Давайте сделаем все правильно. И рискованно.

<img width="816" height="377" alt="image" src="https://github.com/user-attachments/assets/ed56670c-ec38-41ff-99b0-6cf52b0da10f" />

Ух ты, вот оно! Но... раньше это не работало с rm

Теперь мы использовали несколько аргументов

-r означает рекурсивный обход каталогов (и обработку всех элементов как файлов)
-f - принудительно. Другими словами, не спрашивайте, а просто предположите, что пользователь знает, что делает.
Вот почему это рискованная команда.

Попробуйте rm -rf / и прочтите уведомление. 

<img width="379" height="75" alt="image" src="https://github.com/user-attachments/assets/805913a4-c6a4-4bad-b79a-999951ed24c3" />

В наши дни Linux старается быть осторожным с пользователями, и эта команда — понимаете, почему?

</pre>


<br>
<h2>5. Тест</h2>
<br>
<details>
<summary>Вопрос 1: Как проверить текущий каталог? <br>
</summary><br><b>
Ответ: pwd
</b></details>
<br>

<details>
<summary>Вопрос 2: Я нахожусь в /home/user1. Я хочу перейти в /home/user2 по абсолютному пути. Как мне это сделать? <br>
</summary><br><b>
Ответ: cd /home/user2
</b></details>

<br>
<details>
<summary>Вопрос 3: что означает ~ ? <br>
1) корневой каталог <br>
2) домашний каталог <br>
3) временный каталог <br>
4) предыдущий каталог file <br>
</summary><br><b>
Ответ: домашний каталог
</b></details>

<details>
<summary>Вопрос 4. Я хочу перейти в свой домашний каталог. Выберите все подходящие варианты <br>
1) cd HOME <br>
2) cd <br>
3) cd /home/mydir <br>
4) cd $HOME <br>
5) cd ~ <br>
</summary><br><b>
Ответ: Варианты 2, 4 и 5
</b></details>
<br>

<details>
<summary>Вопрос 5. Я хочу перейти в свой домашний каталог, используя $HOME, а затем в каталог app/tests: <br>
</summary><br><b>
Ответ: cd $HOME/app/tests
</b></details>

<br>
<details>
<summary>Вопрос 6. Я хочу создать 100 каталогов с именами от hello001 до hello100. Какая для этого нужна команда? <br>
</summary><br><b>
Ответ: mkdir hello{001..100}
</b></details>

<br>
<details>
<summary>Вопрос 7. Чтобы удалить все каталоги из /directory, нужно выполнить (не используйте команду rm): <br>
</summary><br><b>
Ответ: rmdir /directory/*
</b></details>

<br>
<details>
<summary>Вопрос 8. Как удалить все без подтверждения из /mydir/somedir? 
Предположим, вы находитесь в /mydir и somedir тоже нужно удалить (не используйте абсолютный путь). <br>
</summary><br><b>
Ответ: rm -rf somedir
</b></details>



