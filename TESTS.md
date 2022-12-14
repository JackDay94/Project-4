<h1 align="center">Manual Testing</h1>

## Home page/Navigation

| Test                   | Action                     | Expected result                                                                      | Result |
|------------------------|----------------------------|--------------------------------------------------------------------------------------|--------|
| Navbar Home            | Click link                 | Go to home page                                                                      | Pass   |
| Navbar logo            | Click logo                 | Go to home page                                                                      | Pass   |
| Navbar All Movies      | Click link                 | Go to All movies page                                                                | Pass   |
| Navbar Sign In         | Click link                 | Go to Sign in page                                                                   | Pass   |
| Navbar Register        | Click link                 | Go to register page                                                                  | Pass   |
| Authenticated user nav | Visible fields             | Profile and Add movie visible, Sign in becomes sign out, Register is hidden          | Pass   |
| Superuser nav          | Visible fields             | Admin field visible                                                                  | Pass   |
| Navbar Add movie       | Click link                 | Go to Add movie page                                                                 | Pass   |
| Navbar Profile         | Click link                 | Go to Profile page                                                                   | Pass   |
| Navbar Admin           | Click link                 | Go to Admin page                                                                     | Pass   |
| Navbar Sign Out        | Click link                 | Go to sign out page                                                                  | Pass   |
| Navbar Small screen    | Click Menu icon            | Expands to show all nav links, closes when clicked again                             | Pass   |
| Top rated movie        | Check top rated movie      | Top rated movie image, name and rating displayed                                     | Pass   |
| Highest rated movies   | Check highest rated movies | Top 4 highest rated movies after the top rated displayed with image, name and rating | Pass   |
| Latest Releases        | Check latest releases      | 4 Latest releases displayed with image, name and release date                        | Pass   |
| Latest Reviews         | Check latest reviews       | 4 Latest reviews displayed with movie name, rating, review author and created date   | Pass   |
| All movies button      | Click button               | Go to all movies page                                                                | Pass   |
| Footer facebook icon   | Click icon                 | Go to facebook in a new tab                                                          | Pass   |
| Footer twitter icon    | Click icon                 | Go to Twitter in a new tab                                                           | Pass   |
| Footer youtube icon    | Click icon                 | Go to Youtube in a new tab                                                           | Pass   |
| Footer instagram icon  | Click icon                 | Go to instagram in a new tab                                                         | Pass   |
| Movie image            | Click image                | Go to detail page of the movie that was clicked                                      | Pass   |

## All Movies page

| Test                  | Action                     | Expected result                                                                      | Result |
|-----------------------|----------------------------|--------------------------------------------------------------------------------------|--------|
| Movies display        | Check all movies           | All movies in the Movie model with approved=True are displayed                       | Pass   |
| Movies display        | Check movies               | All movies show an image or placeholder image and their name below them              | Pass   |
| Pagination            | Click pagination links     | Go between pages of movies                                                           | Pass   |
| Movie link            | Click Movie image          | Go to Detail page of movie that was clicked                                          | Pass   |
| Searchbar             | Search without any values  | Return a list of all approved movies                                                 | Pass   |
| Searchbar             | Search for "avatar"        | Return a list of all movies with "avatar" in their name, genre or director           | Pass   |
| Searchbar             | Search for "?"             | Return no movies and instead display text saying no matches were found               | Pass   |

## Movie Detail page

| Test                  | Action                             | Expected result                                                                                                | Result |
|-----------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------|--------|
| Movie image           | Check movie image displays         | Image for the selected movie should show                                                                       | Pass   |
| Movies name           | Check movie name displays          | Movie name appears directly below the movie image                                                              | Pass   |
| Movie Rating          | Check movie rating displays        | Movie rating appears directly below the movie name                                                             | Pass   |
| Movie Rating          | Check movie rating value           | Movie rating value is the average rating of user ratings for the movie                                         | Pass   |
| Movie Rating - No reviews          | Check movie rating value           | Movie rating value displays as 0 when no reviews are present                                                   | Pass   |
| Movie information     | Check movie information            | Movie genre, release date, director and age rating displays under the movie information heading and is correct | Pass   |
| Movie Summary         | Check movie summary                | Movie summary displays and is correct                                                                          | Pass   |
| Review form           | Check review form displays         | Review form displays when an authenticated user is signed in and is hidden when signed out                     | Pass   |
| Review form           | Submit form without review content | Form not submitted and message asking to fill in form displayed                                                | Pass   |
| Review form           | Subit form with review content     | Form is submitted, page is reloaded, success message is displayed, review is posted on movie detail page       | Pass   |
| Reviews               | Check reviews                      | Reviews are displayed correctly and show review author, rating, created date, edited date and review content   | Pass   |
| Reviews               | Check movie without reviews        | Review section will have no reviews and will instead display text saying 'no reviews'                          | Pass   |
| Reviews Edit button   | Click Edit button                  | Go to edit review page for selected review                                                                     | Pass   |
| Reviews Delete button | Click Delete button                | Go to delete review page for selected review                                                                   | Pass   |
| Reviews buttons       | Visible fields                     | Edit and delete review buttons only visible to the user who wrote the review and superuser                     | Pass   |
| Movies buttons        | Visible fields                     | Edit and delete movie buttons only visible to superuser                                                        | Pass   |
| Edit movie button     | Click Edit button                  | Go to edit movie page for selected movie                                                                       | Pass   |
| Delete movie button   | Click Delete button                | Go to delete movie page for selected movie                                                                     | Pass   |

