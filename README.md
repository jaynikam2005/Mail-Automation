# 📧 Email Automation Tool

<div align="center">

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*Automate your email campaigns with ease using Excel data sources*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration)

</div>

---

## 🚀 Overview

**Email Automation Tool** is a Python-based solution that allows you to send personalized bulk emails using data from Excel files. Perfect for newsletters, event invitations, notifications, and marketing campaigns.

### ✨ Key Highlights

- 📊 **Excel Integration** - Read recipient data directly from `.xlsx` files
- 🎯 **Smart Filtering** - Send emails based on custom conditions
- 🔒 **Secure Authentication** - Uses Gmail SMTP with app passwords
- 📝 **Personalized Messages** - Dynamic content based on recipient data
- 🛡️ **Error Handling** - Robust error management and logging
- ⚡ **Batch Control** - Limit emails per run to avoid rate limiting

---

## 📁 Project Structure

```
email_sender/
├── 📄 main.py           # Main email sending logic
├── ⚙️  config.py        # Email configuration settings
├── 🔍 debug_excel.py    # Excel file debugging utility
├── 📊 emails.xlsx       # Sample email data file
└── 📁 __pycache__/      # Python cache files
```

---

## 🌟 Features

| Feature | Description | Status |
|---------|-------------|--------|
| 📨 **Bulk Email Sending** | Send personalized emails to multiple recipients | ✅ |
| 📈 **Excel Data Source** | Import recipient data from Excel files | ✅ |
| 🎛️ **Flexible Filtering** | Filter recipients based on custom conditions | ✅ |
| 🚦 **Send Control** | Limit number of emails per batch | ✅ |
| 🔍 **Debug Mode** | Analyze Excel data before sending | ✅ |
| 📝 **Custom Templates** | Personalize email content | ✅ |
| 🛡️ **Error Recovery** | Continue sending even if some emails fail | ✅ |

---

## 🛠️ Installation

### Prerequisites

- Python 3.7+ 🐍
- Gmail account with 2FA enabled 🔐
- App-specific password generated 🔑

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/email-automation-tool.git
cd email-automation-tool

# Install required packages
pip install pandas openpyxl

# Configure your settings
# Edit config.py with your email credentials
```

### 📦 Dependencies

```txt
pandas>=1.3.0
openpyxl>=3.0.0
```

---

## 🚀 Usage

### 1️⃣ **Prepare Your Excel File**

Create an Excel file (`emails.xlsx`) with the following columns:

| Column | Description | Required |
|--------|-------------|----------|
| `Name` | Recipient's name | ✅ |
| `To_Email` | Recipient's email address | ✅ |
| `Subject` | Email subject line | ✅ |
| `Send?` | Send flag (Y/N) | ❌ |

### 2️⃣ **Configure Email Settings**

Update [`config.py`](config.py) with your credentials:

```python
EMAIL = "your-email@gmail.com"
PASSWORD = "your-app-password"  # Not your regular password!
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

### 3️⃣ **Debug Your Data** (Optional)

Run the debug script to analyze your Excel file:

```bash
python debug_excel.py
```

### 4️⃣ **Send Emails**

Execute the main script:

```bash
python main.py
```

---

## ⚙️ Configuration

### 🎛️ Control Options

Customize the [`send_emails()`](main.py) function with these options:

```python
# Limit total emails sent
MAX_EMAILS = 5  # Set to None for no limit

# Filter by condition
FILTER_CONDITION = None  # Or use: (df['Subject'] == "Python Workshop")

# Use 'Send?' column flag
USE_SEND_FLAG = False  # Set True to use Send? column
```

### 📊 Excel Data Format

Your Excel file should look like this:

| Name | To_Email | Subject | Send? |
|------|----------|---------|-------|
| John Doe | john@example.com | Welcome! | Y |
| Jane Smith | jane@example.com | Newsletter | N |

---

## 🔐 Security Setup

### Gmail App Password Setup

1. **Enable 2FA** on your Gmail account
2. Go to **Google Account Settings** → **Security** → **2-Step Verification**
3. Generate an **App Password** for "Mail"
4. Use this 16-character password in [`config.py`](config.py)

> ⚠️ **Important**: Never commit your actual credentials to version control!

---

## 🚨 Error Handling

The tool includes comprehensive error handling:

- ✅ **SMTP Connection Errors** - Automatic retry logic
- ✅ **Invalid Email Addresses** - Skip and continue
- ✅ **Missing Excel Columns** - Graceful degradation
- ✅ **File Not Found** - Clear error messages

---

## 📈 Examples

### Example 1: Send Welcome Emails

```python
# Filter for welcome emails only
FILTER_CONDITION = (df['Subject'] == "Welcome!")
MAX_EMAILS = 10
```

### Example 2: Use Send Flag

```python
# Only send to recipients marked with 'Y'
USE_SEND_FLAG = True
FILTER_CONDITION = None
```

### Example 3: Test Mode

```python
# Send only to first 3 recipients for testing
MAX_EMAILS = 3
FILTER_CONDITION = None
```

---

## 🐛 Troubleshooting

<details>
<summary><strong>Common Issues & Solutions</strong></summary>

### 🔴 Authentication Failed
- Verify your app password is correct
- Ensure 2FA is enabled on Gmail
- Check if "Less secure app access" is needed

### 🔴 Excel File Not Found
- Ensure `emails.xlsx` is in the same directory
- Check file permissions
- Verify file format is `.xlsx`

### 🔴 Missing Columns
- Run [`debug_excel.py`](debug_excel.py) to check your file structure
- Ensure required columns exist: `Name`, `To_Email`, `Subject`

</details>

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with ❤️ using Python
- Powered by pandas for Excel processing
- Gmail SMTP for reliable email delivery

---

<div align="center">

**Made with 💜 by JAEY**

⭐ Star this repo if you found it helpful!

</div>
