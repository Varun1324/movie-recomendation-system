import time
import streamlit as st
from streamlit_option_menu import option_menu
from model import recommend_movie
#from streamlit_option_menu import option_menu

st.set_page_config(page_title="Movie Recomendation System",layout="wide")

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

hide_streamlit_style = """
    <style>
    /* Hide the menu, settings, and 'Made with Streamlit' watermark */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Add space at the top of the page */
    .block-container {
        margin:0;
        padding-top: 0px;
    }
    .stApp {
        background-color: black;
    }
    </style>
    """

# Apply the custom CSS
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown('''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,600;1,600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Gupter:wght@500&display=swap');
        .navbar {
            width:100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: black;
            border-radius: 5px;
            color:white;
            border-bottom: 1px solid white;
        }
        .navbar-text {
            font-size: 2.3rem;
            font-family:Montserrat;
        }
        .items{
            list-style:none;
            display:flex;    
            font-family:Gupter;
        }
        .items li{
            margin-top:15px;
            font-size: 1.2rem;    
        }
    </style>

    <nav class="navbar">
        <span class="navbar-text">
            CineCue.
        </span>
    </nav>
''', unsafe_allow_html=True)

with st.form(key='input_form'):
    cell1,cell2=st.columns(2,vertical_alignment="bottom")
    cell1.markdown("""<h5>Preferred Year</h5>""",unsafe_allow_html=True)
    year=cell2.number_input("",value=None,max_value=2025)
    cell3,cell4=st.columns(2,vertical_alignment="bottom")
    cell3.markdown("""<h5>Preferred Runtime (in minutes)</h5>""",unsafe_allow_html=True)
    runtime=cell4.number_input("",value=None)
    cell5,cell6=st.columns(2,vertical_alignment="bottom")
    cell5.markdown("""<h5>Select Genre(s)</h5>""",unsafe_allow_html=True)
    available_genres = ['Comedy', 'Drama', 'Family', 'Action', 'Thriller', 'Romance']
    selected_genres = cell6.multiselect("", options=available_genres)
    submit_button = st.form_submit_button(label='SUBMIT')
if submit_button:
    with st.spinner('Wait for it...'):
        time.sleep(5)
    if selected_genres:
        user_input = {
            'year': year,
            'runtime': runtime,
            'genre': selected_genres
        }
        result_set = recommend_movie(user_input)
        st.header("Recommended Movies")
        st.table(result_set)
    else:
        st.write("Please select at least one genre.")

# Create the sidebar
with st.sidebar:
    selected = option_menu("Menu", ["Home", 'About', 'Vision','How it Works'],
        icons=['house','info-circle','file-text','gear'], menu_icon="list", default_index=0)
    st.sidebar.text("")  # Just to force a redraw

# Main content based on selected option
 
if selected == "About":
    with st.container():
        st.header("ABOUT US")
        st.write("Welcome to CineCue, your personalized guide to discovering the best movies tailored just for you. Our mission is simple: to help you find the perfect movie to watch based on your unique preferences.")
elif selected == "Vision":
    with st.container():
        st.header("OUR VISION")
        st.write("We believe that the world of cinema is vast and rich, and there's a perfect movie for everyone. Our goal is to make it easier for you to navigate through thousands of options and find the one that matches your taste. By analyzing your preferred genres, favorite runtimes, and release years, we provide suggestions that feel like they were handpicked just for you.")
elif selected == "How it Works":
    with st.container():
        st.header("How it Works")
        st.write("At the heart of  CineCue is a robust recommendation engine powered by TensorFlow, one of the leading frameworks in machine learning. Our algorithm takes into account various factors such as genre, runtime, and release year to predict movies that you're likely to enjoy. By continually refining our model and incorporating user feedback, we strive to achieve an accuracy of over 90% in our predictions.")
        st.markdown("""
        <div style="display: flex; align-items: center;">
           <li>
            Personalized Recommendations:  We tailor our suggestions to your preferences, ensuring that every recommendation is relevant.
            </li>
            <li>
            User-Friendly Interface: Our platform is designed to be intuitive and easy to navigate, making it simple for you to find the perfect movie.
            </li>
            <li>
            Constantly Evolving: We are always working to improve our algorithm and expand our database to offer you the best possible experience.
            </li>
        </div>
        """, unsafe_allow_html=True)
    