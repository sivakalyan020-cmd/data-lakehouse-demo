"""Simple Great Expectations suite for demonstration.

This script defines a basic Great Expectations expectation on a Pandas DataFrame. In practice you
would integrate this into an Airflow task or an automated data validation step.
"""

import pandas as pd
from great_expectations.dataset import PandasDataset


def run_expectations():
    # Create a simple DataFrame
    df = pd.DataFrame({'value': [1, 2, 3, 4]})
    dataset = PandasDataset(df)
    # Expect all values to be within a predefined set
    dataset.expect_column_values_to_be_in_set('value', [1, 2, 3, 4])
    results = dataset.validate()
    print(results)


if __name__ == "__main__":
    run_expectations()
