# 🛠️ Multi-Source ETL Pipeline

This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline built in Python that ingests data from multiple file formats — **CSV, JSON, and XML** — transforms it, and writes it to a unified output CSV file.

---

## 📌 Project Features

- ✅ Automatically detects and extracts data from:
  - `.csv` files using `pandas.read_csv()`
  - `.json` files using `pandas.read_json()`
  - `.xml` files using `ElementTree`
- ✅ Transforms:
  - Height from inches → meters
  - Weight from pounds → kilograms
- ✅ Combines all data into one dataset
- ✅ Saves the transformed output to `transformed_data.csv`
- ✅ Logs every stage to `log_file.txt` for traceability

---

## 🧰 Tech Stack

- Python 3
- `pandas`
- `glob`
- `datetime`
- `xml.etree.ElementTree`

---

## 📁 Folder Structure

```
ETL folder/
├── etl.py                  # Main ETL pipeline script
├── log_file.txt            # Log of ETL events
├── transformed_data.csv    # Final output file
├── source1.csv/json/xml    # Input data files
├── source2.csv/json/xml
├── source3.csv/json/xml
```

---

## 🚀 How to Run

1. Clone the repository
2. Navigate to the `ETL folder/`
3. Run the script:

```bash
python etl.py
```

This will process all source files and generate:
- `transformed_data.csv`
- `log_file.txt`

---

## 🔍 Example Output (CSV)

| name  | height | weight |
|-------|--------|--------|
| John  | 1.80   | 75.30  |
| Alice | 1.65   | 60.12  |

---

## 👨‍💻 Author

**Miqdad Issa**  
Aspiring Data Engineer | Project-driven learner | Open Source Contributor  
[github.com/miqdad-dev](https://github.com/miqdad-dev)