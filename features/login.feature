# Created by Adrian Kupiec at 03.10.2018
Feature: sign in to e-mail account
  As a user I want to log in
  and check my e-mails

  Scenario:  Log in with valid data
    Given user is on Poczta Onet website
    When user fills in the Sign In form and submits it
    Then User can see email list