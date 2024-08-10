import streamlit as st
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
            border-bottom: 5px solid white;
        }
        .navbar-text {
            font-size: 2rem;
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
        <ul class="items">
            <li>About</li>
            <li>Contact</li>
        </ul>
    </nav>
''', unsafe_allow_html=True)




















# Create the sidebar
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'About', 'Contact'],
#         icons=['house'], menu_icon="cast", default_index=0)
#     st.sidebar.text("")  # Just to force a redraw

# Main content based on selected option
# if selected == "Home":
#     st.markdown('Home')
# elif selected == "About":
#     st.title("About page")
# else:
#     st.title("Contact")
    