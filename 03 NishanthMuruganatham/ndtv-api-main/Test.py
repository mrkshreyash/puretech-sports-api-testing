import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sports-news')
def get_sports_news():
    try:
        api_url = 'https://sports.ndtv.com/api/homepagev3/3.0/get?l=sports'

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('data', {}).get('articles', [])

            sports_news = []
            for article in articles:
                title = article.get('title')
                link = article.get('url')
                sports_news.append({'title': title, 'link': link})

            return jsonify({'sports_news': sports_news})
        else:
            return jsonify({'error': 'Failed to fetch data from NDTV Sports'}), 500
    
    except requests.RequestException as e:
        return jsonify({'error': 'Error fetching data: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
