import subprocess
import os

def test_pipeline():
    # Run the end-to-end script
    try:
        subprocess.run(['python', 'run_analysis.py'], check=True)
        print("Script ran successfully!")
    except subprocess.CalledProcessError:
        raise RuntimeError("Pipeline failed during execution!")

    # List of expected output files
    expected_files = [
        'data/processed/heart_processed.csv',
        'results/figures/categorical_features_cramersv.png',
        'results/figures/categorical_features_distribution.png',
        'results/figures/numerical_features_correlation.png',
        'results/figures/numerical_features_distribution.png',
        'results/figures/pairplot_numerical_features.png',
        'results/figures/point_biserial_correlation.png'
    ]

    # Check if all expected files exist
    missing_files = [f for f in expected_files if not os.path.exists(f)]
    if missing_files:
        raise FileNotFoundError(f"Pipeline incomplete! Missing files: {missing_files}")
    
    print("All expected files were generated successfully!")

# Run the test
if __name__ == "__main__":
    test_pipeline()
