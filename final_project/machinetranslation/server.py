from translator import englishToFrench , frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('templates/index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
