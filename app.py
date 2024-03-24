from pathlib import Path
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
# profile_pic = current_dir / "assets" / "montain.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio"
PAGE_ICON = ":wave:"
NAME = "Abderahmane Chabani"
DESCRIPTION = """
Junior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "chabani.email@gmail.com"
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_data = load_lottieurl("https://lottie.host/0726336c-438d-4781-b7cd-f52d2c9b0229/3SnozGumTX.json")

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/abderahmane-chabani-964858201",
    "GitHub": "https://github.com/chaabaniAbderahmane?tab=repositories",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🌟 North Africa COVID-19 Data Analysis & Visualization": "https://github.com/chaabaniAbderahmane/North-Africa-COVID-19-Data-Analysis-Visualization",
    "🌟 Exploratory Data Analysis and Correlation Study of the Movie Industry Dataset": "https://github.com/chaabaniAbderahmane/Exploratory-Data-Analysis-and-Correlation-Study-of-the-Movie-Industry-Dataset",
    "🌟 Music Player Web Application": "https://podcasts-ebon.vercel.app/",
    "🌟 Interactive Coffee Sales Dashboard with Streamlit Pandas and Plotly": "https://sales-dashboards.streamlit.app/",
    "🌟 Data Cleaning and Transformation for the Nashvill Real Estate Dataset": "https://github.com/chaabaniAbderahmane/Data-Cleaning-and-Transformation-for-the-Nashvill-Real-Estate-Dataset",
    "🌟 Sales Data Analysis and Reporting with SQLite, Pandas, and Plotly Creating a PDF report": "https://github.com/chaabaniAbderahmane/Sales-Data-Analysis-and-Reporting-with-SQLite-Pandas-and-Plotly-Creating-a-PDF-report-",
    "🌟 Data Cleaning and Preparation for London Bike Rental Analysis and Visualization": "https://github.com/chaabaniAbderahmane/-Data-Cleaning-and-Preparation-for-London-Bike-Rental-Analysis-and-Visualization?tab=readme-ov-file",
}





# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()




# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    if lottie_data:
                st_lottie(lottie_data, width=0, height=400, key="lottie_data")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)



# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
"""
- ✔️ Expertise solide en bases de données SQL et NoSQL (MySQL, PostgreSQL, MongoDB)

- ✔️ Maîtrise avancée de Python pour l'analyse de données (Pandas, NumPy, Matplotlib)

- ✔️ Connaissance pratique des outils de BI (Tableau, Power BI) et des ETL (Talend)


    ✔️ Expérience significative dans le développement d'applications web, notamment :
    
    - ► Développement complet d'une application Web de Lecteur Musical similaire à Spotify en utilisant Vue.js, Pinia, Vitest, Vue Router, Composition API et Firebase.
    
    - ► Conception et mise en œuvre d'un site web dédié à simplifier le processus de création et de suivi des demandes de raccordement pour les services de SONELGAZ.
    
    - ► Développement d'une application desktop avec Python et QtDesigner pour le projet de fin d'études à la CDTA, offrant une interface conviviale pour l'analyse de données avancée.
    
- ✔️ Excellentes compétences en communication et aptitude à travailler en équipe
"""
)



# --- SKILLS ---
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python ,Java,C, Php ,javascript, SQL,
- 📊 Data Visulization: Tableau, MS Excel,Streamlit, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

st.write('\n')
# --- JOB 1
st.write("💼", "**Freelance Data Analyst & Developer**")
st.write("09/2022 - Present")


# --- JOB 2
st.write('\n')
st.write("💼", "**Data Scientist | CDTA - Algiers, Algeria**")
st.write("02/2022 - 09/2022")
st.write(
    """
- ► Designed a generic architecture based on domain ontology for task planning between robots and humans.
- ► Constructed a knowledge base to optimize interaction between human operators and robots.
- ► Facilitated collaboration processes through innovative architecture, enhancing operational efficiency.
"""
)

# --- JOB 3
st.write('\n')
st.write("💼", "**Developer | ELIT.Sonalgaz - Algiers, Algeria**")
st.write("03/2019 - 09/2019")
st.write(
    """
- ► Designed and implemented a website dedicated to simplifying the process of creating and tracking connection requests for SONELGAZ services.
- ► Implemented procedure automation, improving operational efficiency and providing users with complete traceability of requests.
"""
)



# --- Some Projects  ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


## ---Contact form ---

st.write("---")
st.write('\n')
st.write('\n')
st.subheader(":mailbox: Get In Touch With Me!")
st.write("---")

contact_form = """
<form action="https://formsubmit.co/chabani.email@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
