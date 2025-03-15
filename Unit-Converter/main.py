import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="💡" , layout="centered")

#custom CSS
st.markdown(
    """
    <style>
        .stButton>button{
        background-color: #f55c7a;
        color: white;
        }
        .stButton>button:hover {
        background-color: #e74c3c;  
        color: white;
        }
        .stSelectbox>select {
            background-color: #957dad;
            color: white;
            border: 1px solid #6c5b7b;
            padding: 8px;
            border-radius: 5px;
        }
        
        .stApp {
            background-color: #fdf6e3;
            color: #2c3e50;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.title("🔁 Unit Converter ")
st.markdown("### Instant Conversions for Length, Weight, and Time.")
st.write("👋 Welcome! Choose your unit, enter the value, and see the conversion instantly!")

selected_Category = st.selectbox("Select Conversion Type:", ["Length", "Weight", "Time"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)

col1,col2 =st.columns(2)

if selected_Category == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Miles","Kilometers","Meters","Inches","Centimeters","Millimeters"])
    with col2:
        to_unit = st.selectbox("To", ["Miles","Kilometers","Meters","Inches","Centimeters","Millimeters"])
elif selected_Category == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms","Grams","Milligrams","Pounds"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms","Grams","Milligrams","Pounds"])
elif selected_Category == "Time":
    with col1:
        from_unit = st.selectbox("From", ["Hours","Minutes","Seconds","Milliseconds"])
    with col2:
        to_unit = st.selectbox("To", ["Hours","Minutes","Seconds","Milliseconds"])

#Conversion Functions
def length_converter(value,from_unit,to_unit):
    length_units = {
    "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
    "Miles": 0.000621371, "Feet": "3.28", "Inches": 39.37  
    }
    return(value/length_units[from_unit]) * length_units[to_unit] 
def Weight_converter(value,from_unit,to_unit):
    weight_units = {
    "Kilograms": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.2046
    }
    return(value/weight_units[from_unit]) * weight_units[to_unit] 
def Time_converter(value,from_unit,to_unit):
    Time_units = {
    "Hours": 1, "Minutes": 60, "Seconds": 3600, "Milliseconds": 3600000
    }
    return(value/Time_units[from_unit]) * Time_units[to_unit]


if st.button("Convert"):
    if selected_Category == "Length":
        result = length_converter(value,from_unit,to_unit)
    elif selected_Category == "Weight":
        result = Weight_converter(value,from_unit,to_unit)
    elif selected_Category == "Time":
        result = Time_converter(value,from_unit,to_unit)

st.success(f"Your result {value} {from_unit}   =   {result:.4f} {to_unit}")
