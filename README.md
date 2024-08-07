# Naturest Oils Stock System

A small company producing sauces needs a simple, uncomplicated system to control the amount of products in the warehouse.
Basic tasks:

Adding manufactured products to the stock.

Recording the quantity and type of products shipped from the warehouse.

Adding new products to the main list.

Checking stock levels.

Checking total sales: product - quantity sold.

Checking the total number of manufactured products: product - quantity produced.



![Am_I_Responsive](/assets/images/responsive.png)

## Table of Contents

### [Stock System Structure](#stock-structure-1)
### [Features_coming_soon](#features-coming-soon)
### [Technologies_used_in_the_project](#technologies-used-in-the-project)
### [Programs_&_Libraries_Used_in_project](#programs--libraries-used-in-project)
### [Testing](#testing-1)
* [Validation_reports](#validation-reports)
* [Manual_Testing](#manual-testing)
* [Lighthouse_Testing](#lighthouse-testing)
### [Deployment](#deployment-1)
### [Bugs](#bugs-1)
### [Credits](#credits-1)
 * [Media](#media)
 * [Other](#other)
---

## Stock Structure:

### Main Menu:
![Main menu](/assets/images/main_menu.png) 
  * Main Menu Contains 4 options:
    * 1 - Update Stock.
    * 2 - Update Product List.
    * 3 - Stock Report.
    * 4 - Finish.

### Update Stock Menu:
![Update menu](/assets/images/update_stock_menu.png)
  * Update Stock Menu Contains 3 option:
   * 1 - Goods In
   * 2 - Goods Out
   * 3 - Return to Main Menu

### Report Menu:
  ![Report Menu](/assets/images/report_menu.png)
   * Report Contains 4 Options
      * 1 - Full Stock By Product.
      * 2 - Total Production.
      * 3 - Total Sale.
      * 4 - Return


## Features coming soon:

* Two levels of access:
  *  Administrator(manager)
  *  General User

* New stock reports:
  * To control raw materials usage.
---

## How to use :

 * Main menu :
    * From the main menu you can select 4 basic options after pressing the appropriate number on the keyboard and  
      pressing 'ENTER', the application will go to the next section or will exit the program(4).
       * After selecting option no. 1, the program will open a menu that will give you the option of updating stock levels.
        * 




       * By selecting the option number 2  you can add another product to the list of products produced in Natures Oils, to do 
         this you need to follow some rules which will be displayed in the terminal:
         * Type and number of characters you can use when entering a new product name.
         * The right size, choose from the size list.
         * Appropriate barcode length.
     
 * Functions :

    * Function startQuiz(quizType) 
      * A function that takes the value of the "quizType" variable and, 
      * depending on the selected category, calls the appropriate function that displays questions.
      * By adding an appropriate class, it hides unnecessary elements and displays elements with questions.

   * Function setQuestionsInRandomPositions() (this function is not in use any more)
      * Sets question numbers in random order and returns an array with these numbers.

   * Functions  loadGeoQuestions() and loadBioQuestions()
      * Invokes a function deselectAnswers() set all answers to unselected.
      * Take the first question from the geography/biology quiz and assigns it to a variable currentQuizData.
      * Displays question and answer changing 'innerText' property for each element.

   * Function deselectAnswers()
      * Unselect all selected answers.

   * Function function submitAnswer()
      * Function using property '.forEach' checks which answer has been selected and assigns the id value to the 'answer' variable.

   * Function displayScore(score, name)
      * The function takes two parameters 'score' - good answers and 'name' the player's name.
      * If the value of 'name' is an empty string, it sets the player's name to 'Player', otherwise it outputs the name provided by the user.
      * The next condition checks the number of correct answers and, depending on the result, displays the equivalent comment.

   * Function restartGame()  
     * function restarts the game(quiz).
     * Sets the necessary variables to the output values.
     * Hide all items and displays the Start section to start the game again.

   * Function cleareInput()  
     * A small function that sets the value of the element with id 'myInput'(user name input box) to an empty string. 

   * Function function randomQuestions()
     * Function responsible for displaying five of 10 questions in random order without repeating the questions..
     * Checks whether the numbers are not repeated.
     * Saves in a variable 'questionsRandomOrder' (array).
     * Returns an array with five numbers. 

---
## Technologies used in the project:

 * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
 ---
## Programs & Libraries Used in project:

 * [Gitpod](https://www.gitpod.io/)
    * To write the code.
 * [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Am I Responsive](https://ui.dev/amiresponsive)
    * Screenshots for README.md file.
---
## Testing:
 * In order to check whether the code does not contain errors, 



### Validation reports:
   
  


### Manual Testing:

<table>
  <tr>
    <th>User Choice</th>
    <th>Expected Action</th>
    <th>Result</th>
  </tr>
  <tr>
    <td>Choice 1</td>
    <td>Pass to next section</td>
    <td>After pressing 'Start' button game passing to section Choice category.</td>
  </tr>
  <tr>
    <td>Geography</td>
    <td>Start Geography quize, display questions.</td>
    <td>Geography questions displayed.</td>
  </tr>
  <tr>
    <td>Biology</td>
    <td>Start Biology quize, display questions.</td>
    <td>Biology questions displayed.</td>
  </tr>
  <tr>
    <td>Submit Answer</td>
    <td>After user set answer , passing to next question.</td>
    <td>Next question displayed.</td>
  </tr>
  <tr>
    <td>Restar Game</td>
    <td>Restart Quize , display fierst page and reset quiz.</td>
    <td>Game restart.</td>
  </tr>
</table>

## Deployment:

### The page was deployed on GitHub.com:

   #### Simple steps:

   * Log in to [Github](https://github.com/).
   * Live "Natures Oils Stock System" app you can find by clicking this link:
     [heroku](https://naturesoilsstock-9ab4d188a6d6.herokuapp.com/)
  
## Unfixed Bugs:
  * All detected bugs have been fixed.

## Credits:
  *  To check the correct operation of most functions, the following was used:
     [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
  * 
### Other:
   * Much of the information about python was obtained from https://www.w3schools.com/python/.
