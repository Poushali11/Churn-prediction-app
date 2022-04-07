# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)



# defining the function which will make the prediction using the data which the user inputs
def prediction(Age,Gender,Income, Balance,Vintage,Transaction_Status,Product_Holdings,Credit_Card,Credit_Category):
    # Pre-processing user input
    if Gender == "Female":
        Gender = 0
    else:
        Gender = 1

    if Income == "10L-15L":
        Income = 0
    elif Income== "5L-10L":
        Income=1
    elif Income=="Less than 5L":
        Income==2
    else:
        Income=3


    if Credit_Category == "Average":
        Credit_Category = 0
    elif Credit_Category =="Good":
        Credit_Category= 1
    else:
        Credit_Category=2

    if Product_Holdings=='3+':
        Product_Holdings= 3

    #Scale data
    scaler = StandardScaler()
    df=scaler.fit_transform([[Age,Gender,Income, Balance,Vintage,Transaction_Status,Product_Holdings,Credit_Card,Credit_Category]])


    # Making predictions
    prediction = classifier.predict(
        [[Age,Gender,Income, Balance,Vintage,Transaction_Status,Product_Holdings,Credit_Card,Credit_Category]])

    if prediction == 0:
        pred = 'will not churn'
    else:
        pred = 'will churn'
    return pred


def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Churn Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    Age = st.number_input('Enter age of the customer')
    Gender = st.selectbox('Select Gender of the customer', ("Male", "Female"))
    Income = st.selectbox('Select Income Range of the customer', ("10L-15L", "5L-10L","Less than 5L","More than 15L"))
    Balance = st.number_input("Customer's balance in bank account")
    Vintage = st.number_input("Number of years customer is associated with the bank")
    Transaction_Status = st.selectbox('Any transaction done or not , yes mean 1, no mean 0', ("1", "0"))
    Product_Holdings = st.selectbox("No. of Product Holdings of the customer",("1","2","3+"))
    Credit_Card = st.selectbox("Does the customer have credit card? If yes,then 1 else 0",("1","0"))
    Credit_Category = st.selectbox("Select the customer credit status",("Average","Good","Poor"))
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(Age,Gender,Income, Balance,Vintage,Transaction_Status,Product_Holdings,Credit_Card,Credit_Category)
        st.success('The customer {}'.format(result))


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
