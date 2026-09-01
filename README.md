💧 Water Leakage Detection System



Project Overview



The Water Leakage Detection System is a machine learning project developed to predict whether a water pipe is likely to experience leakage based on pipe sensor and operational data.



The project follows a complete machine learning workflow, beginning with raw dataset inspection and cleaning, followed by exploratory data analysis, feature engineering, feature selection, model development, evaluation, model saving and deployment through a Streamlit application.



The final system uses \*\*Logistic Regression\*\* to perform binary classification:



\* `0` → No Water Leakage

\* `1` → Water Leakage



The deployed application allows users to enter pipe-related information and receive a predicted leakage status together with a leakage probability.



PROBLEM STATEMENT



People and communities in KwaZulu-Natal (KZN), South Africa, experience water wastage and unreliable water supply due to undetected leaks and faults within water distribution infrastructure. Water leaks can result in significant losses of treated water before the problem is identified and repaired. Existing monitoring and maintenance practices can be reactive, meaning that a leak may only be addressed after it has already caused substantial water loss or disruption to communities.



This project proposes a machine learning-based water leakage detection system that analyses pipe sensor measurements, including pressure, flow rate and other operational sensor information, to identify patterns associated with potential water leakage. The system aims to support earlier detection of potential leaks, allowing responsible water-management personnel to investigate and intervene before further water is wasted.



Project Objectives



The main objectives of the project were to:



1\. Understand and clean the available water pipe dataset.

2\. Identify unusual and suspicious sensor values.

3\. Explore relationships between pipe measurements and leakage.

4\. Perform univariate, bivariate and multivariate analysis.

5\. Engineer additional features from the available sensor measurements.

6\. Identify the features most relevant to leakage prediction.

7\. Train a classification model.

8\. Evaluate the model using appropriate classification metrics.

9\. Save the trained model for reuse.

10\. Develop and deploy an interactive prediction application.





Dataset



The original dataset contains \*\*5,000 records and 13 columns\*\*.



The dataset contains sensor measurements, operational information and location information.



Features



| Feature           | Description                      |

| ----------------- | -------------------------------- |

| Pressure          | Pressure measurement of the pipe |

| Flow\_Rate         | Water flow rate                  |

| Temperature       | Pipe/system temperature          |

| Vibration         | Vibration measurement            |

| RPM               | Rotational speed                 |

| Operational\_Hours | Number of operational hours      |

| Zone              | Pipe zone                        |

| Block             | Pipe block                       |

| Pipe              | Pipe identifier                  |

| Location\_Code     | Combined location identifier     |

| Latitude          | Geographic latitude              |

| Longitude         | Geographic longitude             |

| Leakage\_Flag      | Target variable                  |



Target Variable



`Leakage\_Flag` is the target variable used for binary classification.



\* `0` = No Leakage

\* `1` = Leakage







Data Preparation and Cleaning



The first stage of the project was to inspect the original dataset and understand its structure.



The dataset was checked for:



Data types

Missing values

Duplicate records

Unusual numerical values

Outliers

Invalid geographic coordinates



&#x20;Missing Values



The dataset contained \*\*no missing values\*\* across the variables.



Duplicate Records



The duplicate check returned \*\*0 duplicate records\*\*.



Suspicious Values



During the initial statistical inspection, several sensor and coordinate values were found to be extremely large compared with the normal ranges of the corresponding variables.



For example, the original dataset contained extremely large values in:



\* Pressure

\* Flow Rate

\* Temperature

\* Vibration

\* Latitude

\* Longitude



These values were investigated and corrected during the cleaning process.



The cleaned dataset retained the same number of columns and was reduced from \*\*5,000 records to 4,857 records\*\* after the subsequent outlier-removal process.







Outlier Detection



Outlier analysis was performed using different methods depending on the variable.



IQR Method



The Interquartile Range method was used for:



\* Pressure

\* Flow Rate

\* Vibration

