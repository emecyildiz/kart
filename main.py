
import sys
from PyQt6.QtWidgets import (
	QApplication, QWidget, QLabel, QGraphicsOpacityEffect
)
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation


def main():
	app = QApplication(sys.argv)
	window = QWidget()
	window.setWindowTitle('My First PyQt6 App')
	window.setGeometry(500, 320, 100, 170)

	# Create and style label
	label = QLabel('T', window)
	label.setStyleSheet(
		"font-size: 100px; color: white; font-weight: bold; "
		"font-family: Arial; padding: 10px; border-radius: 8px;"
	)
	label.setAlignment(Qt.AlignmentFlag.AlignCenter)
	label.resize(window.size())

	# Opacity animation
	opacity_effect = QGraphicsOpacityEffect()
	label.setGraphicsEffect(opacity_effect)
	animation = QPropertyAnimation(opacity_effect, b"opacity")
	animation.setDuration(3000)
	animation.setStartValue(0)
	animation.setEndValue(1)
	animation.start()

	# Window settings
	window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
	window.setWindowFlags(
		Qt.WindowType.FramelessWindowHint |
		Qt.WindowType.WindowStaysOnTopHint
	)

	# Auto-close after 5 seconds
	QTimer.singleShot(5000, window.close)

	window.show()
	sys.exit(app.exec())


if __name__ == "__main__":
	main()