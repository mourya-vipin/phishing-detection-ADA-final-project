# Week 5 Reflection: Phishing Detection Baseline

### What I have achieved so far:
* Successfully initialized the project repository, established the Git workflow, and sourced the Naser Abdullah Alam Phishing Email Dataset.
* Built a robust data cleaning pipeline that strips HTML, normalizes URLs, and removes non-ASCII artifacts to prepare raw email bodies for NLP.
* Performed exploratory data analysis (EDA), using data visualization (gradient-shaded bar charts and segmented word clouds) to establish the linguistic differences between phishing and legitimate emails.
* Trained a highly explainable TF-IDF and Logistic Regression baseline model.
* Successfully extracted and visualized the model's coefficients to highlight the specific "trigger words" that drive the classification.

### What I am happy with, from your project work so far:
* I am very happy with how the visualizations turned out. Taking the professor's advice to look into *Information is Beautiful* and *Storytelling with Data*, I focused heavily on making the charts intuitive. The gradient shading on the email length distribution and the coefficient bar chart clearly communicate the story of the data without requiring the viewer to read raw arrays of numbers.
* The baseline model's metrics are exceptionally high (98%+ Precision/Recall). However, extracting the coefficients proved exactly why explainability is crucial: the model is suffering from corpus bias. It learned that specific names ("vince") or companies ("enron") heavily indicate a legitimate email, while specific years ("2004") indicate phishing. It did catch real security triggers ("`account`", "`click`", "`remove`"), but the explainability layer successfully revealed that the model is partially "cheating" based on the dataset origins.

### What I am struggling with, or what challenges I am facing next :
* **Next Step Complexity:** My biggest anticipated challenge is moving from this lightweight TF-IDF baseline to a Transformer model (DistilBERT) in Week 7.
* **Dataset Artifacts:** My baseline revealed that the model relies heavily on corpus-specific artifacts (like the word "enron"). I am curious to see if a Transformer model, which understands semantic context better than TF-IDF, will rely less on these specific nouns and more on the actual intent of the email.
* **Context Windows:** My EDA showed some emails are quite long. While TF-IDF handles long documents easily by just counting words, BERT has a strict token limit (usually 512). I am currently researching the best way to handle this—whether to truncate the emails (which might lose the phishing payload at the bottom of the email) or to chunk them.

### Anything else I’d specifically like the course staff to focus on in giving you feedback or advice:
* **Feedback on Explainability Visuals:** Does the current visualization approach for the model coefficients (the red/green horizontal bar chart) meet the expectations for explainability, or should I be looking to integrate a more interactive tool like LIME/SHAP even for this baseline model?
* **Handling Long Texts in Week 7:** Given the 7-week project timeline, would you recommend I simply truncate long emails to 512 tokens for the Transformer model, or is it worth the engineering time to implement a chunking strategy for the comparison?
