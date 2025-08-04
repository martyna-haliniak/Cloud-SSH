# Linux

# What is Linux?
**Linux** is an open-source, Unix-like operating system (OS) that manages hardware and runs applications. It’s widely used in servers, embedded systems, smartphones (like Android), and even desktops.

Unlike Windows or macOS, Linux is:
- Free and open-source
- Highly customisable
- Built collaboratively by developers and companies worldwide

Linux is based on a **monolithic kernel**, meaning the core of the OS handles most system functions directly.

---


## History of Linux

| Year | Milestone |
|------|-----------|
| **1969** | Unix is developed at Bell Labs. |
| **1983** | Richard Stallman launches the **GNU Project** to create a free Unix-like OS. |
| **1991** | **Linus Torvalds**, a Finnish student, creates and releases the first **Linux kernel** (v0.01). |
| **1992** | Linux adopts the **GNU General Public License (GPL)** and becomes fully open-source. |
| **1994** | Linux kernel v1.0 is released. |
| **2000s** | Major adoption in servers, academia, and embedded devices. |
| **Present** | Powers most servers, supercomputers, Android phones, and more. |

---

## 🌐 Why Is Linux Popular (Especially for Production Servers)?

### Key Reasons:

- **Free & Open Source** – No license costs; full control of the source code.
- **Stability** – Can run for years without crashing or needing a reboot.
- **Security** – Strong user permission system; less malware; regular patches.
- **Performance** – Efficient memory and CPU usage.
- **Scalability** – From small IoT devices to massive data centers.
- **Automation Friendly** – Strong CLI tools, shell scripting, and cron jobs.
- **Community Support** – Massive global community and resources.
- **Ecosystem Support** – Used in Docker, Kubernetes, AWS, Google Cloud, etc.

---

## ✅ Advantages of Linux

| Advantage | Description |
|-----------|-------------|
| **Free** | No cost for most distros. |
| **Open Source** | Modify and inspect the code yourself. |
| **Security** | Limited viruses, better access controls. |
| **Stability** | Reliable, even under heavy load. |
| **Performance** | Lightweight options for older hardware. |
| **Customisable** | Change everything from the kernel to the desktop environment. |
| **Community** | Large base of contributors and documentation. |
| **Programming Friendly** | Built-in tools for developers. |
| **Wide Hardware Support** | Runs on desktops, servers, phones, routers, etc. |

---

## ❌ Disadvantages of Linux

| Disadvantage | Description |
|--------------|-------------|
| **Learning Curve** | Terminal use and system setup can be intimidating for beginners. |
| **Software Compatibility** | Some apps like MS Office or Adobe Suite aren’t natively supported. |
| **Gaming Limitations** | Fewer native games (though improving with Proton/Steam). |
| **Hardware Drivers** | New or obscure hardware may lack Linux drivers. |
| **Fragmentation** | Many distros can make it hard to choose or troubleshoot. |
| **Limited Vendor Support** | Some commercial software and hardware support Windows/macOS first. |

---
## Other Interesting Facts

### Common Linux Use Cases
- **Web Servers**: Apache, NGINX, MySQL, etc.
- **Cloud Platforms**: AWS, GCP, Azure VMs often run Linux.
- **Supercomputers**: Over 95% of the world’s fastest supercomputers run Linux.
- **Android**: Based on the Linux kernel.
- **Embedded Systems**: Routers, smart TVs, automotive systems.
- **Desktops**: For developers, ethical hackers, or privacy-focused users.

### Popular Linux Distributions

| Distro | Focus |
|--------|-------|
| **Ubuntu** | Beginner-friendly; good for desktops and servers |
| **Debian** | Stable and free software-focused |
| **Arch Linux** | Minimalist and DIY; rolling release |
| **Fedora** | Cutting-edge features from Red Hat |
| **CentOS / Rocky / AlmaLinux** | Enterprise-level server OS |
| **Kali Linux** | Security testing and ethical hacking |
| **Raspberry Pi OS** | Lightweight and optimized for Raspberry Pi |

### Useful Linux Tools

| Tool | Function |
|------|----------|
| `bash`, `zsh` | Shell environments |
| `apt`, `yum`, `dnf`, `pacman` | Package managers |
| `ssh` | Remote server access |
| `cron` | Task scheduling |
| `top`, `htop` | Monitor system processes |
| `grep`, `awk`, `sed` | Text processing |
| `systemd`, `init` | System and service management |
| `vim`, `nano` | Text editors |

---

## Summary

Linux is more than just an operating system—it's a **foundation** for modern computing. It powers the internet, data centers, cloud platforms, smartphones, and millions of devices. Whether you're a developer, sysadmin, or tech enthusiast, understanding Linux opens the door to powerful tools and endless customization.

---



## Linux Commands in AWS via Git Bash

### Getting Started
To interact with an AWS EC2 instance, connect through Git Bash. You'll typically be using a Linux-based system like Ubuntu.

### Confirm your environment:
```bash
whoami
# output: ubuntu (if you're inside the instance)
```

```bash
uname
uname --help
# Check OS type and get more options
```

```bash
cat /etc/shells
# Shows available shells on the system
```

### Navigation & File System
```bash
ls
# Lists visible files and folders

ls -a
# Includes hidden files (those starting with .)

ls -l
# Long listing format

ls -la
# All files in long format
```

```bash
cd ..
# Move up one directory

cd ~
# Go to home directory

cd /
# Go to root directory
```


