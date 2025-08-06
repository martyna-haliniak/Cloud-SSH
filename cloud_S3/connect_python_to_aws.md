## Connecting Python to AWS
In Git Bash, make a directory for the credentials using ``` mkdir .aws```.

In that dir, make a file for the credentials:

```bash
nano credentails
  ```

and enter:
```
  [default]
  aws_access_key_id = YOUR_ACCESS_KEY
  aws_secret_access_key = YOUR_SECRET_KEY
```
Save with `Ctrl+O`, then `Enter` and Exit (`Ctrl+X`).

Create another file called `config` - enter:
```
[default]
region = eu-central-1
```
and save. 


In PyCharm:
```
pip install boto3
```

Make a new file to test the connection and use the following code:


``` python
import boto3
from botocore.exceptions import BotoCoreError, ClientError

try:
    sts = boto3.client('sts')
    response = sts.get_caller_identity()
    print("Connected to AWS successfully.")
except (BotoCoreError, ClientError) as e:
    print("Failed to connect to AWS.")
    print(e)
```
