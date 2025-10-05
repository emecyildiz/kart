from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGraphicsOpacityEffect
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('My First PyQt6 App')
window.setGeometry(500, 320, 100, 170)
window.label = QLabel('T',window)
window.label.setStyleSheet("font-size: 100px; color: white; font-weight: bold; " \
"font-family: Arial; padding: 10px; border-radius: 8px;")
opacity_effect = QGraphicsOpacityEffect()
window.label.setGraphicsEffect(opacity_effect)
animation = QPropertyAnimation(opacity_effect, b"opacity")
animation.setDuration(3000)
animation.setStartValue(0)
animation.setEndValue(1)
animation.start()    
window.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
window.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
window.label.resize(window.size())
QTimer.singleShot(5000, window.close)
window.show()
sys.exit(app.exec())