# IMPORT LIBRARIES --------------------------------------------------------

import pandas as pd
import streamlit as st

# -------------------------------------------------------------------------


# PAGE MAIN TITLE ---------------------------------------------------------

st.write("# Probability of Bad Classification")
st.write("Academic Performance = 'F'")
st.write("")
st.write("")

# -------------------------------------------------------------------------


# SIDEBAR (start) ---------------------------------------------------------

st.sidebar.header('User Input Parameters')

def user_input_features():
    
    id_number = st.sidebar.text_input('ID number (insert and press enter)',"")

    gender = st.sidebar.radio('Gender',('male','female'))

    parental_support = st.sidebar.selectbox('Parental Support' ,('0: None','1: Low','2: Moderate','3: High','4: Very High'))

    weekly_study_time = st.sidebar.slider('Weekly Study Time (hours)',0,20,10)

    # creating risk groups (start) -----------------------------------------------------------------
    
    if (gender =='male' ) & ( parental_support=='0: None' ) & ( weekly_study_time<8):
        prediction = 0.70
        risk_group = '5: Very High Risk'
    elif (gender =='male' ) & ( parental_support=='0: None' ) & ( weekly_study_time<12):
        prediction = 0.70
        risk_group = '5: Very High Risk'
    elif (gender =='male' ) & ( parental_support=='0: None' ) & ( weekly_study_time<17):
        prediction = 0.50
        risk_group = '3: Moderate Risk'
    elif (gender =='male' ) & ( parental_support=='0: None' ) & ( weekly_study_time<19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='0: None' ) & ( weekly_study_time>=19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='1: Low' ) & ( weekly_study_time<8):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='male' ) & ( parental_support=='1: Low' ) & ( weekly_study_time<12):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='male' ) & ( parental_support=='1: Low' ) & ( weekly_study_time<17):
        prediction = 0.50
        risk_group = '3: Moderate Risk'
    elif (gender =='male' ) & ( parental_support=='1: Low' ) & ( weekly_study_time<19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='1: Low' ) & ( weekly_study_time>=19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time<8):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='male' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time<12):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='male' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time<17):
        prediction = 0.50
        risk_group = '3: Moderate Risk'
    elif (gender =='male' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time<19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time>=19):
        prediction = 0.25
        risk_group = '1: Very Low Risk'
    elif (gender =='male' ) & ( parental_support=='3: High' ) & ( weekly_study_time<8):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='male' ) & ( parental_support=='3: High' ) & ( weekly_study_time<12):
        prediction = 0.50
        risk_group = '3: Moderate Risk'
    elif (gender =='male' ) & ( parental_support=='3: High' ) & ( weekly_study_time<17):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='3: High' ) & ( weekly_study_time<19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='3: High' ) & ( weekly_study_time>=19):
        prediction = 0.25
        risk_group = '1: Very Low Risk'
    elif (gender =='male' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time<8):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time<12):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time<17):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time<19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='male' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time>=19):
        prediction = 0.25
        risk_group = '1: Very Low Risk'
    elif (gender =='female' ) & ( parental_support=='0: None' ) & ( weekly_study_time<8):
        prediction = 0.70
        risk_group = '5: Very High Risk'
    elif (gender =='female' ) & ( parental_support=='0: None' ) & ( weekly_study_time<12):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='0: None' ) & ( weekly_study_time<17):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='0: None' ) & ( weekly_study_time<19):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='0: None' ) & ( weekly_study_time>=19):
        prediction = 0.50
        risk_group = '3: Moderate Risk'
    elif (gender =='female' ) & ( parental_support=='1: Low' ) & ( weekly_study_time<8):
        prediction = 0.70
        risk_group = '5: Very High Risk'
    elif (gender =='female' ) & ( parental_support=='1: Low' ) & ( weekly_study_time<12):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='1: Low' ) & ( weekly_study_time<17):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='1: Low' ) & ( weekly_study_time<19):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='1: Low' ) & ( weekly_study_time>=19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='female' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time<8):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time<12):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time<17):
        prediction = 0.50
        risk_group = '3: Moderate Risk'
    elif (gender =='female' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time<19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='female' ) & ( parental_support=='2: Moderate' ) & ( weekly_study_time>=19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='female' ) & ( parental_support=='3: High' ) & ( weekly_study_time<8):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='3: High' ) & ( weekly_study_time<12):
        prediction = 0.50
        risk_group = '3: Moderate Risk'
    elif (gender =='female' ) & ( parental_support=='3: High' ) & ( weekly_study_time<17):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='female' ) & ( parental_support=='3: High' ) & ( weekly_study_time<19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='female' ) & ( parental_support=='3: High' ) & ( weekly_study_time>=19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='female' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time<8):
        prediction = 0.57
        risk_group = '4: High Risk'
    elif (gender =='female' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time<12):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='female' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time<17):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='female' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time<19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    elif (gender =='female' ) & ( parental_support=='4: Very High' ) & ( weekly_study_time>=19):
        prediction = 0.42
        risk_group = '2: Low Risk'
    else:
        prediction = 9.99
        risk_group ='9: error'

    # creating a dataframe (start) -----------------------------------------------------------------

    data = {'id_number':id_number,
            'gender': gender,
            'parental_support': parental_support,
            'weekly_study_time': weekly_study_time,
            'risk_group':risk_group,
            'prediction':prediction}
    features = pd.DataFrame(data, index=[0])

    return features


# SIDEBAR (end) ------------------------------------------------------------

# MAIN PAGE (starts again) ---------------------------------------------------------

# Split dataframes -------------------------------------------------------------------------

df = user_input_features()
df2= df[['id_number','gender','parental_support','weekly_study_time']]
df3= df[['prediction','risk_group']]

# Show input variables ---------------------------------------------------------------------

st.subheader('User Input Parameters')
st.write(df2)
st.write("")

# Show output variables --------------------------------------------------------------------

st.subheader('Results')
st.write('This is the result of a decision tree model.')
st.write(df3)
st.write("For probabilities above 0.5, it's recommended that students either increase their study hours or seek help from a tutor.")
st.write("")

# Preparing download files -----------------------------------------------------------------

def convert_df_csv(df):
    return df.to_csv().encode("utf-8")

results_csv = convert_df_csv(df)

st.subheader('Download the Results')

st.download_button(
    label=".csv",
    data=results_csv,
    file_name="results.csv",
    mime="text/csv",
)

def convert_df_json(df):
    return df.to_json().encode("utf-8")

results_json = convert_df_json(df)

st.download_button(
    label=".json",
    data=results_json,
    file_name="results.json",
    mime="text/csv",
)

st.write("")
st.write("")

# Feedbacks space --------------------------------------------------------------------------

st.subheader('Leave your feedback')

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

