from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('My First PyQt6 App')
window.setGeometry(100, 100, 280, 80)
window.show()
sys.exit(app.exec())