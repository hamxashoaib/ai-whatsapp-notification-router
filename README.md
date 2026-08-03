# 🤖 AI WhatsApp Notification Router

> AI-powered WhatsApp Message Notification Router built with **Python**, **Google Gemini**, **Rule-Based Filtering**, and **Retrieval-Based Reasoning** to intelligently classify incoming messages as **Notify**, **Digest**, or **Mute**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📖 Overview

Notification overload is one of the biggest challenges in modern messaging applications. Users receive personal chats, work messages, group discussions, promotional offers, business notifications, and spam throughout the day.

This project provides an **AI-powered notification routing system** that intelligently determines whether a WhatsApp message should:

- 🔔 **Notify** – Important enough to interrupt the user immediately.
- 📥 **Digest** – Useful information that can be shown later.
- 🔕 **Mute** – Low-priority, repetitive, promotional, or suspicious content.

The system combines deterministic rules with contextual reasoning using Google Gemini, enabling personalized and reliable notification decisions.

---

# ✨ Features

- 🤖 Google Gemini AI Integration
- 🧠 Hybrid Rule + LLM Architecture
- 📂 Automatic CSV Dataset Processing
- 📜 Rule-Based Message Classification
- 🔍 Retrieval-Based Context Selection
- 💬 Context-Aware Message Reasoning
- 📊 Confidence Score Prediction
- 📝 Human-Readable Decision Explanation
- 📌 Historical Evidence Message Retrieval
- 🔄 Fallback Prediction when API is unavailable
- 📤 Automatic `output.csv` Generation

---

# 🏗️ Project Structure

```text
.
├── dataset/
│   ├── messages.csv
│   ├── users.csv
│   ├── groups.csv
│   ├── group_members.csv
│   ├── business_accounts.csv
│   ├── user_business_history.csv
│   ├── message_history.csv
│   ├── message_events.csv
│   ├── sample_messages.csv
│   ├── images.csv
│   ├── voice_notes.csv
│   └── output.csv
│
├── config.py
├── data_loader.py
├── predictor.py
├── reasoner.py
├── retrieval.py
├── rules.py
├── multimodal.py
├── prompts.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ System Architecture

```text
                    Incoming Message
                           │
                           ▼
                  Dataset Loader
                           │
                           ▼
                  Rule-Based Engine
                 (High Confidence?)
                    │           │
                  Yes           No
                   │             ▼
            Direct Prediction   Context Retrieval
                                  │
                                  ▼
                           Gemini Reasoning
                                  │
                                  ▼
                       Output Generation
                                  │
                                  ▼
                            output.csv
```

---

# 🤖 AI Pipeline

## 1. Dataset Loading

The system loads all required CSV datasets including:

- Messages
- Users
- Groups
- Business Accounts
- Message History
- Message Events
- Images Metadata
- Voice Notes Metadata

---

## 2. Rule-Based Filtering

The first stage checks whether a message can be classified using predefined rules.

This reduces unnecessary AI calls and improves efficiency.

---

## 3. Context Retrieval

If the message cannot be confidently classified by rules, the system retrieves relevant historical messages and contextual information from the provided datasets.

Retrieved context includes:

- User history
- Previous conversations
- Business interactions
- Related message evidence

---

## 4. Gemini Reasoning

Google Gemini analyzes:

- Message intent
- Urgency
- Importance
- User relevance
- Context

and predicts:

- Action
- Message Type
- Confidence
- Reason

---

## 5. Fallback Strategy

If Gemini is unavailable (such as API quota limits), the system automatically generates a safe fallback prediction, ensuring that every incoming message still receives a valid output.

---

# 📂 Input Files

The project reads:

- messages.csv
- users.csv
- groups.csv
- group_members.csv
- business_accounts.csv
- user_business_history.csv
- message_history.csv
- message_events.csv
- sample_messages.csv
- images.csv
- voice_notes.csv

---

# 📤 Output

The system generates:

```
output.csv
```

with the following columns:

| Column | Description |
|----------|-------------|
| message_id | Incoming message identifier |
| action | notify / digest / mute |
| message_type | Classified message category |
| reason | Human-readable explanation |
| confidence | Prediction confidence |
| evidence_message_ids | Supporting historical messages |

---

# 🛠️ Tech Stack

## Language

- Python

## Libraries

- Pandas
- Google Gemini API
- python-dotenv

## AI

- Google Gemini
- Prompt Engineering
- Rule-Based Reasoning
- Retrieval-Based Context

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/hamxashoaib/ai-whatsapp-notification-router.git

cd ai-whatsapp-notification-router
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run

```bash
python main.py
```

After execution, the project generates:

```
dataset/output.csv
```

---

# 📊 Sample Output

| message_id | action | confidence |
|------------|----------|------------|
| msg_023 | notify | 0.97 |
| msg_091 | mute | 0.98 |
| msg_090 | digest | 0.50 |

---

# 🔮 Future Improvements

- OCR support for image messages
- Speech-to-text processing for voice notes
- Local LLM fallback
- Vector database retrieval
- Adaptive user preference learning
- Multi-language support
- WhatsApp API integration

---

# 👨‍💻 Author

**Hamza Shoaib**

AI & Machine Learning Engineer

- Python
- Generative AI
- AI Agents
- Prompt Engineering
- Automation

---

# 📄 License

This project is released under the MIT License.

---

⭐ If you found this project interesting, consider giving it a star!
