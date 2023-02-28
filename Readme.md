<h1>Тестовое задание от компании стек</h1>
    
    Задание должно быть выполнено на одном из предложенных языков: C++, Kotlin, Java, Python или JavaScript. В крайнем случае допускается выполнение на Delphi или C#

    Дана таблица с показаниями счетчиков электроэнергии за 2 квартал (апрель, май, июнь) в файле "Показания.csv"
    В таблице строка, содержащая номер квартиры - относится к квартирному счетчику. Строка, где № квартиры равен 0 - к общедомовому.
    Необходимо:
    1. Рассчитать потребление электроэнергии за период апрель-май и май-июнь для всех счетчиков (как разность соответствующих показаний). Сформировать новый файл "Потребление.csv", записать в него и исходные, и рассчитанные данные.
    2. Определить, в каком доме, возможно, переданы неверные показания. Критерий: сумма потребления по общедомовому счетчику за оба периода не равна сумме потребления за оба периода всех квартирных с
    
<h1>Развернуть проект</h1>
    
    Алгоритмические задачи выполнены на языке Python 3.10
    
    Установите виртуальное окружение:
        WIN - python -m venv venv
        Linux/Macos - python3 -m venv venv
    
    Активируйте его:
        WIN - venv/Scripts/activate
        Linux/Macos - source venv/bin/activate
    
    Установите файл с зависимостями:
        pip install -r requirements.txt 