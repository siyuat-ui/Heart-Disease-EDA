import pandas as pd

def test_data_validation():
    # Load processed data
    df = pd.read_csv('data/processed/heart_processed.csv')
    
    # Expected columns
    expected_cols = [
        'age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 
        'cholesterol', 'fasting_blood_sugar', 'resting_electrocardiogram',
        'max_heart_rate_achieved', 'exercise_induced_angina', 'st_depression',
        'st_slope', 'num_major_vessels', 'thalassemia', 'target'
    ]
    
    missing_cols = [col for col in expected_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    
    # Value ranges (numeric columns)
    if not df['age'].between(0, 120).all():
        raise ValueError("Column 'age' contains invalid values")
    
    if not df['resting_blood_pressure'].between(50, 250).all():
        raise ValueError("Column 'resting_blood_pressure' contains invalid values")
    
    if not df['cholesterol'].between(50, 600).all():
        raise ValueError("Column 'cholesterol' contains invalid values")
    
    if not df['max_heart_rate_achieved'].between(50, 250).all():
        raise ValueError("Column 'max_heart_rate_achieved' contains invalid values")
    
    if not df['st_depression'].between(0, 10).all():
        raise ValueError("Column 'st_depression' contains invalid values")
    
    if not df['num_major_vessels'].between(0, 4).all():
        raise ValueError("Column 'num_major_vessels' contains invalid values")
    
    # Categorical columns (processed values)
    if not df['sex'].isin(['male', 'female']).all():
        raise ValueError("Column 'sex' contains invalid values")
    
    if not df['chest_pain_type'].isin([
        'typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'
    ]).all():
        raise ValueError("Column 'chest_pain_type' contains invalid values")
    
    if not df['fasting_blood_sugar'].isin([
        'lower than 120mg/ml', 'greater than 120mg/ml'
    ]).all():
        raise ValueError("Column 'fasting_blood_sugar' contains invalid values")
    
    if not df['resting_electrocardiogram'].isin([
        'normal', 'ST-T wave abnormality', 'left ventricular hypertrophy'
    ]).all():
        raise ValueError("Column 'resting_electrocardiogram' contains invalid values")
    
    if not df['exercise_induced_angina'].isin(['no', 'yes']).all():
        raise ValueError("Column 'exercise_induced_angina' contains invalid values")
    
    if not df['st_slope'].isin(['upsloping', 'flat', 'downsloping']).all():
        raise ValueError("Column 'st_slope' contains invalid values")
    
    if not df['thalassemia'].isin(['fixed defect', 'normal', 'reversable defect']).all():
        raise ValueError("Column 'thalassemia' contains invalid values")
    
    # No missing critical data
    critical_cols = ['age', 'sex', 'target']
    for col in critical_cols:
        if df[col].isnull().any():
            raise ValueError(f"Critical column '{col}' contains missing values")
    
    print("Data validation passed!")

# Run the test
if __name__ == "__main__":
    test_data_validation()
