from flask import Blueprint, render_template, request, redirect, url_for, flash

import smtplib
from email.mime.text import MIMEText

booking = Blueprint('booking', __name__)

@booking.route('/booking', methods=['GET', 'POST'])
def booking_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        message = request.form['message']

        content = f"New Booking Request:\nName: {name}\nEmail: {email}\nDate: {date}\nMessage: {message}"

        msg = MIMEText(content)
        msg['Subject'] = 'New Booking Request'
        msg['From'] = 'your_email@example.com'
        msg['To'] = 'your_mailbox@example.com'

        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)

        flash('Your booking request has been sent!', 'success')
        return redirect(url_for('main.index'))
    return render_template('booking.html')