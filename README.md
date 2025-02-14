# passgen-py

## Overview

The **passgen-py** is a user-friendly desktop application built using **PyQt6**, a popular Python framework for creating graphical user interfaces (GUIs). This application allows users to generate secure, random passwords based on customizable criteria such as length, character types (uppercase, lowercase, numbers, and special characters), and more. It is designed to help users create strong passwords for enhanced security.

---

## Features

1. **Customizable Password Length**: Users can specify the desired length of the password.
2. **Character Type Selection**: Users can choose to include or exclude:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Numbers (0-9)
   - Special characters (e.g., !, @, #, $, etc.)
3. **Generate Multiple Passwords**: Users can generate multiple passwords at once.
4. **Copy to Clipboard**: Generated passwords can be copied to the clipboard with a single click for easy use.
5. **User-Friendly Interface**: The application features an intuitive and clean interface for ease of use.
6. **Error Handling**: The application includes validation to ensure users provide valid input (e.g., password length must be a positive integer).

---

## Requirements

To run the Password Generator Application, you need the following:

- **Python 3.7 or higher**
- **PyQt6**: The GUI framework used to build the application.
- **random** and **string**: Python standard libraries for generating random passwords.

### Installation

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).
2. **Install PyQt6**: Install the PyQt6 library using pip:
   ```bash
   pip install PyQt6
   ```
3. **Clone or Download the Application**:
   - Clone the repository (if applicable):
     ```bash
     git clone https://github.com/moxiu33/passgen-py.git
     ```
   - Or download a prebuild binary from [Releases](https://github.com/moxiu33/passgen-py/releases/tag/v1.1) and extract it

---

## How to Use

1. **Launch the Application**:
   - Navigate to the binary file you downloaded and double click the extracted exe.
2. **Set Password Criteria**:
   - Enter the desired password length in the input field.
   - Check or uncheck the boxes to include/exclude uppercase letters, lowercase letters, numbers, and special characters.
3. **Generate Password**:
   - Click the "Generate Password" button to create a password based on your criteria.
4. **Copy to Clipboard**:
   - Click the "Copy to Clipboard" button to copy the generated password for use.
5. **Generate Multiple Passwords**:
   - Use the "Generate Multiple Passwords" feature to create a list of passwords at once.

---

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](https://github.com/moxiu33/passgen-py/blob/main/LICENSE) file for details.

---

## Contact

For questions or feedback, please contact, you can find way to contact me at my website:  http://moxiu33.github.io/

---

Enjoy generating secure passwords with the passgen-py! 🔒
