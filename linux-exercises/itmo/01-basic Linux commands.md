<h2 align="center">Изучение базовых команд Linux</h2>
Команды:
<ul>
  <li>$ pwd - определить текущий каталог.</li>
  <li>$ cd [имя каталога] — осуществить переход в заданный каталог.</li>
  <li>$ ls [имя каталога] - просмотреть список файлов и подкаталогов.</li>
  <li>$ mkdir [имя каталога] — создать каталог с заданным именем.</li>
  <li>$ cp <имя файла 1> <имя файла 2> - скопировать файл «имя файла 1» в файл «имя файла 2», например: cp first.txt copy1.txt.</li>
  <li>$ mv <имя файла 1> <имя файла 2> - переименовать файл «имя файла 1» в файл «имя файла 2», например: mv first.txt orig.txt.</li>
  <li>$ ln «имя файла» «имя ссылки» - создать жёсткую ссылку «имя ссылки» на файл «имя файла». Пример: ln orig.txt copy2.txt.</li>
  <li>$ ln -s «имя файла» «имя ссылки» - создать символическую ссылку «имя ссылки» на файл «имя файла». Пример: ln -s orig.txt copy2.txt.</li>
  <li>$ rm <имя файла> - удалить файл.</li>
  <li>$ touch <имя файла> - создание файла.</li>
  <li>$ man <название команды> - получение справочной документации о выбранной команде.</li>
</ul>
Ознакомлюсь с возможностями команды pwd
<br><br>
<img width="191" height="33" alt="image" src="https://github.com/user-attachments/assets/eaf17f77-9b2d-47c4-9498-cc979d5bfe93" />
<img width="1202" height="531" alt="image" src="https://github.com/user-attachments/assets/f5cb0b69-aba0-4f2e-a78f-4c769507c447" />
<br><br>
Определяю текущий каталог, в котором нахожусь командой pwd
<br><br>
<img width="160" height="39" alt="image" src="https://github.com/user-attachments/assets/b9df387a-e494-4790-96ad-fd476bdd5e8f" />
<br><br>
Перехожу в корневой каталог командой cd
<br><br>
<img width="165" height="40" alt="image" src="https://github.com/user-attachments/assets/03a5f048-369d-4a6f-bf1c-26bc72e150fb" />
<br><br>
Просматриваю содержимое корневого каталога командой ls
<br><br>
<img width="1141" height="42" alt="image" src="https://github.com/user-attachments/assets/88c6250b-5e3b-47c7-b93b-87475480c1ae" />
<br><br>
Возвращаюсь в домашний каталог, используя команду cd без параметров
<br><br>
<img width="148" height="43" alt="image" src="https://github.com/user-attachments/assets/821abbd3-4445-4bbd-8ff0-d642d429d23c" />
<br><br>
Создаю каталог «test», используя команду mkdir
<br><br>
<img width="211" height="21" alt="image" src="https://github.com/user-attachments/assets/19c08b85-28d1-43ec-ab19-5738d302ac96" />
<br><br>
Перехожу в каталог «test», используя команду cd
<br><br>
<img width="185" height="20" alt="image" src="https://github.com/user-attachments/assets/95dd7455-b7bd-45a7-a2f1-00ec9624358a" />
<br><br>
Просматриваю содержимое каталога, используя команду ls
<br><br>
<img width="190" height="41" alt="image" src="https://github.com/user-attachments/assets/cd76b063-e0a4-46d0-92f2-165cd28c0002" />
<br><br>
Создаю каталог «test2», используя команду mkdir
<br><br>
<img width="260" height="21" alt="image" src="https://github.com/user-attachments/assets/178a84db-b7c7-435f-b7aa-0b0a45721639" />
<br><br>
Создаю файл «text» в каталоге «test2» используя команду touch
<br><br>
<img width="317" height="19" alt="image" src="https://github.com/user-attachments/assets/1af4a2ae-e25b-4603-a64b-80f86f6c97c3" />
<br><br>
Переименовываю файл «text» в «textSIT» используя команду mv
<br><br>
<img width="421" height="22" alt="image" src="https://github.com/user-attachments/assets/bca4df2a-5ad2-4454-a5ad-00c4c725a7a8" />
<br><br>
Копирую файл «textSIT» в каталог «test2» под именем «copy.txt», используя команду cp
<br><br>
<img width="452" height="20" alt="image" src="https://github.com/user-attachments/assets/5c22f7bb-6a54-49d3-82e9-d12d0c82b1a8" />
<br><br>
Создаю жесткую ссылку «link» на файл «copy.txt» используя команду ln
<br><br>
<img width="431" height="22" alt="image" src="https://github.com/user-attachments/assets/97cbf20d-611d-4064-b87c-fa56bb95ca44" />
<br><br>
Создаю символическую ссылку «simlink» на файл «copy.txt» используя команду ln
<br><br>
<img width="557" height="23" alt="image" src="https://github.com/user-attachments/assets/396aaff3-fcb7-4904-b3d1-bc2261dd96a2" />
<br><br>
Просмотриваю результаты в текущем каталоге при помощи команды ls с аргументами la
<br><br>
<img width="667" height="167" alt="image" src="https://github.com/user-attachments/assets/967cfc64-cefe-4b8b-a37d-622773fd420e" />
<br><br>
Удаляю созданные файлы и ссылки используя команду rm
<br><br>
<img width="373" height="114" alt="image" src="https://github.com/user-attachments/assets/4fd8c452-39b9-432c-accd-5f7ae412be86" />
<br><br>
<ol>
  <li>Чем отличается вывод команд ls -F и ls -la?</li>
  <li>С помощью какой команды и как можно переместить файл в другой каталог?</li>
  <li>Какие действия вы совершаете, нажимая на кнопки «стрелка вверх» и «стрелка вниз»?</li>
  <li>Куда вы переходите, выполнив команду cd без параметров?</li>
  <li>Как посмотреть, какие еще параметры можно задать команде ls?</li>
  <li>Что такое «жесткая ссылка»?</li>
  <li>Что такое «символическая ссылка»?</li>
  <li>Как осуществить просмотр подкаталогов и их содержимого ?</li>
  <li>Как осуществить вывод содержимого каталога с запятыми в качестве разделителя?</li>
  <li>Как осуществить просмотр скрытых файлов в домашнем каталоге?</li>
  <li>Как осуществить создание нового каталога и необходимых подкаталогов рекурсивно?</li>
  <li>Как осуществить рекурсивное копирование всех файлов из одного каталога в другой?</li>
  <li>Как осуществить рекурсивное копирование всех файлов и подкаталогов из одного каталога в другой?</li>
  <li>Как рекурсивно удалить все файлы и подкаталоги в определенном каталоге?</li>
</ol>








