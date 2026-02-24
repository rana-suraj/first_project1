"""
Simple ETL Pipeline - My First Data Engineering Project
This script fetches data from a public API, transforms it, and saves it locally.
"""

import csv
import json
from datetime import datetime
import requests

# ==================== EXTRACT ====================
def extract_data():
    """
    Extract data from a free public API
    Using JSONPlaceholder - a fake online REST API for testing
    """
    print("Starting extraction...")
    
    # API endpoint for fake posts
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Make the API request
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Successfully extracted {len(data)} records")
        return data
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

# ==================== TRANSFORM ====================
def transform_data(raw_data):
    """
    Clean and transform the raw data
    """
    print("Starting transformation...")
    
    transformed_data = []
    
    for item in raw_data:
        # Create a new cleaned record
        cleaned_record = {
            'post_id': item['id'],
            'user_id': item['userId'],
            'title': item['title'].strip(),  # Remove extra spaces
            'body': item['body'].strip(),    # Remove extra spaces
            'title_length': len(item['title']),
            'body_length': len(item['body']),
            'processed_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        transformed_data.append(cleaned_record)
    
    print(f"Transformed {len(transformed_data)} records")
    return transformed_data

# ==================== LOAD ====================
def load_data(data, filename):
    """
    Save the transformed data to a CSV file
    """
    print(f"Starting load to {filename}...")
    
    if not data:
        print("No data to save")
        return
    
    # Define CSV columns
    fieldnames = ['post_id', 'user_id', 'title', 'body', 
                  'title_length', 'body_length', 'processed_date']
    
    # Write to CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Successfully saved {len(data)} records to {filename}")

# ==================== MAIN EXECUTION ====================
def main():
    """
    Main ETL pipeline execution
    """
    print("=" * 50)
    print("Starting ETL Pipeline")
    print("=" * 50)
    
    # EXTRACT
    raw_data = extract_data()
    if not raw_data:
        print("Pipeline failed at extraction stage")
        return
    
    # TRANSFORM
    transformed_data = transform_data(raw_data)
    
    # LOAD
    output_file = f"posts_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    load_data(transformed_data, output_file)
    
    print("=" * 50)
    print("Pipeline completed successfully!")
    print(f"Check your output file: {output_file}")
    print("=" * 50)

# This ensures the pipeline runs only when script is executed directly
if __name__ == "__main__":
    main()