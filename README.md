# Projet-Velo-vViz

## INTRODUCTION

This project is carried out by three students of the École Centrale de Lyon during the subject of Data Visualization during the last semester of the university. The components are:

• Chamsedinne
• Salah
• Jon

The general objective of the project is to control the basic knowledge of the Javascript D3 library and create an application with a specific utility using the bases learned during the course.

## VELO'VIZ

The first phase of our project was the choice of data, in our case we went trought a city of Lyon page (https://data.grandlyon.com) where there are several dataset in open source about different elements of the city. Our idea, designed a priori during one of the classes, is that we wanted to use a Google maps and enter information on it and on the other hand we also wanted to enter data in real time.

Finally we chose the dataset of the Lyon bikes which, in addition to containing a lot of information, is updated every minute. This information comes in JSON format and contains more than 360 stations with all the characteristics (address, number of bikes available, neighborhood, identification number, etc ...)

The application therefore aims to serve both the citizen and the city council. The citizen can see the availability of bikes in real time and a prediction for the following hours and the city can draw conclusions from the visually represented history.

<table border="0" align="center">
  <tr>
    <td>
      <img src="img/Rapport.JPG" style="width: 100px;">
    </td>
  </tr>
</table>


## FUNCTIONALITIES

In this section we will explain in detail the different functionalities of the project. For this we will use screen captures and we will discuss how to interact with the screen.

First of all, we want to comment why we have chosen this layout. At first we had thought to divide the information and the map in different "div" like other groups have done. Finally, we thought it would be more visual to introduce the information on the map and allowing the user more flexibility. This way of arranging the elements caused us some problems of overlap but finnaly it allowed us to understand the language and also the DOM html.

### 1. General Information

The general information refers to everything that is displayed when you start the application. On the one hand we see all bike stations represented by a circle. This circle has a different size and color for each one depending on the information. The color is a degraded scale between red and green that indicates if the station is full (green), empty (red). The size of the circle is based on the size of the station, the larger circle being the larger the capacity.

In terms of zooming and scrolling the screen, the operation is the same as that of Google Maps, using the buttons at the top left or the mouse.

On the other hand, when we pass the mouse over a station there is a pop up that appears with basic information, name, address, number of bikes and number of seats. The box appears with an opacity transition and disappears in the same way when we remove the mouse.

Finally, if you click on the station, three new graphics appear. First a Pie Chart that indicates again the availability information but in percentage, and then a box that moves with a transition to the lower right corner that contains more detailed information. Finally there is a prediction chart that will be explained below.

<table border="0" align="center">
  <tr>
    <td>
      <img src="img/Rapport1.JPG" style="width: 100px;">
    </td>
  </tr>
</table>


### 2. Velov by neighborhood

This second functionality is more directed to the town Council or to someone who wants to draw conclusions from the given information. This allows us to see the number of bikes in each neighborhood at each moment as it is updated with the movement of the slide bar.

For example, Villeurbane is the largest neighborhood and also the furthest from the center. If we move the slide bar we realize that the number of bikes decreases in the morning and increases in the afternoon. This is due to work schedules, as many people move to the center and then come back for dinner at home. We have checked this with other neighborhoods and on weekends and the trend is even more exaggerated. This can serve as a method of decision when placing new stations or distributing bikes in the city.

The mode of use is by clicking on the "Arrondissement" button on the top left where a table with all the information appears as a transition, as we can see below. Clicking again the box disappears. The information is updated with the time change of the slide Bar.

<table border="0">
  <tr>
    <td>
      <img src="img/Rapport2.JPG" style="width: 100px;">
    </td>
  </tr>
</table>

Each of the number is the neighborhood, and VV is: Vaulx en Velin, V: Villeurbane. Here the map of Lyon.

<table border="0" align="center">
  <tr>
    <td>
      <img src="img/Rapport3.JPG" style="width: 100px;">
    </td>
  </tr>
</table>


### 3. Real-time script and slide bar
### 4. Bikes prediction
