import streamlit as st

# Define the Streamlit app
def app():
    st.title('SVM Regressor')
    # Session state to track form progress
    if "current_form" not in st.session_state:
        st.session_state["current_form"] = "form1"
    
    # Form 1 for login
    if st.session_state["current_form"] == "form1":
        form1 = st.form("intro")
        form1.header('SVM Regressor')
        form1.write('(c) 2024 Louie F. Cervantes')
        form1.write('Department of Computer Science')
        form1.write('College of ICT')
        form1.write('West Visayas state University')
        form1.text('Replace with the actual description')

        #insert the rest of the information here
        submit1 = form1.form_submit_button("Start")
    
        if submit1:
            # Go to the next form
            st.session_state["current_form"] = "form2"
    
    # Form 2 for classifier training
    if st.session_state["current_form"] == "form2":        
        form2 = st.form("training")
        form2.subheader('Classifier Training')        
        # insert the rest of the code to train the classifier here        

        submit2 = form2.form_submit_button("Submit")
    
        if submit2:
            st.session_state["current_form"] = "form3"

    # Form 3 for the price prediction using the trained model
        form3 = st.form("prediction")
        form3.subheader('Prediction')        

        submit3 = form3.form_submit_button("Submit")

        if submit3:
            st.text('replace with the result of the prediction model.')
            st.session_state["current_form"] = "form3"

            
if __name__ == "__main__":
    app()
