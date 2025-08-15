import streamlit as st
st.title("DELIVERY SYSTEM")
name=st.text_input("name")
address=st.text_input("address")
contact=st.text_input("contact")
st.write("payment method")
momo_payment=st.checkbox("momo payment")
pay_now=st.checkbox("pay now")
cash_on_delivery=st.checkbox("cash on delivery")
st.write("did you pay via momo:")
col1,col2=st.columns(2)
with col1:
	yes=st.checkbox("yes")
with col2:	
    no=st.checkbox("no")
if st.button("submit"):
   st.success("details submitted") 