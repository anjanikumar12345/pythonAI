# Cybersecurity Threat Classification Using Machine Learning


## Overview
This project classifies cybersecurity threats using Machine Learning models such as **Random Forest** and **Support Vector Machine (SVM)**. The implementation involves data preprocessing, feature selection, model training, evaluation, and visualization.



## Requirements
Ensure you have the following dependencies installed:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn


```
Additionally, make sure you have a **CSV dataset** named `cybersecurity_data.csv` with labeled threat categories.

## How to Run
1. **Prepare the Dataset**: Ensure your dataset (`telesurgery_cybersecurity_dataset.csv`) is placed in the same directory as the script.
2. **Run the Script**: Execute the following command in a Python environment or Jupyter Notebook:
   ```bash
   python cybersecurity_classification.py
   ```



3. **Model Training & Evaluation**: The script will preprocess the data, train **Random Forest** and **SVM**, and display evaluation metrics such as **accuracy, precision, recall, and F1-score**.
4. **Visualization**: Confusion matrices and feature importance graphs will be displayed to provide insights.




## Expected Output
- **Performance metrics** for each model.
- **Confusion matrix** visualizations.
- **Feature importance** ranking (for Random Forest).




## Next Steps
- Tune hyperparameters for better accuracy.
- Experiment with deep learning models.
- Test on a larger cybersecurity dataset.


