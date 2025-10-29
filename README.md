# Health Insights Dashboard

## Overview

The **Health Insights Dashboard** is a lightweight, local web application designed to visualize and summarize health-related data such as steps, sleep, and calories.  
The goal of this project is to demonstrate how meaningful insights can be extracted and presented clearly **without the use of external libraries or frameworks**.  
It focuses on **simplicity, accessibility, and efficient data presentation**.

This project uses only built-in Python functionality and standard web technologies (HTML, CSS, and JavaScript).  
It can run entirely on a local machine without the need for internet access or additional package installations.

---

## Project Structure

```text
health-dashboard/
│
├── data/
│   └── health_data.csv           
│
├── dashboard/
│   ├── index.html                
│   ├── style.css                 
│   └── script.js               
│
├── scripts/
│   └── serve_dashboard.py        
│
└── README.md                    



---

## What the Project Does

The dashboard provides a **clean visual overview** of user health metrics based on structured data. It displays:

- Daily or weekly step counts  
- Sleep duration and quality  
- Calories burned and consumed  
- Summaries and simple statistics


The interface presents this information through static or dynamically generated charts and summaries.  
The layout is designed to be **minimal and professional**, making it suitable for reports or personal data tracking.

---

## Methods and Implementation

### 1. Data Representation
The project uses a CSV file (`health_data.csv`) as input, containing columns such as steps, sleep, and calorie data.  
JavaScript reads and visualizes this information directly in the browser.

### 2. Local Hosting
A simple Python HTTP server (`serve_dashboard.py`) serves the HTML, CSS, and JavaScript files locally.  
This avoids complex backend setups and ensures the dashboard can be viewed from any web browser.

### 3. Visualization
Charts and summaries are generated using plain JavaScript, leveraging basic HTML canvas elements and CSS for styling.  
No external visualization libraries are used. This makes the project **portable and easy to understand**.

### 4. Design and Layout
The dashboard is designed with **clean lines, soft contrast, and a grid-based structure** for readability.  
The CSS ensures a balanced and professional appearance without relying on external frameworks.


--- 


## Summary Plot
<img width="778" height="940" alt="summary_plot" src="https://github.com/user-attachments/assets/117a9bd1-3700-43c6-b3f4-29f8ad3fe9de" />
