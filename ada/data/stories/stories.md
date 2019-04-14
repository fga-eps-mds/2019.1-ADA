## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## path who_is_ada
* who_is_ada
  - utter_who_is_ada

## path_action_get_pipeline
* greet
  - utter_greet
* action_get_pipeline
  - action_get_pipeline

## path get_pipeline
* action_get_pipeline
  - action_get_pipeline