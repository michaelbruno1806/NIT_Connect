from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    name = request.form['name']
    email = request.form['email']
    checkin = request.form['checkin']
    checkout = request.form['checkout']
    message = request.form['message']

    msg = EmailMessage()
    msg.set_content(f"""
    Booking Request from {name}
    Email: {email}
    Check-in: {checkin}
    Check-out: {checkout}
    Message: {message}
    """)
    msg['Subject'] = f"Booking from {name}"
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'destination_mailbox@example.com'

    try:
        with smtplib.SMTP_SSL('smtp.example.com', 465) as smtp:
            smtp.login('your_email@example.com', 'your_password')
            smtp.send_message(msg)
        flash('Booking submitted successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send booking: {e}', 'danger')

    return redirect('/booking')

if __name__ == '__main__':
    app.run(debug=True)
