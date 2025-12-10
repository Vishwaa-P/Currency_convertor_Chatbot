# 💰 Currency Converter Chatbot (Telegram & Dialogflow)

A smart chatbot integrated with **Telegram** that converts currencies in real-time using natural language processing. Built with **Dialogflow**, **Python (Flask)**, and deployed on **Render**.

> **FOR LEARNING PURPOSES ONLY** :
> This project was created as an exercise to learn chatbot development and API integration.
> * The currency exchange rates are fetched from a free public API and may not be 100% real-time or accurate.
> * The bot may occasionally glitch or experience downtime due to server limitations on the free tier.

---

## 🚀 Features
* **Natural Language Understanding:** Ask in plain English (e.g., *"Convert 100 USD to INR"* or *"What is 50 Euro in JPY?"*).
* **Real-Time Data:** Fetches live exchange rates using the [Frankfurter API](https://www.frankfurter.app/).
* **Multi-Platform:** Logic is handled by Dialogflow, making it easy to extend to other platforms beyond Telegram.
* **Cloud Hosted:** Backend runs 24/7 on Render.

## 🛠️ Tech Stack
* **Backend:** Python (Flask)
* **NLP Engine:** Google Dialogflow ES
* **Messaging Platform:** Telegram
* **Deployment:** Render (Web Service)
* **API:** Frankfurter (Open Source Currency Data)

---

## ⚙️ How It Works
1.  **User** sends a message to the Telegram Bot.
2.  **Telegram** forwards the message to **Dialogflow**.
3.  **Dialogflow** identifies the *Intent* (Currency Conversion) and extracts parameters (Amount, Source Currency, Target Currency).
4.  Dialogflow sends a webhook request to the **Flask App** (hosted on Render).
5.  **Flask App** calls the **Frankfurter API** to get the conversion rate.
6.  The calculated response is sent back to the user on Telegram.

---

## 💻 Local Setup (Run on your machine)

If you want to run this code on your own computer:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Vishwaa-P/Currency_convertor_Chatbot.git](https://github.com/Vishwaa-P/Currency_convertor_Chatbot.git)
    cd Currency_convertor_Chatbot
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**
    ```bash
    python app.py
    ```
    *The app will run locally at `http://127.0.0.1:5001`*

---

## 🌐 Deployment (Render)

This app is deployed using [Render](https://render.com/).
* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `gunicorn app:app`

---

## 📸 demo
<img width="540" height="1154" alt="image" src="https://github.com/user-attachments/assets/2f18397d-8010-4374-ac3d-e445721280c9" />



---

* *Project created for the Dialogflow & Python Backend integration module.*
