# Enhanced Heart Disease Risk Classification Model

## Overview
This project reimagines heart disease risk prediction by transforming raw medical data into actionable insights. It employs advanced data preprocessing, feature engineering, and state-of-the-art machine learning techniques to achieve reliable and meaningful predictions of heart disease risk.

---

## Dataset Overview and Preprocessing

The dataset underwent rigorous cleaning and transformation processes:
- **Outlier Removal**: Ensured data integrity by eliminating anomalous entries.
- **Feature Normalization**: Standardized key features such as blood pressure, weight, and height for consistent scaling.
- **Advanced Clustering**: K-Modes clustering was applied to segregate patterns by gender, unveiling distinct health profiles for males and females.

---

## Feature Engineering and Target Encoding

The dataset was enriched with calculated and categorized metrics:
- **Body Mass Index (BMI)**: Derived and grouped into risk-specific categories.
- **Mean Arterial Pressure (MAP)**: Computed and categorized for better representation.
- **Age Segmentation**: Grouped into cohorts reflecting varying risk levels.
- **Multi-Class Target Encoding**: Expanded prediction scope into five categories:
  - Low Risk
  - Coronary Artery Disease
  - Hypertension-Related Disease
  - Diabetes-Related Disease
  - Multiple Risk Factors

These enhancements provided a robust foundation for model training and better interpretability.

---

## Data Visualization

Visualization was pivotal in understanding trends and correlations within the dataset. Tools like Seaborn and Matplotlib were employed to generate insightful visuals:
- **Heatmaps**: Highlighted correlations among risk factors.
- **Bar Charts**: Illustrated the prevalence of various disease categories.
- **ROC Curves**: Assessed and compared model performance visually.

---

## Model Training

Multiple advanced machine learning algorithms were trained and optimized:
- **Algorithms Used**:
  - Decision Trees
  - Random Forests
  - Multi-Layer Perceptron (MLP)
  - XGBoost
- **Optimization Techniques**:
  - Hyperparameter tuning via GridSearchCV for optimal performance.

Random Forest stood out as the best-performing model after rigorous evaluations.

---

## Evaluation Metrics

A range of evaluation metrics ensured the reliability and accuracy of predictions:
- **Accuracy**: Overall correctness of the model.
- **Precision**: Measure of true positive predictions.
- **Recall**: Sensitivity of the model.
- **F1 Score**: Balance between precision and recall.
- **AUC (Area Under the Curve)**: Insight into the model’s ability to differentiate between classes.

Comprehensive confusion matrices and classification reports validated the effectiveness of the models.

---

## Real-Time Prediction

An interactive system bridges the gap between theoretical modeling and real-world application. Users can input their personal health data to receive:
- **Real-Time Risk Assessments**: Personalized insights into heart health.
- **Actionable Feedback**: Tailored recommendations based on predicted risk.

**Deployed Application**:
- Access the live web application here: [Heart Disease Risk Predictor](https://heart-disease-risk-predictor.onrender.com/)

---

## Installation

Follow these steps to set up the Flask app:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/enhanced-heart-disease-risk.git
   cd enhanced-heart-disease-risk
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   flask run
   ```

5. **Access the Application**:
   Open a browser and navigate to `http://127.0.0.1:5000`.

---

## Key Milestones

1. **Data Preprocessing Completed**:
   - Outlier removal and feature normalization finalized.
   - Clustering implemented to uncover gender-specific health profiles.
2. **Feature Engineering Introduced**:
   - BMI, MAP calculations, and age segmentation integrated.
3. **Machine Learning Models Developed**:
   - Multiple algorithms tested and Random Forest selected as the best performer.
4. **Deployment Achieved**:
   - Flask-based web application successfully deployed to [Render](https://heart-disease-risk-predictor.onrender.com/).

---

## Project Outcomes

1. **Improved Risk Stratification**:
   - Enhanced prediction capabilities with multi-class target encoding.
2. **User-Friendly Interface**:
   - Real-time prediction system empowers users with actionable health insights.
3. **Scalable Framework**:
   - Modular codebase and deployment-ready setup for further development.

---

## Project Flowchart

### Data Processing Flow:
1. Data Cleaning
2. Feature Engineering
3. Data Visualization
4. Model Training
5. Real-Time Prediction

---

## Conclusion

This Enhanced Heart Disease Risk Classification Model combines robust data processing, insightful visualizations, and advanced machine learning techniques to offer a practical solution for heart disease risk assessment. By empowering users with personalized insights, the project aims to contribute significantly to preventive healthcare.

