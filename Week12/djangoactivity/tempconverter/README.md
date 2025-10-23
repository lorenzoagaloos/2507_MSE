# Temperature Converter Django Web App

A simple functional temperature converter web application built with Django.

## Features
- Convert between Celsius, Fahrenheit, and Kelvin
- Clean, modern user interface with gradient design
- Real-time conversion
- Responsive design for mobile and desktop
- Input validation and error handling

## How to Run

1. **Navigate to the project directory:**
   ```bash
   cd djangoactivity
   ```

2. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

3. **Open your browser and visit:**
   ```
   http://127.0.0.1:8000/

4. **Click on the Temperature Converter Button to open the converter page**
   ```

## Usage
1. Enter a temperature value
2. Select the unit you're converting FROM (Celsius, Fahrenheit, or Kelvin)
3. Select the unit you're converting TO
4. Click "Convert Temperature"
5. View your result instantly!

## Temperature Conversion Formulas
- **Celsius to Fahrenheit:** (°C × 9/5) + 32 = °F
- **Celsius to Kelvin:** °C + 273.15 = K
- **Fahrenheit to Celsius:** (°F - 32) × 5/9 = °C
- **Kelvin to Celsius:** K - 273.15 = °C

## Technologies Used
- Django 5.2.7
- Python 3
- HTML5
- CSS3 (with modern gradients and animations)

## Development Notes
- The app uses Django's template system for rendering
- CSRF protection is enabled for form security
- Input validation prevents invalid data submission
- Responsive design works on all screen sizes
