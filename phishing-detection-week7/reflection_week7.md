# Week 7 Reflection: Model Comparison & Advanced Explainability

### What I have achieved so far
* **Incorporated Validation Feedback:** Implemented 5-Fold Cross-Validation on the baseline. The CV metrics held at ~97% Precision and ~98% Recall, proving the Week 5 metrics were not an artifact of a lucky split.
* **Addressed Length Assumptions:** I removed the assumption that shorter lengths inherently indicate phishing. We now treat length strictly as an exploratory variable to prevent injecting human bias into our analysis.
* **Explored Context Windows:** Tested "Head" vs "Tail" truncation for Transformer inputs using the DistilBERT tokenizer. Because phishing hooks (urgency, fake sender) happen at the top of an email, I demonstrated that Head truncation (first 512 tokens) is the superior strategy.
* **Implemented Neural Network Comparison:** Introduced an MLP classifier (Multi-Layer Perceptron) to act as our opaque deep-learning comparison model. I tracked the compute time and created a visual tradeoff analysis comparing it against the baseline.
* **LIME UI Integration:** Successfully implemented Local Interpretable Model-agnostic Explanations (LIME) and embedded the HTML output into a working Streamlit application (`app.py`), complete with theme-agnostic CSS to ensure readability in both light and dark modes.

### What I am happy with
* **The LIME output validated my Week 5 hypothesis perfectly.** In Week 5, I suspected the baseline model suffered from corpus bias. When I ran LIME on email Index 42, the model flagged it as Legitimate with 92% confidence simply because it contained academic words like `research`, `science`, `university`, and `learning`. LIME successfully proved that the model is making decisions based on benign dataset artifacts rather than deep semantic security logic!
* I am thrilled with the Streamlit app. Seeing the model highlight trigger words in real-time makes the concept of "Explainability" tangible and fulfills the vision of a tool an actual security analyst could use on a daily basis.

### What I am struggling with, or what challenges I am facing next
* **Compute Restraints:** I initially wanted to fine-tune DistilBERT for the neural network comparison, but the compute cost on my local hardware was too high, even with a 10,000-row sample. I pivoted to an MLP to fulfill the opaque model requirement. The MLP still proved the tradeoff point (achieving slightly higher precision/recall but taking significantly more compute time than Logistic Regression).
* **Structuring the Final Video:** My final deliverable requires demonstrating the UI, the code, and the tradeoffs in 15 minutes. Balancing the "live demo" of the app with the presentation of the mathematical tradeoffs (Accuracy vs. Compute vs. Explainability) will require careful scripting.

### Anything else I’d specifically like the course staff to focus on in giving you feedback or advice
* **MLP vs. Transformer:** Given local compute limitations, is comparing the Logistic Regression baseline against the MLP Neural Network sufficient for the final tradeoff analysis, or should I attempt to spin up a cloud GPU environment to explicitly fine-tune DistilBERT for the final video?
* **Tradeoff Presentation:** For the final report and video, do you prefer visual charts (like the compute-time bar chart I started in the notebook) or a more text-based evaluation matrix to summarize the Explainable vs. Opaque model comparison?