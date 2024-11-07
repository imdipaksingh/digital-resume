from pathlib import Path
import streamlit as st
from PIL import Image


# -----Path Setting----
current_dir = Path(__file__).parent if "__file__"in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assests" / "CV.pdf"
profile_pic = current_dir / "assests" / "pic.jpg"   









# --Genral Setting--------
PAGE_TITLE = "Digital CV | Deepak Singh"
PAGE_ICON = ":wave:"
NAME = "DEEPAK SINGH"
DESCRIPTION = """
PLSQL and SQL DEveloper and DATA Analyst
"""
email = "singhdeepak2904@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "www.linkedin.com/in/deepak-singh-70ba09193",
    "LeetCode" : "https://leetcode.com/u/imdipaksingh/"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#st.title("Hello There!!")


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte =  pdf_file.read()
profile_pic = Image.open(profile_pic)


# --hero section --
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 download resume",
        data = PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", email)




# Social Link

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# Experiance And Qalification

st.write("#")
st.subheader("PROFILE")
st.write("""
         Senior Data Analyst with over 6 years of experience in SQL, reporting automation, and dashboard development. Adept at creating complex data queries and transforming data from operational sources to analytical databases. Strong in logical and analytical concepts, with expertise in Excel and experience with BI tools such as Power BI and Tableau. Highly detail-oriented, capable of multitasking, and experienced in automating repetitive tasks to streamline operations.
         """)

# Skills

st.write("#")
st.subheader("Skills")
st.write("""
- PLSQL
- SQL
- Unix
- Shell Scripting
- Python
- Power BI
- Postman
- Tableau
- Cherwell
- Control M
- Microsoft Excel
""")

# -- work history--
st.write("#")
st.subheader("Work History")
st.write("---")

#--job1
st.write("🏢", "**Technology Analyst | Infosys, Bengaluru**")
st.write("November 2022 - Present")
st.write("Project - Utility")
st.write("""
- 👉 Gather and interpret user requirements to design and develop new reports and enhance existing ones.
- 👉 Build complex SQL queries for data transformation and migration between operational sources and analytical databases.
- 👉 Perform regular testing of reports and deliverables, ensuring data accuracy and consistency.
- 👉 Work closely with stakeholders to automate repetitive tasks, improving overall team efficiency.
- 👉 Optimize database performance through query tuning and indexing strategies.
""")

#--job1
st.write("🏢", "**IT Analyst | TCS, Mumbai**")
st.write("December 2017 - October 2022")
st.write("Project - Banking")
st.write("""
- 👉 Wrote PL/SQL programs for data retrieval, automation of daily reports, and handling exceptions.
- 👉 Developed UNIX shell scripts to automate daily manual tasks and maintain system operations.
- 👉 Created database triggers, packages, functions, and stored procedures to support data conversion.
- 👉 Conducted performance tuning and optimization of SQL queries for enhanced system performance.
- 👉 Develop and automate dashboards for daily, weekly, and monthly reporting needs.
- 👉 Automated and analysed daily transaction decline reports, identifying key issues and proposing solutions to stakeholders, which led to a reduction in declined transactions from 26% to less than 1%.
""")


# certification
st.write("#")
st.subheader("CERTIFICATION")
st.write("🎓 Google Data Analytics Professional Certificate")

# certification
st.write("#")
st.subheader("🎓 EDUCATION ")
st.write("""
- Bachelors Of Engineering
- Gujarat Technological University
- 2013 - 2017
 """)

# Languages
st.write("#")
st.subheader("LANGUAGES")
st.write("""
- English
- Hindi
- Gujarati
""")

# HObies
st.write("#")
st.subheader("HOBBIES")
st.write("""
- Reading
- Sports
- Travel
""")