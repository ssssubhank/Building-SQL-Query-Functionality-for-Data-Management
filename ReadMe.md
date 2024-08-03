# Building SQL Query Functionality for Data Management

This repository contains a Python script for handling SQL-like queries on CSV files. The script supports basic SQL clauses: `SELECT`, `FROM`, `WHERE`, and `ORDER BY`.

## Supported Clauses

### 1. `SELECT`

The `SELECT` clause specifies which columns to retrieve from the CSV file. You can select all columns or specific columns.

- **All Columns**:
  ```sql
  SELECT * FROM filename
  ```

- **Specific Columns**:
  ```sql
  SELECT column1, column2 FROM filename
  ```

### 2. `FROM`

The `FROM` clause specifies the CSV file from which to read data. It must be used in conjunction with the `SELECT` clause.

- **Example**:
  ```sql
  SELECT * FROM filename
  ```

### 3. `WHERE`

The `WHERE` clause filters the results based on a condition. Only rows that meet the condition will be included in the result.

- **Condition Example**:
  ```sql
  WHERE column = value
  ```

- **Multiple Conditions** (AND, OR):
  ```sql
  WHERE column1 = value1 AND column2 = value2
  WHERE column1 = value1 OR column2 = value2
  ```

### 4. `ORDER BY`

The `ORDER BY` clause sorts the results based on one or more columns. You can specify the sort order as either ascending (`ASC`) or descending (`DESC`). If no sort order is specified, the default is ascending.

- **Order by Column (Ascending)**:
  ```sql
  ORDERBY column ASC
  ```

- **Order by Column (Descending)**:
  ```sql
  ORDERBY column DESC
  ```

## Query Examples

### 1. Valid Query with All Columns Selected, Filtered by Age, and Ordered by Age (Ascending)
**Query file content:**
```sql
SELECT * FROM sample.csv WHERE age > 25 ORDERBY age ASC
```

### 2. Valid Query with Specific Column Selected, Filtered by City, and Ordered by Age (Descending)
**Query file content:**
```sql
SELECT name FROM sample.csv WHERE city = 'San Francisco' ORDERBY age DESC
```

### 3. Query with `WHERE` Clause but Missing `ORDER BY` (Default to No Sorting)
**Query file content:**
```sql
SELECT * FROM sample.csv WHERE name = 'John'
```

### 4. Query with `ORDER BY` but Missing Sort Order (Default to Ascending)
**Query file content:**
```sql
SELECT * FROM sample.csv ORDERBY name
```

### 5. Query with `WHERE` and `ORDER BY` with Missing Sort Order (Default to Ascending)
**Query file content:**
```sql
SELECT * FROM sample.csv WHERE age < 30 ORDERBY age
```

### 6. Specific Query with All Columns Selected, Filtered by Age, and Ordered by Age (Ascending)
**Query file content:**
```sql
SELECT * FROM sample.csv WHERE age > 20 ORDERBY age ASC
```

## Sample CSV File (`sample.csv`)

To test the queries, use the following sample CSV content:

```csv
name,age,city
John,25,New York
Jane,30,San Francisco
Doe,22,Los Angeles
```

## Running the Script

To run the script, follow these steps:

1. Create a query file (e.g., `query_file.txt`) with one of the query examples above.
2. Place the `sample.csv` file in the same directory as the script.
3. Run the script with the query file as the input:

   ```bash
   python query_script.py query_file.txt
   ```

The script will output the results of the query, formatted as a table.
