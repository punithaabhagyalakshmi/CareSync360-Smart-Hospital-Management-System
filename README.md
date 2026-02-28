# CareSync360-Smart-Hospital-Management-System
As part of the 10-Hour Hackathon FORGEX 2026 conducted by the Department of IST, Anna University on 25/02/2026, we developed and deployed a Smart Hospital Workflow &amp; Patient Visit Management System that digitizes patient registration, prioritizes emergency cases, and provides real-time tracking using Flask and Firebase.

## 📌 Overview

The Smart Hospital Workflow & Patient Visit Management System is a cloud-based web application developed during the 10-Hour Hackathon – FORGEX 2026 conducted by the Department of Information Science and Technology (IST), Anna University.

This system digitizes hospital patient flow management by automating registration, implementing intelligent queue prioritization, and providing real-time status tracking using Firebase Realtime Database.

---

## 🚨 Problem Statement

Many hospitals still rely on manual queue systems, which lead to:

- Long waiting times  
- Poor emergency prioritization  
- Lack of real-time workflow visibility  
- Operational inefficiencies  

Emergency patients may experience delays due to the absence of structured prioritization systems.

---

## 🎯 Our Solution

We built a smart digital workflow system that:

- Automates patient registration  
- Generates unique Patient IDs and Tokens  
- Implements a priority-based queue system  
- Provides real-time consultation tracking  
- Stores data securely in the cloud  

---

## 🚀 Features

- Digital Patient Registration  
- Auto-generated Patient ID & Token  
- Intelligent Priority Queue  
  - Emergency (Highest Priority)  
  - Senior Citizen  
  - Normal  
- Real-Time Consultation Status Updates  
- Admin Dashboard with Live Statistics  
- Patient History Search  
- Firebase Cloud Data Storage  
- Scalable and Cloud-Ready Architecture  

---

## 🛠 Tech Stack

**Frontend**
- HTML  
- CSS  
- JavaScript  

**Backend**
- Flask (Python)

**Database**
- Firebase Realtime Database

**Cloud Platform**
- Google Firebase

---

## 🏗 System Architecture

Client (Browser)  
⬇  
Flask Backend  
⬇  
Firebase Realtime Database  
⬇  
Admin Dashboard  

---

## 📦 Installation

● 1. Clone the Repository
git clone https://github.com/punithaabhagyalakshmi/CareSync360-Smart-Hospital-Management-System

● 2. Install Dependencies
pip install -r requirements.txt

● 3. Add Firebase Service Key
Place your downloaded Firebase service account file in the root directory:
firebase-key.json

 ● 4. Update Database URL

In `app.py`, replace with your Firebase Realtime Database URL:

python
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id-default-rtdb.firebaseio.com/'
})

● 5. Run the Application
python app.py

# 🎯 Objectives
Reduce patient waiting time
Improve emergency case prioritization
Digitize hospital workflow
Enhance transparency and efficiency
Provide scalable healthcare management

## 👥 Team
Developed by a team of 3 members.
● Punithaa Bhagyalakshmi G
● Kumutha S
● Gopika P

Developed as part of:
FORGEX 2026 – 10 Hour Hackathon,
Department of Information Science and Technology,
Anna University.
25/02/2026

# 📜 License
This project was developed for academic and hackathon purposes.

