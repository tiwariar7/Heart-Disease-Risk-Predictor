# Enhanced Heart Disease Risk Prediction Model

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
   python app.py
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

## Foundational Research Papers for Enhanced Heart Disease Risk Classification Model

### 1. Framingham Heart Study
**Title**: "A General Cardiovascular Risk Profile for Use in Primary Care: The Framingham Heart Study"  
**Authors**: D'Agostino RB et al.  
**Published in**: Circulation, 2008  
**Summary**: This paper provides a comprehensive cardiovascular risk model based on long-term population data. It includes risk factors like age, cholesterol, blood pressure, and diabetes, forming the basis for heart disease prediction models.  
**Relevance**: Use this as a theoretical background for feature selection and risk profiling.  
**Link**: [Framingham Heart Study PDF](https://www.ahajournals.org/doi/full/10.1161/CIRCULATIONAHA.107.699579)

---

### 2. Data Preprocessing Techniques
**Title**: "Efficient Techniques for Data Preprocessing in Medical Data Mining"  
**Authors**: P. Garla et al.  
**Published in**: SpringerLink, 2012  
**Summary**: Discusses data cleaning, handling missing values, and feature engineering techniques for medical datasets.  
**Relevance**: Use this as a guide for preparing and preprocessing your dataset effectively.  
**Link**: Available via Springer or institutional access.

---

### 3. Machine Learning in Healthcare
**Title**: "An Introduction to Machine Learning for Clinicians"  
**Authors**: Rajkomar A, Dean J, Kohane I  
**Published in**: Nature Medicine, 2019  
**Summary**: This paper provides an overview of machine learning applications in healthcare, emphasizing models like Random Forest and XGBoost for risk predictions.  
**Relevance**: Use this paper to justify your choice of machine learning algorithms.  
**Link**: [Nature Medicine PDF](https://www.nature.com/articles/s41591-018-0316-z)

---

### 4. Heart Disease Prediction Models
**Title**: "A Comprehensive Study of Heart Disease Prediction Using Machine Learning"  
**Authors**: Vaishali S, Poonkuzhali R  
**Published in**: Elsevier Procedia Computer Science, 2018  
**Summary**: This paper examines various machine learning techniques applied to heart disease datasets, comparing model performance metrics.  
**Relevance**: Directly aligns with your project's goal of comparing models like Random Forest, XGBoost, and MLP.  
**Link**: Accessible via Elsevier or institutional access.

---

### 5. Explainable AI for Heart Disease
**Title**: "Explainable AI Models for Heart Disease Prediction Using Medical Data"  
**Authors**: Choi E, Schuetz A, Stewart WF  
**Published in**: IEEE Transactions on Biomedical Engineering, 2020  
**Summary**: Focuses on interpretability of machine learning models, explaining predictions with SHAP or LIME visualizations.  
**Relevance**: Use this for adding an explainable AI layer to your interactive prediction system.  
**Link**: [IEEE Explore](https://ieeexplore.ieee.org/)

---

### 6. Hypertension and Risk Profiling
**Title**: "Risk Factors for Hypertension: Insights from Machine Learning"  
**Authors**: Krittanawong C et al.  
**Published in**: Hypertension Journal, 2017  
**Summary**: Highlights feature importance and risk factors contributing to hypertension.  
**Relevance**: Enhances your model's focus on hypertension-related disease classification.  
**Link**: Available via institutional access.

---

### 7. Predictive Analytics in Cardiovascular Risk
**Title**: "Predictive Analytics for Cardiovascular Risk with Big Data Applications"  
**Authors**: Sharma A, Rani S  
**Published in**: Springer Advances in Computational Intelligence, 2020  
**Summary**: Explores how big data and predictive analytics can enhance the early detection of cardiovascular risks. The paper emphasizes using ensemble methods and feature importance analysis for accurate predictions.  
**Relevance**: Offers insights into handling large-scale medical datasets and leveraging ensemble techniques.  
**Link**: Available via Springer or institutional access.

---

### 8. Cardiovascular Disease Prediction with ML
**Title**: "Using Machine Learning for Predicting Cardiovascular Disease: A Review"  
**Authors**: Haq A, Li J, Ali R  
**Published in**: IEEE Access, 2019  
**Summary**: A review of machine learning algorithms for cardiovascular disease prediction, including their challenges and benefits in real-world applications.  
**Relevance**: Provides a comparative analysis of ML models like SVM, Random Forest, and Neural Networks, directly relevant to your project.  
**Link**: [IEEE Access](https://ieeexplore.ieee.org/)

---

### 9. Feature Selection for Medical Datasets
**Title**: "Feature Selection Techniques for Medical Data Mining: A Comprehensive Review"  
**Authors**: Nguyen H, Huang JZ  
**Published in**: Journal of Biomedical Informatics, 2020  
**Summary**: Discusses advanced feature selection techniques for medical datasets, which improve model performance by reducing dimensionality and enhancing interpretability.  
**Relevance**: Useful for understanding the best practices in feature engineering and selection for heart disease risk prediction.  
**Link**: Available via Elsevier or institutional access.

---

### 10. Gender-Specific Risk Factors for Heart Disease
**Title**: "Sex Differences in Cardiovascular Risk Factors and Outcomes: A Comprehensive Study"  
**Authors**: Mosca L, Barrett-Connor E  
**Published in**: Circulation, 2011  
**Summary**: Explores gender-specific patterns in cardiovascular risk factors and outcomes, emphasizing tailored risk prediction models.  
**Relevance**: Can enhance the gender-specific clustering you have implemented in your project.  
**Link**: [Circulation Journal](https://www.ahajournals.org/doi/full/10.1161/CIRCULATIONAHA.110.968792)

---

### 11. Multi-Class Classification in Health Predictions
**Title**: "Multi-Class Classification Approaches for Disease Prediction in Healthcare"  
**Authors**: Maji S, Pal A  
**Published in**: ACM Transactions on Intelligent Systems, 2018  
**Summary**: Explores multi-class classification challenges and methods, focusing on healthcare datasets with diverse outcomes.  
**Relevance**: Aligns with your model's multi-class target encoding.  
**Link**: Available via ACM Digital Library.



### Conclusion

This Enhanced Heart Disease Risk Classification Model combines robust data processing, insightful visualizations, and advanced machine learning techniques to offer a practical solution for heart disease risk assessment. By empowering users with personalized insights, the project aims to contribute significantly to preventive healthcare.

