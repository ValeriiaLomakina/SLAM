from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow
from welcome import Ui_MainWindow


class FileSelectForm(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.file_name = None
        self.title = "SLAM"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNameDialog()

        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        self.file_name = fileName


class WelcomeForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.video = None
        self.ground_data = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.video_buton.clicked.connect(self.video_button_clicked)
        self.ui.ground_data_button.clicked.connect(self.ground_data_button_clicked)
        self.ui.confirm_button.clicked.connect(self.confirm_button_clicked)

    def video_button_clicked(self):
        dialog = FileSelectForm(self)
        dialog.show()

        self.ui.video_field.setText(dialog.file_name)

    def ground_data_button_clicked(self):
        dialog = FileSelectForm(self)
        dialog.show()

        self.ui.ground_data_field.setText(dialog.file_name)

    def confirm_button_clicked(self):
        self.video = self.ui.video_field.text()
        self.ground_data = self.ui.ground_data_field.text()

        self.close()

    def get_paths(self):
        return self.video, self.ground_data
