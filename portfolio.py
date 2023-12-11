import streamlit as st

def main():
    st.title("My Professional Online Portfolio")
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About Me", "Resume", "Projects", "Contact"])

    if page == "Home":
        show_home()
    elif page == "About Me":
        show_about_me()
    elif page == "Resume":
        show_resume()
    elif page == "Projects":
        show_projects()
    elif page == "Contact":
        show_contact()

def show_home():
    st.header("Welcome to My Portfolio")
    st.write("This is the home page of my professional online portfolio. Feel free to explore!")

def show_about_me():
    st.header("About Me")
    st.write("I am a passionate individual with a background in [Your Field].")

def show_resume():
    st.header("Resume")
    st.write("### Education")
    st.write("- Degree in [Your Degree], [Your University], Year")
    st.write("### Experience")
    st.write("- Job Title, Company, Year")
    st.write("### Skills")
    st.write("- Skill 1, Skill 2, Skill 3")

def show_projects():
    st.header("Projects")
    st.write("#### Project 1")
    st.write("Description of Project 1.")
    st.write("#### Project 2")
    st.write("Description of Project 2.")

def show_contact():
    st.header("Contact")
    st.write("Feel free to contact me at [Your Email].")

if __name__ == "__main__":
    main()
