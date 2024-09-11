# QR Code Generator

This is a simple web application for generating and downloading QR codes based on user-provided URLs. The application is built using Python with Flask for the backend and HTML/CSS for the frontend.

## Features

- **Generate QR Codes**: Input a URL and generate a QR code.
- **Download QR Codes**: Download the generated QR code as a PNG file.
- **Responsive Design**: The page is styled to be visually appealing and functional on both desktop and mobile devices.

## Technologies Used

- **Python**: Programming language used for the backend.
- **Flask**: Web framework for Python used to build the server-side logic.
- **HTML/CSS**: Markup and styling used for the frontend.
- **qrcode**: Python library for generating QR codes.
- **Jinja2**: Templating engine used by Flask for rendering HTML.

## Installation and Setup

Follow these steps to set up and run the application locally:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a Virtual Environment** (Optional but recommended):

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask Application**:

    ```bash
    python app.py
    ```

    By default, the application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Open the Application**: Navigate to `http://127.0.0.1:5000/` in your web browser.
2. **Generate a QR Code**:
    - Enter a URL in the input field and click the "Generate QR Code" button.
    - The generated QR code will appear below the form.
3. **Download the QR Code**:
    - Click the "Download QR Code" button to download the QR code as a PNG file.

## Project Structure

- **`app.py`**: The main Python script containing the Flask application logic.
- **`templates/index.html`**: The HTML template for the main page.
- **`static/styles.css`**: The CSS file for styling the page.
- **`requirements.txt`**: List of Python dependencies.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes or feature requests, please open an issue first to discuss what you would like to change.

## Acknowledgments

- **Flask**: For providing a lightweight framework to build the web application.
- **qrcode Library**: For QR code generation.
