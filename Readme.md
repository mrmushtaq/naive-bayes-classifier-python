# Naive Bayes Classifier (From Scratch)

This project implements a **Naive Bayes Classifier** in Python without using machine learning libraries like scikit-learn.

It allows the user to:
- Load data from a CSV file
- Select input features manually
- Calculate prior probabilities and conditional probabilities
- Predict the most likely class using Bayes' Theorem

---

## 📁 Project Structure
naive-bayes-classifier-python/
│
├── naive_bayes.py # Main program
├── data/
│ └── data3.csv # Dataset used for predictions
├── README.md # Project documentation
├── requirements.txt # Required Python libraries
└── .gitignore # Ignore temporary/system files


---

## 🚀 How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the program
python naive_bayes.py
✅ Features

Calculates P(Class) and P(Feature | Class)

Uses Laplace Smoothing to avoid zero probabilities

Supports any CSV dataset with categorical values

Pure Python implementation (no ML libraries)

📌 Requirements
pandas
numpy

⚠ Note

Make sure your dataset file is placed inside the data/ folder.

Modify the path in pd.read_csv() if needed.

✨ Future Improvements

Add GUI using Tkinter or Streamlit

Save outputs to a text file or JSON

Convert to scikit-learn compatible model
