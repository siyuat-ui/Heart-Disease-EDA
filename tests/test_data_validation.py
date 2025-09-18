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
    assert not missing_cols, f"Missing columns: {missing_cols}"
    
    # Value ranges (numeric columns)
    assert df['age'].between(0, 120).all(), "Column 'age' contains invalid values"
    assert df['resting_blood_pressure'].between(50, 250).all(), "Column 'resting_blood_pressure' contains invalid values"
    assert df['cholesterol'].between(50, 600).all(), "Column 'cholesterol' contains invalid values"
    assert df['max_heart_rate_achieved'].between(50, 250).all(), "Column 'max_heart_rate_achieved' contains invalid values"
    assert df['st_depression'].between(0, 10).all(), "Column 'st_depression' contains invalid values"
    assert df['num_major_vessels'].between(0, 4).all(), "Column 'num_major_vessels' contains invalid values"
    
    # Categorical columns (processed values)
    assert df['sex'].isin(['male', 'female']).all(), "Column 'sex' contains invalid values"
    assert df['chest_pain_type'].isin([
        'typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'
    ]).all(), "Column 'chest_pain_type' contains invalid values"
    assert df['fasting_blood_sugar'].isin([
        'lower than 120mg/ml', 'greater than 120mg/ml'
    ]).all(), "Column 'fasting_blood_sugar' contains invalid values"
    assert df['resting_electrocardiogram'].isin([
        'normal', 'ST-T wave abnormality', 'left ventricular hypertrophy'
    ]).all(), "Column 'resting_electrocardiogram' contains invalid values"
    assert df['exercise_induced_angina'].isin(['no', 'yes']).all(), "Column 'exercise_induced_angina' contains invalid values"
    assert df['st_slope'].isin(['upsloping', 'flat', 'downsloping']).all(), "Column 'st_slope' contains invalid values"
    assert df['thalassemia'].isin(['fixed defect', 'normal', 'reversable defect']).all(), "Column 'thalassemia' contains invalid values"
    
    # No missing critical data
    for col in ['age', 'sex', 'target']:
        assert not df[col].isnull().any(), f"Critical column '{col}' contains missing values"
