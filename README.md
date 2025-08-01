# Introduction to Cloud Computing

## What is Cloud?


Cloud computing refers to the delivery of computing services—such as servers, storage, databases, networking, software, and analytics—over the internet ("the cloud"). Instead of owning physical hardware, users can access scalable resources on demand, paying only for what they use. 

---
## History of Cloud Computing

The concept of cloud computing dates back to the 1960s, when computer scientist John McCarthy envisioned computing as a utility. However, it wasn't until the early 2000s that modern cloud services took shape:

- **2002**: Amazon launched AWS (Amazon Web Services), offering storage and computing services.
- **2006**: AWS introduced EC2 (Elastic Compute Cloud), revolutionising on-demand infrastructure.
- **Late 2000s**: Google and Microsoft entered the market with Google Cloud and Azure.
- **2010s onward**: Cloud adoption grew rapidly across industries, enabling innovations like SaaS (Software as a Service), big data processing, and AI development.

Cloud computing continues to evolve, driving digital transformation across the globe.

---
## What Are the 4 Main Cloud Deployment Models?

1. **Public Cloud**  
   Services are delivered over the internet by third-party providers (e.g., AWS, Google Cloud). Shared infrastructure, cost-effective, and scalable.

2. **Private Cloud**  
   Cloud infrastructure is dedicated to one organisation. Offers greater control and security, typically hosted on-premises or in a private data centre.

3. **Hybrid Cloud**  
   Combines public and private clouds, allowing data and applications to move between them. Useful for flexibility and gradual cloud adoption.

4. **Multi-Cloud**  
   Involves using services from multiple cloud providers (e.g., AWS, Azure, and Google Cloud together). This strategy helps avoid vendor lock-in, improves resilience, and allows organisations to optimise performance by matching workloads to the most suitable provider.


---

## What Are the 3 Main Cloud Service Types?

1. **IaaS (Infrastructure as a Service)**  
   Provides virtualised computing resources like servers, storage, and networking.  
   _Example: Amazon EC2, Microsoft Azure VMs_

2. **PaaS (Platform as a Service)**  
   Offers a platform for developers to build, test, and deploy applications without managing the underlying infrastructure.  
   _Example: Google App Engine, Heroku_

3. **SaaS (Software as a Service)**  
   Delivers software over the internet, accessible via a web browser. No installation needed.  
   _Example: Gmail, Dropbox, Microsoft 365_

---

## Current Market Share
Worldwide market share of leading cloud infrastructure service providers in Q4 2024.

![Market Share](market_share.png)

---


## Notes
Local - on premises
Cloud - access through internet, e.g. AWS, Azure, GCP, Gmail (as a service), dropbox (storage)


### Models
- **Public Cloud**
    e.g. AWS, Google Data Centre
- **Private Cloud**
    Own hardware instead of using data centre
- **Hybrid Cloud**
    Mix of public and private
    e.g. service split into multiple pieces, part on public cloud, part on private cloud, connection between the two
- **Multi Cloud**
    services on multiple cloud providers in case one goes down (tends to be the reason due to regulations)
    e.g. have connections between GCP, Azure, AWS


### Service Types
- **IaaS**: Infrastructure as a Service
    Renting servers - Specify requirements, price usually per hour for running it, ..
- **PaaS**: Platform as a Service
    Renting an environment - Rent a server but need your own environment (set up server yourself) *wrong
- **SaaS**: Software as a Service
    Rent software - runs on the cloud (e.g. Microsoft 365)
- **FaaS**: Functions as a Service
    1 off functions (adhoc) - run it and that's it, usally event driven (event-something uploaded, deleted, updated)


### Data Centre (DC)
Multiple in different places, they're connected and gouped, e.g. Europe

London - One data centre, multiple locations in different regions (Availability Zones) that make up the data centre
Backup if one AZ goes down

### Cloud Advantages and Disadvantages

**Advantages**
- Accessible from anywhere
- Scalability (vertical and horizontal)
- Price
- Physical security

**Disadvantages**
- Less control (trust)
- Needs managing (planning, ensuring company doesn't pay for cloud that's not being used for example)


#### Pricing: CapEx vs OpEX
- Capital expenditure - upfront payment, balue back over time
- Operating Expenditure - pay for what you use (preferred by companies)





