
import pandas as pd
from bs4 import BeautifulSoup
import requests as r
import streamlit as st
from gsheetsdb import connect


conn = connect()

@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

cloud_comparison = st.secrets["Cloud_Comparison"]

alternative_products = run_query(f'SELECT * FROM "{cloud_comparison}"')

with st.sidebar:
    azure_networking_product = st.radio('Choose an Azure networking product', ['VNet', 'VPN Gateway', 'Load Balancer'])
                                                                               
                                                                             
    
if azure_networking_product == 'VNet':
    st.subheader('Basic Concept')
    st.markdown("A virtual network, in general, can be thought of as a virtual routing switch hosted in the cloud that all services connect to and use to communicate with each other. Azure's virtual network offering is called VNet. Further down the page you will find a list of virtual network offerings by other cloud providers.")

     
    def get_azuredoc_info():
        req = r.get(f"https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview",
                    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"})
        soup = BeautifulSoup(req.content, features="html.parser") #converting the content/text returned by request to a BeautifulSoup object
        azure_doc_info = soup.find("div", class_="content").find_all("p")
        return azure_doc_info

    azure_doc_info = get_azuredoc_info()

        
    st.subheader("Azure VNet")
    why_vnet = azure_doc_info[1].text
    st.markdown(why_vnet)
    st.write('https://azure.microsoft.com/en-us/services/virtual-network/')  

    st.subheader("Video Tutorial")
    with st.expander("Expand for tutorial"):
        st.video("https://www.youtube.com/embed/7rzawA--r20")
    
    
    
    st.subheader("Similar Offerings by other vendors")
   
    with st.expander("Expand for details"):
        vendor, product, link = st.columns(3)
        
        with vendor:
            for alt in alternative_products:
                st.write(f"{alt.Vendors}")
        
        with product:
            for alt in alternative_products:
                st.write(f"{alt.Virtual_Network}")
        
        with link:
            for alt in alternative_products:
                st.write(f"{alt.Virtual_Network_link}")

       
     
    st.subheader("Important difference(s), if any, with competitive offerings")
    st.markdown("Azure VNet and AWS VPC are created in a region. They can span across multiple Availability Zones(AZ) though and subnets exist inisde an AZ. In comparison, a Google Cloud VPC is a global resource and is not associated with any specific region. The subnets in it are region specific. ")        

    #st.subheader("Click the below link for more info")
    #st.write('https://azure.microsoft.com/en-us/services/virtual-network/')       
 

if azure_networking_product == 'VPN Gateway':
    

    #@st.cache(suppress_st_warning=True)
    def get_vpn_info():
        req = r.get(f"https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways",
                    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"})
        soup = BeautifulSoup(req.content, features="html.parser") #converting the content/text returned by request to a BeautifulSoup object
        vpn_info = soup.find("div", class_="content").find_all("p")
        return vpn_info

    vpn_info = get_vpn_info()

    st.subheader('Basic Concept')
    st.markdown(vpn_info[1].text)
    
        
    st.subheader("VPN Gateway")
    st.markdown(vpn_info[0].text)
    st.write('https://azure.microsoft.com/en-us/services/vpn-gateway/')  

    st.subheader("Video Tutorial")
    with st.expander("Expand for tutorial"):
        st.video("https://youtu.be/yYnACA8ggNI")
    
        
    
    st.subheader("Similar Offerings by other vendors")
   
    with st.expander("Expand for details"):
        vendor, product, link = st.columns(3)
        
        with vendor:
            for alt in alternative_products:
                st.write(f"{alt.Vendors}")
        
        with product:
            for alt in alternative_products:
                st.write(f"{alt.Network_Gateway}")
        
        with link:
            for alt in alternative_products:
                st.write(f"{alt.Network_Gateway_link}")
     
    st.subheader("Important difference(s), if any, with competitive offerings")
    #st.markdown("Azure VNet and AWS VPC are created in a region. They can span across multiple Availability Zones(AZ) though and subnets exist inisde an AZ. In comparison, a Google Cloud VPC is a global resource and is not associated with any specific region. The subnets in it are region specific. ")        

        
  
if azure_networking_product == 'Load Balancer':
    

    #@st.cache(suppress_st_warning=True)
    def get_lb_info():
        req = r.get(f"https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview",
                    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"})
        soup = BeautifulSoup(req.content, features="html.parser") #converting the content/text returned by request to a BeautifulSoup object
        lb_info = soup.find("div", class_="content").find_all("p")
        return lb_info

    lb_info = get_lb_info()

    st.subheader('Basic Concept')
    st.markdown(lb_info[0].text)
    
        
    st.subheader("Azure Load Balancer")
    st.markdown(lb_info[1].text)
    st.write('https://azure.microsoft.com/en-us/services/load-balancer/#overview')  

    st.subheader("Video Tutorial")
    with st.expander("Expand for tutorial"):
        st.video("https://youtu.be/wJvmXM81tEI")
    
    

    
    
    st.subheader("Similar Offerings by other vendors")
   
    with st.expander("Expand for details"):
        vendor, product, link = st.columns(3)
        
        with vendor:
            for alt in alternative_products:
                st.write(f"{alt.Vendors}")
        
        with product:
            for alt in alternative_products:
                st.write(f"{alt.Load_Balancers}")
        
        with link:
            for alt in alternative_products:
                st.write(f"{alt.Load_Balancers_link}")
        
     
    st.subheader("Important difference(s), if any, with competitive offerings")
   
        
      



