*** Settings ***
Documentation    Suite description

*** Test Cases ***
Test title
    [Tags]    DEBUG
    First Keyword
    Second Keyword

Second Test Case
    [Tags]    Release
    MultiKeyword
    Second Keyword
    First Keyword

*** Keywords ***
First Keyword
    Sleep    3 seconds

Second Keyword
    Sleep    3 seconds

MultiKeyword
    First Keyword
    Second Keyword
