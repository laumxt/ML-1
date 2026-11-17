# ML-1: Predicting tree planting years

A notebook-based machine-learning project exploring how to predict the planting year of trees in Grenoble from the city's tree inventory. The notebooks cover data preparation, preprocessing pipelines, regression, and model selection.

## Repository contents

- `arbres_grenoble_epsg4326.csv` — tree inventory data used in the notebooks.
- `Notebooks/ML10_Data_cleaning.ipynb` and `Notebooks/ML10_Data_cleaning_Eng.ipynb` — clean and explore the data, including handling missing values and extracting geographic coordinates.
- `Notebooks/ML11_Pipeline_Model.ipynb` and `Notebooks/ML11_Pipeline_Model_Eng.ipynb` — prepare features and build/evaluate a baseline regression pipeline.
- `Notebooks/ML12_GridSearch_RandomForest.ipynb` and `Notebooks/ML12_GridSearch_RandomForest_Eng.ipynb` — compare tree-based regressors and tune hyperparameters with cross-validation.
- `Aurélien Géron - Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.pdf` — accompanying reference material.

The `Eng` notebooks are English versions; the corresponding notebooks without that suffix are in French where available.

## Getting started

1. Clone the repository and create/activate a Python environment with Jupyter, pandas, NumPy, Matplotlib, Seaborn, and scikit-learn installed.
2. Start Jupyter from the repository root:

   ```bash
   jupyter lab
   ```

3. Open the notebooks in order: data cleaning (ML10), pipeline and baseline model (ML11), then model tuning (ML12). Run the data-cleaning notebook first so its prepared dataset is available to later notebooks.

`requirements.txt` is an environment export containing machine-specific local package paths, so it is not a portable installation file. Install dependencies in your environment using your preferred package manager.

## Project goal

The notebooks use the `annedeplantation` field as the prediction target and demonstrate a machine-learning workflow: inspect and clean the source data, split data for training and evaluation, preprocess numeric and categorical features in a pipeline, and compare model performance.
