# Redis Key Viewer/Manager (Python)

A CLI tool to inspect and manage keys in a Redis database.

## Features

-   **List Keys**: Search keys with patterns (e.g., `user:*`).
-   **Inspect Key**: View type, TTL, and value of a specific key.
-   **Delete Key**: Remove a key from the database.
-   **Safe Mode**: CLI interactions prevent accidental bulk deletions.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run Redis**: Ensure you have a Redis instance running (e.g., `docker run -p 6379:6379 redis`).

## Usage

```bash
# List keys matching a pattern
python run_manager.py list "session:*"

# Get details of a key
python run_manager.py get "session:123"

# Delete a key
python run_manager.py delete "session:123"
```

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
