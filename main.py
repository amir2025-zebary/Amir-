from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # برای ارسال اطلاعات ثبت‌نام‌ها به قالب
    participants = []
    with open('registrations.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            participants.append(row)
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        # ذخیره کردن اطلاعات ثبت‌نام شده در فایل CSV
        with open('registrations.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email])
    
    return render_template('index.html', participants=participants)

if __name__ == '__main__':
    app.run(debug=True)
