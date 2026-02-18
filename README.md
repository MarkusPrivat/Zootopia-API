# 🐾 Animal Website Generator

A Python-based tool that utilizes the **API-Ninjas Animals API** to fetch detailed animal information and automatically generates a visually structured HTML webpage.



## 🚀 Features

* **Real-time Querying:** Search for any animal species via the API-Ninjas interface.
* **Automated Serialization:** Converts complex JSON data into clean, readable HTML list elements.
* **Dynamic Templating:** Merges live data into an existing HTML template using placeholder replacement.
* **Robust Error Handling:** Validates user input and provides visual feedback on the generated page if an animal is not found.

## 🛠️ Installation

1.  **Clone the Repository** (or copy the files into a local directory).
2.  **Install Dependencies:**
    Make sure you have `requests` and `python-dotenv` installed:
    ```bash
    pip install requests python-dotenv
    ```
3.  **Get an API Key:**
    Register for free at [API-Ninjas](https://api-ninjas.com/) to obtain your API Key.
4.  **Configure Environment Variables:**
    Create a file named `.env` in the root directory and add your key:
    ```text
    NINJA_API_KEY=your_secret_api_key_here
    ```

## 📂 Project Structure

* `main.py`: Handles file I/O, HTML generation logic, and the main program loop.
* `animals_api.py`: Manages the connection and requests to the external API.
* `animals_template.html`: The base HTML file (must include the `__REPLACE_ANIMALS_INFO__` placeholder).
* `.env`: Stores your sensitive API key securely (ensure this is in your `.gitignore`).

## 📖 Usage

1.  Run the application via your terminal or PyCharm:
    ```bash
    python main.py
    ```
2.  Enter the name of an animal when prompted (e.g., "Lion", "Cheetah", or "Fox").
3.  The program will generate (or update) a file called `animals.html`.
4.  Open `animals.html` in any web browser to view the results.



## 🔧 Technical Details

### Data Mapping
The script specifically extracts and formats the following fields from the API response:
* **Name:** The primary identifier of the animal.
* **Locations:** Geographical regions where the animal is found.
* **Characteristics:** Including Diet, Type, Lifespan, and Color.

### HTML Serialization
The `serialize_animal` function wraps the data in a specific CSS-friendly structure:
```html
<li class="cards__item">
    <div class="card__title">Animal Name</div>
    <div class="card__text">
        <ul>
            <li><strong>Location:</strong> Region Name</li>
            </ul>
    </div>
</li>