## Add Movie page

| Test                  | Action                                               | Expected result                                                                                                                  | Result |
|-----------------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------|
| Add Movie Form        | Displays correctly                                   | Fields for name, genre, release date, director, age rating and summary displayed                                                 | Pass   |
| Add Movie Form        | Submit with no content                               | Form not submitted and message displayed asking to fill in content                                                               | Pass   |
| Add Movie Form        | Submit with only name                                | Form not submitted and message displayed asking to fill in content                                                               | Pass   |
| Add Movie Form        | Submit with name and release date                    | Form not submitted and message displayed asking to fill in content                                                               | Pass   |
| Add Movie Form        | Submit with name, release date and director          | Form not submitted and message displayed asking to fill in content                                                               | Pass   |
| Add Movie Form        | Submit with name, release date, director and summary | Form submitted, data added to the Movies model with the information submitted, redirect to home page and display success message | Pass   |
| Add Movie Form        | Submit with all fields filled                        | Form submitted, data added to the Movies model with the information submitted, redirect to home page and display success message | Pass   |

## Edit Movie page

| Test                  | Action                                               | Expected result                                                                                                                                                     | Result |
|-----------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Edit Movie Form       | Displays correctly                                   | Fields for name, genre, release date, director, age rating and summary displayed                                                                                    | Pass   |
| Edit Movie Form       | Prepopulated with content                            | All fields are prepopulated with content for the current movie being edited                                                                                         | Pass   |
| Edit Movie Form       | Submit with no content                               | Form not submitted and message displayed asking to fill in content                                                                                                  | Pass   |
| Edit Movie Form       | Submit with only name                                | Form not submitted and message displayed asking to fill in content                                                                                                  | Pass   |
| Edit Movie Form       | Submit with name and release date                    | Form not submitted and message displayed asking to fill in content                                                                                                  | Pass   |
| Edit Movie Form       | Submit with name, release date and director          | Form not submitted and message displayed asking to fill in content                                                                                                  | Pass   |
| Edit Movie Form       | Submit with name, release date, director and summary | Form submitted, data added to the Movies model with the information submitted, redirect to home page and display success message, movie updated with edited content | Pass   |
| Edit Movie Form       | Submit with all fields filled                        | Form submitted, data added to the Movies model with the information submitted, redirect to home page and display success message, movie updated with edited content | Pass   |

## Delete Movie page

| Test            | Action                                               | Expected result                                                                                                                                                      | Result |
|-----------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Movie details   | Displays correctly                                   | Movie name, image, genre, release date, director, age rating and summary displayed on page correctly                                                                 | Pass   |
| Delete button   | Click button                                         | Movie is deleted from the Movie model, redirect to home page and display a success message                                                                           | Pass   |

## Edit Review page

| Test             | Action                                               | Expected result                                                                                                                                                     | Result |
|------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Edit Review form | Displays correctly                                   | Rating and review content fields are displayed                                                                                                                      | Pass   |
| Edit Review form | Prepopulated                                         | Form is prepopulated with review content for the movie that the user has written                                                                                    | Pass   |
| Edit Review Form | Submit with no content                               | Form not submitted and message displayed asking to fill in content                                                                                                  | Pass   |
| Edit Review Form | Submit with all fields filled                        | Form submitted, review updated with new review data, redirect to home page and display success message                                                              | Pass   |

## Delete Review page

| Test             | Action                                               | Expected result                                                                                                                                                     | Result |
|------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Review details   | Displays correctly                                   | Full user review details for the corresponding movie are displayed                                                                                                  | Pass   |
| Delete button    | Click button                                         | Review is deleted from the review model and the movie page, redirects to home page and displays a success message                                                   | Pass   |

## Sign up page

| Test                         | Action                                 | Expected result                                                                                                                                                             | Result |
|------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Register form                | Displays correctly                     | Registration form shows username, email, password and password(again)                                                                                                       | Pass   |
| Register form invalid submit | Submit register form with invalid data | Form is not submitted and message displays telling user what went wrong and how to fix it                                                                                   | Pass   |
| Register form valid submit   | Submit register form with valid data   | Form submitted, new user created and added to user model, profile created and added to profile model, user signed in and redirected to home page, success message displayed | Pass   |
| Sign in link   | Click sign in link   | Go to sign in page | Pass   |

## Logout page

| Test                         | Action                                 | Expected result                                                                                                                                                             | Result |
|------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Logout button                | Click logout button                    | Logs the user out of their account, redirects to the home page and displays a success message                                                                               | Pass   |

## Login page

| Test                      | Action                              | Expected result                                                                           | Result |
|---------------------------|-------------------------------------|-------------------------------------------------------------------------------------------|--------|
| Login form                | Displays correctly                  | Displays the username and password fields for signing in                                  | Pass   |
| Login form invalid submit | Submit login form with invalid data | Form is not submitted and message displays telling user what went wrong and how to fix it | Pass   |
| Login form valid submit   | Submit login form with valid data   | User is logged into their account and redirected to home page with a success message      | Pass   |
| Sign up link              | Click sign up link                  | Go to sign up page                                                                        | Pass   |

## Profile page

| Test                    | Action                            | Expected result                                                                                                         | Result |
|-------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------|
| Profile form            | Displays correctly                | Displays the current user's username and Age, favourite genre and favourite director fields                             | Pass   |
| Profile form submit     | Submit profile form               | Form is submitted and updates fields in the profile model for the user, reloads the page and displays a success message | Pass   |