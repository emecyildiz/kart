import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QGraphicsOpacityEffect
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QTimer

def main():
    app = QApplication(sys.argv)
    word = "WELCOME_HOME"
    windows = []  # Store the windows here

    for i, letter in enumerate(word):
        window = QWidget()
        window.setWindowTitle('Letter Display')
        window.setGeometry(100 + (i * 120), 320, 100, 170)
        window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        window.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        label = QLabel(letter, window)
        label.setStyleSheet("""
            font-size: 100px;
            color: white;
            font-weight: bold;
            font-family: Arial;
            padding: 10px;
            border-radius: 8px;
        """)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.resize(window.size())

        # Opacity effect and animation
        opacity_effect = QGraphicsOpacityEffect()
        label.setGraphicsEffect(opacity_effect)

        animation = QPropertyAnimation(opacity_effect, b"opacity")
        animation.setDuration(3000)  # Will become visible in 3 seconds
        animation.setStartValue(0)
        animation.setEndValue(1)

        # Store to prevent garbage collection
        window.animation = animation
        windows.append(window)

        # This way, the current window and animation are captured in the lambda
        QTimer.singleShot(5000, lambda w=window, a=animation: (w.show(), a.start(), QTimer.singleShot(5000, w.close)))

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
