# Stock Price CRUD Operations with InfluxDB

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations for stock price data using InfluxDB. It also includes logging for all operations and stores logs in a `logs.txt` file.

## Features

- **Create**: Insert stock price data (open, high, low).
- **Read**: Query stock price data for a specific stock over a given number of days.
- **Update**: Modify stock price data.
- **Delete**: Delete stock price data within a specified time range.
- **Logging**: Logs all operations in a `logs.txt` file.

## Prerequisites

Ensure the following software is installed on your system:

- **Python 3.7+**
- **InfluxDB** (installed and running): [Installation Guide](https://docs.influxdata.com/influxdb/v2.0/install/)
- **InfluxDB Python Client**: This is required to interact with the InfluxDB instance.

## Getting Started

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Set Up Virtual Environment (Optional but Recommended)

It is highly recommended to set up a virtual environment for dependency management.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate

# Activate the virtual environment (Windows)
.env\Scriptsctivate
```

### Step 3: Install Dependencies

Install the required Python dependencies using `pip`.

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the project root directory and add the following environment variables to configure your InfluxDB connection details:

```env
INFLUXDB_URL=http://localhost:8086
INFLUXDB_TOKEN=your-influxdb-token
INFLUXDB_ORG=your-org-name
INFLUXDB_BUCKET=your-bucket-name
```

### Step 5: Run the Project

Once the environment is set up and dependencies are installed, you can run the `main.py` file.

```bash
python main.py
```

### Step 6: Interact with CRUD Operations

Follow the prompts in the terminal to perform the following CRUD operations:

1. **Create**: Add stock data by entering the stock name, open price, high price, and low price.
2. **Read**: Retrieve stock data by specifying the stock name and the number of days to fetch.
3. **Update**: Modify existing stock data by specifying new open, high, and low prices.
4. **Delete**: Remove stock data by entering the time range.

### Step 7: View Logs

All the CRUD operations are logged into the `logs.txt` file located in the root directory. Check this file for success, failure, or error messages related to the CRUD operations.

### Example Logs (`logs.txt`)

```
2024-10-18 12:35:21,101 - INFO - Inserted data for AAPL with Open: 150.50, High: 155.20, Low: 148.70
2024-10-18 12:37:45,202 - INFO - Queried data for MSFT: [('64.50', 'High'), ('62.13', 'Low')]
2024-10-18 12:40:09,307 - ERROR - Error occurred while updating data: Stock not found.
```

### Step 8: Stop the Project

To stop the project, simply press `Ctrl + C` in your terminal.

## Development

### .gitignore

Ensure the following files and directories are added to your `.gitignore` to avoid pushing them to your repository:

```bash
# .gitignore

__pycache__/
venv/
.env
logs.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
