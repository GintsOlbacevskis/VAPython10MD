import threading
import time
import random

# Function to simulate file download
def download_file(file_name):
    print(f"Starting download: {file_name}")
    download_time = random.randint(2, 5)  # Simulate download time
    time.sleep(download_time)
    print(f"Completed download: {file_name} (Time: {download_time}s)")

# Main program
if __name__ == "__main__":
    # List of files to download
    files = ["Test.zip", "Test.docx", "Test.txt", "Test.jpg", "Test.pdf"]

    # Create and start threads
    threads = []
    for file in files:
        thread = threading.Thread(target=download_file, args=(file,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All downloads completed!")