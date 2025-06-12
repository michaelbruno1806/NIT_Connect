from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/services')
def services():
    return render_template('services.html')

@main.route('/service-detail')
def service_detail():
    return render_template('service_detail.html')

@main.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

# app/booking/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import current_app as app
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