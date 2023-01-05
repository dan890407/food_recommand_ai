from flask import Flask, render_template, jsonify,request, redirect, url_for
import json
app = Flask(__name__)
with open("clussum_data2.json","r",encoding="UTF-8") as f:
    data=json.load(f)
with open("sent_data.json","r",encoding="UTF-8") as g:
    data_sent=json.load(g)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/",methods=['POST'])
def my_form_post(): 
    text = request.form['text'] 
    processed_text = text.upper()
    print(processed_text)
 
    for k,v in data_sent.items():
        if processed_text in k:
            pos=str(round(v["possitive"],2))
            neg=str(round(v["negative"],2))
            print(f"pos:{pos}")
            print(f"neg:{neg}")
    for key,value in data.items():
        if processed_text in key:
            if value["0"]!="廣告":
                review_1=value["0"]
            else:
                review_1="無評論"
            if value["1"]!="廣告":
                review_2=value["1"]
            else:
                review_2="無評論"
            if value["2"]!="廣告":
                review_3=value["2"]
            else:
                review_3="無評論"
            if value["3"]!="廣告":
                review_4=value["3"]
            else:
                review_4="無評論"
            if value["4"]!="廣告":
                review_5=value["4"]
            else:
                review_5="無評論"
            return render_template("index2.html",review_1=review_1,review_2=review_2,review_3=review_3,review_4=review_4,review_5=review_5,negative=neg,positive=pos)
    return render_template("index2.html",review="查無此店")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True,port=7777,host="0.0.0.0") 