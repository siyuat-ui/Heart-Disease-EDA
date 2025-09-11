# Heart Dataset Analysis

## 1. EDA Summary

- **Data size:** 303 rows and 14 columns (13 independent + 1 target variable), later reduced to 296 after removing faulty data points
- **Missing values:** None
- **Feature types:**
  - Six features are numerical
  - Seven features are categorical
- **Target variable:** Fairly balanced, 54% no-disease to 46% has-disease

### Correlations
- Correlation between features is generally **weak**
- **Numerical features** fairly correlated with target:
  - `num_major_vessels`: -0.47
  - `max_heart_rate_achieved`: 0.43
  - `st_depression`: -0.43
- **Categorical features** better correlated with target:
  - `chest_pain_type`, `num_major_vessels`, `thalassemia`, `exercise_induced_angina`
  - Highest: `thalassemia` (0.52)
- **Cholesterol** has little correlation with heart disease

**Takeaway:** Features with higher predictive power could be **`chest_pain_type`, `num_major_vessels`, `thalassemia`, `exercise_induced_angina`, `max_heart_rate_achieved`,** and **`st_depression`**.

---

## 2. Numerical Features

### Age
- The average age in the dataset is **54.5 years**
- The oldest is **77 years**, whereas the youngest is **29 years**

### Cholesterol
- The average registered cholesterol level is **247.15**
- Maximum level is **564** and the minimum level is **126**
- A healthy cholesterol level is **<200 mg/dl**, and usually high levels are associated with heart disease

### Resting Blood Pressure
- Mean: **131**, Max: **200**, Min: **94**

### Max Heart Rate Achieved
- The average max heart rate registered is **149.5 bpm**
- Maximum: **202 bpm**, Minimum: **71 bpm**

### ST Depression
- The average value of ST depression is **1.06**
- Maximum: **6.2**, Minimum: **0**

### Number of Major Blood Vessels
- Maximum: **3**, Minimum: **0**, Mean: **0.68**

---

## 3. Categorical Features

### Chest Pain
- More than 75% of patients experience either **typical angina** or **non-angina** chest pain
- Patients with **atypical angina** or **non-angina** chest pain are more likely to have heart disease

### Resting Electrocardiogram
- Patients with **Left ventricular hypertrophy** are the fewest (~1.4%)
- The rest are almost a 50-50 split between **ST-T abnormality** and **normal** ECG results
- **ST-T abnormality** correlates more with heart disease

### ST-Slope
- Most patients have a **downsloping** or **flat** ST-Slope
- **Downsloping** ST-Slope is a strong indicator of heart disease

### Thalassemia
- Most patients have **normal** or **reversable defect**
- Patients with **reversable + fixed defects** are less likely to have heart disease
- Those with **normal thalassemia** are more likely to have heart disease (counterintuitive)

### Fasting Blood Sugar
- ~85% of patients have **<120 mg/ml** fasting blood sugar
- Lower fasting blood sugar is associated with a ~54% chance of heart disease

### Exercise Induced Angina
- Two-thirds of patients showed **no exercise induced angina**
- 76% with angina had **no heart disease**, whereas ~69% without angina were diagnosed with heart disease

### Sex
- More patients are **male**
- **Females** appear more likely to suffer from heart disease

---

## 4. Correlation Summary

### Overall Correlations
- Correlation between features is generally **weak**

### Numerical Features
- **num_major_vessels**: -0.47 correlation with target
- **max_heart_rate_achieved**: 0.43 correlation with target
- **st_depression**: -0.43 correlation with target

### Categorical Features
- **chest_pain_type**, **num_major_vessels**, **thalassemia**, and **exercise_induced_angina** show stronger correlations with target
- **thalassemia** has the highest correlation at 0.52

### Cholesterol
- Surprisingly, **cholesterol** has little correlation with heart disease
