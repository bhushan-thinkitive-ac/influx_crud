# Stock Price CRUD Operations with InfluxDB

This project demonstrates a basic CRUD (Create, Read, Update, Delete) operation for stock price data using InfluxDB. It includes logging for all operations and stores the logs in a `logs.txt` file.

## Features

- **Create**: Insert stock price data (open, high, low).
- **Read**: Query stock price data for a specific stock over a given number of days.
- **Update**: Modify stock price data.
- **Delete**: Delete stock price data within a specified time range.
- **Logging**: All operations are logged into a `logs.txt` file.

## Prerequisites

Before running the project, make sure you have the following installed:

1. **Python 3.7+**
2. **InfluxDB**: Ensure that InfluxDB is installed and running on your system. [Installation Guide](https://docs.influxdata.com/influxdb/v2.0/install/)
3. **InfluxDB Client**: The Python client for InfluxDB is used to interact with the database.

## Getting Started

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
