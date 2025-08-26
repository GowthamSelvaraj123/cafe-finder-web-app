 <h1>Cafe Finder Web App</h1>
    <p>A full-stack Flask web application to discover, add, and manage cafes with WiFi and coffee availability.</p>
    <h2>Features</h2>
    <ul>
        <li>View a list of cafes with location, WiFi, and coffee availability</li>
        <li>Add new cafes to the list</li>
        <li>Delete existing cafes</li>
        <li>Responsive design using Bootstrap 5</li>
        <li>Uses Flask and SQLAlchemy for backend functionality</li>
    </ul>
    <h2>Technologies Used</h2>
    <ul>
        <li>Python 3</li>
        <li>Flask</li>
        <li>SQLAlchemy</li>
        <li>SQLite</li>
        <li>Bootstrap 5</li>
        <li>Jinja2 Templates</li>
    </ul>
    <h2>Installation</h2>
    <p>Follow these steps to run the project locally:</p>
    <ol>
        <li>Clone the repository: <code>git clone https://github.com/yourusername/cafe-finder.git</code></li>
        <li>Navigate into the project folder: <code>cd cafe-finder</code></li>
        <li>Create a virtual environment: <code>python -m venv .venv</code></li>
        <li>Activate the virtual environment:</li>
        <ul>
            <li>Windows: <code>.venv\Scripts\activate</code></li>
            <li>Mac/Linux: <code>source .venv/bin/activate</code></li>
        </ul>
        <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Run the app: <code>python run.py</code></li>
        <li>Open your browser and go to <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a></li>
    </ol>
    <h2>Folder Structure</h2>
    <pre>
    cafe-finder/
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   └── routes/
    │       └── main.py
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   └── add_cafe.html
    ├── static/
    │   └── (optional css/js/images)
    ├── cafes.db
    ├── run.py
    └── requirements.txt
    </pre>
    <h2>Usage</h2>
    <p>Once the app is running:</p>
    <ul>
        <li>Navigate to the homepage to see the list of cafes</li>
        <li>Click "Add Cafe" to add a new cafe</li>
        <li>Click "Delete" to remove a cafe</li>
        <li>Icons show WiFi and coffee availability</li>
    </ul>
    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>

    <h2>Author</h2>
    <p>Gowtham S.</p>
