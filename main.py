from flask import Flask, render_template
from kubernetes import client, config
import logging

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(filename='app.log', level=logging.DEBUG)

@app.route('/')
def index():
    try:
        # Загрузка конфигурации k8s
        config.load_config()

        v1 = client.CoreV1Api()

        # Получение информации о нодах
        nodes = v1.list_node().items

        node_info = []
        for node in nodes:
            uptime = node.metadata.creation_timestamp
            name = node.metadata.name
            node_info.append({'name': name, 'uptime': uptime})

        return render_template('index.html', node_info=node_info)

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        return f"Ошибка: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
