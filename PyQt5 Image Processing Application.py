import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QFileDialog, QToolBar, QVBoxLayout,
    QWidget, QSlider, QPushButton, QProgressBar, QColorDialog
)
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QPixmap, QImage, QPalette, QColor, QPainter, QPen, QFont


class ImageProcessor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processing App")
        self.setGeometry(100, 100, 1300, 850)
        self.setAcceptDrops(True)

        self.image = None
        self.original_image = None
        self.history = []
        self.redo_stack = []

        self.drawing = False
        self.last_point = QPoint()
        self.pen_color = Qt.red
        self.canvas_pixmap = QPixmap()
        self.theme = "dark"

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.title_label = QLabel("\n IMAGE PROCESSING APP\n")
        self.title_label.setFont(QFont("Helvetica", 24, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label, stretch=2)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.layout.addWidget(self.progress_bar)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.cap = None
        self.live_mode = False

        self.create_toolbar()
        self.create_sliders()
        self.set_dark_theme()

    def create_toolbar(self):
        toolbar = QToolBar("Tools")
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        actions = {
            "Open": self.open_image,
            "Save": self.save_image,
            "Reset": self.reset_image,
            "Undo": self.undo,
            "Redo": self.redo,
            "Grayscale": self.grayscale_image,
            "Blur": self.apply_blur,
            "Edge": self.apply_edge_detection,
            "Sharpen": self.sharpen_image,
            "Brightness+": lambda: self.adjust_brightness(10),
            "Brightness-": lambda: self.adjust_brightness(-10),
            "Contrast+": lambda: self.adjust_contrast(1.2),
            "Contrast-": lambda: self.adjust_contrast(0.8),
            "Draw Color": self.pick_color,
            "Start Live": self.start_live_preview,
            "Stop Live": self.stop_live_preview,
            "Toggle Theme": self.toggle_theme,
        }

        for name, func in actions.items():
            btn = QPushButton(name)
            btn.clicked.connect(func)
            toolbar.addWidget(btn)

    def create_sliders(self):
        self.slider_blur = QSlider(Qt.Horizontal)
        self.slider_blur.setRange(1, 99)
        self.slider_blur.setValue(1)
        self.slider_blur.setSingleStep(2)
        self.slider_blur.valueChanged.connect(self.apply_blur)
        self.layout.addWidget(self.slider_blur)

        self.slider_edge = QSlider(Qt.Horizontal)
        self.slider_edge.setRange(0, 255)
        self.slider_edge.setValue(100)
        self.slider_edge.valueChanged.connect(self.apply_edge_detection)
        self.layout.addWidget(self.slider_edge)

    def open_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Image")
        if path:
            self.progress_bar.setValue(0)
            self.timer.start(50)
            self.image = cv2.imread(path)
            self.original_image = self.image.copy()
            self.history.clear()
            self.redo_stack.clear()
            self.progress_bar.setValue(50)
            self.show_image(self.image)
            self.progress_bar.setValue(100)
            self.timer.stop()

    def save_image(self):
        if self.image is not None:
            path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.jpg *.bmp)")
            if path:
                if not any(path.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.bmp']):
                    path += '.png'
                self.progress_bar.setValue(0)
                self.timer.start(50)
                cv2.imwrite(path, self.image)
                self.progress_bar.setValue(100)
                self.timer.stop()

    def reset_image(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.history.clear()
            self.redo_stack.clear()
            self.show_image(self.image)

    def undo(self):
        if self.history:
            self.redo_stack.append(self.image.copy())
            self.image = self.history.pop()
            self.show_image(self.image)

    def redo(self):
        if self.redo_stack:
            self.history.append(self.image.copy())
            self.image = self.redo_stack.pop()
            self.show_image(self.image)

    def add_history(self):
        if self.image is not None:
            self.history.append(self.image.copy())
            self.redo_stack.clear()

    def grayscale_image(self):
        if self.image is not None:
            self.add_history()
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            self.show_image(self.image)

    def apply_blur(self):
        if self.original_image is not None:
            self.add_history()
            k = self.slider_blur.value()
            k = k + 1 if k % 2 == 0 else k
            self.image = cv2.GaussianBlur(self.original_image, (k, k), 0)
            self.show_image(self.image)

    def apply_edge_detection(self):
        if self.original_image is not None:
            self.add_history()
            gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, self.slider_edge.value(), 255)
            self.image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            self.show_image(self.image)

    def sharpen_image(self):
        if self.image is not None:
            self.add_history()
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            self.image = cv2.filter2D(self.image, -1, kernel)
            self.show_image(self.image)

    def adjust_brightness(self, val):
        if self.image is not None:
            self.add_history()
            self.image = cv2.convertScaleAbs(self.image, alpha=1, beta=val)
            self.show_image(self.image)

    def adjust_contrast(self, factor):
        if self.image is not None:
            self.add_history()
            self.image = cv2.convertScaleAbs(self.image, alpha=factor, beta=0)
            self.show_image(self.image)

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen_color = color

    def start_live_preview(self):
        if not self.live_mode:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("Camera not accessible")
                return
            self.live_mode = True
            self.timer.start(30)

    def stop_live_preview(self):
        if self.live_mode:
            self.timer.stop()
            if self.cap:
                self.cap.release()
            self.live_mode = False

    def update_frame(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                self.image = frame.copy()
                self.show_image(self.image)
                self.progress_bar.setValue((self.progress_bar.value() + 10) % 100)

    def toggle_theme(self):
        if self.theme == "light":
            self.set_dark_theme()
        else:
            self.set_light_theme()

    def set_dark_theme(self):
        self.theme = "dark"
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(40, 40, 40))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)
        self.central_widget.setStyleSheet("background-color: #2e2e2e;")
        self.title_label.setStyleSheet("color: #00ffff;")

    def set_light_theme(self):
        self.theme = "light"
        self.setPalette(self.style().standardPalette())
        self.central_widget.setStyleSheet("background-color: #ffffff;")
        self.title_label.setStyleSheet("color: #000080;")

    def show_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        bytes_per_line = ch * w
        qimg = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pix = QPixmap.fromImage(qimg)
        self.canvas_pixmap = pix.scaled(
            self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio)
        self.image_label.setPixmap(self.canvas_pixmap)

    # -------- Paint Logic -------- #
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.image_label.underMouse():
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing and self.image_label.underMouse():
            painter = QPainter(self.canvas_pixmap)
            pen = QPen(self.pen_color, 5, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.image_label.setPixmap(self.canvas_pixmap)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ImageProcessor()
    win.show()
    sys.exit(app.exec_())
