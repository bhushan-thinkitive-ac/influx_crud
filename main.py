import logging
from influx_client import InfluxClient
from datetime import datetime, timedelta

# Step 1: Configure the logger to write to a logs.txt file
logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def perform_crud_operation():
    client = InfluxClient()
    
    print("Select an operation to perform:")
    print("1. Create (Insert Data)")
    print("2. Read (Query Data)")
    print("3. Update Data")
    print("4. Delete Data")
    choice = input("Enter the number corresponding to the operation (1-4): ")

    try:
        if choice == '1':
            # Create/Insert Operation
            stock_name = input("Enter stock name: ")
            open_price = float(input("Enter open price: "))
            high_price = float(input("Enter high price: "))
            low_price = float(input("Enter low price: "))
            client.write_data(stock_name=stock_name, open_price=open_price, high_price=high_price, low_price=low_price)
            logging.info(f"Inserted data for {stock_name} with Open: {open_price}, High: {high_price}, Low: {low_price}")
            print(f"Inserted data for {stock_name}")

        elif choice == '2':
            # Read Operation
            stock_name = input("Enter stock name to query: ")
            days = int(input("Enter the number of days to look back: "))
            start_time = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"
            result = client.query_data(stock_name=stock_name, start_time=start_time)
            logging.info(f"Queried data for {stock_name}: {result}")
            print(f"Queried data for {stock_name}: {result}")

        elif choice == '3':
            # Update Operation
            stock_name = input("Enter stock name: ")
            open_price = float(input("Enter new open price: "))
            high_price = float(input("Enter new high price: "))
            low_price = float(input("Enter new low price: "))
            timestamp = datetime.utcnow().isoformat() + "Z"
            client.update_data(stock_name=stock_name, open_price=open_price, high_price=high_price, low_price=low_price, timestamp=timestamp)
            logging.info(f"Updated data for {stock_name} at {timestamp} with Open: {open_price}, High: {high_price}, Low: {low_price}")
            print(f"Updated data for {stock_name} at {timestamp}")

        elif choice == '4':
            # Delete Operation
            stock_name = input("Enter stock name to delete: ")
            start = input("Enter the start time (e.g., '1970-01-01T00:00:00Z'): ")
            stop = datetime.utcnow().isoformat() + "Z"
            client.delete_data(stock_name=stock_name, start=start, stop=stop)
            logging.info(f"Deleted data for {stock_name} from {start} to {stop}")
            print(f"Deleted data for {stock_name} from {start} to {stop}")

        else:
            logging.error(f"Invalid choice: {choice}")
            print("Invalid choice. Please select a valid operation.")
    
    except Exception as e:
        logging.error(f"Error occurred during operation: {str(e)}")
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    perform_crud_operation()
