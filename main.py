import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QGraphicsOpacityEffect
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QTimer

def main():
    app = QApplication(sys.argv)
    word = "TANRI"
    windows = []  # Pencereleri burada tutuyoruz

    for i, letter in enumerate(word):
        window = QWidget()
        window.setWindowTitle('Letter Display')
        window.setGeometry(600 + (i * 120), 320, 100, 170)
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

        # Opacity efekti ve animasyon
        opacity_effect = QGraphicsOpacityEffect()
        label.setGraphicsEffect(opacity_effect)

        animation = QPropertyAnimation(opacity_effect, b"opacity")
        animation.setDuration(3000)  # 3 saniyede görünür olacak
        animation.setStartValue(0)
        animation.setEndValue(1)

        # Sakla ki çöp olmasın
        window.animation = animation
        windows.append(window)

        # Bu şekilde lambda içinde o anki window ve animation saklanır
        QTimer.singleShot(5000, lambda w=window, a=animation: (w.show(), a.start(), QTimer.singleShot(5000, w.close)))

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
