import streamlit as st
from pymongo import MongoClient
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title='Rahul Patil - Data Scientist', page_icon=':office:', layout='wide')




col1, col2, col3 = st.columns((3))

# Set the title and header
with col1:
    st.title("Rahul Patil - Data Scientist")

# load animation 
def load_lottie(url: str):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


# Contact Information
with col1:
    st.subheader("Contact Information")
    st.write("""
    **Email:** rahul.datascientist.04@gmail.com  
    **Phone:** 9552328154
    **Portfolio:** [Rahul-Patil](rahulpatil.streamlit.app)  
    **LinkedIn:** [Rahul-Patil](https://www.linkedin.com/in/rahul-patil-1a7930188/)  
    **GitHub:** [Rahul-Patil](https://github.com/rahul-patil0411)
    """)
with col3:
    lottie_hello = load_lottie('https://lottie.host/03f63272-ebfd-421f-a05d-d5a115ea834d/MNRX76Zr4S.json')
    st_lottie(
        lottie_hello,
        key='Hello Buddy',
        quality='high',
        height=300,
        width=300,
        speed=1,
        loop=2
    )




# Profile
st.subheader("Profile")
st.write("""
A Results-driven professional with a strong foundation as an Assistant Professor specializing in Big Data, exhibiting
proficiency in Hadoop, Pig, Hive, AWS, and advanced Python programming. Adept at designing and delivering
comprehensive curriculum covering Big Data concepts, Machine Learning, and Predictive Modelling. Seeking a transition to a
data engineer role, equipped with skills in ETL, data integration, and expertise in managing and optimizing raw data through
automation, coupled with practical experience in advanced technologies and Parametric Evaluation data analysis.""")



# Professional Experience
st.subheader("Professional Experience")

st.write("**Symbiosis Skills and Professional University - Data Science Trainer**")
st.write("""
Key Note: All Practical and Skill conducted in below 4 subjects are advanced up to industry standards.

**1) Big Data Architecture and Ecosystem**
- Proven experience as an Assistant Professor specializing in Big Data, with in-depth knowledge of key technologies
such as Hadoop, Pig, Hive, and AWS. Proficient in teaching both theoretical concepts and practical applications of
these tools to students.
- Designed and delivered a comprehensive curriculum encompassing essential topics in Big Data, including Hadoop
Administration, MapReduce Programming, Machine Learning, Data Analysis, and API integration. Ensured students
receive a well-rounded education in the field, preparing them for real-world challenges.
- Integrated Project Management principles into the curriculum, guiding students through practical project
implementations. Specialized in teaching Predictive Modeling techniques, emphasizing the application of Machine
Learning for data-driven decision-making.
- Instructed students in the principles of Data Visualization, emphasizing effective communication of insights
derived from Big Data analysis. Additionally, provided hands-on training in Extract, Transform, Load (ETL) processes,
enhancing students' skills in preparing and transforming data for analysis.
         
**2) Evolutionary Computation**
- Proven experience as an Assistant Professor specializing in Evolutionary Computation, with in-depth knowledge of
key topics such as Genetic Algorithms, Artificial Immune Systems, and Quantum Genetic Algorithms. Proficient in
teaching both theoretical concepts and practical applications of these algorithms to students.
- Designed and delivered a comprehensive curriculum encompassing essential topics in evolutionary computation,
including Genetic Operators (selection, crossover, mutation), Multi-objective Optimization, and performance
indicators such as Generational Distance and Hypervolume. Prepared students to tackle real-world challenges using
these advanced techniques.
- Integrated Optimization Problems into the curriculum, covering NP-complete problems and various Vehicle
Routing Problem (VRP) variants. Guided students through practical implementations and integer programming
formulations for complex optimization scenarios.
- Instructed students in modern Computing Paradigms such as Cluster, Grid, and Cloud Computing, as well as
emerging technologies like the Internet of Things (IoT) and Fog Computing. Emphasized key issues including
security, scalability, and energy consumption, preparing students for the evolving landscape of computational
technologies.
         
**3) Internet and Web Technologies**
- Proven experience as an Assistant Professor specializing in Internet and Web Technologies, with comprehensive
knowledge of key web technologies and programming languages. Proficient in teaching both theoretical concepts
and practical applications to students.
- Designed and delivered a detailed curriculum covering essential Web Essentials topics such as HTTP protocols,
HTML5, CSS, and XHTML, ensuring students understand both the fundamentals and advanced features of web
development.
- Taught JavaScript client-side scripting, including variables, functions, conditions, loops, and events, enabling
students to create dynamic and interactive web pages by integrating HTML, CSS, and JavaScript.
- Delivered lessons on XML, including its components, DTD and Schemas, and transformations using XSLT, providing
students with skills to effectively use XML in web applications.
- Guided students through PHP Programming, covering script creation, variables, constants, data types, control
structures, arrays, functions, and working with MySQL databases, preparing them for backend web development.
- Introduced PERL and Ruby, teaching fundamental concepts such as variables, arrays, hashes, regular expressions,
and control structures, along with practical applications in file handling and web document retrieval for PERL, and an
overview of Ruby on Rails for Ruby.
         
**4) R programming**
- Proven experience as an Assistant Professor specializing in R Programming, with in-depth knowledge of both
fundamental and advanced R concepts. Proficient in teaching theoretical and practical applications of R
programming to students.
- Designed and delivered a comprehensive curriculum covering essential R Programming topics, including
installation, data types, control structures (if, if…else, switch statements), and various loops (repeat, while, for).
Provided practical training on using built-in and user-defined functions.
- Taught students String and Vector Manipulation, including constructing and manipulating strings, vectors, lists,
matrices, arrays, factors, and data frames. Introduced students to various R packages to enhance their programming
capabilities.
- Delivered lessons on R Data Interfaces, teaching how to input, read, and analyse data from CSV, Excel, binary, and
XML files, ensuring students are equipped to handle diverse data sources.
- Instructed students in creating R Charts and Graphs, including pie charts, bar charts, box plots, histograms, line
charts, scatter plots, and matrix plots. Emphasized the importance of data visualization in data analysis.
- Covered R Statistics extensively, teaching measures of central tendency and dispersion, linear regression, multiple
linear regression, logistic regression, probability computation, and hypothesis testing. Prepared students to perform
comprehensive statistical analysis using R.
""")

