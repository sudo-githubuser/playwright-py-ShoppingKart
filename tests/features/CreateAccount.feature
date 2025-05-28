Feature: Create Account
  Description: Creating account in shopping kart page

  Rule: Users can create a new account in shopping kart
    Background:
      Given User is on the home page
      When User navigates to create account page

    @End2End @Smoke @Regression
    Scenario: Create an account with valid and unique email ID
      When User fills the registration form with valid data
      And User submits the form
      Then User should see the account creation success message