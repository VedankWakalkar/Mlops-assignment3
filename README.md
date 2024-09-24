Project Overview:
This project is a web-based application that allows users to filter data from the famous Iris dataset based on species and visualize the distribution of key features for the selected species. Built using FastAPI for the backend, the app provides a user-friendly interface to interact with the dataset, retrieve filtered results, and display feature distributions through histograms.

Key Features:
Data Filtering by Species:

The application accepts the name of an Iris species (e.g., Iris-setosa, Iris-versicolor, Iris-virginica) as input and filters the corresponding rows from the dataset.
If the species is not found in the dataset, an error message is returned, ensuring proper validation.
Visualization of Feature Distributions:

For each species, the application generates histograms representing the distribution of four key features: Sepal Length, Sepal Width, Petal Length, and Petal Width.
These visualizations are created dynamically using Matplotlib and displayed on the webpage, giving users insights into how the features are distributed for the selected species.
REST API Integration:

The backend is powered by FastAPI, which serves as the RESTful API for the web application. The API provides an endpoint (/filter-data/{species}) to retrieve filtered data and the corresponding visualizations.
FastAPI ensures fast, asynchronous communication between the frontend and the backend, allowing smooth user interaction and data retrieval.
Responsive Webpage:

The user interface is designed using simple HTML, CSS, and JavaScript, offering an intuitive input field for species names and displaying the results in a clean, readable format.
The webpage makes use of JavaScript's fetch API to communicate with the FastAPI backend asynchronously, providing real-time feedback and visualizations to the user.
Technologies Used:
FastAPI: A high-performance web framework used for developing the backend REST API.
Pandas: For reading and manipulating the Iris dataset.
Matplotlib: Used to create feature distribution visualizations (histograms).
HTML/CSS: To design the front-end user interface.
JavaScript (fetch API): For making asynchronous API calls to the backend and dynamically updating the webpage with results.
Uvicorn: ASGI server for running FastAPI applications.
How It Works:
Data Loading:

The Iris dataset is loaded into a Pandas DataFrame when the FastAPI server starts. The dataset contains information about three species of Iris flowers: Iris-setosa, Iris-versicolor, and Iris-virginica, with each row containing measurements of four key features: Sepal Length, Sepal Width, Petal Length, and Petal Width.
Filtering Process:

The user enters the name of a species into the input field on the webpage. This input is sent to the FastAPI backend, which filters the DataFrame based on the selected species and returns the relevant rows to the frontend.
Data Visualization:

Along with the filtered data, the backend uses Matplotlib to generate histograms for the four key features, visualizing their distribution for the selected species. These plots are saved as image files and sent back to the frontend to be displayed.
Displaying Results:

The filtered data is displayed in a tabular format, and the feature distributions are shown as images, providing an easy-to-understand overview of the selected Iris species.
Use Case:
This project is especially useful for data scientists and students learning about data analysis, filtering, and visualization. By interacting with the Iris dataset, users can gain insights into how different Iris species vary in terms of their physical characteristics.
Future Enhancements:
Support for Multiple Species Selection: Allow users to select multiple species and compare feature distributions between them.
Additional Visualizations: Introduce scatter plots and box plots for further analysis of the relationships between features.
UI Improvements: Enhance the user interface for better responsiveness and aesthetics, especially for mobile devices.
Conclusion:
The Iris Species Data Filter and Visualization Web Application provides a seamless way to explore and visualize data. It combines the power of FastAPI for quick API interactions, Pandas for data manipulation, and Matplotlib for dynamic visualizations, all wrapped in a simple and intuitive web interface. This project serves as an excellent demonstration of how modern web technologies can be combined to create an interactive data analysis tool.
