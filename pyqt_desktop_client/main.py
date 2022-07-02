import sys
from threading import Thread

from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLineEdit, QLabel)
import aiohttp
import asyncio
import requests
import json


class MainUiClass(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()

        self.label_path = QLabel("укажите количество изображений")
        self.line_edit_path = QLineEdit("20")

        self.label_result = QLabel("")
        self.btn_start = QPushButton("запуск")
        self.btn_start.clicked.connect(self.start_action)

        self.layout.addWidget(self.label_path, 0, 0)
        self.layout.addWidget(self.line_edit_path, 0, 1)

        self.layout.addWidget(self.label_result, 1, 0)
        self.layout.addWidget(self.btn_start, 1, 1)

        self.setGeometry(640, 480, 640, 480)
        self.setWindowTitle('PyQt5')
        self.setLayout(self.layout)
        self.show()

    def start_action(self):
        try:
            count = int(self.line_edit_path.text())

            new_thread = Thread(target=MainUiClass.sync_get_request, args=[count, self])
            new_thread.start()
        except Exception as error:
            print(error)
            count = 1
        print(f"count = {count}")

    @staticmethod
    def sync_get_request(count, obj):
        url = f'http://127.0.0.1:8000/get_request/?count={count}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        print(response)
        if response.status_code == 200:
            data = str(response.content.decode())
            print(f"data: {data}")

            json_data = json.loads(response.content)
            obj.label_result.setText(json_data["result"])
        else:
            print("Ошибка получения данных")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUiClass()
    sys.exit(app.exec_())
