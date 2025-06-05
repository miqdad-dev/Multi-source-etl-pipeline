import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = "log_file.txt"
target_file = "transformed_data.csv"

def extract_from_csv(file_to_process):
    dataframes = pd.read_csv(file_to_process)
    return dataframes

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe
#o extract from an XML file, you need first to parse the data from the file using the ElementTree function.
def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight",])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight" ).text)
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True)
    return dataframe

#Use glob library to identify all files in the folder that match a specific pattern.
def extract():
    extracted_data = pd.DataFrame(columns=["name", "height", "weight"]) #create an empty DataFrame to store the extracted data

    #process all CSV files, except the target file
    for csvfile in glob.glob("ETL folder/*.csv"): #find all CSV files in the current directory
        if csvfile != target_file: #check if the file is not the target file
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)
    
    #process all JSON files
    for jsonfile in glob.glob("ETL folder/*.json"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 

    #process all XML files
    for xmlfile in glob.glob("ETL folder/*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)

    return extracted_data

# Transform the extracted data
def transform(data):
    # Convert height from inches to meters and round to 2 decimal places
    # 1 inch = 0.0254 meters
    data['height'] = round(data.height * 0.0254, 2)
    
    # Convert weight from pounds to kilograms and round to 2 decimal places
    # 1 pound = 0.453592 kilograms
    data['weight'] = round(data.weight * 0.45359237, 2)
    
    return data

# Load the extracted data, transform it, and save it to a CSV file
def load_data(target_file, transformed_data):  #load_data function takes the target file name and the transformed data as parameters
    transformed_data.to_csv(target_file) # Save the transformed data to a CSV file
    
# Log the transformation process
def log_process(message):
    timestamp_format = "%Y-%m-%d %H:%M:%S"  # Define the timestamp format year-month-day hour:minute:second
    now = datetime.now() # Get the current date and time
    timestamp = now.strftime(timestamp_format) # Format the timestamp
    with open(log_file, "a") as f: # Open the log file in append mode
        f.write(timestamp + "," + message + "\n")  # Write the timestamp and message to the log file

# Main ETL process
# Log the initialization of the ETL process 
log_process("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_process("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_process("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_process("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_process("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_process("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_process("Load phase Ended") 
 
# Log the completion of the ETL process 
log_process("ETL Job Ended") 