st.write("**Parenthesis Systems PVT. LTD. - Data Scientist Intern**")
st.write("""
- Developed and implemented an automated Python program for handling raw data, optimizing the conversion of raw data
into formatted datasets.
- Acquired practical experience with advanced technologies, including fuzzy logics and AWS API services, showcasing a
versatile skill set in data science.
- Monitored and analyzed Parametric Evaluation data for heat treatment furnaces using HuMac, applying various algorithms
to predict trends and contribute to data-driven decision-making.
- Gained in-depth knowledge in the domain of heat treatment furnaces, understanding the unique challenges and
requirements of industrial processes.
- Suggested and implemented changes in raw data structures, improving data quality for more effective analysis.
Collaborated with the team to enhance overall data processing capabilities
""")

st.write("**Parentheses System PVT. LTD. - Intern Data Analyst**")
st.write("""
- Skilled in using Python (Pandas, NumPy) for data analysis, and creating impactful data visualizations using Matplotlib and Seaborn.
- Develop ETL pipelines and collaborate with cross-functional teams to deliver data-driven insights.
- Present complex analytical findings to business teams and bridge the gap between technical and non-technical stakeholders.
""")

st.write("**Dotmg Studio - Web Developer and Digital Marketer**")
st.write("""
- Increased website traffic by 25% through data-driven SEO initiatives.
- Developed visually appealing websites using frontend technologies like HTML, CSS, JS, and Django.
- Created robust web applications using backend technologies such as PHP, SQL, DBMS, and PostgreSQL.
""")

# Education
st.subheader("Education")

st.write("**M.Sc. Data Science** - Symbiosis Skills and Professional University (2021 - 2023) Pune")
st.write("**B.Sc. CS** - PCCCS (2018-2021) Pune")

# Skills
st.subheader("Skills")
st.write("""
- **Data Analyst:** Power BI, Tableau, AWS Glue, ETL, Python (Matplotlib, Seaborn, Plotly)
- **Data Mining:** SQL, NoSQL, MongoDB, Cloud extraction, PostgreSQL
- **Cloud Computing:** AWS, GCP, Azure
- **Web Development:** HTML, CSS, Django, Bootstrap, SQL, DBMS, JavaScript, PHP
- **Documentation:** Excel, Word, PowerPoint
- **DevOps:** Git, GitHub, Docker, Unix
""")

# Certifications
st.subheader("Certifications")
st.write("""
- **Data Science Master** - Physics Wallah
- **Build a Data Science Web App with Streamlit and Python** - Coursera
- **Data Analytics Part 2: Extending and Applying Core Knowledge**
""")

# Projects
st.subheader("Projects")

st.write("[**Data Visualization - Power BI**](https://linktr.ee/Kaumilmg)")
st.write("""
- Conducted in-depth analysis across different fields using Power BI for data visualization.
- Strong grasp of live data, SQL, Python, and various dataset formats such as JSON, CSV, Excel, and SQL.
- Utilized Python packages like pandas, numpy, matplotlib, seaborn, and plotly for visualization.
""")

st.write("[**Flipkart Product Review Using Python - AWS (Code pipeline, Beanstalk), MongoDB**](https://github.com/kaumil-mg/web-scrap)")
st.write("""
- Web scraped product reviews using BeautifulSoup and Selenium, stored data in MongoDB, and automated deployment with AWS services.
""")

st.write("[**E-commerce Website - HTML & CSS, PHP, JS**](https://www.youtube.com/watch?v=6TDlgTe8gEQ)")
st.write("""
- Built a dynamic e-commerce website with essential features such as product catalog, shopping cart, secure checkout, and showcased skills in database management and user authentication.
""")



# Footer
st.write("For more details, visit my [LinkedIn](https://www.linkedin.com/in/kaumilmg/) or [GitHub](https://github.com/kaumil-mg).")
