# AI-Powered Household Energy Prediction System

## About the Project

The **AI-Powered Household Energy Prediction System** is a machine learning based web application that helps predict household energy consumption.

We use electricity every day, but most of the time we only look at the electricity bill at the end of the month. It can be difficult to understand which factors are affecting our energy consumption and whether we are using more electricity than usual.

The main idea behind this project is to use **Machine Learning to analyze household energy-related data and predict energy consumption**. The prediction can help users understand their usage better and encourage them to make more energy-efficient decisions.

The project combines a **React frontend, Flask backend, and Machine Learning models** into one complete web application.

---

## Why We Built This Project

We wanted to work on a project where AI could be used to solve a real-world problem.

Energy consumption is something that every household deals with, and even small improvements in the way electricity is used can make a difference over time.

Through this project, we wanted to explore how machine learning can be used to understand energy usage and provide useful predictions through a simple web application.

---

## Main Objectives

* Predict household energy consumption using machine learning.
* Understand the factors that affect energy usage.
* Provide a simple interface for users to enter their information.
* Display the predicted energy consumption clearly.
* Help users become more aware of their energy usage.
* Explore the use of AI for sustainability.

---

## Machine Learning Models

We used two machine learning algorithms in this project:

* **Random Forest**
* **XGBoost**

The models are trained using household energy-related data. After preprocessing the data, the models learn patterns from the training data and use those patterns to make predictions for new inputs.

The general process is:

```text
Dataset
   ↓
Data Preprocessing
   ↓
Train/Test Split
   ↓
Random Forest + XGBoost
   ↓
Model Evaluation
   ↓
Energy Consumption Prediction
```

---

## Technologies Used

### Frontend

* React.js
* JavaScript
* HTML
* CSS
* Vite

### Backend

* Python
* Flask
* REST API

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest
* XGBoost
* Joblib

### Tools

* VS Code
* Git
* GitHub

---

## How the Application Works

The application has a frontend and backend that work together.

The user first interacts with the React application. The required household and energy-related information is entered through the interface.

The React frontend sends this information to the Flask backend using a REST API. The backend processes the input and passes it to the trained machine learning model.

The model generates the prediction, and the result is sent back to the frontend and displayed to the user.

```text
User
 ↓
React Frontend
 ↓
Flask REST API
 ↓
Machine Learning Model
 ↓
Prediction
 ↓
React Frontend
 ↓
User
```

---

## Project Features

### Login

Users can log in to the application and access the main dashboard.

### Dashboard

The dashboard provides a central place to access the different parts of the application.

### Energy Prediction

Users can enter the required household information and get an estimated energy consumption prediction.

### Analytics

The analytics section is intended to help users understand their energy consumption and identify usage patterns.

### Settings

The application also includes a settings section for managing application-related options.

---

## Project Structure

```text
Household-energy-predictor/
│
├── backend/
│
├── data/
│
├── frontend/
│
├── ml/
│
├── models/
│
├── .gitignore
│
└── README.md
```

### Folder Description

**backend/**
Contains the Flask backend and API-related code.

**frontend/**
Contains the React application and user interface.

**data/**
Contains the dataset used for the project.

**ml/**
Contains machine learning and data preprocessing related code.

**models/**
Contains the trained machine learning models.

---

## Running the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/Nireeksha-26/Household-energy-predictor.git
```

Then:

```bash
cd Household-energy-predictor
```

---

### Step 2: Run the Backend

Go to the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install flask flask-cors pandas numpy scikit-learn xgboost joblib
```

Start the Flask server:

```bash
python app.py
```

The backend will normally run at:

```text
http://127.0.0.1:5000
```

---

### Step 3: Run the Frontend

Open another terminal and go to the frontend folder:

```bash
cd frontend
```

Install the required packages:

```bash
npm install
```

Start the React application:

```bash
npm run dev
```

Vite will provide a local URL, usually similar to:

```text
http://localhost:5173
```

Open that URL in your browser.

---

## SDG Alignment

This project is related to the following Sustainable Development Goals:

### SDG 7 – Affordable and Clean Energy

The project encourages people to understand their electricity consumption and use energy more efficiently.

### SDG 12 – Responsible Consumption and Production

By making energy consumption easier to understand, the system can encourage more responsible use of electricity.

### SDG 13 – Climate Action

Reducing unnecessary energy consumption can contribute to more sustainable living and help reduce environmental impact.

---

## Who Can Use This?

The project can be useful for:

* Individual household users
* Families interested in monitoring energy usage
* Students learning about AI and sustainability
* People interested in reducing electricity wastage
* Educational institutions demonstrating AI-based projects

---

## Expected Impact

The main purpose of this project is to make household energy consumption easier to understand.

Instead of simply checking the electricity bill every month, users can use predictions to get a better idea of their expected consumption.

The project can help create awareness about energy usage and encourage people to develop better energy-saving habits.

The actual impact of the system can be measured in the future through user testing, prediction accuracy, feedback, and changes in simulated energy consumption.

---

## Future Improvements

There are several things we would like to add to the project in the future:

* Real-time smart meter data
* Daily, weekly, and monthly consumption reports
* Personalized energy-saving suggestions
* Notifications for unusually high energy consumption
* Better visualization of historical energy usage
* Explainable AI to show why a particular prediction was made
* Cloud deployment
* Mobile-friendly version
* Integration with renewable energy and solar power data

---

## What We Learned

Working on this project helped us understand how different areas of software development can be connected in a single application.

We gained practical experience in:

* Data preprocessing
* Machine learning
* Random Forest
* XGBoost
* Python
* Flask
* REST APIs
* React.js
* Frontend and backend integration
* Git and GitHub
* Applying AI to sustainability problems

One of the main things we learned was that building a machine learning model is only one part of an AI application. Connecting the model with a backend and creating a simple interface for users was also an important part of the project.

---

## Project Repository

GitHub:

https://github.com/Nireeksha-26/Household-energy-predictor

---


## Author

**Nireeksha Acharya**

Computer Science and Engineering Student

---

## Conclusion

The AI-Powered Household Energy Prediction System is our attempt to combine **Machine Learning and Web Development** to address a simple but important sustainability problem.

The project is still open to improvement, and we hope to make it more useful in the future by adding real-time data, personalized recommendations, and better energy analytics.
