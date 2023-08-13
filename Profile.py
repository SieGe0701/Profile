import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
lottie_aniamation = "https://lottie.host/3cf84871-6625-430b-bbe4-6a240f856162/zA5xYIlEfu.json"

st.set_page_config(page_title="My profile", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)


local_css("style/style.css")

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Skills and Projects"],
        icons=["house", "book"],
        default_index=0,
        orientation="",
        styles={
            "container": {"padding": "0!important"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#00008b",
            }
        }
    )
if selected == "Home":
    with st.container():
        st.subheader("Hi, I am R Srinivas Prabu :wave:")
        st.title("Data Science and Engineering, MIT Manipal")
        st.write(
            "I am passionate about ML and DL implementations in medical and buisness fields")
        st.write(
            "[Linked In >](https://www.linkedin.com/in/srinivas-prabhu-3b090b279/)")

    with st.container():
        st.write("---")
        col1, col2 = st.columns(2)
        with col1:
            st.header("What I do?")
            st.write("##")
            st.write(
                """
            Hello , to those of you visiting my site I'm a DSE undergrad currently persuing B.Tech
            in MIT Manipal,I am very much interested in ML and DL applications in the medical as well as buisness field
            I'm proficient in ML and am currently learning DL and NLP.
            Provided below is my github account if you want to check my projects, it has both finished and unfinished projects.
            """
            )
            st.write("[Github link >](https://github.com/SieGe0701)")

        with col2:
            st_lottie(lottie_aniamation, height=200, key="coding")

    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image, text = st.columns((1, 2))
        with image:
            st.image(
                "https://t4.ftcdn.net/jpg/00/42/28/37/360_F_42283748_EiXhF88tPQVwPHgGzjjF8WPmsCtDLzLQ.jpg")
        with text:
            st.subheader("Hit and Run classification")
            st.write("""
            This is a Project that uses a realtime Traffic crashes dataset from 
            Chicago data portal, to classify wether the crash was Hit and Run or Not.
            Ensemble models used for the prediction were:
                     -RandomForestClassifier
                     -XGboost
                     -Votingclassifier
                     -Adaboost Classifier
                     -LightGradientBoostingMachine Classifier
            """)

    with st.container():
        img, txt = st.columns((1, 2))
        with img:
            st.image(
                "https://img.freepik.com/free-vector/illustration-fake-news-concept_53876-40823.jpg?size=626&ext=jpg")
        with txt:
            st.subheader("Fake news Detection")
            st.write("""
            This is a Project that detects wether the news is True or Fake,
            Models used:
                     -LogisticRegression
                     -DecisionTree
                     -RandomForestClassifer
                     -XGBoostClassifier
            The model was deployed using streamlit library.
            """)

    with st.container():
        st.write("---")
        st.header("Get in touch with me!")
        st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/sprabhur81@gmail.com" method="POST">
     <input type="hidden" name="_captcha value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name= "meessage" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>    
    """
    left, right = st.columns(2)
    with left:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right:
        st.empty()

if selected == "Skills and Projects":
    with st.container():
        html_template = """
        <u><h2>Skills</h2></u>
        <ul>
        <li style="font-size:20px">
            <b style="font-size: 20px">Languges:</b> C/C++, Java, Python, SQL 
        </li>
        <li style="font-size:20px">
            <b style="font-size: 20px">Libraries:</b> Pandas(4/5),ScikitLearn(4/5),TensorFlow(3/5),Stable-Baseline3(3/5)
        </li>
        <li style="font-size:20px">
            <b style="font-size: 20px">Databases:</b> OracleDB 
        </li>
        <li style="font-size:20px">
            <b style="font-size: 20px">Relevant course work:</b> Data Structure, Design and Analysis of Algorithms , Machine Learning, Deep Learning etc
        </li>
        <li style="font-size:20px">
            <b style="font-size: 20px">Area of Interests:</b> Machine Learning, Deep Learning, AI, Data Analysis  
        </li>
        <li style="font-size:20px">
            <b style="font-size: 20px">Soft Skills:</b> Self Learning, Time sense, Productivity, Communication skills, Adaptablity 
        </li>

        </ul>
        """
        st.markdown(html_template,unsafe_allow_html=True)

    with st.container():
        with st.container():
            st.write("---")
            st.header("My Projects")
            st.write("##")
            image, text = st.columns((1, 2))
            with image:
                st.image(
                "https://t4.ftcdn.net/jpg/00/42/28/37/360_F_42283748_EiXhF88tPQVwPHgGzjjF8WPmsCtDLzLQ.jpg")
            with text:
                st.subheader("Hit and Run classification")
                st.write("""
            This is a Project that uses a realtime Traffic crashes dataset from 
            Chicago data portal, to classify wether the crash was Hit and Run or Not.
            Ensemble models used for the prediction were:
                     -RandomForestClassifier
                     -XGboost
                     -Votingclassifier
                     -Adaboost Classifier
                     -LightGradientBoostingMachine Classifier
            """)
                st.write("[Github link >](https://github.com/SieGe0701/Hit-and-Run-Classification)")

        with st.container():
            img, txt = st.columns((1, 2))
            with img:
                st.image(
                    "https://img.freepik.com/free-vector/illustration-fake-news-concept_53876-40823.jpg?size=626&ext=jpg")
            with txt:
                st.subheader("Fake news Detection")
                st.write("""
                This is a Project that detects wether the news is True or Fake,
                Models used:
                     -LogisticRegression
                     -DecisionTree
                     -RandomForestClassifer
                     -XGBoostClassifier
                The model was deployed using streamlit library.
                """)
                st.write("[Github link >](https://github.com/SieGe0701/Fake-news-Prediction)")