import boto3
import pprint as pp
import pandas as pd
import io
import json

from pandas.io.common import file_path_to_url

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
#
# bucket_list = s3_client.list_buckets()
# pp.pprint(bucket_list)    # turns into a python dictionary

s3 = boto3.resource('s3')

#Let's see the list of buckets first
for bucket in s3.buckets.all():
    print(bucket.name)


# Output object names using resource
bucket = s3_resource.Bucket('data-eng-resources')
for obj in bucket.objects.all():
    print(obj.key)

# Output object names using client
response = s3_client.list_objects_v2(Bucket='data-eng-resources')

for obj in response['Contents']:
    print(obj['Key'])


# get_object() in client:
response = s3_client.get_object(Bucket='data-eng-resources', Key='python/happiness-2019.csv')
content = response['Body'].read().decode('utf-8')
print(content[:300])

# Load python/happiness.csv into dataframe
df = pd.read_csv(io.StringIO(content))
print(df.head())

# ------------------------------------------------
# Write JSON file about yourself
my_info = {
    "name": "Martyna",
    "age": 25,
    "gender": "female",
    "location": "Skelmersdale"
}

s3_client.put_object(
    Body=json.dumps(my_info),
    Bucket="data-eng-resources",
    Key="Martyna/info.json"
)


# Check
response = s3_client.get_object(Bucket='data-eng-resources', Key='Martyna/info.json')
content = response['Body'].read().decode('utf-8')
print(content)

# ------------------------------------------------
# Read the fish market CSV data inside the data-eng-resources bucket
response = s3_client.get_object(Bucket='data-eng-resources', Key='python/fish-market.csv')
content_fish = response['Body'].read().decode('utf-8')
print(content_fish[:300])

# Write a version of it that is transformed back to s3 - 'data-eng-resources/Data504/fish/your-name-fish-transformed'
    # Transformation: data averaged by fish species

# Load into DataFrame
df = pd.read_csv(io.StringIO(content_fish))
# Transform df: Average numeric values by Species
df_avg = df.groupby('Species').mean(numeric_only=True).reset_index()
# Convert transformed df to csv
csv_buffer = io.StringIO()
df_avg.to_csv(csv_buffer, index=False)
# Upload to S3
upload_key = 'Data504/fish/martyna-fish-transformed.csv'
s3_client.put_object(
    Bucket='data-eng-resources',
    Key=upload_key,
    Body=csv_buffer.getvalue()
)


# Read the fish market CSV data inside the data-eng-resources bucket
response = s3_client.get_object(Bucket='data-eng-resources', Key='Data504/fish/martyna-fish-transformed.csv')
content_fish_transformed = response['Body'].read().decode('utf-8')
print(content_fish_transformed[:300])


# ------------------------------------------------
# Load deaths on eight thousanders csv
bucket_name = 'data-eng-resources'
file_path = 'deaths_on_eight_thousanders.csv'
key = 'Martyna/deaths_on_eight_thousanders.csv'

with open(file_path, 'rb') as csvfile:
    s3_client.upload_fileobj(csvfile, bucket_name, key)

# Read .csv
response = s3_client.get_object(Bucket='data-eng-resources', Key='Martyna/deaths_on_eight_thousanders.csv')
content_deaths = response['Body'].read().decode('utf-8')
print(content_deaths[:300])
# Turn into DataFrame
df = pd.read_csv(io.StringIO(content_deaths))
# Transformation: Count deaths by mountain
deaths_by_mountain = df['Mountain'].value_counts().reset_index()
deaths_by_mountain.columns = ['Mountain', 'Deaths']
print(deaths_by_mountain)

# Convert transformed df to csv
csv_buffer = io.StringIO()
deaths_by_mountain.to_csv(csv_buffer, index=False)
# Upload to S3
upload_key = 'Martyna/deaths_by_mountain.csv'
s3_client.put_object(
    Bucket='data-eng-resources',
    Key=upload_key,
    Body=csv_buffer.getvalue()
)

