# Created by Galac at 10/11/2024
Feature: Tests for community page

  Scenario: User can open the community page
    Given Open the main page soft
    Then Log in to the page
    And Click on the continue button
    And Click on settings option
    And Click on Community option
    When Verify the right page opens
    And Verify “Contact support” button is available and clickable


    
