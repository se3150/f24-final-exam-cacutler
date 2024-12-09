Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.
    Scenario: I can successfully encode a secret message
        Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
        # write your steps here
        When I add "test" to the inputfield "#letters"
        And I select the "2" option for element "#shift-amount"
        And I click on the button "#submit"
        Then I expect that element "#decoded_message p" contains the text "uftu"
    Scenario: I can successfully decode a secret message
        Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
        # write your steps here
        When I add "uftu" to the inputfield "#letters"