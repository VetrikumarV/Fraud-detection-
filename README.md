
# Fraud Detection App

This is a simple web app built using Streamlit to predict whether a transaction is fraudulent based on user inputs.

## 💻 How to Run Locally

1. **Clone or Download this repository**

2. **Install required packages**:
```
pip install -r requirements.txt
```

3. **Add your `model.pkl` file** to the same folder as `app.py`. This should be a trained scikit-learn model.

4. **Run the Streamlit app**:
```
streamlit run app.py
```

## 🧾 Inputs Used for Prediction
- Transaction Amount
- Transaction Time (hour of the day)
- User Age

## 🧠 Model
Make sure the model was trained using the same features and preprocessing format. The model should be serialized as `model.pkl` using `pickle` or `joblib`.

---

Made with ❤️ using Streamlit.
