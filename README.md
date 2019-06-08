# Final Project of ECE143 -Analysis on Jobs and Leetcode questions (Group 14)
## Team Members
Shreya Ganesaraman


Zeyuan Li


Meihua Su 


Zhongke Ma: z2ma@eng.ucsd.edu

## Getting Started
This project contains both getting data from leetcode and analysis.
For the demo, please use the "DEMO_TO_RUN.ipynb".

## Problem

## Dataset

## File Structure

master branch
|
+----DEMO_TO_RUN.ipynb
|
+----DEMO_TO_RUN.py
|
+----Presentation.pdf
|
+----code
|       |   1. Data Extraction.ipynb
|       |   2. Dictionary JSON Generators.ipynb
|       |   3. Dataframe Generators.ipynb
|       |   4. Plot Problems against tags.ipynb
|       |   5. Plot problem nums of different companies.ipynb
|	|   6. Plot wordcloud.ipynb
|	|   7. Plot world map of jobs.ipynb
|	|   Plot_Difficulty_Of_Different_Companies.py
|	|   Plot_Pie_Chart.py
|	|   Plot_problem_nums_of_different_company.py
|	|   Plot_WC.py
|	|   Plot_Work_Distribution.py
+
|    data
|	|   company_folder
|	|   output_ACSolns
|	|   output_ALLQus     

## Instructions on running the code
Python version-> Python 3.5 or later

### Required packages
01. import numpy


02. import os


03. import matplotlib.pyplot as plt


04. import pandas as pd


05. import numpy as np


06. import string


07. import wordcloud


08. from wordcloud import WordCloud


09. from stop_words import get_stop_words


10. import shapefile as shp


11. import seaborn as sns


12. import plotly


13. import geopandas as gpd


14. from shapely.geometry import Point, Polygon


15. import plotly.plotly as py


16. import plotly.graph_objs as go


***********************DEMO*************************

The DEMO_TO_RUN contains analysis codes which using the files under "output_AllQus", "output_ACSolns" and "company_folder".
To run the code, please have the folders and file ready.
It contains "Bar Chart", "Pie Chart", "Word Cloud", "US MAP of Job Distribution" (with the html page generation)
