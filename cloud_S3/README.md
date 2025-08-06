# Python + AWS S3 Notes

See `connect_python_to_aws.md` to connect with credentials using Git Bash.

## S3 Basics
- **S3** = Simple Storage Service, stores files ("objects") inside "buckets".

- **Buckets** are like folders at the top level; objects are files inside buckets.

- **Objects** are referenced by bucket name + key (key = file path/name).

---
## Required Imports:
``` python
import boto3
import pandas as pd
import json
import io
```
## boto3: Clients vs Resources

``` python
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
```
| Feature       | Client                                   | Resource                            |
|---------------|------------------------------------------|-----------------------------------|
| Level         | Low-level API                            | High-level, object-oriented       |
| Method names  | Map directly to AWS REST API operations | More Pythonic, abstracted methods |
| Example       | `s3_client.get_object(...)`              | `s3_resource.Bucket('bucket').objects.all()` |

---

## Listing Buckets and Objects
List all buckets:

``` python
for bucket in s3_resource.buckets.all():
    print(bucket.name)
```

List objects in a bucket (resource):
``` python
bucket = s3_resource.Bucket('bucket-name')
for obj in bucket.objects.all():
    print(obj.key)
```

List objects (client):
``` python
response = s3_client.list_objects_v2(Bucket='bucket-name')
for obj in response['Contents']:
    print(obj['Key'])
```
---

## Reading an Object from S3
Use `get_object` from client to get file content:
```python
response = s3_client.get_object(Bucket='bucket-name', Key='file.csv')
content = response['Body'].read().decode('utf-8')
```

(Some files may need encoding like `utf-8` to avoid issues.)

Convert content to pandas DataFrame:
``` python

df = pd.read_csv(io.StringIO(content))
```

---
## Writing/Uploading Data to S3
Upload simple objects:

``` python
s3_client.put_object(
    Bucket='bucket-name',
    Key='folder/filename.json',
    Body=json.dumps(data_dict)
)
```

Upload a file object:
```python
with open('localfile.csv', 'rb') as f:
    s3_client.upload_fileobj(f, 'bucket-name', 'path/on/s3.csv')
```

---
## Transform Your Dataset Using Pandas
Once you've read your CSV data into a pandas DataFrame, you can perform various transformations depending on your goals. Here are some common examples:


#### 1. Grouping and Aggregating

Use `groupby()` to group data and apply aggregation functions.

Example: Average numeric values by category

```python
df_grouped = df.groupby('CategoryColumn').mean(numeric_only=True).reset_index()
```
Other aggregation options:

```python
df.groupby('CategoryColumn').sum()
df.groupby('CategoryColumn')['ValueColumn'].max()
df.groupby(['Col1', 'Col2']).agg({'Col3': 'mean', 'Col4': 'count'})
```

#### 2. Counting Values
Use `value_counts()` to count the frequency of unique values.

Example: Count occurrences of values in a column

```python
value_counts = df['SomeColumn'].value_counts().reset_index()
value_counts.columns = ['SomeColumn', 'Count']
```

#### 3. Data Cleaning
Remove unwanted data or fix inconsistent values.

```python
df.dropna()  # remove rows with missing values
df.fillna(0)  # replace missing values with 0
df['Column'] = df['Column'].str.strip()  # remove whitespace
```

#### 4. Creating New Columns
Create calculated columns or combine existing ones.

```python
df['NewColumn'] = df['Col1'] + df['Col2']
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
```

#### 5. Renaming and Reordering Columns
```python
df.rename(columns={'OldName': 'NewName'}, inplace=True)
df = df[['Col2', 'Col1', 'Col3']]  # reorder columns
```

#### 6. Filtering Rows
```python
df_filtered = df[df['ValueColumn'] > 100]
df_filtered = df[df['Category'] == 'Bream']
``` 

#### 7. Exporting Transformed Data
After transforming your data, write it back to a CSV format to upload to S3:

``` python
csv_buffer = io.StringIO()
df_transformed.to_csv(csv_buffer, index=False)
```
Then upload with:

```python
s3_client.put_object(
    Bucket='your-bucket-name',
    Key='your/folder/path/filename.csv',
    Body=csv_buffer.getvalue()
)
```