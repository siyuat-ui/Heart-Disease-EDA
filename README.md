# Heart Disease Dataset - Exploratory Data Analysis

A comprehensive exploratory data analysis (EDA) project for the Heart Disease dataset, featuring automated data preprocessing, visualization generation, and correlation analysis using multiple statistical methods.

## Project Overview

This project performs an end-to-end analysis of the Heart Disease dataset to identify patterns and relationships between various cardiovascular risk factors and heart disease occurrence. The analysis includes:

- **Data Preprocessing**: Automated cleaning, filtering, and feature transformation
- **Comprehensive Visualizations**: Distribution plots, correlation heatmaps, and pairplots
- **Statistical Analysis**: Pearson correlations, point-biserial correlations, and Cramer's V associations
- **Quality Assurance**: Built-in data validation and pipeline integrity tests

## Objectives

- Understand the distribution and relationships between cardiovascular risk factors
- Identify key predictors of heart disease through statistical correlation analysis
- Generate publication-ready visualizations for medical research insights
- Provide a reproducible analysis pipeline with comprehensive testing

## Features Analyzed

### Numerical Features
- **Age**: Patient age in years
- **Cholesterol**: Serum cholesterol levels (mg/dl)
- **Resting Blood Pressure**: Blood pressure at rest (mmHg)
- **Max Heart Rate Achieved**: Maximum heart rate during exercise
- **ST Depression**: Exercise-induced ST depression
- **Number of Major Vessels**: Vessels colored by fluoroscopy (0-3)

### Categorical Features
- **Sex**: Male/Female
- **Chest Pain Type**: Typical angina, atypical angina, non-anginal pain, asymptomatic
- **Fasting Blood Sugar**: Above/below 120mg/ml
- **Resting ECG**: Normal, ST-T wave abnormality, left ventricular hypertrophy
- **Exercise Induced Angina**: Yes/No
- **ST Slope**: Upsloping, flat, downsloping
- **Thalassemia**: Fixed defect, normal, reversible defect

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/siyuat-ui/Heart-Disease-EDA.git
   cd heart-disease-analysis
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv heart_env
   
   # On Windows
   heart_env\Scripts\activate
   
   # On macOS/Linux
   source heart_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   The script will automatically install dependencies if they're missing.

4. **Create required directories**
   ```bash
   mkdir -p results/figures
   ```

5. **Run the analysis**
   ```bash
   python run_analysis.py
   ```

## Usage & Expected Outputs

### Running the Complete Analysis

Execute the main pipeline script:

```bash
python run_analysis.py
```

The script will automatically:
1. Load and preprocess the raw data
2. Generate numerical feature visualizations
3. Create categorical feature plots
4. Compute correlation matrices
5. Save all outputs to the `results/figures/` directory

### Expected Output Files

After successful execution, the following files will be generated in `results/figures/`:

- **numerical_features_distribution.png** - KDE plots showing distribution of continuous variables by target
- **pairplot_numerical_features.png** - Pairwise scatter plots of numerical features
- **categorical_features_distribution.png** - Count plots for categorical variables
- **numerical_features_correlation.png** - Pearson correlation heatmap
- **point_biserial_correlation.png** - Point-biserial correlations with target variable
- **categorical_features_cramersv.png** - Cramer's V association matrix for categorical features

### Data Validation

Run data quality checks:

```bash
python tests/data_validation.py
```

### Pipeline Integrity Test

Verify the complete pipeline:

```bash
python tests/pipeline_integrity.py
```

## Analysis Highlights

### Statistical Methods Used

1. **Pearson Correlation**: Measures linear relationships between numerical features
2. **Point-Biserial Correlation**: Assesses relationships between continuous and binary variables
3. **Cramer's V**: Evaluates associations between categorical variables

### Data Preprocessing

- Filters out invalid data points (`ca >= 4`, `thal == 0`)
- Transforms numerical codes to meaningful categorical labels
- Standardizes feature names for clarity
- Validates data integrity throughout the process

## Testing

The project includes comprehensive testing:

- **Data Validation**: Ensures data quality and expected value ranges
- **Pipeline Integrity**: Verifies successful execution and output generation
- **Automated Dependency Management**: Handles missing packages gracefully
