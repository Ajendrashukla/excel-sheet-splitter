from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/split', methods=['POST'])
def split():
    file = request.files['file']
    output_folder = 'app/static/split_files'

    if file:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        file.save(os.path.join(output_folder, 'temp_file.xlsx'))

        xls = pd.ExcelFile(os.path.join(output_folder, 'temp_file.xlsx'))

        split_files = []

        for sheet_name in xls.sheet_names:
            df = pd.read_excel(os.path.join(output_folder, 'temp_file.xlsx'), sheet_name=sheet_name)
            current_time = datetime.datetime.now().strftime('%H-%M-%S')
            split_filename = f'{sheet_name}_{current_time}.xlsx'
            split_filepath = os.path.join(output_folder, split_filename)
            df.to_excel(split_filepath, index=False)
            split_files.append(split_filename)

        return render_template('index.html', split_files=split_files)

if __name__ == '__main__':
    app.run(debug=True)
