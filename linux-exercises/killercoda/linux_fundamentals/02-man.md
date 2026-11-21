<h1>Урок 2: Ваш лучший друг — man</h1>

<pre>
  Linux не прощает ошибок, но дает нам много подсказок. 
  У каждой (или почти у каждой) команды есть своя справка, мы уже изучили ее для ls команды.

  Теперь пришло время познакомиться с очень мощным инструментом — man.
</pre>

<br>
<h2>1. Первый взгляд на команду ls</h2>
<pre>
Начнем с простой man команды. 
  
Что ж, она дает нам подсказку. Давайте воспользуемся ею.

<img width="259" height="52" alt="image" src="https://github.com/user-attachments/assets/24b9ec5f-4aeb-4854-97f2-53e7abb82868" />
<img width="856" height="910" alt="image" src="https://github.com/user-attachments/assets/e306f894-6e72-4e88-b7a2-36b6ede60231" />

Теперь мы можем потратить как минимум 10 минут на изучение того, что представляет собой man команда, всех ее аргументов, опций и возможностей.

Попробуйте перемещаться по документу с помощью стрелок. Когда закончите, нажмите q , чтобы выйти.

Хорошо, теперь давайте применим полученные знания и узнаем больше о ls.

<img width="182" height="36" alt="image" src="https://github.com/user-attachments/assets/86a53f87-d61b-4442-8dad-4cafb75871a7" />
<img width="861" height="1250" alt="image" src="https://github.com/user-attachments/assets/aa8b060f-d09b-48a9-b29c-b884538cdcf8" />

</pre>


<br>
<h2>2. Получение дополнительной информации</h2>
<br>
<pre>
Теперь мы знаем, как получить доступ к man, но это только первая страница.

У нас есть возможность перемещаться по страницам (или разделам). Но какие разделы нам доступны?

       1   Executable programs or shell commands
       2   System calls (functions provided by the kernel)
       3   Library calls (functions within program libraries)
       4   Special files (usually found in /dev)
       5   File formats and conventions eg /etc/passwd
       6   Games
       7   Miscellaneous  (including  macro  packages  and  conventions), e.g.
           man(7), groff(7)
       8   System administration commands (usually only for root)
       9   Kernel routines [Non standard]

Хорошо, давайте попробуем получить команды системного администрирования для ls команды.

<img width="264" height="59" alt="image" src="https://github.com/user-attachments/assets/255a9ff2-d2c8-4d01-ae69-b31303af60c1" />

Что ж, для ls нет страницы 8. Как проверить, какие разделы/страницы нам доступны?

<img width="332" height="55" alt="image" src="https://github.com/user-attachments/assets/c57f1ebe-cfb7-4178-95dc-3664c4c8f2ea" />

Хорошо, теперь мы видим, что ls содержит только 1 страницу.

Хорошо, давайте воспользуемся другой командой. На этот раз это будет intro. Эта команда представлена во введении к командам Linux.

<img width="552" height="172" alt="image" src="https://github.com/user-attachments/assets/27985108-4819-4adb-b12d-ac8673bd3ee4" />

</pre>


<br>
<h2>3. Список всех файлов</h2>
<br>
<pre>
У нас есть возможность быстро проверить, что делает команда.
  
whatis ls показывает краткое описание функционала.

То же самое можно сделать с помощью man.

<img width="334" height="90" alt="image" src="https://github.com/user-attachments/assets/f8b85e2b-1cc2-4dbe-9d17-78e47065c14f" />


man -k ls ищет указанную команду во всех справочных страницах и выводит их все.

<img width="755" height="1244" alt="image" src="https://github.com/user-attachments/assets/b6f524ce-9ffd-4f60-9928-682de1807156" />

man -w ls возвращает местоположение файла, из которого отображается страница.

<img width="206" height="52" alt="image" src="https://github.com/user-attachments/assets/362c0980-26f2-4820-a8bc-fbc19d92e170" />

Поздравляем
Теперь вы можете легко использовать man!
</pre>
