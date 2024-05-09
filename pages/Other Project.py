import streamlit as st

def main():
    
    st.markdown(
        """
        <style>
            .main {
                background-color: #f2f2f2;
                padding: 20px;
                text-align: center;
            }
            .title {
                color: #008080;
                font-size: 25px;
                transition: transform 0.1s;
            }
            .title:hover {
                transform: scale(1.1);
            }
            .image {
                border-radius: 50%;
                width: 150px;
                height: 150px;
                object-fit: cover;
                transition: transform 0.5s;
            }
            .image:hover {
                transform: rotate(360deg);
            }
            .navigation {
                padding: 20px;
            }
            .project {
                padding: 20px;
                margin-bottom: 30px;
                background-color: #ffffff;
                border-radius: 5px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: transform 0.5s;
            }
            .project:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            }
            .btn {
                padding: 10px 20px;
                margin: 5px;
                cursor: pointer;
                text-decoration: none;
                transition: background-color 0.5s;
            }
            .btn-primary {
                background-color: white;
                border: none;
                border-radius: 5px;
                color: #ffffff;
            }
            .btn-primary:hover {
                background-color: #005757;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="container">
            <div class="main">
                <h2 class="title">Welcome to My Portfolio</h2>
                <div class="navigation">
                    <a class="btn btn-primary" href="#home">Home</a>
                    <a class="btn btn-primary" href="#about">About Me</a>
                    <a class="btn btn-primary" href="#contact">Contact</a>
                    <a class="btn btn-primary" href="#projects">Projects</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="container">
            <div class="main" id="home">
                <h3></h3>
                <img class="image img-thumbnail" src="https://lh3.googleusercontent.com/a/ACg8ocI9zdpXHBgAuxaYJ_87083DQ10epjpIh0896lJr0se-WCM=s288-c-no" alt="Soni Agung Wahyudiyanta">
                <h3 class="mt-3" style="font-size:18px;">Soni Agung Wahyudiyanta</h3>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="container">
            <div class="main" id="about">
                <h3>About Me</h3>
                <p class="text-justify">I am dedicated to honing my data analysis skills through web research, forum engagement, and self-directed learning, alongside hands-on experience gained from boot camps. Proficient in Production Planning Control (PPC), I excel in leveraging MS Excel for precise production forecasting and scheduling. As an industrious student at Pelita Bangsa University, pursuing Industrial Engineering, I blend theoretical knowledge with practical insights, fostering a promising career trajectory.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="container">
            <div class="main" id="contact">
                <h3>Contact</h3>
                <p>WhatsApp: <a href="https://wa.link/kssl0s">0859-4377-1157</a></p>
                <p>Email: <a href="mailto:sonyagung308@gmail.com">sonyagung308@gmail.com</a></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="container">
            <div class="main" id="projects">
                <h3>Projects</h3>
                <div class="row">
                    <div class="col-md-6">
                        <div class="project">
                            <h4 class="mb-3">Bank Customer Churn Prediction | EDA | Machine Learning</h4>
                            <p>This project focuses on predicting customer churn in the banking sector using machine learning techniques. It involves data preprocessing, exploratory data analysis, and building predictive models.</p>
                            <img class="image img-thumbnail mb-3" src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*S3p9A6Sjnsl_fo3cAHSoZA.png" alt="Bank Customer Churn Prediction">
                            <a class="btn btn-primary" href="https://github.com/Sony-Agung/bankcustomer-churn/blob/main/Final_Project_Bank_Customer_Churn_Prediction%20(1).ipynb">View Project</a>
                            <a class="btn btn-primary" href="https://bankcustomer-churn.streamlit.app/">Application</a>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="project">
                            <h4 class="mb-3">Ergonomic Analysis of CNC Machine Production| EDA | ML</h4>
                            <p>CNC machine production analysis involves understanding steps from programming to execution. Machine Learning (ML) predicts machine performance, while Exploratory Data Analysis (EDA) helps understand production data patterns. This approach enhances production efficiency and quality..</p>
                            <img class="image img-thumbnail mb-3" src="https://w7.pngwing.com/pngs/482/939/png-transparent-machine-milling-computer-numerical-control-cnc-router-cnc-machine-angle-wood-3d-printing-thumbnail.png" alt="Bank Customer Churn Prediction">
                            <a class="btn btn-primary" href="https://github.com/Sony-Agung/predict_ergo">View Project</a>
                            <a class="btn btn-primary" href="https://prediksi-ergo.streamlit.app/">Application</a>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="project">
                            <h4 class="mb-3">Predict Student Exam | EDA | ML</h4>
                            <p>Analyzing and predicting student exam performance involves understanding student data and utilizing Machine Learning to forecast exam outcomes. It entails data analysis, ML model building, evaluation, optimization, and implementation. With this approach, we can effectively predict student exam performance to aid in enhancing learning outcomes.</p>
                            <img class="image img-thumbnail mb-3" src="https://miro.medium.com/v2/resize:fit:1400/1*8BrAADDVmFGq_bKyoty2yQ.jpeg" alt="Bank Customer Churn Prediction">
                            <a class="btn btn-primary" href="https://github.com/Sony-Agung/predict-students-exam">View Project</a>
                            <a class="btn btn-primary" href="https://predict-students-exam.streamlit.app/">Application</a>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="project">
                            <h4 class="mb-3">The death toll in the conflict between Palestine and Israel | EDA </h4>
                            <p>The analysis of casualties in the Palestine-Israel conflict aims to understand the impact of the conflict, gather data, identify trends, and highlight the need for peace.</p>
                            <img class="image img-thumbnail mb-3" src="https://www.thesquiz.com.au/wp-content/uploads/2020/07/Shortcuts-Website-17.png" alt="Bank Customer Churn Prediction">
                            <a class="btn btn-primary" href="https://github.com/Sony-Agung/Fatalities-of-Palestine---Israel/blob/main/KORBAN_TEWAS_DALAM_KONFLIK_ISRAEL_PALESTINA_2000_2023.ipynb">View Project</a>     
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="project">
                            <h4 class="mb-3">Credit card Details Binary Classification Problem Random Forest | EDA | Supervised Learning</h4>
                            <p>The project aims to develop a machine learning model to identify suspicious credit card transactions, addressing security concerns amid the increasing reliance on financial technology for banking and payments.</p>
                            <img class="image img-thumbnail mb-3" src="https://storage.googleapis.com/kaggle-datasets-images/3762169/6507180/561e51062132fd3b3538dbf6e3f4025a/dataset-cover.png" alt="Bank Customer Churn Prediction">
                            <a class="btn btn-primary" href="https://github.com/Sony-Agung/projek/blob/main/Credit%20card%20Details%20Binary%20Classification%20Problem.ipynb">View Project</a>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="project">
                            <h4 class="mb-3">HR Dataset Classificaton SVM | EDA | Supervised</h4>
                            <p>This project aims to analyze an HR dataset to understand the factors affecting employee satisfaction and retention. Through data analysis and machine learning, we will identify patterns and trends to help improve human resource management and decision-making within the company.</p>
                            <img class="image img-thumbnail mb-3" src="https://hranalyticslive.netlify.app/images/hranalytics.jpg" alt="Bank Customer Churn Prediction">
                            <a class="btn btn-primary" href="https://github.com/Sony-Agung/projek/blob/main/Supervised%20II%20(svm)%20binary(yes%20or%20true).ipynb">View Project</a>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="project">
                            <h4 class="mb-3">Mall Customers Clustering K-Means | EDA | Unsupervised</h4>
                            <p>This project focuses on customer segmentation at a shopping mall. The dataset includes variables such as CustomerID, Gender, Age, Annual Income, and Spending Score. The goal is to utilize data segmentation techniques to group customers based on characteristics like age, income, and spending patterns. Understanding these customer groups allows the mall to develop more effective marketing strategies, tailor product offerings, and enhance customer satisfaction.</p>
                            <img class="image img-thumbnail mb-3" src="https://www.aimtechnologies.co/wp-content/uploads/2023/09/customer-segmentation-social.png" alt="Bank Customer Churn Prediction">
                            <a class="btn btn-primary" href="https://github.com/Sony-Agung/projek/blob/main/unsupervised%20I.ipynb">View Project</a>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="project">
                            <h4 class="mb-3">Titanic Dataset Classification KNN,Decission Tree, Random Forest, Logistic Regression | EDA | Machine Learning</h4>
                            <p>The aim of this project is to analyze the Titanic dataset and build a predictive model to predict whether a passenger survived or not during the Titanic disaster. By understanding the factors influencing survival, this project can provide insights into more effective rescue strategies and factors that may affect outcomes in similar emergency situations in the future.</p>
                            <img class="image img-thumbnail mb-3" src="https://media.licdn.com/dms/image/C4D12AQHsDRbH7GXOZg/article-cover_image-shrink_720_1280/0/1604989195408?e=2147483647&v=beta&t=Sq8lv3D1ux7dlVC2R34L7Z--UWHXp4nnCw5Y8j2ciqw" alt="Bank Customer Churn Prediction">
                            <a class="btn btn-primary" href="https://github.com/Sony-Agung/projek/blob/main/Supervised%201.ipynb">View Project</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
