import subprocess
import os

def test_pipeline():
    # Run the end-to-end script
    result = subprocess.run(['python', 'run_analysis.py'], capture_output=True, text=True)
    
    # Check return code
    assert result.returncode == 0, f"Pipeline failed!\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"

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
    assert not missing_files, f"Pipeline incomplete! Missing files: {missing_files}"
