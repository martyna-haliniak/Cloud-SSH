# SSH and GitHub Setup
---
## What is SSH?
**SSH** (Secure Shell) is a protocol used to securely connect to remote servers and systems via the command line. It uses **key pairs** (public and private keys) to establish secure connections without requiring a password.

#### SSH Key Pairs
- Private Key = the secret "key" kept on your machine (like the real key)
- Public Key = a "padlock" placed on the service (e.g., GitHub or AWS)

SSH uses encryption to verify identity and establish secure communication

---

## Connecting to GitHub via SSH
#### 1. Generate SSH Key Pair
In Git Bash (cd /.ssh)
   ```bash
   ssh-keygen -t rsa -b 4096 -C "mhaliniak@spartaglobal.com"
  ```

When asked where to save it, enter a custom name (e.g.):
`martyna-github-keypair`

You can leave the passphrase empty for simpler access.


#### 2. Add Public Key to GitHub
Show your public key:
  ```bash
  cat martyna-github-keypair.pub
  ```

Copy the full output and paste it into GitHub > Settings > SSH and GPG Keys > New SSH Key.

#### 3. Add Private Key to SSH Agent
Start the agent:
```bash
eval `ssh-agent -s` 
```

Add your private key:
```bash
ssh-add martyna-github-keypair
```


#### 4. Test the Connection
Run:
```bash
ssh -T git@github.com
```

You should see:
``"Hi martyna-haliniak! You've successfully authenticated, but GitHub does not provide shell access."``


#### 5. Link GitHub Repo Using SSH
After creating a GitHub repo, change the remote URL from HTTPS to SSH:
```bash
git remote add origin git@github.com:martyna-haliniak/ssh_test_repo.git
```


#### 6. Remove Key Pair (if needed)
```bash
rm martyna-github-keypair
rm martyna-github-keypair.pub
```





---------------------- 
## AWS EC2 SSH Access

#### 1. Create Key Pair  
- Go to **AWS EC2 > Key Pairs**
- Create a new key pair named: `data504-martyna-keypair.pem`
- Download the `.pem` file and save it to your `~/.ssh/` directory



#### 2. Launch EC2 Instance  
- Choose **Ubuntu** as the OS (e.g., t2.nano or t3.nano instance type)
- Create a new **Security Group**:
  - Name: `data504-martyna-basic-sg`
  - Add **inbound rules** to allow:
    - SSH (port 22) from your IP
    - HTTP (port 80) from anywhere (optional for web access)


#### 3. Connect via SSH (Git Bash)  
1. Set secure file permissions for your `.pem` file:
   ```bash
   chmod 400 "data504-martyna-keypair.pem"
   ```

Connect to your instance:
```bash
ssh -i "data504-martyna-keypair.pem" ubuntu@ec2-3-76-29-2.eu-central-1.compute.amazonaws.com
```

Once connected, you can verify:
```bash
pwd
```
Output: `/home/ubuntu`


#### 4. Terminate the Instance (When Done)
Go to your instance in the AWS Console

Click Instance State > Terminate Instance

Confirm termination




