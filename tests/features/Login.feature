Feature: Login
  Description: Login with valid user credentials

  Rule: Users can login with valid user credentials
    Background:
      Given User is on the home page
      When User navigates to login page

    @End2End @Smoke @Functional @Regression
    Scenario: Login with valid user credentials
      Given User enters valid email address, password
      When User clicks on sign in
      Then Home page is displayed
      And User is logged out