import streamlit as st
import urllib.parse


WHATSAPP_Number="+923112519069"

st.set_page_config(
    page_title="TechCart",
    page_icon="📱",
    layout="wide",
)
st.title("💻TechCart")
st.write("Smart Products.Simple shopping.")

menu = st.radio("Menu",
                ["Home","Products","Categories","About","Contact"],
                 horizontal=True)

st.divider()

if menu == "Home":
    st.header("Welcome to my TechCart")

    st.write("Discover useful technology products at affordable prices")
    st.button("🛍️ SHOP NOW")

    st.divider()


    st.header("Why shop with us? ")
    col1,col2,col3=st.columns(3)
    with col1:
        st.subheader("Quality Products")
        st.write("We offer  high quality products")
    with col2:
            st.subheader("Affordable Prices")
            st.write("We offer affordable and resonable prices")    

    with col3:
                st.subheader("Easy Ordering")
                st.write("Order your favourite proucts.")    




elif menu =="Products":
    st.header("Our Products")
    st.write("Our Products will appear here")
    st.divider()
    col1,col2,col3=st.columns(3)
    with col1:
            st.image("earbuds.png",use_container_width=True)
            st.subheader("Premimum Earbuds")
            st.write("Comfotable wireless earbuds")
            st.write("Price: Rs.1500")
            message="""Hello! I am Interested in ordering:
            Product:Earbuds
            Price=1500 Rs
            Please provide more details"""
            whatsapp_url=(
                   f"https://wa.me/{WHATSAPP_Number}?text={urllib.parse.quote(message)}"                  #format ha same rahega
            )
            st.link_button("🛍️Shop Now",whatsapp_url)
    with col2:
                st.image("laptop.png",use_container_width=True)
                st.subheader("HP Laptop")
                st.write("8Th Generation Laptop")
                st.write("Price: Rs.15000")
                message="""Hello! I am Interested in ordering:
                            Product:HP LAPTOP
                            Price=15000 Rs
                            Please provide more details"""
                whatsapp_url=(
                                   f"https://wa.me/{WHATSAPP_Number}?text={urllib.parse.quote(message)}"                  #format ha same rahega
                            )
                st.link_button("🛍️Shop Now",whatsapp_url)
    with col3:
                    st.image("mouse.png",use_container_width=True)
                    st.subheader("HP Mouse")
                    st.write("Laltop Mouse wireless")
                    st.write("Price: Rs.2000")
                    st.button("🛍️Buy Mouse")            







elif menu =="Categories":
    st.header("Products Categories")
    st.write("Our Products categories will appear here")
elif menu =="About":
    st.header("About TechCart")
    st.write("Learn more about our store.")
elif menu =="Contact":
    st.header("Contact us")
    st.write("Our Contact will appear here")