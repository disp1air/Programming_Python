При вызове функции open возвращается новый объект файла, соединенный с внешним файлом. Объект файла обладает методами для чтения и записи данных и для выполнения различных операций над файлами. Кроме того, функция open предоставляет переносимый интерфейс к используемой файловой системе.

в Python 3.X строки типа str всегда представляют текст Юникода (символы ASCII или многобайтовые символы), а строки типов bytes и bytearray представляют простые двоичные данные.

Объект файла, возвращаемый функцией open, обладает методами для чтения данных (read, геadline, readlines), записи данных (write, writelines), освобождения системных ресурсов (close), перемещения по файлу (seek), принудительного выталкивания выходных буферов на диск (flush), получения соответствующего дескриптора файла (fileno) и других.

# Вывод в файлы
Чтобы создать новый файл, следует вызвать функцию open с двумя аргументами: внешним именем создаваемого файла и строкой режима “w” (от write – запись). Чтобы сохранить данные в файле, нужно вызвать метод write объекта файла со строкой, содержащей данные, которые нужно сохранить, а затем метод close, чтобы закрыть файл. Метод write вернет количество символов или байтов, записанных в файл.

В вызове функции open, первый аргумент может содержать необязательный полный путь к файлу. Если просто передать имя файла без указания пути, файл окажется в текущем рабочем каталоге Python. To есть он появится в том месте, откуда был запущен программный код. Если быть более точным, в случае отсутствия абсолютного пути в имени файла путь к нему определяется относительно текущего рабочего каталога.

При открытии в режиме w Python либо создает новый файл, если он еще не существует, либо стирает текущее содержимое файла, если он уже присутствует.

Закрытие. Использованный выше метод файла close завершает формирование содержимого файла и освобождает системные
ресурсы. Например, закрытие файла влечет выталкивание на диск буферизованных выходных данных.

Если необходимо обеспечить явное закрытие файла в любом случае, у вас есть два пути: наиболее типичный – использование инструкции try с предложением finally, потому что оно позволяет реализовать выполнение заключительных операций для любых типов исключений.

В последних версиях Python появилась инструкция with, обеспечивающая более краткий способ реализации заключительных операций для объектов определенных типов, включая закрытие файлов.

# Чтение из файлов
существует много способов чтения входного файла:
    file.read() - Возвращает строку, содержащую все символы (или байты), хранящиеся в файле.
    file.read(N) - Возвращает строку, содержащую очередные N символов (или байтов) из файла.
    file.readline() - Читает содержимое файла до ближайшего символа \n и возвращает строку.
    file.readlines() - Читает файл целиком и возвращает список строк.

read() и readlines() загружают в память сразу весь файл.
вызовы readline() и read(N) возвращают лишь часть файла (очередную строку или блок из N символов или байтов). Оба метода возвращают пустую строку по достижении конца файла.
итераторы файлов объединяют в себе удобство метода readlines() и экономное отношение к памяти метода readline(),
и на сегодняшний день являются наиболее предпочтительным способом построчного чтения текстовых файлов.

# Чтение строк с помощью итераторов файлов
В последних версиях Python объект файла включает итератор, который при каждом обращении извлекает только одну строку из файла в любых итерационных контекстах, включая циклы for и генераторы списков. Практическая выгода заключается в том, что теперь нет необходимости вызывать метод readlines в цикле for, чтобы построчно просканировать содержимое файла, – итератор читает строки автоматически:

                                    >>> file = open('data.txt')
                                    >>> for line in file: # нет необходимости вызывать readlines
                                        print(line, end='') # итератор каждый раз читает следующую строку

Более того – теперь файл можно открывать непосредственно в инструкции цикла, как временный, который будет автоматически закрыт сборщиком мусора после выхода из цикла (так как часто цикл – это единственная ссылка на объект файла):

                                    >>> for line in open('data.txt'): # еще короче: временный объект файла
                                    ... print(line, end='') # будет закрыт при утилизации автоматически

Кроме того, такая форма обхода строк в файле не вызывает загрузку всего содержимого файла в список строк, поэтому она более экономно расходует память при работе с большими текстовыми файлами.
по достижении конца файла методы чтения возвращают пустую строку, а итератор возбуждает исключение, чтобы прервать итерации.

# Другие режимы открытия файлов
Помимо режимов открытия файлов “w” и “r” (по умолчанию) большинством платформ поддерживается строка режима открытия “а”, означающая «append» (дополнение). В этом режиме вывода методы записи добавляют данные в конец файла, и вызов функции open не уничтожает текущее содержимое файла.

Функция open может принимать дополнительные аргументы. Чаще всего используются первые три аргумента – имя файла, режим открытия и размер буфера. Все они, кроме первого, являются необязательными: если они опущены, принимается режим открытия по умолчанию “r” (ввод) и разрешается полная буферизация.

# Инструменты для работы с каталогами
os.popen – она выполняет команду оболочки и возвращает объект файла, из которого можно прочесть вывод команды.
Строки, возвращаемые командой оболочки, содержат замыкающий символ конца строки, но его легко можно отсечь. Кроме того, функция os.popen возвращает итератор, точно такой же, как итератор объектов файлов:
                                    >>> for line in os.popen('dir /B'):
                                            print(line[:-1])

                                    >>> lines = [line[:-1] for line in os.popen('dir /B')]

Модуль glob
glob.glob, – инструмент, принимающий шаблон имени файла и возвращающий список (не генератор) имен файлов,
соответствующих этому шаблону.

                                    >>> glob.glob('*.py')

Если поиск нужно осуществлять в каталоге, отличном от текущего рабочего каталога, в шаблон нужно включить путь к каталогу.

Вообще функция glob несколько мощнее, чем здесь описано. Например, ее можно использовать для получения списка имен из нескольких каталогов, так как каждый уровень в передаваемом пути к каталогу также можно определить в виде шаблона:

                                    >>> for path in glob.glob(r'PP3E\Examples\PP3E\*\s*.py'): print(path)

                                    PP3E\Examples\PP3E\Lang\summer-alt.py
                                    PP3E\Examples\PP3E\Lang\summer.py
                                    PP3E\Examples\PP3E\PyTools\search_all.py

Здесь мы получили список имен файлов, соответствующих шаблону s*.py, из двух разных каталогов. Так как в качестве имени предшествующего каталога был использован групповой символ *, Python перебрал все возможные пути к файлам.

Функция os.listdir
Функция listdir из модуля os является еще одним способом получить список имен файлов. Она принимает простую строку с именем каталога и возвращает список, содержащий имена всех файлов в каталоге – как просто файлов, так и вложенных под-
каталогов.

Функция обхода дерева os.walk
os.walk является функцией-генератором – для каждого каталога в дереве она возвращает кортеж из трех элементов,
содержащий имя текущего каталога, а также списки всех файлов и всех подкаталогов в текущем каталоге. В каждой итерации функция перемещается к следующему подкаталогу, а инструкция цикла выполняет свое тело для следующего уровня в дереве (например, открывает все файлы в этом подкаталоге и производит поиск по их содержимому).

Если вам будет интересно узнать, что в действительности происходит внутри генератора os.walk, попробуйте несколько раз вызвать его метод __next__ (или передать его встроенной функции next), как это автоматически делается циклом for, – каждый раз вы будете перемещаться к очередному подкаталогу в дереве.
