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

### [User_Experience_(UX)](#user-experienceux)
* [User_expectations](#user-expectations)
### [Quiz Structure](#quiz-structure-1)

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


## User Experience(UX)
   <ul>
   <li>A small game created to test knowledge in various fields</li>
   <li>Due to limited time, it currently only has two categories: geography and biology</li>
   <li>The user can enter his name and then select the category in which he wants to test himself.</li>
   </ul>

 ### User expectations:

 * First-time users:
    * For every user, the most important thing is a simple and easy menu, as well as ease and smoothness of moving to subsequent sections of the quiz.

 * When visiting the website again:
    * The main goal should be to improve your result.

 * Frequent user goals
    * The main goal for each user should be to obtain the maximum number of points (correct answers).
    * Competition to be the best.
  - - -


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

* Minimum 6 categories.
* 100 questions in each category, 25 randomly selected for the quiz.
* Section displaying the top 10
---

## Java script structure :

 * EventListeners :
    * After DOM is loaded each button is getting Event Listener.

     * The conditional if statement checks which button was selected by the user by checking its id.

     * If the "Start" button has been pressed :
       * Section with id 'welcome' was hidden by adding a class 'invisible'.
       * Section with id 'choice_game' is displayed by deleting the class 'invisible'.
       * The username is taken and assigned to the variable.
       * The results variable is declared and gets its value from the function 'setQuestionsInRandomPositions()'.

     * In the quiz selection section there are two buttons 'Geography' and 'Biology'. Both of them call functions 'startQuize() 
       when clicked.

      * If the "Geography" is pressed :
       * 'select_game' set to invisible.
       * 'question_area' set to visible.
       * Button to submit bio quiz question set to 'invisible'.
       * Button to submit geo quiz question set to 'visible'.
       * The loadGeoQuestions() function is called and displays geography questions.

      * If the "Bilogogy" is pressed :
       * 'select_game' set to invisible.
       * 'question_area' set to visible.
       *  Button to submit geography quiz question set to 'invisible'.
       *  Button to submit biology quiz question set to 'visible'.
       *  The loadBioQuestions() function is called and displays biology questions.
       * After completing the quiz, a section giving the quiz result is displayed.

      * If the 'Reset Game' button is pressed:
       * Restarts the game and returns to the start page. 

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
 * [Google Fonts](https://fonts.google.com/)
    * Webside fonts, download links.
* [Am I Responsive](https://ui.dev/amiresponsive)
    * Screenshots for README.md file.
---
## Testing:
 * In order to check whether the code does not contain errors, they were used
   TW3C Markup Validator and W3C CSS Validator services.
   To check the correctness of the JS code, the jshint tool was used.


 * [jshint](https://jshint.com/)
 * [W3C Markup Validtor](https://validator.w3.org/)
 * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

### Validation reports:
   
   * HTML warning in W3C Markup Validator:
  ![warning_html](/assets/images/screenshots/html_warning.png)
  ![emplty_h2](/assets/images/screenshots/empty_he_element.png)

  * After solving the problem:
  ![html_no_warnings](/assets/images/screenshots/html_no_warnings.png)

  * W3C CSS Validator shows one error and one warning.
  ![css_error](/assets/images/screenshots/css_error.png)

  * After solving the problem:
  ![css_ok](/assets/images/screenshots/css_ok.png)

  * jshint found 37 warning in js code.
  ![jshint_test](/assets/images/screenshots/jshint_37warnings.png)

  * After solving the problem with most of the warnings, one remained
  ![jshint_warnings](/assets/images/screenshots/jshint_warnings.png)


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
   
 * One error was detected in the button testing process:
   * In the conditional statement : "if (answer === questionsBio[result[currentQuiz]].correctAnswer)" wrong value was entered.
   * Before the fix : questionsBio[currentQuiz].correctAnswer - Due to this bug, correct answers were incorrectly checked.
   * The correct value should be: questionsBio[result[currentQuiz]].correctAnswer , after this fix everything started working 
   properly.


* The website was tested on Google Chrome, Microsoft Edge.
* The website was tested  on a desctop 27" screen, laptop lenovo LOQ, and Samsung Galaxy S22 mobile phone.
* Dev Tools was used to test how the site looks on various screen sizes.

### Lighthouse testing:
   ![lighthouse](/assets/images/screenshots/lighthouse_desktop.png)
  
#### Mobile analysis
   ![lighthouse](/assets/images/screenshots/start_Lighthouse.png)
  

## Deployment:

### The page was deployed on GitHub.com:
   #### Simple steps:

   * Log in to [Github](https://github.com/).
   * In the upper left corner of the screen, click the menu next to your account name.
   * In the expanded menu in the repositories tab, select the appropriate repositories (Magda's cakes).
   * On the opened page, find "settings", then "pages".
   * Under "Source", click the dropdown menu "None" and select "Main".
   * Now you can clik in to "Save" button.
   * Page should automatically refresh.
   * Done, a link to the page should appear after some time.

   * Live "Gography or biology" webside you can find by clicking this link:
     https://krzysztofkadela.github.io/Geography-or-Biology/

    
## Unfixed Bugs:
   * During final testing, I discovered a few issues with displaying some elements on different screen sizes (responsive).
       * Most of them have been corrected but some problems still exist and need to be solved later

   * There is one more problem to solve, for functions declared within loops referencing an outer scoped variable.
       * Due to time constraints, the problem has not been resolved but will be corrected soon.
       * ![unfix_wornings](/assets/images/screenshots/unfix_worning.png)

## Credits:
    
 ### Media: 
   * Photos used in the project come from Pexels.com free photos https://www.pexels.com/.
   
### Other:
   * Much of the information about html css and javascript was obtained from https://www.w3schools.com/.
   * The idea for displaying questions in the quiz and some of the functions were taken (modified to adapt to this game) from a   YouTube tutorial: https://www.youtube.com/watch?v=CqddbIrEM5I.

   ## Acknowledgements:

 * Many thanks to my mentor Mitko Bachvarov for his helpful feedback.

