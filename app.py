import streamlit as st

def main(database): 
    ccc1,ccc2,ccc3 = st.columns([1,3,1])
    ccc2.subheader("")
    st.write('This is an application for quick analysis and visualization of powder XRD data. Read the following documents before using this software.  This software is created by Chihaya Fujiwara (https://researchmap.jp/C_Fujiwara or -----). If you have any questions, please contact this email address ---[at]--.')
    with st.expander('Quick Summary'):
        markdown2 = """        
        * **Exp file** ： You can load a .ras file, which is the experimental X-ray diffraction data from RIGAKU instrument. You can also convert .ras files to .csv files here.
        * **Candidate composition** ： Please select the elements that are considered to be included. These database displayed here is based on **Crystallography Open Database (COD)** (https://www.crystallography.net/cod/). If you would like to get more information of the database, please access the url(https://www.crystallography.net/cod/search.html) and enter the corresponding COD ID. 
            (For example 9006388 : NaCl).
        * **Candidate List** ：Here you can select the data for which you want the XRD diffraction pattern to be displayed. 
        * **XRD pattern** :  The XRD pattern of the actual measurement loaded can be compared with the XRD pattern of the selected crystal structure. These Simulations are based on the **pymategen** python library (https://pymatgen.org/pymatgen.analysis.diffraction.html). 
        * **Exp data** : You can save the experimental XRD resutls as .csv files.
        * **Cif data** : You can check the reference cif file by interfacing it with **VESTA** (https://jp-minerals.org/vesta/jp/). The XRD simulation pattern can also be saved as a csv file.
        * **Background** : You can perform a various background processes here.
        * **Upload cif file** : CIF files can be optionally added to the database. Just upload the ciffile and press the button database upload..
        """

        st.markdown(markdown2)        


if __name__ == '__main__':
    main()