Project Details
Puzzle: Escape Room

Soft skills analyzed: empathy, eye for detail, critical thinking, 
organizational skills, decision making, time management.
a) empathy - The user will be given a riddle: 'Until I am measured I am not known. \nYet 
how you miss me when I have flown.'. It checks if the user can understand the emotions
based on this riddle and can relate to the things lost, which will lead the user to the answer.

b) eye for detail - The user has to thoroughly look through the entire room to pick numbers which
checks how detailed the user is.

c) critical thinking - The user will be given a riddle which checks the user's ability to think

d) organizational skills - The combination of the door is divided into parts. The user will be given
a clue from where the user will be able to arrange the codes in order to get the final code.

e) decision making - The user has to make the right choice of the door to escape.

f) time management** - if the user completes the game in time, the user is fast
and can manage time well. [UNDER PROGRESS]


Puzzle Description: The main theme for analyzing the soft skills is based 
on an escape room. Mert and user[the user who will be playing] are room-mates.
Both were sleeping after a busy day. At some point of time user hears Mert's 
scream and goes to check but Mert was nowhere in the scene. The user gets a 
feeling of his life is at risk and wants to escape the room. The user finds Mert has
changed the lock combination for the door. As the user is thinking for the combination
he hears noises and wants to escape the room in a hurry. Mert has had left some clues
for the doors code combinations. Both of the doors have the same combination. The user has 
to find the right door to escape in time.


Dead ends:
i) Selecting the wrong door with the right code combination. Leads to a popup and the games end after
3 seconds.
ii) <Not implemeneted yet> A timer of 5 minutes to complete the puzzle.
Reason for not implementing: timeout_decorator error. For windows it was showing error. Working with
the signal module to implement this feature


Ways to solve:
i)Find the right key combination and select the right door to win the game


Steps:
i) I have used pygame, tkinter and pillow modules to build my project.
   for backend I have used mysql database. I have pymysql for python-mysql connectivity.
ii) My project has 4 python files. 
    a) selection.py - Shows if the user wants to enter as an admin or as an user.
       If the user selects admin then the user will be directed to adminLogin page and 
       if the user selects user then the user will be directed to userLogin page.
    b) adminLogin.py - Shows adminLogin page where the admin has to login with his/her 
       username and password. 
       The admin will have access to the mysql database, where he can view all the users registered.
       The admin can insert new users, delete existing users or update any existing user's details.
       [for deletion the admin can delete one user at a time. The admin needs to select the user
        he/she wants to delete.]
       The admin cannot update the softskill column as it will be updated after the user plays the game.
    c) userRegister.py - Any new user can register themselves.
    d) userLogin.py - The user can login and start playing to analyze their solfskills.
iii) I have used pictures from google. 
iv) I have taken help from google for building the project.

Language used: Python, mysql

work under progress: 
i) I am trying to implement flask for the cookie creation, so that the user can
start from his/her last saved point and for the restart game option.

ii) modifying to make the game run for a time limit using timeout_decorative module, time modules.