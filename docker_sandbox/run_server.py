from flask import Flask, request, jsonify, json
from os import remove
from virus_scanner import FilesScan

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def upload_and_scan_file():
    uploaded_file = request.files.get('file')
    matches = json.loads(request.form.get('matches', '{}'))
    if not uploaded_file:
        return jsonify({'error': 'No file uploaded'}), 400

    uploaded_file.save('/app/' + uploaded_file.filename)

    docker_program_path = '/app/' + uploaded_file.filename

    scanned_file = FilesScan(file_path=docker_program_path)

    if matches:
        response = scanned_file.check_signature_file_hash(matches)
    else:
        response = scanned_file.check_signature_file_yara()

    remove(docker_program_path)

    if response:
        return response

    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)