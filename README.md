Запускаем:
docker compose up --build

Streamlit: http://localhost:8501
Kafka UI: http://localhost:8080

В Streamlit загрузите CSV и нажмите «Отправить строки в Kafka». Каждая строка будет отправлена отдельным JSON-сообщением в топик `transactions`. ML-сервис читает этот топик, применяет модель и пишет результаты в `scoring`. Оба топика видны в Kafka UI.
