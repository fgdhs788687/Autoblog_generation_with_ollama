from ollama import chat, ChatResponse
# import os 
import requests
from bs4 import BeautifulSoup

def scrape(url):
    page = requests.get(url).text 

    soup = BeautifulSoup(page, 'html.parser') # 
    paragraph = soup.find_all('p') # It will collect all the text inside the <p> tags and store it in a list.
    page_text = '' # This is an empty string that will be used to store the text of the page.
    for line in paragraph: # Now we will loop through the list of paragraphs and add the text of each paragraph to the page_text string.
        page_text += line.text # This .text will extract all the text from the paragraph and add it to the page_text string leaving out the html tags.
    
    return page_text    

# This function will take a query as i/p and give us a response from the AI. We will use this function to generate the blog post and the title.
def post(query):
    response: ChatResponse = chat(model='gemma3:1b', messages=[
        {
            'role': 'user',
            'content': query,
        },
    ])
    return response.message.content

# This function will take the text of the page as i/p and give us a title for the blog post.
def title(post):
    query = f"""
    Generate ONLY ONE short blog title.
    Do not give options.
    Do not give explanations.
    Do not ask questions.
    Return only the title text.

    Text:
    {post}
    """
    response: ChatResponse = chat(
        model='gemma3:1b',
        messages=[{'role': 'user', 'content': query}]
    )
    return response.message.content.strip()



# Cretes a blog post for the given url and saves it in an html file. It will keep asking for urls until the user types exit(). 
# Each time a new blog post will be added to the html file. 
while True:
    url = input('url:')
    if url.lower() == 'exit()':
        with open('autoblog.html', 'w', encoding='utf-8') as file:
            file.write("")
        quit()

    text = scrape(url)
    query = f'''
                 Write a 200 word blog post about this text: {text}
             '''
    response_post = post(query)
    response_title = title(text)

    print(f'{response_title}')
    print(f'{response_post}')
    print('**************************')
    with open('autoblog.html', 'a', encoding='utf-8') as file:
        file.write(f'''
        <article>
            <h1>{response_title}</h1>
            <p>{response_post}</p>
            <hr>
        </article>
        ''')
