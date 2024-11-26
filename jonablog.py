import streamlit as st

# Set the title of the page
st.title("My Biography Blog :teddy bear:")

# Add a photo (Make sure to replace 'your_image.jpg' with your actual image file path)
st.image(SNOW_20241026_180458_236.jpg,caption='Have a Good Day', width=150)

# Introduction Section
st.header("Introduction")
st.write("""
Hi! I'm **Jonavell Ga**, a First Year student at Surigao del Norte State University, 
I love reading books and watching dramas.
""")

# Education Section
st.header("Educational Attainment")
st.write("""
Here are my educational attainment:
1. **Elementary** - Graduated as an Honor Student and recieve awards.
2. **High School** - Graduated also as a Honor Student and receive an award.
3. **Senior High School** - Also graduate as a honor student, and experience a training for NC3.
""")

# Contact Section
st.header("Contact Me")
st.write("""
Feel free to reach out for any questions, project collaboration, or just to connect!
""")

# Contact Form
with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button("Send Message")
    
    if submit_button:
        if not name or not email or not message:
            st.error("Please fill in all fields.")
        else:
            st.success(f"Thank you {name}! Your message has been sent successfully.")
            st.write(f"Subject: General Inquiry")
            st.write(f"Message: {message}")
            st.write(f"We’ll reach out to you at {email}.")
