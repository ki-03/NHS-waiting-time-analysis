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

5. **Analysis**
   - Investiagate factors contributing to long waiting times
   - Explore relatioship between waiting time and missed appointments
   
## 📊 Key Findings
- The majority of appointmnets are scheduled within a short time frame:
  - Median waiting time is approximately 5 days
  - Average waiting time is around 7 days
  - 75% of appointments occur within 10 days

- A subset of appointments (~11%) experience longer waiting times (>15 days), indicating that the delays exists but are not widespread
- Analysis if appointment outcomes (attended, cancelled, did not attend) shows similar distirbution across both long and normal waiting time, suggesting that longer waits do not significantly impact patient attendance behaviour.
- Demographic factors such as age group do not show meaningful difference between long-wait and normal wait appointments
- Scheduling related factors such as day of the week adn insurance type also do not demostrate a strong relationship
- Overall, no strong patterns were identified in the available data that explain why certain appointments experience longer waiting times.

## ⚠️ Limitations
- The dataset does not include key operational variable such as:
  - Healthcare provider availability
  - department capacity
  - appointment type or urgency level

- These missing factors are likely critical in explaining longer waiting times.
- The dataset is synthetic, meaning it stimulates real world behabiour but may not capture all complexities of actual healthcare systems.
- The analysis is based on observational data and does not establish casual relationships.

## 🔄 Reflection & Learnings

During this project, I experienced moments of confusion and lack of direction, particularly in the middle of the analysis phase. This was mainly due to exploring multiple approaches without a clearly defined structure, which made the workflow feel unorganised and overwhelming.

This highlighted the importance of having a structured plan before starting the analysis.

For future projects, I will:
- Define a clear and focused objective at the beginning
- Create a simple workflow or flowchart outlining key steps (data understanding → cleaning → analysis → insights)
- Prioritise analyses that directly align with the project objective
- Avoid exploring too many methods at once without a clear purpose

This approach will help maintain clarity, reduce confusion, and ensure that the analysis remains aligned with the main goal.
