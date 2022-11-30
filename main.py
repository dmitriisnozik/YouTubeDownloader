from __future__ import unicode_literals
import sys
import os
import yt_dlp
from PyQt6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from design import Ui_MainWindow
import threading


class Main(QMainWindow):
    video_url = None

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")
        
        self.ui.select_btn.clicked.connect(self.chosen_video)
        self.ui.download_btn.clicked.connect(self.download_start)
        self.ui.pushButton.clicked.connect(self.change_dir)

    def chosen_video(self):
        global video_url

        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(self.ui.select_link.text(), download=False)
        self.ui.selected_video.setText(info_dict.get('title', None))
        video_url = self.ui.select_link.text()

    def change_dir(self):
        dir_name = QFileDialog.getExistingDirectory()
        os.chdir(dir_name)
        self.ui.pushButton.setText(dir_name)

    def download_start(self):
        global video_url

        def start():
            format_dict = {
                'Audio only (best)': 'bestaudio',
                'Audio only (worst)': 'worstaudio',
                'Video only (best)': 'bestvideo',
                'Video only (worst)': 'worstvideo',
                'Best quality': 'best',
                'Worst quality': 'worst'
            }

            ydl_opts = {
                'format': format_dict[self.ui.comboBox.currentText()],
                        }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

        th = threading.Thread(target=start)
        th.start()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec())
    