from process import *

from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads/'
app.config['PROCESSED_FOLDER'] = './static/processed/'

# Ensure the directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            if request.files:
                image = request.files['image']
                img_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(img_path)

                # Simpan Gambar Hasil
                # Setting nama file
                grayscale_img_filename = f"grayscale_{image.filename}" 
                gaussian_img_filename = f"gaussian_{image.filename}" 
                highboost_img_filename = f"highboost_{image.filename}" 
                median_img_filename = f"median_{image.filename}" 
                
                # Setting path
                grayscale_img_path = os.path.join(app.config['PROCESSED_FOLDER'], grayscale_img_filename) 
                gaussian_img_path = os.path.join(app.config['PROCESSED_FOLDER'], gaussian_img_filename) 
                highboost_img_path = os.path.join(app.config['PROCESSED_FOLDER'], highboost_img_filename) 
                median_img_path = os.path.join(app.config['PROCESSED_FOLDER'], median_img_filename) 
                # Ambil gambar yang mau diproses
                processed_image = import_image(img_path)
                
                # Proses gambar
                img_1 = prep_image_1(processed_image, save_path = grayscale_img_path)
                img_2 = prep_image_2(img_1, save_path = gaussian_img_path)
                img_3 = prep_image_3(img_2, save_path = highboost_img_path)
                img_4 = prep_image_4(img_3, save_path = median_img_path)

                return render_template('index.html', 
                                       uploaded_image = image.filename, 
                                       processed_image_1 = grayscale_img_filename,
                                       processed_image_2 = gaussian_img_filename,
                                       processed_image_3 = highboost_img_filename,
                                       processed_image_4 = median_img_filename)
    except Exception as e:
        print("An error occurred:", str(e))
        # Print the full traceback
        import traceback
        traceback.print_exc()

    return render_template('index.html')

@app.route('/display/<filename>')
def send_uploaded_image(filename=''):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/display_processed/<filename>')
def send_processed_image(filename=''):
        return send_from_directory(app.config['PROCESSED_FOLDER'], filename)
if __name__ == '__main__':
    app.run(debug=True)