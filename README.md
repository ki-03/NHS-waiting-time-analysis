# NHS-waiting-time-analysis

## 📌 Problem Statement
## Long waiting times for medical appointments are a major challenge in healthcare systems like the NHS. Patients often wait weeks or months for care, which can delay treatment and negatively impact health outcomes.

## 🎯 Objective
## The objective of this project is to analyse appointment scheduling data to understand waiting times and identify factors contributing to delays in patient care. The goal is to provide insights that can help improve resource utilization and reduce waiting times.

## 📊 Dataset
## - Source: [Medical Appointment Scheduling Dataset](https://www.kaggle.com/datasets/carogonzalezgaltier/medical-appointment-scheduling-system)
## - Description: A synthetic dataset stimulating a healthcare appointment system, including patient details, scheduling information and appointment outcomes. 

## 🧠 Approach
The analysis follows a structured process:
1. **Data Loading & Understanding**
   - Imported datasets (appointments, patients, slots)
   - Explored structure and relationship between the tables

2. **Data Preparation**
   - Merged datasets using common keys (patient_id, slot_id)
   - Handled duplicate columns created during merging
   - Ensured correct data types for analysis (eg., datetime conversion)

3. **Feature Engineering**
   - Identified and validated waiting time using the scheduling interval
   - Renamed variables for better clarity (e.g., waiting_days)

4. **Exploratory Data Analysis (EDA)**
   - Analysed distribution of waiting times
   - Identified key statistics (mean, median, percentiles)

5. **Planned Analysis**
   - Investiagate factors contributing to long waiting times
   - Explore relatioship between waiting time and missed appointments
   - Generate insights to improve scheduling efficiency
     

