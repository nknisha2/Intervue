# Intervue.io Automation Test

## Overview
This repository contains an automated test script using **Selenium with Python** to verify the login, search, and logout flow of [Intervue.io](https://www.intervue.io).

## Test Scenarios
- Open the website
- Click on "Login"
- Switch to the login window
- Enter credentials and log in
- Verify successful login
- Capture screenshot if any step fails
- logout

##  Setup Instructions

### 1️⃣ Install Dependencies
Ensure you have **Python** and **ChromeDriver** installed. Then, install required Python libraries:

# Automated Web Test using Selenium

## Prerequisites
Ensure you have:
- **Python** installed ([Download](https://www.python.org/downloads/))
- **Google Chrome** (Latest version)
- **ChromeDriver** (Managed by `webdriver-manager`)

## Installation Steps
1. pip install selenium webdriver-manager
   ## Run the script using:
   1. python Intervue_test.py
      
(If login fails, a screenshot will be saved as test_failure.png.)




### **3️⃣ `requirements.txt`**
```txt
selenium
webdriver-manager
