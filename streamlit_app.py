import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
# Title of the CV
st.title("John Doe's CV")

# Contact Information
st.subheader("Contact Information")
st.write("""
- **Email:** john.doe@example.com
- **Phone:** +123 456 7890
- **LinkedIn:** [linkedin.com/in/johndoe](https://www.linkedin.com/in/johndoe)
- **GitHub:** [github.com/johndoe](https://github.com/johndoe)
""")

# Summary
st.subheader("Summary")
st.write("""
I am a highly motivated software developer with a passion for creating innovative solutions and a strong background in Python, data analysis, and machine learning.
""")

# Experience
st.subheader("Experience")
st.write("""
**Software Developer at XYZ Corp**
*January 2020 - Present*
- Developed and maintained web applications using Python and Django.
- Implemented machine learning models to improve product recommendations.
- Collaborated with cross-functional teams to design and implement new features.

**Junior Developer at ABC Inc**
*June 2018 - December 2019*
- Assisted in the development of internal tools using Python and Flask.
- Wrote unit tests to ensure code quality and reliability.
- Participated in code reviews and provided constructive feedback.
""")

# Education
st.subheader("Education")
st.write("""
**Master of Science in Computer Science**
*University of Technology, 2018*
- Graduated with Honors
- Relevant coursework: Machine Learning, Data Mining, Software Engineering

**Bachelor of Science in Information Technology**
*Institute of Technology, 2016*
- Relevant coursework: Algorithms, Databases, Web Development
""")

# Skills
st.subheader("Skills")
st.write("""
- Programming Languages: Python, JavaScript, SQL
- Web Development: Django, Flask, React
- Data Analysis: Pandas, NumPy, Scikit-learn
- Tools: Git, Docker, Jenkins
""")

# Projects
st.subheader("Projects")
st.write("""
**Project Name**
- Description of the project and technologies used.

**Another Project**
- Description of the project and technologies used.
""")

# Certifications
st.subheader("Certifications")
st.write("""
- **Certified Python Developer**, Python Institute, 2019
- **Machine Learning Specialization**, Coursera, 2020
""")

# Interests
st.subheader("Interests")
st.write("""
- Machine Learning
- Open Source Contribution
- Hiking and Outdoor Activities
""")
