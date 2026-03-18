import smtplib
from email.message import EmailMessage

print("--- Initializing Automated Email Engine ---")

# Email setup
msg = EmailMessage()
msg['Subject'] = "Daily AI Report: Sales Prediction 🚀"
msg['From'] = "your_email@gmail.com"
msg['To'] = "your_email@gmail.com"

email_body = """Good Morning CEO,

Here is your daily AI automated report:
- Total Invoices Scanned: 150
- Predicted Buyers Today: 45
- System Status: 100% Online

Regards,
Wajiha's AI Automation Bot
"""

msg.set_content(email_body)

# Sending email
try:
    print("Connecting to Gmail server...")
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("mjiya0056@gmail.com", "fnijcbzrygrpneyy")
        smtp.send_message(msg)

    print("✅ Email sent successfully!")

except Exception as e:
    print(f"❌ Error: {e}")