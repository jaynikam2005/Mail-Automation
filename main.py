import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT

def send_emails():
    # Read Excel file
    df = pd.read_excel("emails.xlsx")
    
    # ===== CONTROL OPTIONS =====
    # 1. Limit total emails sent (set to None for no limit)
    MAX_EMAILS = 5
    
    # 2. Filter by condition (set to None to disable)
    FILTER_CONDITION = None  # Set to None to disable filtering, or use conditions like: (df['Subject'] == "Python Workshop")
    
    # 3. Use 'Send?' column (create this column in Excel if needed)
    USE_SEND_FLAG = False  # Set False to ignore (since this column doesn't exist in your Excel)
    
    # ===== PROCESS FILTERS =====
    if FILTER_CONDITION is not None:
        df = df[FILTER_CONDITION]
    
    if USE_SEND_FLAG and 'Send?' in df.columns:
        df = df[df['Send?'] == "Y"]  # Or use == 1 for numeric flags
    
    if MAX_EMAILS:
        df = df.head(MAX_EMAILS)
    
    # ===== SEND EMAILS =====
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    
    for index, row in df.iterrows():
        try:
            name = row["Name"]
            email = row["To_Email"]
            subject = row["Subject"]
            
            msg = MIMEMultipart()
            msg["From"] = EMAIL
            msg["To"] = email
            msg["Subject"] = subject
            
            body = f"""
            Hi {name},
            
            This is regarding: {subject}
            
            Regards,
            Your Team
            """
            msg.attach(MIMEText(body, "plain"))
            
            server.sendmail(EMAIL, email, msg.as_string())
            print(f"Sent to {name} ({email}) - {subject}")
            
        except Exception as e:
            print(f"Failed to send to {email}: {str(e)}")
    
    server.quit()

if __name__ == "__main__":
    send_emails()