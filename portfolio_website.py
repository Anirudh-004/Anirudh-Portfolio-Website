from email.mime import image
import json
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title=" Welcome to my Portfolio", page_icon=":simple_smile:", layout="wide")


def lottie_image(url):
    res=requests.get(url)
    if res.status_code !=200:
        return None
    else:
        return res.json()


Image_work=lottie_image('https://assets6.lottiefiles.com/packages/lf20_w51pcehl.json')
Image1=Image.open("C:/Users/aniru/Portfolio website/images/dataset-card.jpg")
Image2=Image.open("C:/Users/aniru/Portfolio website/images/image1-2.png")

def style_site(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


style_site('C:/Users/aniru/Portfolio website/style.css')


with st.container():
    st.subheader("Hi, I am Anirudh,:raised_hands:")
    st.title('Data Science and Data Analytics enthusiast :computer:')
    st.title('About Me')
    st.write("""
    College graduate with extensive knowledge in computer science, data science and currently
    pursuing Master’s in Web and Data Science in Germany and doing an Internship job. Passionate about
    communication and seeking to leverage my interpersonal skills to provide a friendly, and fun atmosphere
    at the organization I work. I love challenges and challenging situations, for that is when my learning curve
    is at its peak.
""")
st.write("[Learn More on my projects > ] (https://github.com/Anirudh-004)")
st.write("[Learn More on my Data Visualization dashboards using Tableau > ] (https://public.tableau.com/app/profile/anirudh.kudaragundi.anand.rao)")
st.write("[Check out my LinkedIn profile > ] (https://www.linkedin.com/in/anirudh-kudaragundi-anand-rao/)")

with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.title("My Interests")
        st.write("##")
        st.write(
            """
            I would like to let you know some of the key areas which have been my focus during my masters studies.
            
            * I have a good grasp of coding using python and have been part of solving many different tasks.
            * Data Science, Data Analytics, Databases, Big Data, Docker, Business Intelligence, Machine Learning & AI, Python programming
              are my key interests.
            * Analysis of data and discovering patterns is what I am passionate about.
            
            If my profile sounds interesting to you, I would be glad to have a discussion with you and if all the criteria matches perfectly, then I would be glad to work with you!

            """
        )

    with right_column:
        st_lottie(Image_work, height=300, key='Data Science')


with st.container():
    st.write("---")
    st.title('My Projects')
    st.write("##")
    image_column,text_column=st.columns((1,2))

    with image_column:
        st.image(Image1)
    with text_column:
        st.title("Flask-app-for-Bank-authentication-Note-using-Docker")
        st.subheader('Machine learning web application using FLASK API for bank authentication note and containerizing the application using docker')
        st.write(
            """
            In this project, the machine learning model predicts whether the bank note is authenticated or not. 
            The results of the model will be as follows: 
            If Authentication is true then 1 or if authentication is false the result is 0.')
            """)
        st.write("[Learn More on this project > ] (https://github.com/Anirudh-004/Flask-app-for-Bank-authentication-Note-using-Docker)")
    

    
with st.container():
    image_column,text_column=st.columns((1,2))

    with image_column:
        st.image(Image2)
    with text_column:
        st.title("Data pipeline application using Flask Web framework")
        st.subheader('Building a data pipeline using FLASK API for titanic dataset containerizing the application using docker')
        st.write(
            """
            In this project, an end-to-end data pipeline machine learning model is implemented that predicts whether the person has survived or not. 
            The results of the model will be as follows: 
            If a person has survived then the result is 1 or if a person has not survived then the result is 0'.
            Also, we infer from this project that building a data pipeline helps us to eliminate manual steps and helps us to carry out a smooth process
            during the flow of data from one stage to another in production environment.
            """)
        st.write("[Learn More on this project > ] (https://github.com/Anirudh-004/Data_Pipelines)")


with st.container():
    st.write("---")
    st.header("Get in Touch with Me!:smile:")
    st.write("##")

    contact_form="""
    <form action="https://formsubmit.co/anirudhka04@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Please type your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()




          
    
    


