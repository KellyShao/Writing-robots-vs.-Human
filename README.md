# A Reversed Turing Test for Detecting Machine-made Texts
This research aims to detecting machine-generated articles and dialogs.

## Introduction
As AI technologies rapidly advance, the artifacts created by machines will become prevalent. As recent incidents by the *Deepfake* illustrate, then, being able to differentiate  man-made vs. machine-made artifacts, especially in social media space, becomes more important. In this preliminary work, in this regard, we formulate such a classification task as the *Reverse Turing Test* (RTT) and investigate on the contemporary status to be able to classify man-made vs. machine-made texts. Studying real-life machine-made texts  in three domains of financial earning reports, research articles, and chatbot dialogues, we found that the classification of man-made vs. machine-made texts  can be done at least as accurate as 0.84 in F1 score. We also found some differences between man-made and machine-made in sentiment, readability, and textual features, which can help differentiate them. 

**Publication**: Jialin Shao, Adaku Uchendu, and Dongwon Lee. 2019. A Reverse Turing Test for Detecting Machine-Made Texts. In Proceedings of the 10th ACM Conference on Web Science (WebSci '19). ACM, New York, NY, USA, 275-279. DOI: https://doi.org/10.1145/3292522.3326042


## Datasets
We have collected or generated man-made vs. machine-made texts in three domains as follows:
### 1. Academic Papers: 
**machine-made text**: Using [SCIgen](https://pdos.csail.mit.edu/archive/scigen/), an automatic CS paper generator, developed at MIT, we have generated 908 synthetically-generated Computer Science papers. The collection is named as raw_paper_M. 

**man-made text**: For the man-made academic papers, next, we first collected an open-source dataset from  Kaggle, which contains papers published in the AAAI Neural Information Processing Systems (NIPS) conferences, and papers from the Translation Archive that includes papers from 52 different computer science conferences. Due to the influence from NIPS, note that man-made academic paper dataset has more AI flavour. A total of 7,876 papers in this collection is named as raw_paper_H.

### 2. Earnings Reports:
**machine-made text**: For machine-made news articles, we crawled and scraped data from media websites, such as Yahoo Finance and Forbes. Two leading companies, *Automated Insights* and *Narrative Science*, are in partnership with *Yahoo Finance* and *Forbes*, respectively, providing auto-generated financial earning reports.
Merging the reports of these two websites together and removing each company's canned copyright message (e.g., "this story is generated by Automated Insights"), we obtained a total of 4,210 earning reports, named as raw\_report_M.

**man-made text**: For man-made news articles, next, we chose earnings report of similar lengths and topics, written by human reporters. We collected 2,100 earnings reports from a financial website [MarketWatch](https://www.marketwatch.com/) and named it as raw_report_H. Figure~\ref{fig:examples} provides the examples of man-made vs. machine-made earnings reports in our datasets.

### 3. Chatbot Dialogues:
**machine-made text** & **man-made text**: The chatbot dialogue data comprises of machine-made and man-made texts from a chatbot competition, known as *the Society for the Study of Artificial Intelligence and Simulation of Behaviour* [AISB](https://www.aisb.org.uk/). In this competition, a human judge (A) converses with a counterpart who can be either another human (B) or a chatbot (C) (i.e., identity hidden). The response from the counterpart is generated in texts and rated by the human judge (A) for the ability to pass the Turing Test (i.e., how response is likely to be written by a human). 
The dataset, consisting of 993 dialogues, is named as raw_dialog_M and raw_dialog_H, for the machine-made and man-made texts, respectively. 




