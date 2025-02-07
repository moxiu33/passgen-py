import sys
import random
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QCheckBox,
    QPushButton,
    QLineEdit,
    QComboBox,
    QStackedWidget,
    QListWidget,
    QMessageBox,
    QTextBrowser,
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt, QSettings, QUrl

# Constants for character sets
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIALS = "!@#$%^&*()_+-=[]{}|;:,.<>?"

class AdvancedPassGen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AdvancedPassGen")
        self.setGeometry(100, 100, 600, 400)

        # Load settings
        self.settings = QSettings("MyCompany", "AdvancedPassGen")
        self.theme = self.settings.value("theme", "light")

        # Create UI
        self.create_ui()

        # Apply saved theme
        self.apply_theme(self.theme)

    def create_ui(self):
        # Main layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.addItems(["Password Generator", "Settings", "About"])
        self.sidebar.setFixedWidth(150)
        self.sidebar.setStyleSheet("""
            QListWidget {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 10px;
                color: black; /* Default text color */
            }
            QListWidget::item:selected {
                background-color: #0078d7;
                color: black; /* Keep text color black when selected */
            }
        """)
        self.sidebar.currentRowChanged.connect(self.switch_page)
        main_layout.addWidget(self.sidebar)

        # Stacked widget for pages
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        # Password Generator Page
        self.password_generator_page = QWidget()
        self.create_password_generator_page()
        self.stacked_widget.addWidget(self.password_generator_page)

        # Settings Page
        self.settings_page = QWidget()
        self.create_settings_page()
        self.stacked_widget.addWidget(self.settings_page)

        # About Page
        self.about_page = QWidget()
        self.create_about_page()
        self.stacked_widget.addWidget(self.about_page)

    def create_password_generator_page(self):
        layout = QVBoxLayout()

        # Password length
        length_layout = QHBoxLayout()
        length_layout.addWidget(QLabel("Password Length:"))
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(4, 50)
        self.length_spinbox.setValue(12)
        length_layout.addWidget(self.length_spinbox)
        layout.addLayout(length_layout)

        # Character types
        self.lower_checkbox = QCheckBox("Include Lowercase Letters")
        self.lower_checkbox.setChecked(True)
        layout.addWidget(self.lower_checkbox)

        self.upper_checkbox = QCheckBox("Include Uppercase Letters")
        self.upper_checkbox.setChecked(True)
        layout.addWidget(self.upper_checkbox)

        self.numbers_checkbox = QCheckBox("Include Numbers")
        self.numbers_checkbox.setChecked(True)
        layout.addWidget(self.numbers_checkbox)

        self.specials_checkbox = QCheckBox("Include Special Characters")
        self.specials_checkbox.setChecked(True)
        layout.addWidget(self.specials_checkbox)

        # Generate button
        generate_button = QPushButton("Generate Password")
        generate_button.setStyleSheet("""
            QPushButton {
                background-color: #0078d7;
                color: white;
                padding: 10px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)
        generate_button.clicked.connect(self.generate_password)
        layout.addWidget(generate_button)

        # Password display
        self.password_lineedit = QLineEdit()
        self.password_lineedit.setReadOnly(True)
        self.password_lineedit.setPlaceholderText("Generated Password")
        self.password_lineedit.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.password_lineedit)

        # Copy button
        copy_button = QPushButton("Copy to Clipboard")
        copy_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 10px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        copy_button.clicked.connect(self.copy_password)
        layout.addWidget(copy_button)

        self.password_generator_page.setLayout(layout)

    def create_settings_page(self):
        layout = QVBoxLayout()

        # Theme selection
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Theme:"))
        self.theme_combobox = QComboBox()
        self.theme_combobox.addItems(["light", "dark"])
        self.theme_combobox.setCurrentText(self.theme)
        theme_layout.addWidget(self.theme_combobox)
        layout.addLayout(theme_layout)

        # Save button
        save_button = QPushButton("Save Settings")
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #0078d7;
                color: white;
                padding: 10px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)

        self.settings_page.setLayout(layout)

    def create_about_page(self):
        layout = QVBoxLayout()

        # About text
        about_text = QTextBrowser()
        about_text.setOpenExternalLinks(True)
        about_text.setHtml("""
            <h1>PassGen-py</h1>
            <p>This is a password generator application built with PyQt6.</p>
            <p>It allows you to generate secure passwords with customizable options.</p>
            <p><b>Made by <a href="https://moxiu33.github.io">Moxiu</a></b></p>
            <p>GitHub: <a href="https://github.com/moxiu33">moxiu33</a></p>
        """)
        layout.addWidget(about_text)

        self.about_page.setLayout(layout)

    def switch_page(self, index):
        self.stacked_widget.setCurrentIndex(index)

    def generate_password(self):
        length = self.length_spinbox.value()
        use_lower = self.lower_checkbox.isChecked()
        use_upper = self.upper_checkbox.isChecked()
        use_numbers = self.numbers_checkbox.isChecked()
        use_specials = self.specials_checkbox.isChecked()

        characters = ""
        if use_lower:
            characters += LOWERCASE
        if use_upper:
            characters += UPPERCASE
        if use_numbers:
            characters += NUMBERS
        if use_specials:
            characters += SPECIALS

        if not characters:
            QMessageBox.warning(self, "Error", "Please select at least one character type.")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        self.password_lineedit.setText(password)

    def copy_password(self):
        password = self.password_lineedit.text()
        if password:
            QApplication.clipboard().setText(password)
            QMessageBox.information(self, "Copied", "Password copied to clipboard!")
        else:
            QMessageBox.warning(self, "Error", "No password generated.")

    def save_settings(self):
        self.theme = self.theme_combobox.currentText()
        self.settings.setValue("theme", self.theme)
        self.apply_theme(self.theme)
        QMessageBox.information(self, "Saved", "Settings saved successfully.")

    def apply_theme(self, theme):
        palette = QPalette()
        if theme == "dark":
            palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Base, QColor(35, 35, 35))
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        else:
            # Light mode
            palette.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))
            palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.Base, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))
            palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)
        QApplication.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedPassGen()
    window.show()
    sys.exit(app.exec())