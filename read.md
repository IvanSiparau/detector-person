Данный проект предоставляет возможность детекцию людей на видеоролике.

Для развертывание проекта необхадимо выполнить следующие bash команды 


1. git clone https://github.com/IvanSiparau/detector-person.git
2. cd detector-person
3. python -m venv venv
4. venv\Scripts\activate (для Windows, source venv/bin/activate Linux / macOS)
5. pip install -r requirements.txt

После этого необхадимо запустить приложение, выполнив следующие команды

```python main.py --input путь_к_входному_видео.mp4 --output путь_к_выходному_видео.mp4```

К примеру, 

```python main.py --input crowd.mp4 --output output.mp4```
