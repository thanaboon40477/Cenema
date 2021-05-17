from flask import Flask, render_template, jsonify, request, redirect, url_for, make_response
import requests

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def canemaget():
    if request.method == "GET":
        return render_template('home.html')

    elif request.method == "POST":
        url = "https://api.themoviedb.org/3/search/movie?api_key=ce387bb2a644ab271d330fbd4a77c8d0&query=a"

        response = requests.get(url, verify=False)
        box = response.json()
        lst = []
        links = "https://image.tmdb.org/t/p/w500"
        for i in box["results"]:
            image = links + i["poster_path"]
            
            group = {'original_language':i['original_language'], 'original_title':i['original_title'], 
                    'poster_path': image, 'title':i['title'], 'vote_average':i['vote_average']}
                    
            lst.append(group)
               
        data = {
            'ref':lst
        }
        print(data)
        return data



if __name__ == "__main__":
    app.run(debug=True, port=8080)