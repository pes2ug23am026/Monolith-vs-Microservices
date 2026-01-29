# LAB 2 – Monolithic and Microservices Architecture  
## Cloud Computing Laboratory

---

## Overview
This laboratory experiment focuses on understanding and analyzing **Monolithic** and **Microservices** architectures using a web-based event management system. The lab demonstrates how architectural design choices affect scalability, reliability, fault tolerance, and performance in cloud-based applications.

The experiment also uses **load testing** to observe how the system behaves under concurrent user access and how performance can be improved through optimization.

---

## Monolithic Architecture

### Description
A **Monolithic Architecture** is an architectural style in which all application functionalities are developed, deployed, and executed as a single unit. All modules share the same codebase, runtime environment, and database.

### Fest Analogy
The monolithic application is compared to a college fest managed using **one large counter**:
- Registration
- Event listing
- Checkout/payment
- My-events dashboard  

All services are handled by the same team at the same place. If any part of the counter fails, the entire fest operation stops. This analogy clearly illustrates the tightly coupled nature of monolithic applications.

---

### Characteristics of Monolithic Architecture
- Single codebase and deployment unit
- Tightly coupled components
- Shared database
- Centralized logging and debugging
- Single point of failure

---

### Advantages of Monolithic Architecture
- Simple and easy to understand
- Faster development for small teams
- Direct communication between components
- Easier debugging and testing
- Simple deployment process

---

### Disadvantages of Monolithic Architecture
- Difficult to scale individual features
- Entire application must be redeployed for small changes
- Increased maintenance complexity over time
- Poor fault isolation
- Single point of failure

---

### Failure Demonstration
The lab intentionally introduces a fault in the checkout module. When this fault is triggered, the entire application crashes, even though other modules are unrelated. This demonstrates the **single point of failure** problem in monolithic architectures.

---

## Microservices Architecture

### Description
**Microservices Architecture** is an architectural style where an application is divided into multiple small, independent services. Each service is responsible for a specific business functionality and can be developed, deployed, and scaled independently.

### Fest Analogy
In the microservices approach, the fest is managed using **multiple independent stalls**:
- One stall for registration
- One stall for event listing
- One stall for checkout/payment
- One stall for my-events dashboard  

If one stall fails, the rest of the fest can continue operating. This represents improved fault isolation and scalability.

---

### Characteristics of Microservices Architecture
- Independent services with specific responsibilities
- Separate deployments for each service
- Communication through network APIs
- Independent scalability
- Better fault isolation

---

### Advantages of Microservices Architecture
- Scalability of individual services
- Improved reliability and fault isolation
- Faster and safer deployments
- Easier maintenance for large applications
- Cloud-native and container-friendly

---

### Disadvantages of Microservices Architecture
- Increased system complexity
- Network latency due to inter-service communication
- Complex debugging and monitoring
- Requires service discovery and orchestration
- Higher operational overhead

---

## Load Testing Using Locust

### Description
Load testing is performed using **Locust**, an open-source load testing tool that simulates concurrent users accessing application endpoints. This helps analyze application performance under load and observe response times, request rates, and failures.

The lab uses load testing to:
- Study system behavior under concurrent access
- Observe performance before and after optimization
- Understand the impact of architectural design on performance

---

## Performance Optimization
The experiment includes performance optimization of selected routes such as:
- `/checkout`
- `/events`
- `/my-events`

Performance metrics before and after optimization are compared to observe improvements in response time and request handling capacity.

---

## Why FastAPI is Used
FastAPI is used in this lab to reflect modern cloud application development practices. It offers high performance, support for asynchronous programming, and easy integration with cloud-native tools. Despite using FastAPI, the application remains monolithic due to its single codebase and deployment model.

---

## Conclusion
This lab provides a practical understanding of monolithic and microservices architectures. While monolithic systems are simple and easy to build, they suffer from scalability and fault tolerance limitations. Microservices address these issues by enabling independent services but introduce additional complexity. The experiment highlights the importance of choosing the right architecture based on application requirements.
