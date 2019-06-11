## path_start
* start{"command": "start"}
  - action_start

## path_set_repository_github
* action_set_repository_github
  - action_set_repository_github

## path_set_repository_gitlab
* action_set_repository_gitlab
  - action_set_repository_gitlab

## path_create_issue
* start_create_issue
  - utter_start_issue
* issue_name
  - utter_issue_name
  - action_issue_name
* create_issue
  - action_create_issue

## path_comment_issue
* comment_issue
  - action_comment_issue

## path_help
* help{"command": "help"}
  - utter_help

## path_begin
* begin
  - utter_begin

## path_greetings
* greet
  - utter_greet

## path_greet_reply
* greet_reply
  - utter_greet_reply

## path_goodbye
* goodbye
  - utter_goodbye
  - utter_restart

## path_compliments
* compliments
  - utter_compliments_reply

## path_thanks
* thanks
  - utter_thanks

## path_who_is_ada
* who_is_ada
  - utter_who_is_ada

## path_religion
* religion
  - utter_religion

## path_who_am_i
* who_am_i
  - utter_who_am_i

## path_name_complete
* name_complete
  - utter_name_complete

## path_joke
* joke
  - utter_joke

## path_license
* license
  - utter_license

## path_good_night
* good_night
  - utter_good_night

## path_good_afternoon
* good_afternoon
  - utter_good_afternoon

## path_good_morning
* good_morning
  - utter_good_morning

## path_how_are_you
* how_are_you
  - utter_how_are_you

## path_user_affirms_something
* affirm
  - utter_affirm  

## path_marry_or_date
* marry_or_date
  - utter_marry_or_date

## path_sad
* sad
  - utter_sad

## path_creators
* creators
  - utter_creators

## path_action_get_report
* action_get_report
  - utter_start_report
  - action_get_report

## set_pipeline
* set_pipeline
  - action_set_pipeline

## path_next_release
* intended_for_next_release
  - utter_intended_for_next_release

## path_whats_pipeline
* whats_pipeline
  - utter_whats_pipeline

## path_adas_architecture
* adas_architecture
  - utter_adas_architecture

## path_rerun_pipeline
* rerun_pipeline
  - action_rerun_pipeline

## path_report_github
* action_get_report_github
  - utter_start_report
  - action_get_report_github

## path_contributor_issues
* action_get_issues_of_contributor
  - action_get_issues_of_contributor

## path_find_project_collaborators_basic
* find_project_collaborators
  - utter_find_project_collaborators
  - action_find_project_collaborators

## path_find_project_collaborators_sad
* find_project_collaborators
  - utter_find_project_collaborators
  - action_find_project_collaborators
* deny OR sad
  - utter_find_project_collaborators_sad

## path_find_project_collaborators_happy
* find_project_collaborators
  - utter_find_project_collaborators
  - action_find_project_collaborators
* affirm OR begin
  - utter_find_project_collaborators_happy

## path_find_project_collaborators_thanks
* find_project_collaborators
  - utter_find_project_collaborators
  - action_find_project_collaborators
* thanks
  - utter_find_project_collaborators_thanks
