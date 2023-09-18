from flask import Flask, render_template
from kubernetes import client, config
import logging
from datetime import datetime, timezone

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG)

@app.route('/')
def index():
    try:
        # Загрузка конфигурации k8s
        config.load_config()

        v1 = client.CoreV1Api()
        nodes = v1.list_node().items
        node_info = []
        for node in nodes:
            creation_time = node.metadata.creation_timestamp
            current_time = datetime.now(timezone.utc)
            days_passed = (current_time - creation_time).days
            name = node.metadata.name
            node_info.append({'name': name, 'days_passed': days_passed, 'creation_time': creation_time})
        return render_template('index.html', node_info=node_info)
    except Exception as err:
        logging.error(f"ERROR: {err}")
        return f"ERROR: {err}", 500

if __name__ == '__main__':
    app.run(debug=True)
