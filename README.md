**AI in Security — Phishing Detection (Explainable ML vs. Black Box)**

### **Prompt**
In computer security, analysts often hesitate to trust “black box” AI models because they need to understand *why* an alert was triggered. I want to build a phishing email detection system that compares a highly explainable, traditional NLP model (e.g., TF‑IDF + Logistic Regression or Random Forest) against a more complex neural network or small transformer model. My goal is to analyze the tradeoffs: does the computational cost and loss of explainability in deep learning justify the performance gains for this specific security task? The final tool will not only flag phishing but also highlight the specific words/features that triggered the alert.

---

### **Execution Plan**

#### **By Week 5 Homework Deadline**
**What:**
- Collect and clean a robust phishing dataset (e.g., Kaggle phishing corpus, Enron spam dataset).
- Build the explainable baseline model.

**How:**
- Use Python, Pandas, and Scikit‑learn to tokenize text, apply TF‑IDF, and train a Logistic Regression or Random Forest classifier.
- Compute baseline metrics with emphasis on Precision and Recall (critical for reducing alert fatigue).

**Why:**
- Establishing a strong, explainable baseline is essential before adding complexity.
- This step demonstrates control over the data pipeline and provides a foundation for comparison.

---

#### **By Week 7 Homework Deadline**
**What:**
- Implement the comparison model (e.g., small BERT or MLP).
- Build the explainability layer.

**How:**
- Train the more complex model and track compute/time requirements.
- Use SHAP or LIME to extract feature importance from the baseline model.
- Build a simple Streamlit or Gradio UI where a user pastes an email and sees:
  - prediction
  - highlighted trigger words/features

**Why:**
- This fulfills the core analytical goal: measuring the tradeoff between cheap/explainable vs. expensive/opaque models.
- The UI makes the tool usable for a hypothetical security analyst.

---

#### **By the Final Due Date**
**What:**
- Polish the UI, finalize the tradeoff analysis, and record the demonstration video.

**How:**
- Ensure the Streamlit app runs smoothly locally.
- Write a short report summarizing accuracy vs. compute vs. explainability.
- Record the 15‑minute video demonstrating:
  - the working UI
  - the modeling code
  - the tradeoffs and design decisions

**Why:**
- This meets the final delivery requirements and demonstrates clear communication of technical tradeoffs.

---