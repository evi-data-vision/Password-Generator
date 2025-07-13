import streamlit as st
import random
import string
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt')

nltk.download('words')
from nltk.corpus import words

st.title('Password Generator!')

pass_type = st.radio('select your password type :' , ['PIN Code' , 'Random Password' , 'Memorable Password'] , index  = None)

if pass_type == 'PIN Code' :
    letters = string.digits
    length = st.slider('Select the length of PIN Code : ' , min_value = 6 , max_value = 32 , value = 8)
    password = ''.join(random.choices(letters , k = length))
    st.write('Your Generated PIN Code is : ' , password)

elif pass_type == 'Random Password' :
     upper = st.toggle('Uppercase Letters')
     digits = st.toggle('Digits')
     sign = st.toggle('Special Characters')
     length = st.slider('Select the length of Password : ' , min_value = 6 , max_value = 32 , value = 8)

     letter = string.ascii_lowercase
     if upper : letter += string.ascii_uppercase
     if digits : letter += string.digits
     if sign : letter += string.punctuation

     password = ''.join(random.choices(letter , k = length))
     st.write('Your Generated Password is : ' , password)

elif pass_type == 'Memorable Password' :
    seperator = st.selectbox('Seperator : ' , ['-' , '_' , ',' , '.'])
    capitalize = st.toggle('Capitalize First Letter of Each Word')
    
    if capitalize :
        word_list = [word.capitalize() for word in words.words()]
    else : 
        word_list = [word.lower() for word in words.words()]
    length = st.slider('Select the number of words : ' , min_value = 2 , max_value = 8 , value = 3)
    password = seperator.join(random.choices(word_list, k=length))
    st.write('Your Generated Memorable Password is : ' , password)
elif pass_type == 'None' :
    pass

