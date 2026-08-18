from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    result_hash = None
    is_match = None
    original_text =""
    target_hash =""

    if request.method == 'POST':
        # retrieve data from html form
        original_text = request.form.get('text_input', '')
        algorithm = request.form.get('algorithm', 'md5')
        target_hash = request.form.get('target_hash','')

        # Encoding string to bytes by hashlib
        encoded_text = original_text.encode('utf-8')

        # Generate hash based on selected algorithm
        if algorithm == 'md5':
            result_hash = hashlib.md5(encoded_text).hexdigest()
        elif algorithm == 'sha256':
            result_hash = hashlib.sha256(encoded_text).hexdigest()

        # check provided target hash
        if target_hash:
            is_match = (result_hash == target_hash)

    # pass variable to html page
    return render_template(
        'index.html',
        result_hash=result_hash,
        is_match = is_match,
        original_text=original_text,
        target_hash=target_hash
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)