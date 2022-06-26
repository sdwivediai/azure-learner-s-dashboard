
import pandas as pd
from bs4 import BeautifulSoup
import requests as r
import streamlit as st
from gsheetsdb import connect

# # Create a connection object.
conn = connect()


# # Perform SQL query on the Google Sheet.
# # Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

cloud_comparison = st.secrets["Cloud_Comparison"]



with st.sidebar:
    azure_networking_product = st.radio('Choose an Azure networking product', ['VNet', 'VPN Gateway', 'CDN', 'AFD', 'DNS', 'Traffic Manager', 'Express Route', 'Load Balancer'])


if azure_networking_product == 'VNet':
    st.subheader('Basic Concept')
    st.markdown("A virtual network, in general, can be thought of as a virtual routing switch hosted in the cloud that all services connect to and use to communicate with each other. Azure's virtual network offering is called VNet. Further down the page you will find a list of virtual network offerings by other cloud providers.")

    #what, why = st.columns(2)

    #@st.cache(suppress_st_warning=True)
    def get_azuredoc_info():
        req = r.get(f"https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview",
                    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"})
        soup = BeautifulSoup(req.content, features="html.parser") #converting the content/text returned by request to a BeautifulSoup object
        azure_doc_info = soup.find("div", class_="content").find_all("p")
        return azure_doc_info

    azure_doc_info = get_azuredoc_info()

    #with what:
        #st.subheader("What is Azure Virtual Network")
        #what_is_vnet = azure_doc_info[0].text
        #st.markdown(what_is_vnet)
        

    #with why:
        #st.subheader("Why use an Azure VNet")
        #why_vnet = azure_doc_info[1].text
        #st.markdown(why_vnet)
        
    st.subheader("Azure VNet")
    why_vnet = azure_doc_info[1].text
    st.markdown(why_vnet)
    st.write('https://azure.microsoft.com/en-us/services/virtual-network/')  

    st.subheader("Video Tutorial")
    with st.expander("Expand for tutorial"):
        st.video("https://www.youtube.com/embed/7rzawA--r20")
    
    
    alternative_products = run_query(f'SELECT * FROM "{cloud_comparison}" where Category = "Virtual Network"')
    
    
    st.subheader("Similar Offerings by other vendors")
   
    with st.expander("Expand for details"):
 
        vendor, product, link =st.columns(3)

        with vendor: 
            st.subheader("Vendor")
            st.write("Google")
            st.write("AWS")
            st.write("IBM")
            st.write("Oracle")
            st.write("Alibaba")
            st.write("Huawei")


        with product:
            st.subheader("Offering Name")
            st.write(alternative_products[0].Google)
            st.write(alternative_products[0].AWS)
            st.write(alternative_products[0].IBM)
            st.write(alternative_products[0].Oracle)
            st.write(alternative_products[0].Alibaba)
            st.write(alternative_products[0].Huawei)

        with link:
            st.subheader("Link")
            st.markdown("https://cloud.google.com/vpc", unsafe_allow_html=True)
            st.markdown("https://aws.amazon.com/vpc/", unsafe_allow_html=True)
            st.markdown("https://cloud.ibm.com/docs/vpc?topic=vpc-getting-started", unsafe_allow_html=True)
            st.markdown("https://cloud.oracle.com/networking", unsafe_allow_html=True)
            st.markdown("https://www.alibabacloud.com/product/vpc", unsafe_allow_html=True)
            st.markdown("https://www.huaweicloud.com/intl/en-us/product/vpc.html", unsafe_allow_html=True)

     
    st.subheader("Important difference(s), if any, with competitive offerings")
    st.markdown("Azure VNet and AWS VPC are created in a region. They can span across multiple Availability Zones(AZ) though and subnets exist inisde an AZ. In comparison, a Google Cloud VPC is a global resource and is not associated with any specific region. The subnets in it are region specific. ")        

    #st.subheader("Click the below link for more info")
    #st.write('https://azure.microsoft.com/en-us/services/virtual-network/')       
 

if azure_networking_product == 'VPN Gateway':
    st.subheader('Basic Concept')
    st.markdown("A virtual network, in general, can be thought of as a virtual routing switch hosted in the cloud that all services connect to and use to communicate with each other. Azure's virtual network offering is called VNet. Further down the page you will find a list of virtual network offerings by other cloud providers.")

    #what, why = st.columns(2)

    #@st.cache(suppress_st_warning=True)
    def get_azuredoc_info():
        req = r.get(f"https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview",
                    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"})
        soup = BeautifulSoup(req.content, features="html.parser") #converting the content/text returned by request to a BeautifulSoup object
        azure_doc_info = soup.find("div", class_="content").find_all("p")
        return azure_doc_info

    azure_doc_info = get_azuredoc_info()

    #with what:
        #st.subheader("What is Azure Virtual Network")
        #what_is_vnet = azure_doc_info[0].text
        #st.markdown(what_is_vnet)
        

    #with why:
        #st.subheader("Why use an Azure VNet")
        #why_vnet = azure_doc_info[1].text
        #st.markdown(why_vnet)
        
    st.subheader("Azure VNet")
    why_vnet = azure_doc_info[1].text
    st.markdown(why_vnet)
    st.write('https://azure.microsoft.com/en-us/services/virtual-network/')  

    st.subheader("Video Tutorial")
    with st.expander("Expand for tutorial"):
        st.video("https://www.youtube.com/embed/7rzawA--r20")
    
    
    alternative_products = run_query(f'SELECT * FROM "{cloud_comparison}" where Category = "Virtual Network"')
    
    
    st.subheader("Similar Offerings by other vendors")
   
    with st.expander("Expand for details"):
 
        vendor, product, link =st.columns(3)

        with vendor: 
            st.subheader("Vendor")
            st.write("Google")
            st.write("AWS")
            st.write("IBM")
            st.write("Oracle")
            st.write("Alibaba")
            st.write("Huawei")


        with product:
            st.subheader("Offering Name")
            st.write(alternative_products[0].Google)
            st.write(alternative_products[0].AWS)
            st.write(alternative_products[0].IBM)
            st.write(alternative_products[0].Oracle)
            st.write(alternative_products[0].Alibaba)
            st.write(alternative_products[0].Huawei)

        with link:
            st.subheader("Link")
            st.markdown("https://cloud.google.com/vpc", unsafe_allow_html=True)
            st.markdown("https://aws.amazon.com/vpc/", unsafe_allow_html=True)
            st.markdown("https://cloud.ibm.com/docs/vpc?topic=vpc-getting-started", unsafe_allow_html=True)
            st.markdown("https://cloud.oracle.com/networking", unsafe_allow_html=True)
            st.markdown("https://www.alibabacloud.com/product/vpc", unsafe_allow_html=True)
            st.markdown("https://www.huaweicloud.com/intl/en-us/product/vpc.html", unsafe_allow_html=True)

     
    st.subheader("Important difference(s), if any, with competitive offerings")
    st.markdown("Azure VNet and AWS VPC are created in a region. They can span across multiple Availability Zones(AZ) though and subnets exist inisde an AZ. In comparison, a Google Cloud VPC is a global resource and is not associated with any specific region. The subnets in it are region specific. ")        

    #st.subheader("Click the below link for more info")
    #st.write('https://azure.microsoft.com/en-us/services/virtual-network/')       
      

