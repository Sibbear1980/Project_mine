# тестирование модели эмоц. окраса текста из задания 3 https://github.com/Vika00224/URFU_Project_1/tree/main/HomeWork%203%20All

from fastapi.testclient import TestClient
from Api import app                        # импорт приложения из App.py

client = TestClient(app)


# тест 1
def test_predict():
    response = client.post("/predict/",
        json={"text": "It was a wonderful journey. We have visited many beautiful places and seen many sightings! I am happy!"}
    )
    json_data = response.json() 

    assert response.status_code == 200                 # проверка ответа приложения
    assert json_data['Результат:'] == 'позитивный :)'  # проверка правильности работы модели определения эмоц окраса текста

# тест 2
def test_predict():
    response = client.post("/predict/",
        json={"text": "I hate traffic jams"}
    )
    json_data = response.json() 

    assert json_data['Результат:'] == 'негативный (('

# тест 3
def test_predict():
    response = client.post("/predict/",
        json={"text": "Today spring has come"}
    )
    json_data = response.json() 

    assert json_data['Результат:'] == 'нейтральный'    
