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
### [Deployment](#deployment-1)
### [Bugs](#bugs-1)
### [Credits](#credits-1)
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
        * Update Stock Menu:
          * '1' -  The program will display all products one by one with a question asking how many pieces to add to the warehouse.
          * '2' - Displays all products individually with a question asking how many pieces were sent out.   
          * '3' - Selecting the third option will return you to the previous menu.
      * By selecting the option number 2  you can add another product to the list of products produced in Natures Oils, to do 
         this you need to follow some rules which will be displayed in the terminal:
        * Type and number of characters you can use when entering a new product name.
        * The right size, choose from the size list.
        * Appropriate barcode length.
      * Option 3  report options:
        * '1' - After selecting this option, the current stock status for each product will be displayed.
        * '2' - Total number of products produced for each of the list.
        * '3' - Total number of products sold.
        * '4' - Return to previous menu

### Data storage :
   * The app uses 'Google Sheets to store all data:
      * the application uses the information stored in the worksheets:
        * product list: 
        - ![Product List](/assets/images/product_list_worksheet.png)

   

---
## Technologies used in the project:

 * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
 ---
## Programs & Libraries Used in project:

 * [Gitpod](https://www.gitpod.io/)
    * To write the code.
 * [Github](https://github.com/)
    * Storing the files online.
 * [Heroku](https://heroku.com)
    * To deploy project.
 * [Am I Responsive](https://ui.dev/amiresponsive)
    * Screenshots for README.md file.
---
## Testing:

### Validation reports:
  * ![Valid](/assets/images/validator.png)

  * No errors.
  
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

### This app was deployed using Code Institute's mock terminal for Heroku

   #### Simple steps:

   * Fork or clone this repository
   * Create a new Heroku app
   * Set the build packs to Python and NodeJs in that order
   * Link the heroku app to the repository
   * Click on Deploy
   * Live "Natures Oils Stock System" app you can find by clicking this link:
     [heroku](https://naturesoilsstock-9ab4d188a6d6.herokuapp.com/)


## Bugs Detected:
  * 
  
## Unfixed Bugs:
  * All detected bugs have been fixed.

## Credits:
  *  To check the correct operation of most functions, the following was used:
     [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
  *  Google sheets to store data.
### Other:
   * Much of the information about python was obtained from https://www.w3schools.com/python/.
