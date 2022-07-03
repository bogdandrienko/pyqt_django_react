import sys
import aiohttp
import asyncio
import requests
import json
from threading import Thread
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLineEdit, QLabel, QCheckBox)


class MainUiClass(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()

        self.label_path = QLabel("укажите количество изображений")
        self.line_edit_path = QLineEdit("20")

        self.label_result = QLabel("")

        self.check_box_sync = QCheckBox("async")
        self.btn_start = QPushButton("запуск")
        self.btn_start.clicked.connect(self.start_action)

        self.layout.addWidget(self.label_path, 0, 0)
        self.layout.addWidget(self.line_edit_path, 0, 1)

        self.layout.addWidget(self.label_result, 1, 0)
        self.layout.addWidget(self.check_box_sync, 1, 1)
        self.layout.addWidget(self.btn_start, 1, 2)

        self.setGeometry(640, 480, 640, 480)
        self.setWindowTitle('PyQt5')
        self.setLayout(self.layout)
        self.show()

    def start_action(self):
        try:
            count = int(self.line_edit_path.text())
            if not self.check_box_sync.isChecked():
                new_thread = Thread(target=MainUiClass.sync_get_request, args=[count, self])
                new_thread.start()
            else:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(MainUiClass.async_post_request(count, self))
        except Exception as error:
            print(error)

    @staticmethod
    def sync_get_request(count, obj):
        url = f'http://127.0.0.1:8000/get_request/?count={count}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            obj.label_result.setText(json.loads(response.content)["result"])
        else:
            print("Ошибка получения данных")
            obj.label_result.setText("Ошибка получения данных")

    @staticmethod
    async def async_post_request(count, obj):
        # url = f'http://127.0.0.1:8000/get_request/?count={count}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36',
        }
        # async with aiohttp.ClientSession() as session:
        #     async with session.get(url, headers=headers) as response:
        #         text = await response.text()
        #         json_data = json.loads(text.encode())
        #         obj.label_result.setText(json_data["result"])

        for i in range(1, count):
            async with aiohttp.ClientSession() as session:
                async with session.get("https://picsum.photos/370/250") as response:
                    data = await response.read()

                    async with aiohttp.ClientSession() as session1:
                        async with session1.post(
                                url="http://127.0.0.1:8000/post_request/",
                                data={"title": f"image {i}", "image": data},
                                # data=form,
                                headers=headers
                        ) as response1:
                            data1 = await response1.read()
                    # with open("temp/test.jpg", "wb") as f:
                    #     f.write(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUiClass()
    sys.exit(app.exec_())
