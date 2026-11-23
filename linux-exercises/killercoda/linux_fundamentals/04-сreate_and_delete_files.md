<h1>Урок 4: Создание и удаление файлов</h1>


<br>
<h2>1. Создание файла</h2>
<pre>
Чтобы создать пустой файл в Linux, нужно использовать команду touch . Давайте сделаем это.

<img width="216" height="40" alt="image" src="https://github.com/user-attachments/assets/77f0ea63-7ede-4014-9e1e-4344761fcd66" />

Получилось?

<img width="333" height="56" alt="image" src="https://github.com/user-attachments/assets/f893322b-8da9-4964-9ed5-40dbae9b7541" />

Да, файл существует. Мы также видим, что файл имеет 0 размер, другими словами, он пуст.

Конечно, как и в предыдущем сценарии, мы можем создать несколько файлов.

<img width="267" height="21" alt="image" src="https://github.com/user-attachments/assets/d34b99d6-2a61-41ce-9dca-5d4e42363702" />

Давайте воспользуемся подстановочным знаком * для вывода списка всех файлов

<img width="767" height="206" alt="image" src="https://github.com/user-attachments/assets/21c691b9-9c86-48e2-9a61-6d9be94560c1" />

Это не совсем то, что нам нужно, но если * означает любую строку, 
то иногда нам нужно вывести список конкретных подгрупп. Давайте сначала подготовимся.

<img width="262" height="36" alt="image" src="https://github.com/user-attachments/assets/05f239b6-c302-4372-b8e2-7db7bc12125f" />

Хорошо, теперь нам нужно вывести только список try1 и try2 . 
Если я использую ls try* мы получим все три файла.

<img width="167" height="57" alt="image" src="https://github.com/user-attachments/assets/20990f95-d2a4-42c0-8a80-0ca38cb150f8" />

Вместо * можно использовать ?. Этот знак означает any single character.

Давайте попробуем

<img width="168" height="59" alt="image" src="https://github.com/user-attachments/assets/e8b9b1e2-8575-4f0d-a945-14592c7c7b3b" />


Да, это оно.

Давайте теперь создадим какую-нибудь структуру.

mkdir testdir
touch testdir/mytest{01..1000} testdir/file{01..1000}

Вы знаете, что мы сделали?
</pre>


<br>
<h2>2. Удаление файла</h2>
<br>
<pre>
Мы уже знаем соответствующую команду. Это rm.

Мы можем удалить один файл

<img width="176" height="41" alt="image" src="https://github.com/user-attachments/assets/51ef9980-0783-4a52-ba4f-eea96c2d39a1" />


Мы можем удалить более одного файла

<img width="198" height="36" alt="image" src="https://github.com/user-attachments/assets/3abffcf9-113f-4232-9fd1-a7ce7d10cd30" />

Очевидно, что мы можем удалить несколько файлов

<img width="307" height="45" alt="image" src="https://github.com/user-attachments/assets/b46daf7a-cc17-4338-bd72-cbe54d319874" />

И, да, мы можем удалить все файлы, каталоги, всю структуру целиком

<img width="214" height="38" alt="image" src="https://github.com/user-attachments/assets/ce982f8b-4c6d-4fec-9dc4-3c06eea4db5d" />

Что -rf означает? Это объясняется в предыдущем уроке.
</pre>


<br>
<h2>3. Создание файла с помощью vim</h2>
<br>
<pre>
Хорошо, vim не является частью этого урока. 
Но я хочу убедиться, что мы понимаем, что touch — это не единственный способ создания файлов.

Давайте попробуем

<img width="208" height="20" alt="image" src="https://github.com/user-attachments/assets/ee0a54c7-f1d3-43f7-bc3a-faa1a83bc5ac" />
<img width="884" height="1253" alt="image" src="https://github.com/user-attachments/assets/0851fd02-5884-4315-be08-b9109aae734e" />

Мы открыли vim редактор. Об этом мы поговорим позже, а сейчас достаточно следовать инструкциям.

Чтобы начать вводить текст в редакторе (перейти в режим вставки), нажмите i .

<img width="885" height="78" alt="image" src="https://github.com/user-attachments/assets/230a6709-4994-4198-8530-855d4a94684e" />

Вставьте какой-нибудь текст, например

<img width="883" height="91" alt="image" src="https://github.com/user-attachments/assets/edf0e266-8339-428a-a4c4-e0313130812e" />

Теперь нажмите ESC для перехода в командный режим и введите :wq

<img width="886" height="61" alt="image" src="https://github.com/user-attachments/assets/b0dd6560-026e-4f75-bf56-fce6051499b6" />

Вы вышли из vim и теперь можете проверить файл

<img width="353" height="53" alt="image" src="https://github.com/user-attachments/assets/3ea3883b-0936-4f84-b9bc-bcf5bd1c4942" />

Да, у нас есть файл, и он не пустой!

Этот урок был очень коротким. 
В создании и удалении файлов нет ничего волшебного. 
Конечно, touch и vim — не единственные способы создания файлов.
</pre>
