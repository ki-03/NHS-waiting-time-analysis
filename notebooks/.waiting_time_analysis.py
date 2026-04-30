# %%
import pandas as pd 

# %%
print("Setup successful")

# %%
appointments = pd.read_csv("../data/appointments.csv")
patients = pd.read_csv("../data/patients.csv")
slots = pd.read_csv("../data/slots.csv")

# %%
appointments.head()
type(appointments)
appointments.columns

# %%
patients.head()
patients.columns

# %%
slots.head()
slots.columns

# %%
# merging all three datasets into one

df = appointments.merge(patients, on="patient_id", how="left")
df = df.merge(slots, on="slot_id", how="left")

df.shape

# %%
pd.set_option('display.max_columns', None)
df.head()

# %%
# checking if the date are identical in both appointment and slot

(df["appointment_date_x"] == df["appointment_date_y"]).all()
(df['appointment_time_x'] == df['appointment_time_y']).all()

# checking if the sex are identical in both appointment and patient
(df["sex_x"] == df["sex_y"]).all()

# %%
# since both of them are same, dropping one for clean code
df = df.drop(columns=['appointment_date_y', 'appointment_time_y'])

df = df.drop(columns=["sex_y"])

# %%
df = df.rename(columns={
    "appointment_date_x": "appointment_date",
    "appointment_time_x": "appointment_time"
})

df = df.rename(columns={
    "sex_x": "sex"
})

# %%
df.head()

# %%
df["scheduling_date"] = pd.to_datetime(df["scheduling_date"])
df["appointment_date"] = pd.to_datetime(df["appointment_date"])

# %%
df.dtypes

# %%
df = df.rename(columns={"scheduling_interval": "waiting_days"})

# %%
df["waiting_days"].describe()

# %%
import matplotlib.pyplot as plt
import seaborn as sns 

plt.figure(figsize=(10,5))
sns.histplot(df["waiting_days"], bins=30, kde=True)
plt.title("Distribution of Waiting Days")
plt.xlabel("Waiting Days")
plt.ylabel("Number of Appointments")
plt.show()

# %%
# the waiting time distribution is right-sekwed, indicating that most appointments are scheduled within the first few days after booking. However, a smaller portion of patients experience significantly longer waits of up to 30 days. 

# %%
# looking for missing values
df.isnull().sum().sort_values(ascending=False)

# %%
# checking if these missing values are no show appointments
df[df["check_in_time"].isnull()].groupby("status").size()

# %%
# which groups have longer waiting times?
df.groupby("status")["waiting_days"].mean().sort_values()

# %%
# waiting times by age groups
df.groupby("age_group")["waiting_days"].mean().sort_values()

# %%
df.select_dtypes(include=["int64", "float64"]).columns

# %%
df.select_dtypes(include=["datetime64[ns]"]).columns

# %%
df.select_dtypes(include=["object", "category"]).columns

# %%
# checking the longer waits 
long_waits = df[df["waiting_days"] > 15]

# %%
long_waits.shape

# %%
# percentage of long waits
len(long_waits) / len(df) * 100

# %%
long_waits["status"].value_counts(normalize=True).mul(100).round(2)

# %%
long_waits["age_group"].value_counts(normalize=True).mul(100).round(2)

# %%
long_waits["insurance"].value_counts(normalize=True).mul(100).round(2)

# %%
df["status"].value_counts(normalize=True).mul(100).round(2)

# %%
# what charactersitics are different for long waits vs normal waits
df["wait_category"] = df["waiting_days"].apply(
    lambda x: "Long wait" if x > 15 else "normal wait"
)

# %%
ct = pd.crosstab(df["age_group"], df["wait_category"], normalize="columns") * 100

# %%
import seaborn as sns
import matplotlib.pyplot as plt 
plt.figure(figsize=(8,6))
sns.heatmap(ct, annot=True, fmt= ".2f", cmap="coolwarm")
plt.title("Age group vs waiting cateogry")
plt.show()

# %%
# checking for the insurance

pd.crosstab(df["insurance"], df["wait_category"], normalize="columns") * 100


# %%
df["weekday"] = df["appointment_date"].dt.day_name()
pd.crosstab(df["weekday"], df["wait_category"], normalize="columns") * 100



