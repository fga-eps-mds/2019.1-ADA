## happy path
* greet
  - utter_greet
* mood_great
  - utter_usr_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* usr_happy
  - utter_usr_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_bye

## say goodbye
* bye
  - utter_bye

## intoduce_ada
* intoduce_ada
  - utter_intoduce_ada

# more_info?
* more_info?
  - utter_more_info?

## action path
* greet
  - utter_greet
* action_test
  - action_test
