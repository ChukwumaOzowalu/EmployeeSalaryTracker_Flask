from flask import Flask, render_template, request
import employeeObject

app = Flask(__name__)

@app.route('/')
def index():
    # Assume num_employees is calculated or retrieved from somewhere
    num_employees = 5  # Example value

    return render_template('index.html', num_employees=num_employees)

@app.route('/process_form', methods=['POST'])
def process_form():
    try:
        num_employees = int(request.form['num_employees'])
    except ValueError:
        return 'Invalid value for number of employees'

    if num_employees <= 0:
        return 'Number of employees must be greater than zero'

    employees = []

    for i in range(num_employees):
        name = request.form.get(f'name{i}', '')
        id_number = request.form.get(f'id_number{i}', '')
        department = request.form.get(f'department{i}', '')
        job_title = request.form.get(f'job_title{i}', '')
        salary = request.form.get(f'salary{i}', '')
        salary_change = request.form.get(f'salary_change{i}', '')

        # Process the employee data here
        employee_data = {
            'name': name,
            'id_number': id_number,
            'department': department,
            'job_title': job_title,
            'salary': salary,
            'salary_change': salary_change
        }
        employees.append(employee_data)

    # Process the employees list
    # For example, I can save the data to a database or perform other operations

    return 'Form submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)