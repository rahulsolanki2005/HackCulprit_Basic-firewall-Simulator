# Hack Culprit Virtual Internship - Project Report

## Project Title: Basic Firewall Simulator  

### Submitted by:  
**Name:** Rahul Solanki  
**Internship Role:** Virtual Intern  
**Organization:** Hack Culprit  
**GitHub Profile:** https://github.com/rahulsolanki2005  
**Project Duration:** October 2025 – November 2025  
**Project Repository:** https://github.com/rahulsolanki2005/HackCulprit_Basic-firewall-Simulator

---

## 1. Executive Summary
This document outlines the design, development, and implementation of the project titled **"Basic Firewall Simulator"**, undertaken as part of the Hack Culprit Virtual Internship. The objective was to simulate a simple packet generator and firewall system that evaluates and filters network packets based on predefined rules. The project provides hands-on experience in **Python programming**, **terminal UI/UX design**, and **basic cybersecurity logic**, focusing on understanding how firewall mechanisms work at a fundamental level.

---

## 2. Problem Statement
[Briefly describe the challenge or gap the project addresses.]

**Example:**  
In the current digital landscape, beginners often struggle to understand how firewall rules are applied and how packets are filtered. This project provides a **lightweight, interactive Python-based firewall simulator** that demonstrates packet generation, rule checking, and filtering — offering a simplified yet practical learning experience.

---

## 3. Project Objectives
- To gain practical exposure to basic cybersecurity concepts like packet filtering and rule-based access control.  
- To understand network packet structure (IP, Port, Protocol).  
- To improve Python programming, especially using external libraries for better terminal UI (Rich).  
- To simulate real-world firewall behavior in a beginner-friendly environment.

---

## 4. Development Approach
The project was completed in the following stages:

1. **Requirement Analysis & Planning** – Defined scope, tools, and expected outcomes.  
2. **Development** – Implemented packet generator and firewall logic using Python.  
3. **UI Enhancement** – Integrated the `rich` library for colorful, table-based terminal output.  
4. **Testing & Debugging** – Ensured clean input handling and logical rule validation.  
5. **Documentation & Deployment** – Created structured README and code cleanup for GitHub submission.

---

## 5. Tools & Technologies

| **Category**       | **Tools / Technologies Used**         |
|--------------------|----------------------------------------|
| Programming        | Python                                 |
| Libraries          | rich, random, time                      |
| IDE / Tools        | VS Code, Git, GitHub                    |
| Version Control    | GitHub Repository                       |
| OS / Environment   | Windows / Linux Terminal                |

---

## 6. Installation & Setup

To run this project locally, follow the steps below:

    # Clone the repository
    git clone https://github.com/rahulsolanki2005/HackCulprit_Basic-firewall-Simulator

    # Navigate to the project directory
    cd basic-firewall-simulator

    # Install required dependency
    pip install rich

    # Run the application
    python firewall_simulator.py

> **Note:** Ensure Python 3.8+ and the `rich` library are installed before running.

---

## 7. Key Features
- ✅ **Interactive Terminal Interface** using `rich` (colored tables and borders)  
- ✅ **Random Packet Generator** (IP, Ports, Protocols)  
- ✅ **Rule-Based Firewall Simulation** with Allow/Block/Drop logic  
- ✅ **Logging System** to save filtered packet data to `firewall_log.txt`  
- ✅ **Clean User Input Handling** (prevents crashes on invalid input)  
- ✅ **Welcome Menu with Continue / Exit Options** for smooth start-up experience

---

## 8. Demonstration
Example terminal output (start screen):

    ─────────────────────────────────────────────
          Simple Packet Generator & Firewall
    ─────────────────────────────────────────────

    Welcome to Basic Firewall Simulator
    Press C to Continue or E to Exit:

After continuing, packets are displayed in a formatted table, followed by firewall filtering results and a summary of allowed, blocked, and dropped packets. There is also an option to save the log to `firewall_log.txt`.

---

## 9. Challenges Encountered
- Creating a **visually appealing terminal interface** while keeping the code lightweight.  
- Managing **input validation** for incorrect entries.  
- Maintaining **simplicity** while introducing **professional presentation** using `rich`.

---

## 10. Scope for Future Enhancements
- Add **real network packet sniffing** using `scapy`.  
- Implement **customizable firewall rules** via config file.  
- Add **live packet monitoring UI** (streaming mode).  
- Export logs in **CSV or JSON** formats for analysis.  
- Provide a small web UI to visualize results.

---

## 11. Conclusion
This project successfully demonstrates how basic firewalls inspect and filter packets using Python. It enhanced my understanding of network protocols, terminal UI development, and Python scripting. Through this internship, I developed both **technical and documentation skills**, aligning with real-world cybersecurity practices.

---

## 12. Acknowledgements
I would like to express my gratitude to the **Hack Culprit** team for providing this opportunity and guidance during the internship. Special thanks to mentors and peers for continuous support, code reviews, and valuable feedback that helped in improving the final version of this project.

---

## 13. License
This project is distributed under the **MIT License**.  
You are free to use, modify, and distribute it with proper credit.

---
