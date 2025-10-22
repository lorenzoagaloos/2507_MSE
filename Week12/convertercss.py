"""A simple Flask web application for temperature conversion."""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page."""
    return redirect(url_for('convert'))

@app.route('/convertercss', methods=['GET', 'POST'])
def convert():
    """Handle temperature conversion requests."""
    result = None
    if request.method == 'POST':
        temp = float(request.form['temp'])
        conversion = request.form['conversion']

        if conversion == 'c_to_f':
            result = f"{temp}°C = {(temp * 9/5) + 32:.2f}°F"
        elif conversion == 'f_to_c':
            result = f"{temp}°F = {(temp - 32) * 5/9:.2f}°C"
        elif conversion == 'c_to_k':
            result = f"{temp}°C = {temp + 273.15:.2f}K"
        elif conversion == 'k_to_c':
            result = f"{temp}K = {temp - 273.15:.2f}°C"
        elif conversion == 'f_to_k':
            result = f"{temp}°F = {(temp - 32) * 5/9 + 273.15:.2f}K"
        elif conversion == 'k_to_f':
            result = f"{temp}K = {(temp - 273.15) * 9/5 + 32:.2f}°F"

    return render_template('convertercss.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
