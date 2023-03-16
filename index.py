from flask import Flask, render_template, request,  redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    text = "  "
    if request.method == 'POST':
        #version 1:
        opt1 = request.form.to_dict()
        for key in opt1:
            if key == "string":
                string = opt1[key]
        #version 2:
        string2 = request.form["string"]
        # if you need float : floatvar = float(float2)
        print(string2)        
        return render_template('index.html', text=string2)
    else:
        return render_template('index.html')
@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        #version 1:
        opt1 = request.form.to_dict()
        for key in opt1:
            if key == "string":
                string = opt1[key]
            if key == "float": 
                floata = opt1[key]
        print(string, floata)
        #version 2:
        string2 = request.form["string"]
        float2 = request.form["float"]
        # if you need float : floatvar = float(float2)
        print(float2)
        print(string2)
        # have a high speed
        myobj = gTTS(text=string2, lang=language, slow=False)
          
        # Saving the converted audio in a mp3 file named
        # welcome 
        myobj.save("welcome.wav")
        testvoice()
        return render_template('example.html')
    else:
        return render_template('example.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=8000)  