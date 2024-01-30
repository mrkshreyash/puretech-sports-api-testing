import requests
import streamlit as st
def fetch_sports_news():
    # Replace 'http://127.0.0.1:5000/news?category=sports' with your server's URL
    url = 'http://127.0.0.1:5000/news?category=sports'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            news_data = response.json()

            # Check if the response contains sports news data
            if news_data.get('success') and news_data.get('category') == 'sports':
                sports_news = news_data.get('data')
                for news_item in sports_news:
                    st.title(f"Title: {news_item['title']}")
                    st.write(f"Author: {news_item['author']}")
                    st.write(f"Content: {news_item['content']}")
                    st.write(f"Date: {news_item['date']}")
                    st.write(f"Read more: {news_item['readMoreUrl']}")
                    st.image(news_item['imageUrl'])
                    # st.write(news_item['readMoreUrl'])
                    st.write()
                    st.write("-------------------------------")

            else:
                print("No sports news available.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    st.set_page_config(
        page_title="New Data",
        layout='wide'
    )

    fetch_sports_news()
