## story 0 happy path
* hello
  - utter_hello
  - utter_what_is_your_name
* username
  - action_username
* user_good
  - utter_user_good
  - utter_bot_asks_where_are_you_from
* bot_asks_where_are_you_from
  - action_birthplace
 
## story 0 unhappy path 
* hello
  - utter_hello
  - utter_what_is_your_name
* username
  - action_username
* user_sad
  - utter_user_sad
  - utter_bot_asks_where_are_you_from
* bot_asks_where_are_you_from
  - action_birthplace
 
## story 1
* age
  - utter_user_asks_age
  - utter_bot_asks_age
* bot_asks_age
  - action_userage
  
## story 2
* are_you_chatbot
  - utter_are_you_chatbot

## story 3
* bot_bad_working
  - utter_bot_bad_working
  - utter_bot_write_what_work_bad
* bot_write_what_work_bad
  
## story 4
* bot_be_better
  - utter_bot_be_better
  
## story 5
* bot_busy
  - utter_bot_busy
  
## story 6
* bot_good_working
  - utter_bot_good_working
  
## story 7
* bot_waits
  - utter_bot_waits

## story 8
* user_asks_how_are_you
  - utter_user_asks_how_are_you
  
## story 9
* bot_welcome
  - utter_bot_welcome
  
## story 10
* bye
  - utter_bye
  
## story 11 happy path
* good_evening
  - utter_good_evening
* user_good
  - utter_user_good
  
## story 11 unhappy path
* good_evening
  - utter_good_evening
* user_sad
  - utter_user_sad
  
## story 12
* good_morning
  - utter_good_morning
  
## story 13
* haha
  - utter_haha
  
## story 14
* nice_to_meet_you
  - utter_nice_to_meet_you
  
## story 15
* no
  - utter_no
  
## story 16
* right
  - utter_right
 
## story 17
* user_answer_my_question
  - utter_user_answer_my_question

## story 18
* user_asks_acquaintance
  - utter_user_asks_acquaintance
    
## story 19
* user_asks_boss
  - utter_user_asks_boss
  
## story 20
* user_asks_cancel
  - utter_user_asks_cancel
  
## story 21
* user_asks_here
  - utter_user_asks_here
  
## story 22
* user_asks_ready
  - utter_user_asks_ready
  
## story 23
* user_asks_sure
  - utter_user_asks_sure
  
## story 24
* user_asks_whatsup
  - utter_user_asks_whatsup
  
## story 25
* user_back
  - utter_user_back
  
## story 26
* user_busy
  - utter_user_busy
  
## story 27
* user_cannot_sleep
  - utter_user_cannot_sleep
  
## story 28
* user_does_not_want_to_talk
  - utter_user_does_not_want_to_talk
  
## story 29
* user_dont_care
  - utter_user_dont_care
  
## story 30
* user_excited
  - utter_user_excited
  
## story 31
* user_going_to_bed
  - utter_user_going_to_bed
 
## story 32
* user_happy
  - utter_user_happy
  
## story 33
* user_here
  - utter_user_here
  
## story 34
* user_joking
  - utter_user_joking
  
## story 35
* user_lonely
  - utter_user_lonely
  
## story 36
* user_look_like
  - utter_user_looks_like
  
## story 37
* user_says_annoying
  - utter_user_says_annoying
  
## story 38
* user_says_no_problem
  - utter_user_says_no_problem
  
## story 39
* user_says_sorry
  - utter_user_says_sorry
  
## story 40
* user_says_thank_you
  - utter_user_says_thank_you
  
## story 41
* user_sleepy
  - utter_user_sleepy
  
## story 42
* user_testing
  - utter_user_testing
  
## story 43
* user_tired
  - utter_user_tired
  
## story 44
* user_upset
  - utter_user_upset
  
## story 45
* user_waits
  - utter_user_waits
  
## story 46
* user_wants_to_talk
  - utter_user_wants_to_talk
  
## story 47
* user_will_be_back
  - utter_user_will_be_back

## story 48
* what_do_you_mean
  - utter_what_do_you_mean
  
## story 49
* wow
  - utter_wow
  
## story 50
* wrong
  - utter_wrong
  

## story 51
* user_asks_what_can_you_cook
  - utter_user_asks_what_can_you_cook
* give_example
  - utter_give_example
  
## story 52
* user_asks_music
  - utter_user_lovely_music
  - utter_bot_asks_music
* user_lovely_music
  - utter_user_good
  
## story 53
* bot_doesnt_sleep
  - utter_bot_doesnt_sleep
  
## story 54
* user_plays_instrument
  - utter_user_plays_instrument
  
