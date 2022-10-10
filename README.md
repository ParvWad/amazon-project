# Amazon-Discord-Project
 
# Goal: 
The goal for this project was to be able to have a script that can take user input and then scrape the amazon webage, and then store the data retrived in a csv file.    From there, the project was improved to be hosted on discord instead of a standalone python script. Lastly, the project was updated to work for voice based user input as well as text based user input.

# Usage:
![image](https://user-images.githubusercontent.com/73033647/194969168-bbfbde7e-475b-4e2e-b44f-41e47ce9b5bc.png)

Image above showcases a text based user input. User should input an amazon scrape command over text by using the following format, .amazon ____ where ____ is the object they would like to find the price off. The bot will find the amazon choice for this product and return its relavent information. If the object is not found/ an irrelavent object is found, then the bot will let the user know of the problem. 

![image](https://user-images.githubusercontent.com/73033647/194946793-d36947b3-460f-4178-9f99-dcb2cd1ef038.png)

Output displayed to user on Discord in the format of Price in first line. Name of the object found in the second line, and the url being reutrned last. All objects will be instantly added to the users "shopping list". 


![image](https://user-images.githubusercontent.com/73033647/194969288-c02f1f5c-469c-4a71-b269-f188130de3a3.png)

User Can direct bot to joining a voice channel by typing .join ____. Where ____ is the channel name the bot should join. In the event that the channel does not exist, the user will be informed of the problem and the bot will not join any channel.


![image](https://user-images.githubusercontent.com/73033647/194948093-638247e1-080d-446c-9f14-61b1a4b3681a.png)

A succsesfull invocation of the .join command will result in the bot joining a voice channel as shown, where it will wait for approximately 5 minutes before leaving. 
