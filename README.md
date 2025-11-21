## 📩 Daily Tech News Emailer

This project fetches the latest TechCrunch tech news using the NewsAPI and sends a daily email summary to your inbox. It uses Python, the requests library for API calls, and Gmail’s SMTP service to send emails.

## 🚀 Features

- Fetches top technology headlines from TechCrunch

- Sends up to 20 articles directly to your email

- Simple setup using a config.json file

- Works seamlessly on PythonAnywhere for automated daily emails

---

## 🔧 Installation & Setup

1. Clone or download the project
```
git clone https://github.com/yourusername/daily-tech-news-emailer.git
cd daily-tech-news-emailer
```
2. Create config.json

Inside the project folder, create a file named config.json:
```
{
  "api_key": "YOUR_NEWSAPI_KEY",
  "email": "your_email@gmail.com",
  "email_password": "YOUR_GMAIL_APP_PASSWORD"
}
```
Where to get credentials:

NewsAPI Key:
https://newsapi.org

Gmail App Password:

Enable 2-Step Verification

Visit https://myaccount.google.com/apppasswords

Generate a 16-character password

Place it in "email_password"

---

## ▶️ Running Locally

- Make sure you have Python 3 installed.

- Install dependencies:

- pip install requests

```
Run the script:

python main.py
```

You should now receive today’s TechCrunch news via email.

---

## ☁️ Deploying on PythonAnywhere

You can automate this script to run daily using PythonAnywhere.

1. Upload your project files

- On PythonAnywhere → Files tab → upload:

- main.py

- send_email.py

- config.json


2. Set Up a Scheduled Task

- Go to Tasks → Add a scheduled task.

- Command:

  - python3 main.py

- Choose the time you want it to run daily.

PythonAnywhere will now automatically email you the tech news every day.
