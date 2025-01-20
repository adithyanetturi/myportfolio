import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Portfolio",
    page_icon="🌟",
    layout="wide"
)

# Custom CSS for styling
def custom_css():
    st.markdown("""
        <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: #f9f9f9;
        }
        .section {
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .project {
            margin-bottom: 1rem;
            padding: 1rem;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 0.5rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        .contact-form button {
            background-color: #007bff;
            color: white;
            padding: 0.7rem 1.2rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

custom_css()

# Sidebar navigation

menu = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Education","Contact"])

# Home Section
if menu == "Home":
    st.title("Welcome to My Portfolio! 🎉")
    st.subheader("Hi, I'm Adithya Ram Netturi 👋")
    st.title("My Intro")
    st.write("Aspiring Machine Learning Engineer with a B.Tech in Computer Science, specializing in Artificial Intelligence and Machine Learning, from Malla Reddy University. Passionate about leveraging innovative AI and ML techniques to solve real-world problems. As a fresher, I aim to apply my strong foundation in data science, model development, and algorithm optimization to contribute to impactful projects and continuously enhance my skills in cutting-edge technologies.")
    st.image("313311429_1167554643833973_9097668581803739699_n.jpg",  use_container_width = True)

# Projects Section
elif menu == "Projects":
    st.header("Projects")
    st.write("Here are some of the projects I've worked on:")
    
    projects = [
        {"title": "MLOPS ON TITANIC DATASET", "description": "This is an amazing project where I built python using Dagshub", "link": "https://dagshub.com/adithyanetturi23/my-first-repo"},
        {"title": "Iris Classification Model with MLFlow ", "description": "This project demonstrates my skills in MLFlow", "link": "https://github.com/adithyanetturi/intro_to_mlops"},
        {"title": "Diabetes-Prediction", "description": "A cool project that showcases my Machine learning skills", "link": "https://github.com/adithyanetturi/Diabetes-Prediction"},
    ]
    
    for project in projects:
        st.markdown(f"### {project['title']}")
        st.write(project["description"])
        st.markdown(f"[Learn more]({project['link']})")

# Skills Section
elif menu == "Skills":
    st.header("Skills")
    st.write("These are the technologies and tools I'm proficient in:")
    
    skills = [
        "Python", "Streamlit", "Machine Learning", "SQL"
        "Deep Learning", "MLFlow","MLOps","Story Telling"
    ]
    
    for skill in skills:
        st.button(f"- {skill}")

# Education Section
elif menu == "Education":
    st.header("Education")
    st.write("Here's a brief overview of my academic background:")
    
    education = [
        {"Course": "B.Tech in Computer Science", "institute": "Malla Reddy University", "year": "2020-2024"},
        {"Course":"M.P.C","institute":"Narayana Junior collage","year":"2018-2020"},
        {"Course":"SSC","institute":"Brillant Grammer High School","year":"2018"}
    ]
    
    for edu in education:
        st.markdown(f"**{edu['Course']}** - {edu['institute']} ({edu['year']})")

# Work Experience Section


# Contact Section
elif menu == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out to me:")
    
    st.link_button("Linkdin",url="https://www.linkedin.com/in/adithya-netturi/")
    st.link_button("GMAIL",url="mailto:adithyanetturi23@gmail.com")
    st.link_button("GitHub",url="https://github.com/adithyanetturi")
    st.link_button("DagsHub",url="https://dagshub.com/adithyanetturi23")

# Footer
st.markdown("---")
st.markdown("© 2025 Adithya ram Netturi. Built with Streamlit.")
