from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', '1987')

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Debug email configuration
logger.debug(f"Mail Username: {app.config['MAIL_USERNAME']}")
logger.debug(f"Mail Password: {'*' * len(app.config['MAIL_PASSWORD']) if app.config['MAIL_PASSWORD'] else 'Not set'}")

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Log form data
        logger.debug(f"Form data received: {request.form}")
        
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        reason = request.form.get('reason')

        # Validate required fields
        if not all([name, email, message, reason]):
            logger.error("Missing required fields")
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('home') + '#contact')

        # Validate email format
        if '@' not in email or '.' not in email:
            logger.error(f"Invalid email format: {email}")
            flash('Please enter a valid email address', 'error')
            return redirect(url_for('home') + '#contact')

        # Create email message
        msg = Message(
            subject=f"Portfolio Contact: {reason}",
            sender=email,
            recipients=[app.config['MAIL_USERNAME']]
        )
        
        msg.body = f"""
        New Contact Form Submission:
        
        Name: {name}
        Email: {email}
        Reason: {reason}
        
        Message:
        {message}
        """
        
        # Log before sending
        logger.debug(f"Attempting to send email to {app.config['MAIL_USERNAME']}")
        
        # Send email
        mail.send(msg)
        
        # Log success
        logger.info("Email sent successfully")
        flash('Message sent successfully! I will get back to you soon.', 'success')
        
    except Exception as e:
        # Log the full error
        logger.error(f"Error sending email: {str(e)}", exc_info=True)
        flash('Failed to send message. Please try again later or contact me directly via email.', 'error')
    
    return redirect(url_for('home') + '#contact')

@app.route('/download-resume')
def download_resume():
    return send_from_directory('static', 'resume.pdf', as_attachment=True)

if __name__ == '__main__':
    # Verify email configuration on startup
    if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
        logger.warning("Email configuration is incomplete. Please check your .env file.")
    app.run(debug=True) 