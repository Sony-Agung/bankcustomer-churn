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
                </div>
                <div class="row">
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
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
