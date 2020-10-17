# ai4cybersecurity
It's impractical to deal with threats of malware, which is increasing exponentially, by the analysis conducted only by human operators. This leads us to the use of some algorithm which allows us to automate introductory phases of analysis known as **tiage**. These algorithms help cybersecurity professionals respond effectively to ongoing attacks by conducting a preliminary screening of threats.

Here are tasks done by AI in the field of cybersecurity.  
* Classification : Properly indentifies types of similar attacks.  
* Clustering : Indentifies the classes to which samples belong when information about those classes are not available in advance.  
* Predictive analysis : Indentifies threats as they occur. NN and DL are used frequently because algorithms in use need to be optimized dynamically by learning.  

Popular uses of AI in cybersecurity.  
* Network Protection : Done by implementing IDS(Intrusion Detection Systems).  
* Endpoint Protection : Detecting threats such as ransomware.  
* Application Security : Countering SSRF(Server Side Request Forgery), SQL Injection, XSS(Cross-Site Scripting) and DDoS(Distributed Denial of Service) attacks by using AI and ML tools.  
* Suspect user behavior  

# Detecting Spam
Among the initial applications of AI to a cybersecurity field, spam detection is the major one since various approaches could be taken.  
Here are some of those approaches.
* Perceptron
* Support Vector Machine
* Phishing Detection with logistic regression and decision tree
* Naive Bayes
* NLP
To implement a reliable spam filter, we need to introduce a score assigned on each message and allow it to help spam filters distinguish between spam mails and hams.(not spam messages) Also, our algorithms on which filters are based should be able to change its parameters dynamically, otherwise it would fail to deal with malicious senders' attempts. 

## Perceptron
Defined in src/spam_filter/perceptron.py.  
pros
* Simple binary linear classifier  

cons
* Only applicable when the analyzed data is linearly separable

The following charts clearly show the Perceptron's weakness.
![alt text](https://github.com/froprintoai/ai4cybersecurity/blob/master/spam_filter/img/img1.png?raw=true)