### File Operations
#### Viewing File Contents
```bash
cat filename.txt
head filename.txt
tail filename.txt
nl filename.txt
```


#### Search in Files
```bash
cat chicken-joke.txt | grep chicken
# Highlights all lines with the word "chicken"
```

### Creating, Moving, Copying, Deleting
#### Create a Directory
```bash
mkdir funny-stuff
```
#### Create with Spaces
```bash
mkdir "my pictures"
```
#### Move or Rename
```bash
mv oldname.txt newname.txt
```
#### Copy
```bash
cp original.txt copy.txt
```
#### Remove a File
```bash
rm file.txt
```
#### Remove Directory (Recursive)
```bash
rm -r directory_name
```
#### Force delete everything (use with extreme caution)
```bash
rm -rf foldername
# Deletes everything in foldername and doesn’t ask questions
```

### Downloading Files
#### Using curl
```bash
curl https://example.com/image.jpg --output image.jpg
```
#### Using wget
```bash
wget https://example.com/image.jpg -O image2.jpg
```
#### Confirm file type
```bash
file image.jpg
# e.g., JPEG image data
```

### Package Management (Ubuntu/Debian)
#### Step 1: Update
```bash
sudo apt update -y
```
#### Step 2: Upgrade
```bash
sudo apt upgrade -y
```
- `sudo` = SuperUser Do
- `-y` = Automatically answers “yes” to prompts

#### Install packages
```bash
sudo apt install tree -y
tree
```


### Switching to Root User
```bash
sudo su
# Switches to root
```

```bash
cd /root
# Only accessible after sudo su
```

```bash
exit
# Exit root mode, back to normal ubuntu user
```


### Bash Scripts
Use scripts to automate installations and configurations.

#### Create script manually
```bash
sudo nano install_nginx.sh
```
#### Make it executable
```bash
sudo chmod +x install_nginx.sh
```

### Sample Bash Script: install_nginx.sh
```bash
#!/bin/bash

# update
sudo apt update -y

# upgrade
sudo apt upgrade -y

# install nginx
sudo apt install nginx -y

# restart nginx
sudo systemctl restart nginx

# enable nginx on boot
sudo systemctl enable nginx
```

#### After running:
```bash
nginx -v
# Check if nginx is installed
```
```bash
sudo systemctl status nginx
# Check service status (press 'q' to exit)
```

#### Make sure:
- Your AWS security group allows HTTP (port 80) and SSH (port 22)
- You can access the site using the Public IPv4 address in your EC2 summary

---
## Linux Processes & Permissions

### Process Management

#### List All Running Processes
```bash
ps aux
# Shows all processes with detailed info: user, PID, CPU, memory, command, etc.
```

#### List Processes for a Specific User
```bash
ps -u <username>
# Lists processes owned by a particular user
```
#### List System Processes (Owned by Root)
```bash
ps -U root -u root u
# Displays system processes run by the root user
```


### What are Child Processes?
A **child process** is a process created by another (parent) process.
Example: When you run a shell script or a command like nano, the shell forks a child process to run it.

You can see parent-child relationships using:

```bash
pstree
```

### Running a Process in the Background
To run a command in the background:
```bash
command &
# Example:
sleep 30 &
```

To see background jobs:
```bash
jobs
```


### Ending a Process
#### Method 1: Using kill with PID
```bash
kill <PID>
```
#### Method 2: Using killall (by name)
```bash
killall <process_name>
```

#### Method 3: Using `top` or `htop`

In `top`: press `k` then enter the PID

In `htop`: use arrow keys to highlight, then press `F9`





### Kill Signals
**1 (SIGHUP)** – Hangup signal: Tells the process to reload (used to re-read config).

**15 (SIGTERM)** – Terminate: Politely asks the process to stop. Default signal.

**9 (SIGKILL)** – Force kill: Immediately ends the process (can’t be ignored).

Use with:
```bash
kill -<signal> <PID>
# Examples:
kill -1 1234    # Reload process
kill -15 1234   # Graceful shutdown
kill -9 1234    # Force shutdown
```


### Linux Permissions
Linux permissions are based on:

- **User (u)** – Owner of the file
- **Group (g)** – Group associated with the file
- **Other (o)** – Everyone else

Each permission is represented by:
- **r** – Read
- **w** – Write
- **x** – Execute



###  Long Format Permissions (ls -l)
Example:

```bash
-rwxr-xr--
```

Breakdown:
- First character: File type (- = file, d = directory)
- Next 3: Owner permissions (rwx)
- Next 3: Group permissions (r-x)
- Last 3: Other permissions (r--)


### Short Format Permissions (Octal)
Each set of 3 characters converts to a number:
- r = 4
- w = 2
- x = 1

Add them up:
- rwx = 7
- rw- = 6
- r-- = 4
- --- = 0

So:

```bash
chmod 764 file.txt
# Means:
# user: rwx (7)
# group: rw- (6)
# other: r-- (4)
```



### Changing File Permissions
#### Give Execute Permission to User Only
```bash
chmod u+x script.sh
```

#### Remove Write Permission from Group
```bash
chmod g-w file.txt#
```

#### Set Full Permissions for Owner, Read-Only for Others
```bash
chmod 744 file.txt
```

#### Make a File Readable and Writable for All
```bash
chmod 666 notes.txt
```

#### Make a Script Executable by Everyone
```bash
chmod a+x script.sh
```

---
