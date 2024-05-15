from flask import Flask, request,render_template
from PIL import Image
from io import BytesIO
import base64
from imgText import WebPage
import os

app= Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["image"]
        uploaded_text = request.form["text"]
        webpage = WebPage(uploaded_file, uploaded_text)
        image =  webpage.Create_Image(filename = uploaded_text)
        # image_path = "/tmp/" + uploaded_text + ".jpg"
        # print(image_path)
                    # Create a BytesIO buffer to save image
        buffer = BytesIO()
        image.save(buffer, format="JPEG")
        buffer.seek(0)
        img_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return render_template("index.html", image=img_data)
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)