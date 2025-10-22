from django.shortcuts import render

def index(request):
    """Main view for temperature converter"""
    context = {
        'result': None,
        'input_temp': '',
        'from_unit': 'celsius',
        'to_unit': 'fahrenheit'
    }
    
    if request.method == 'POST':
        try:
            input_temp = float(request.POST.get('temperature', 0))
            from_unit = request.POST.get('from_unit', 'celsius')
            to_unit = request.POST.get('to_unit', 'fahrenheit')
            
            # Convert to celsius first (as a base)
            if from_unit == 'fahrenheit':
                temp_celsius = (input_temp - 32) * 5/9
            elif from_unit == 'kelvin':
                temp_celsius = input_temp - 273.15
            else:  # celsius
                temp_celsius = input_temp
            
            # Convert from celsius to target unit
            if to_unit == 'fahrenheit':
                result = (temp_celsius * 9/5) + 32
            elif to_unit == 'kelvin':
                result = temp_celsius + 273.15
            else:  # celsius
                result = temp_celsius
            
            context.update({
                'result': round(result, 2),
                'input_temp': input_temp,
                'from_unit': from_unit,
                'to_unit': to_unit
            })
        except (ValueError, TypeError):
            context['error'] = 'Please enter a valid number'
    
    return render(request, 'converter/index.html', context)