\* Operational Hours



Z-Score Method



The Z-score method was used for:



\* RPM

\* Temperature



Geographic coordinates were also checked against valid latitude and longitude ranges.



The analysis identified:



\* 42 Pressure outliers using IQR

\* 36 Flow Rate outliers using IQR

\* 36 Vibration outliers using IQR

\* 0 Operational Hours outliers using IQR

\* 13 RPM outliers using Z-score

\* 18 Temperature outliers using Z-score



After the cleaning process, the resulting dataset contained \*\*4,857 records\*\*.







Exploratory Data Analysis



Exploratory Data Analysis was performed to understand the structure of the dataset and investigate relationships with water leakage.



The analysis included:



Univariate Analysis



The project examined individual variables using:



\* Histograms

\* Boxplots

\* Frequency distributions

\* Categorical distributions

\* Leakage class distribution



Bivariate Analysis



Relationships between individual variables and leakage status were investigated using:



\* Flow Rate vs Leakage Status

\* Pressure vs Leakage Status

\* Temperature vs Leakage Status

\* Vibration vs Leakage Status

\* RPM vs Leakage Status

\* Operational Hours vs Leakage Status

\* Leakage by Zone

\* Leakage by Block

\* Leakage by Pipe



&#x20;Multivariate Analysis



Multiple-variable relationships were explored using:



\* Correlation heatmaps

\* Pair plots

\* Multivariable visualisations







Feature Engineering



Additional features were created to capture relationships that were not represented directly by the original variables.



&#x20; Pressure-to-Flow Ratio



A `Pressure\_Flow\_Ratio` feature was created:



`Pressure\_Flow\_Ratio = Pressure / Flow\_Rate`



This feature represents the relationship between pipe pressure and water flow rather than considering the two measurements independently.



&#x20;Operational Hours Level



Operational hours were also grouped into three levels:



\* Low

\* Medium

\* High



&#x20;Vibration Deviation



A `Vibration\_Deviation` feature was created to represent the absolute difference between an observation's vibration value and the overall mean vibration.







Feature Selection



Feature relationships with the leakage target were investigated using correlation analysis.



The strongest relationships identified included:



\* `Pressure\_Flow\_Ratio`

\* `Flow\_Rate`

\* `Pressure`



The correlation analysis showed:



\* Flow Rate: `0.3347`

\* Pressure: `-0.3336`

\* Pressure Flow Ratio: `-0.3789`



A Random Forest analysis was also used to examine feature importance.



The three strongest features were:



1\. `Pressure\_Flow\_Ratio` — 0.3811

2\. `Flow\_Rate` — 0.3156

3\. `Pressure` — 0.2601



Based on this analysis, these three features were selected for the final Logistic Regression model.





Machine Learning Model



The final model uses \*\*Logistic Regression\*\*.



The selected input features are:





Pressure\_Flow\_Ratio

Flow\_Rate

Pressure





The target variable is:





Leakage\_Flag



The model was trained using the selected features and then used to predict leakage on unseen test data.







Training, Validation and Testing



The project progressed through training, validation and testing stages.



The data was divided into:



\* Training data

\* Validation data

\* Testing data



The notebook also used \*\*5-fold cross-validation\*\* during model development.



The average cross-validation score obtained was approximately:



\*\*95.69%\*\*



The validation accuracy was approximately:



\*\*95.88%\*\*



The final testing accuracy was approximately:



\*\*95.54%\*\*



\---



Model Evaluation



The final Logistic Regression model was evaluated using:



\* Confusion Matrix

\* Accuracy

\* Precision

\* Recall

\* F1-Score



&#x20;Final Results



| Metric    | Result |

| --------- | -----: |

| Accuracy  | 95.54% |

| Precision | 66.67% |

| Recall    | 55.56% |

| F1-Score  | 60.61% |



Confusion Matrix





