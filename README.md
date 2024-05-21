# Marks2CSV

## Introduction

Marks2CSV is an innovative tool designed to automate the process of 
converting student marks from answer sheet tables into well-structured 
CSV files. This utility is particularly useful for educators of [SJCET, Palai](https://sjcetpalai.ac.in)
who handle multiple student answer sheets and need to systematically 
record marks for further assessment and analysis.

## Why Marks2CSV?

Traditionally, marks from internal exams are recorded on the front of
each student's answer sheet, with individual question scores noted. 
Educators are then tasked with the laborious job of transcribing these 
marks into a CSV file format that adheres to specific requirements for 
further mapping to Course Outcomes (COs). This manual process is not 
only time-consuming but also prone to errors.

Marks2CSV simplifies this process. For a class of 60 students, instead 
of manually typing each student's marks into a spreadsheet, educators 
can now ease this process by just providing pictures of front of answer
sheet to the system and Marks2CSV will do the rest.

## Process Workflow

1. **Receives the Captured Image**: Begin by capturing an image of the entire answer sheet.

2. **Crop and Warp Image**: The image is then cropped and warped to focus only on the answer sheet section.

3. **Extract Table Containing Marks**: From the warped image, extract the table that contains the marks.

4. **Crop Out Each Cell of the Table**: Isolate each cell within the table for further processing.

5. **Text Recognition**: Each cropped cell is fed into the model for text recognition to detect the marks written inside.

6. **Map the Predicted Marks**: Convert the recognized marks of current answer sheet into the required CSV format.

7. **Repeat for Other Students**: This entire process is repeated for each student's answer sheet.


## Built With
<p>
  <a href="https://www.python.org">
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  </a>
  <a href="https://www.tensorflow.org">
    <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white"/>
  </a>
  <a href="https://opencv.org">
    <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
  </a>
  <a href="https://streamlit.io">
    <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"/>
  </a>
  <a href="https://github.com/xavctn/img2table">
    <img alt="img2table" src="https://img.shields.io/badge/img2table-007EC6?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>


## Team
<p>
  <a href="https://www.linkedin.com/in/aneetajose"> 
    <img alt="Aneeta Jose" src="https://img.shields.io/badge/-Aneeta%20Jose-0077B5?style=flat-square&logo=linkedin&logoColor=white"/>
  </a>
  <a href="https://www.linkedin.com/in/donsabu/"> 
    <img alt="Don Sabu" src="https://img.shields.io/badge/-Don%20Sabu-0077B5?style=flat-square&logo=linkedin&logoColor=white"/>
  </a>
  <a href="https://www.linkedin.com/in/jacob-philip0810">
    <img alt="Jacob Philip" src="https://img.shields.io/badge/-Jacob%20Philip-0077B5?style=flat-square&logo=linkedin&logoColor=white"/>
  </a>
  <a href="https://www.linkedin.com/in/pranav-p-9873a825a"> 
    <img alt="Pranav P" src="https://img.shields.io/badge/-Pranav%20P-0077B5?style=flat-square&logo=linkedin&logoColor=white"/>
  </a>
</p>

## Future Directions

As Marks2CSV continues to evolve, we aim to expand its capabilities and accessibility. Key developments in the pipeline include:

- **Desktop Application**: Package the system into a standalone desktop application, complete with an easy-to-install setup. This will provide educators with a robust, user-friendly interface directly on their PCs, streamlining the process further.

- **Integrated Webcam Stand**: Develop a customized webcam stand setup that can be bundled with the desktop application. This stand will help educators consistently capture high-quality images of answer sheets without the need for manual adjustments, ensuring optimal results.

- **Mobile Application**: Extend functionality to a mobile platform, allowing educators to capture, process, and convert marks into CSV files directly from their smartphones. This mobile app will offer convenience and portability, making it possible to handle grading tasks on the go.

These enhancements are aimed at making Marks2CSV not just a tool but a comprehensive solution for educational assessment management.



## Acknowledgements
This project is a continuation of the work initiated by our seniors. We build upon the foundation laid in the previous version of the Marks2CSV tool.

- **Original Project**: View the initial project [here](https://github.com/004Ajay/Marks2CSV_S6_Mini_Project).
