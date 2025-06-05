Feature: Homepage hyperlink
  Description: Verify Homepage hyperlinks

  Rule: User click on homepage hyperlinks to verify
    Background:
      Given User sign in and enters valid email address, password
      When User clicks on sign in

    @Functional
    Scenario: Homepage hyperlinks in bottom navigation bar-01
      Given Home page is displayed
      When User clicks on "Notes" link
      Then Notes page is displayed in new tab
      When User clicks on "Write for us" link
      Then Write for us page is displayed in new tab
      When User clicks on "Subscribe" link
      Then Subscribe page is displayed in new tab
      And Logout


    Scenario: Homepage hyperlinks in bottom navigation bar-02
      Given Home page is displayed
      When User clicks on "Search Terms" link
      Then Search terms page is displayed in new tab
      When User clicks on "Privacy and Cookie policy" link
      Then Policy page is displayed in new tab
      When User clicks on "Advanced Search" link
      Then Advance search page is displayed in new tab
      And Logout

    Scenario: Homepage hyperlinks in user account section
      Given Home page is displayed
      When User expands account section
      Then Three sections are displayed
      When User clicks on "My Account" link
      Then User account page is displayed
      When User expands account section
      And Clicks on "My Wish List" link
      Then User wish list page is displayed
      And Logout

    Scenario: Homepage hyperlinks in top navigation bar-01
      Given Home page is displayed
      When User clicks on "What's New" link
      Then "What's new" page is displayed
      When User clicks on "Sale" link
      Then 'Sale' page is displayed
      When User expands training section
      And Click on video download
      Then Video download page is displayed
      And Logout

    Scenario: Homepage hyperlinks in top navigation bar-02 (Women)
      Given Home page is displayed
      When User mouse hover women section
      Then two sections tops and bottoms are displayed
      When When user mouse hover on "Tops" section
      Then four sub-sections "jackets", "hoodies & sweatshirts", "tees", "Bras & tanks" are displayed
      When When user mouse hover on "Bottoms" section
      Then two sub-sections "Pants", "Shorts" are displayed
      And Logout

    Scenario: Homepage hyperlinks in top navigation bar-03 (Men)
      Given Home page is displayed
      When User mouse hover men section
      Then two sections tops and bottoms are displayed
      When When user mouse hover on "Tops" section
      Then four sub-sections "jackets", "hoodies & sweatshirts", "tees", "Bras & tanks" are displayed
      When When user mouse hover on "Bottoms" section
      Then two sub-sections "Pants", "Shorts" are displayed
      And Logout

    Scenario: Homepage hyperlinks in top navigation bar-03 (Gear)
      Given Home page is displayed
      When User mouse hover gear section
      Then three sections "Bags", "Fiteness Equipment" and "Watches" are displayed
      And Logout




