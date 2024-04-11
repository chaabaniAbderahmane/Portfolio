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
Highly motivated and detail-oriented Data Analyst with a strong foundation in data analysis, visualization, and reporting. Skilled in developing and implementing data collection systems, identifying business needs, and creating predictive models that improve forecasting accuracy. Proven ability to collaborate with cross-functional teams and deliver data-driven insights that drive revenue growth and operational efficiency..
"""
EMAIL = "chabani.email@gmail.com"
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_data = load_lottieurl("https://lottie.host/3d2fa690-c7ec-440e-af07-67f30b49bd40/FQNXHOM7O2.json")

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/abderahmane-chabani-964858201",
    "GitHub": "https://github.com/chaabaniAbderahmane?tab=repositories",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🌟 News Veracity Assessment with Logistic Regression": " https://github.com/chaabaniAbderahmane/News-Veracity-Assessment-with-Logistic-Regression",
    "🌟 Urgent Care Analytics Dashboard": "https://public.tableau.com/app/profile/abderrahmane.chabani/viz/EmergencyRoomDashbord/Dashboard1?publish=yes",
    "🌟 Exploratory Data Analysis and Correlation Study of the Movie Industry": "https://github.com/chaabaniAbderahmane/Exploratory-Data-Analysis-and-Correlation-of-the-Movie-Industry",
    "🌟 Predictive Modeling for Credit Card Fraud Detection": "https://github.com/chaabaniAbderahmane/Predictive-Modeling-for-Credit-Card-Fraud-Detection",
    "🌟 Music Player Web Application":"https://podcasts-ebon.vercel.app/",
    "🌟 Interactive Coffee Sales Dashboard with Streamlit Pandas and Plotly": "https://saledash.streamlit.app/",
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
- ✔️ Strong expertise in SQL and NoSQL databases (MySQL, PostgreSQL, MongoDB)

- ✔️ Advanced proficiency in Python for data analysis (Pandas, NumPy, Matplotlib)

- ✔️ Practical knowledge of BI tools (Tableau, Power BI) and ETL tools (Talend)


    ✔️  Significant experience in web application development, including: :
    
    - ►  Full development of a Music Player web application similar to Spotify using Vue.js, Pinia, Vitest, Vue Router, Composition API, and Firebase.
    
    - ► Design and implementation of a website dedicated to simplifying the process of creating and tracking connection requests for SONELGAZ services.
    
    - ► Development of a desktop application with Python and QtDesigner for the final year project at CDTA, offering a user-friendly interface for advanced data analysis.
    
- ✔️ Excellent communication skills and ability to work in a team
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
st.subheader(" Some Projects")
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
<form action="https://formsubmit.co/171219fda143246249ed20eb41a70099" method="POST">
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