\[\[537  10]

&#x20;\[ 16  20]]





The confusion matrix represents the model's correct and incorrect predictions for the two classes:



\* No Leakage

\* Leakage



The model correctly classified most observations while also identifying a portion of the actual leakage cases.







&#x20;Feature Importance



The project also examined the Logistic Regression coefficients to understand which processed features had the strongest influence on the model.



The feature analysis showed that the selected pressure and flow-related measurements played an important role in the prediction.



This provides some interpretability into the factors influencing the leakage classification.







&#x20;Saving the Model



After developing and evaluating the final model, the trained model was saved using Joblib.



The project saves:





final\_model.pkl

scaler.pkl



The saved files allow the trained model and preprocessing information to be reused without retraining the model every time the application starts.





Streamlit Application



The trained model was integrated into an interactive Streamlit application.



The application allows users to enter pipe sensor information and obtain a leakage prediction.



The application provides:



\* Water leakage prediction

\* No leakage prediction

\* Leakage probability

\* No-leakage probability



The application uses the saved machine learning model rather than retraining the model when a user makes a prediction.







&#x20;Deployment



The Streamlit application was deployed online so that the model can be accessed through a web browser.



&#x20;Live Application



\*\*Water Leakage Detection System\*\*



https://water-leakage-detector.streamlit.app/







&#x20;Repository Structure





Water\_Leakage\_Detection/

│

├── app.py

├── final\_model.pkl

├── scaler.pkl

├── requirements.txt

├── Leakeage\_Prediction.ipynb

└── README.md





File Descriptions



\*\*`Leakeage\_Prediction.ipynb`\*\*



Contains the machine learning workflow, including:



\* Data loading

\* Data inspection

\* Data cleaning

\* Outlier detection

\* Exploratory data analysis

\* Feature engineering

\* Feature selection

\* Model training

\* Validation

\* Testing

\* Model evaluation



\*\*`app.py`\*\*



Contains the Streamlit application used to interact with the trained model.



\*\*`final\_model.pkl`\*\*



Contains the saved final Logistic Regression model.



\*\*`scaler.pkl`\*\*



Contains the saved scaling information used during the modelling process.



\*\*`requirements.txt`\*\*



Contains the Python packages required to run the application.







&#x20;Technologies Used



The project was developed using:



\* Python

\* Jupyter Notebook

\* Pandas

\* NumPy

\* Matplotlib

\* Seaborn

\* SciPy

\* Scikit-learn

\* Joblib

\* Streamlit







Running the Project Locally



Clone the repository and navigate into the project directory.



Install the required dependencies:





pip install -r requirements.txt



Run the Streamlit application:





streamlit run app.py





The application will then open in a web browser.







&#x20;Machine Learning Lifecycle



The project follows the following machine learning lifecycle:



Raw Dataset

&#x20;    ↓

Data Understanding

&#x20;    ↓

Data Cleaning

&#x20;    ↓

Outlier Detection

&#x20;    ↓

Exploratory Data Analysis

&#x20;    ↓

Feature Engineering

&#x20;    ↓

Feature Selection

&#x20;    ↓

Train / Validation / Test

&#x20;    ↓

Model Training

&#x20;    ↓

Model Evaluation

&#x20;    ↓

Final Model

&#x20;    ↓

Model Saving

&#x20;    ↓

Streamlit Application

&#x20;    ↓

Deployment





&#x20;Conclusion



The project demonstrates how machine learning can be applied to a water leakage detection problem.



The workflow progressed from raw sensor data through data preparation and exploratory analysis to feature engineering, feature selection, model development and evaluation.



The final Logistic Regression model uses `Pressure\_Flow\_Ratio`, `Flow\_Rate` and `Pressure` as its primary predictive features and achieved a testing accuracy of approximately \*\*95.54%\*\*.



The trained model was saved and integrated into a Streamlit application, allowing users to interact with the prediction system through a web interface.



The complete machine learning process and supporting analysis are available in the accompanying Jupyter Notebook.