## story 55
* user_asks_about_movies
  - utter_user_asks_about_movies
  - utter_bot_asks_about_movies
* users_lovely_movies
  - utter_user_good
  
## story 56
* user_asks_sport
  - utter_user_asks_sport
  - utter_bot_asks_sport
* bot_asks_sport
  - utter_sport_right
  - action_userlovelysport
  
## story 57
* user_what_is_your_name
  - utter_user_what_is_your_name
  
## story 58
* user_asks_do_you_have_family
  - utter_user_asks_do_you_have_family
  - utter_bot_do_you_have_family
* yes
  - utter_questions_about_family
  
## story 59
* user_asks_do_you_have_family
  - utter_user_asks_do_you_have_family
  - utter_bot_do_you_have_family
* no
  - utter_no
  
## story 60
* user_asks_tale
  - action_tale

## story 61
* user_asks_what_are_you_doing
  - utter_user_asks_what_are_you_doing
  
## story 62
* user_asks_and_you
  - utter_user_asks_and_you
  
## story 63
* user_angry
  - utter_user_angry
  
## story 64
* user_wants_to_play
  - utter_user_wants_to_play
  
## story 65
* user_asks_film_recommendation
  - utter_user_asks_film_recommendation
* film_genre
  - action_film
  
## story 66
* user_asks_music_recommendation
  - utter_user_asks_music_recommendation
* music_genre
  - action_music
  
## story 67
* user_asks_book_recommendation
  - utter_user_asks_book_recommendation
* book_genre
  - action_book
  
## story 68 happy path
* user_asks_language_knowledge
  - utter_user_asks_language_knowledge
* yes
  - action_translate
  
## story 68 unhappy path
* user_asks_language_knowledge
  - utter_user_asks_language_knowledge
* no
  
## story 69
* user_asks_about_weather
  - utter_user_asks_about_weather
  
## story 70
* user_asks_about_food
  - utter_user_asks_about_food
  - utter_bot_asks_about_food
* bot_asks_about_food
  - action_userlovelyfood
   
## story 71 happy
* user_asks_about_cooking
  - utter_user_asks_about_cooking
  - utter_bot_asks_about_cooking
* yes
  - utter_bot_asks_about_cooking_love
* bot_asks_about_cooking_love
  - utter_user_good

## story 72 unhappy
* user_asks_about_cooking
  - utter_user_asks_about_cooking
  - utter_bot_asks_about_cooking
* no
  - utter_bot_asks_about_cooking_hate
  
## story 73
* user_hates_his_work
  - utter_user_hates_his_work
  
## story 74
* user_hates_studying
  - utter_user_hates_studying
  
## story 75
* user_asks_birth_date
  - utter_user_asks_birthdate
  - utter_bot_asks_birthdate
* bot_asks_birthdate{"user_birthdate":"19.09.2018"}
  - action_userbirthdate
  
## story 76
* user_asks_help
  - utter_user_asks_help
  
## story 77
* user_asks_hobby
  - utter_user_asks_hobby
  - utter_bot_asks_hobby
* user_hobby
  - utter_user_good
  
## story 78
* user_asks_hungry
  - utter_user_asks_hungry

  
## story 79 happy path
* user_asks_what_can_do
  - utter_user_asks_what_can_do
* yes
  - utter_interesting_questions
* user_answer
  - utter_repeat
* yes
  - utter_interesting_questions
  
## story 80 unhappy path 1
* user_asks_what_can_do
  - utter_user_asks_what_can_do
* yes
  - utter_interesting_questions
* user_answer
  - utter_repeat
* no
  

## story 81 unhappy path 2
* user_asks_what_can_do
  - utter_user_asks_what_can_do
* no
  - utter_no
  
## story 82
* user_asks_what_do_you_do
  - utter_user_what_do_you_do
  - utter_what_do_you_do
* users_profession
  
## story 83
* user_asks_what_do_you_read
  - utter_user_asks_what_do_you_read
  - utter_bot_asks_what_do_you_read
* bot_asks_what_do_you_read

## story 84
* user_asks_where_are_you_from
  - utter_user_asks_where_are_you_from
  
## story 85
* user_asks_work_location
  - utter_user_asks_work_location
  
## story 86
* user_birthday
  - utter_user_birthday
  
## story 87 short
* user_bored
  - utter_user_bored
  
## story 88 long
* user_bored
  - utter_user_bored
* give_example
  - utter_suggestion

## story 89
* user_do_you_love_animals
  - utter_user_do_you_love_animals

## story 90
* user_asks_what_to_cook{"cooking":"легкие блюда"}
  - action_cooking
