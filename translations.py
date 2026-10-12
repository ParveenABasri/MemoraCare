"""Internationalization (i18n) engine and localized datasets for MemoraCare.
Supports: English (en), Assamese (as), Bengali (bn), and Hindi (hi).
Featuring polite, emotionally comforting tone and voice guidance tailored for elderly dementia care.
"""
from __future__ import annotations

import random
from typing import Any

LANGUAGES = {
    "en": "🇬🇧 English",
    "as": "🇮🇳 অসমীয়া (Assamese)",
    "bn": "🇮🇳 বাংলা (Bengali)",
    "hi": "🇮🇳 हिन्दी (Hindi)",
}

SPEECH_VOICE_LANGS = {
    "en": "en-IN",
    "as": "as-IN",
    "bn": "bn-IN",
    "hi": "hi-IN",
}

TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": {
        # Sidebar & General
        "app_title": "MemoraCare",
        "app_subtitle": "NER cognitive companion",
        "role_label": "I am using this as",
        "role_patient": "Patient",
        "role_caregiver": "Caregiver",
        "language_label": "Language / ভাষা / भाषा",
        "local_date_label": "Local date",
        "offline_notice_title": "Offline-first prototype",
        "offline_notice_body": "Gameplay, scores, reminders, and AI recommendations stay on this device.",
        "btn_back_to_activities": "← Back to Activities",
        "btn_find_home_sidebar": "🏠 Find My Way Home",
        "btn_return_dashboard": "← Return to Dashboard",
        "hero_eyebrow": "MemoraCare · NER memory companion",
        "hero_heading": "Good day, let us take it gently.",
        "hero_subheading": "Choose one small activity. There is no rush at all.",
        "hero_greeting_audio": "Good day to you, my dear friend. Let us take today very gently and comfortably. Choose any small activity that you like. There is no rush at all.",
        "find_home_banner_title": "🏠 Find My Way Home",
        "find_home_banner_sub": "See your distance and direction to home, or call your caregiver with one tap.",
        "find_home_banner_btn": "🏠 Open Find My Way Home (Direction & Help) →",
        "choose_activity": "Choose a gentle activity",
        "tab_card_pairs": "Card pairs",
        "tab_sequence": "Sequence",
        "tab_object_match": "Object match",
        "tab_brain_exercise": "Brain exercise",
        
        # Voice Common UI
        "voice_listen_aloud": "🔊 Listen Aloud",
        "voice_listen_greeting": "🔊 Listen with Gentle Voice",
        "voice_listen_reminders": "🔊 Listen to Today's Reminders",
        "voice_reminders_spoken_intro": "Here is your gentle reminder for today. You have {count} items scheduled: {items}. Please take good care.",
        "voice_reminders_none": "You have no reminders scheduled for today. Please relax and have a peaceful time.",
        "voice_speak_brain_question": "🔊 Listen to Question & Choices",
        "voice_mic_btn": "🎙️ Speak Your Answer",
        "voice_mic_listening": "🎙️ Listening gently... Please speak your answer clearly.",
        "voice_mic_heard": "🎙️ Heard: \"{text}\"",
        "voice_mic_matched": "✅ Selected: {choice}",
        "voice_mic_no_match": "💡 Heard: \"{text}\". Please tap your answer or speak again.",
        "voice_caregiver_summary": "🔊 Listen to Patient Activity Summary",
        "voice_caregiver_spoken": "Here is the summary. The patient has completed {count} activities with an average accuracy of {acc} percent. Completed rate is {comp} percent.",
        "audio_not_supported": "Voice audio is not supported in this browser.",
        "mic_not_supported": "Voice microphone input is not supported in this browser.",

        # Reminders Panel
        "reminders_heading": "Today's reminders",
        "no_reminders": "No reminders yet.",
        "reminder_status_done": "Done",
        "reminder_status_now": "Now",
        "reminder_type_medication": "Medication",
        "reminder_type_meal": "Meal",
        "reminder_type_game": "Game session",
        "reminder_type_appointment": "Appointment",
        
        # Progress & Analytics
        "progress_heading": "Progress",
        "progress_empty": "Complete an activity to see progress here.",
        "metric_activities": "Activities",
        "metric_avg_accuracy": "Average accuracy",
        "metric_completed": "Completed",
        "chart_daily_accuracy": "Daily accuracy trend",
        "chart_activity_accuracy": "Accuracy by activity",
        
        # Card Pairs Game
        "pairs_title": "Find the matching pairs",
        "difficulty_level": "Difficulty Level",
        "level_easy": "Easy",
        "level_medium": "Medium",
        "level_hard": "Hard",
        "pairs_caption_easy": "3 pairs · 6 cards",
        "pairs_caption_medium": "5 pairs · 10 cards",
        "pairs_caption_hard": "8 pairs · 16 cards",
        "pairs_instruction": "Flip two cards to find matching pairs.",
        "pairs_mismatch": "Those cards do not match. Take your time, choose another card.",
        "pairs_matched_status": "Matched: {matched} of {total} pairs · Attempts: {attempts}",
        "pairs_win_msg": "🎉 Wonderful! You found every pair with patience in {attempts} attempts.",
        "ai_recommendation_msg": "AI difficulty engine ran on this score. Recommended next difficulty: **{rec}**.",
        "btn_play_next_level": "Play next ({level}) →",
        "btn_replay_same": "Replay {level} with fresh cards",
        
        # Sequence Game
        "sequence_title": "Remember the sequence",
        "seq_caption_easy": "3 items · Gentle",
        "seq_caption_medium": "5 items · Standard",
        "seq_caption_hard": "7 items · Challenge",
        "seq_show_instruction": "Look at each item carefully. There is no rush. Press **Next item** when you are ready.",
        "seq_item_counter": "Item {curr} of {total} · Round {round_num}",
        "btn_next_item": "Next item →",
        "btn_ready_recall": "Ready to recall sequence →",
        "btn_review_start": "Review from start",
        "seq_answer_instruction": "Tap the items below in the exact order you saw them.",
        "seq_selected_status": "Selected {count} of {total} items · *{remaining} more needed*",
        "seq_all_selected": "All {total} items selected! Ready to check.",
        "seq_no_items_yet": "No items tapped yet. Tap the buttons below in order.",
        "btn_undo_last": "Undo last",
        "btn_clear_answer": "Clear answer",
        "btn_check_sequence": "Check sequence",
        "seq_round_success": "✨ Excellent! You remembered Round {round_num} beautifully.",
        "seq_round_take_time": "Take a calm breath. When you feel ready for the next sequence, click the button below.",
        "btn_begin_next_round": "Begin next round →",
        "seq_win_msg": "🎉 Wonderful! You completed all 3 sequence rounds in {attempts} attempt(s).",
        "seq_fail_msg": "A lovely effort. You successfully completed {rounds} round(s). Take it gently.",
        "seq_was_msg": "The sequence was: **{expected}**",
        "btn_replay_seq_same": "Replay {level} with fresh sequence",
        
        # Object Match Game
        "object_title": "Connect the Companions",
        "object_caption_easy": "3 pairs · Gentle",
        "object_caption_medium": "5 pairs · Everyday Life",
        "object_caption_hard": "7 pairs + Distractor",
        "object_instruction": "Match each object on the Left with its companion on the Right.",
        "object_how_to": "💡 **How to play:** 1. Tap an object on the **Left** to choose it. 2. Then tap its partner on the **Right** to connect them.",
        "object_left_header": "1. Starting Objects",
        "object_right_header": "2. Companion Partners",
        "object_selected_banner": "👉 **Selected:** {name} · *Now choose its matching partner on the right!*",
        "object_please_select_left": "👉 Please tap an item on the Left first!",
        "object_match_success": "✨ Wonderful connection! {left} pairs with {right} ({explanation}).",
        "object_win_msg": "🎉 Wonderful! You connected all {total} companion pairs in {attempts} attempts!",
        "object_connected_header": "🏆 Connected Companions",
        "btn_replay_obj_same": "Replay {level} with fresh companions",
        
        # Brain Exercises
        "brain_title": "A gentle brain exercise",
        "brain_caption_easy": "Gentle math & categories",
        "brain_caption_medium": "Market math & analogies",
        "brain_caption_hard": "Multi-step reasoning & patterns",
        "brain_sub_instruction": "Enjoy short, playful questions. You can also tap the microphone to speak your answer.",
        "brain_question_counter": "Question {curr} of {total} · {cat}",
        "brain_choose_prompt": "Choose your answer:",
        "btn_check_answer": "Check answer",
        "btn_continue_exercise": "Continue to next exercise →",
        "brain_correct_msg": "Wonderful! That is exactly right: {ans}. Great job!",
        "brain_incorrect_msg": "A very sweet try! The answer is {ans}. You are doing wonderfully, take it gently.",
        "brain_win_msg": "🎉 Brain exercises complete: {correct}/{total} correct! You did great.",
        "btn_replay_brain_same": "Replay {level} with fresh questions",
        
        # Find My Way Home & Compass
        "nav_page_caption": "MemoraCare · Gentle Home Navigation Assistance · Offline-First",
        "nav_mode_label": "Location Mode",
        "nav_mode_sim": "🧪 Demo Simulation Presets (Offline)",
        "nav_mode_manual": "✍️ Manual GPS Coordinates",
        "nav_mode_gps": "📡 Browser / Device GPS",
        "nav_sim_prompt": "Choose a demo scenario to test guidance:",
        "nav_sim_close": "🟢 Very Close to Home (~35m) · At the doorstep",
        "nav_sim_park": "🟡 Nearby Park (~320m) · Short neighborhood walk",
        "nav_sim_market": "🟠 Daily Bazaar / Market (~850m) · Few streets away",
        "nav_sim_far": "⚠️ Further Away (~2.4 km) · Across town",
        "nav_lat_input": "Your Current Latitude",
        "nav_lon_input": "Your Current Longitude",
        "nav_gps_acquired": "📡 Device GPS acquired: {lat:.5f}° N, {lon:.5f}° E",
        "nav_gps_requesting": "📡 Requesting device GPS coordinates via your browser... (If prompted, please tap 'Allow')",
        "nav_gps_fallback": "*(Using local fallback while GPS resolves)*",
        "compass_title": "🧭 Compass Direction to Home",
        "compass_direction_prompt": "Face {heading} ({bearing}°) to walk towards Home",
        "compass_instruction": "Keep the dark green pointer facing forward in your hand as you walk.",
        "btn_listen_audio": "🔊 Tap to Listen to Directions Aloud",
        "btn_call_caregiver": "📞 CALL CAREGIVER: {name} ({phone})",
        "home_info_title": "🏡 Your Home Information",
        "home_info_address": "Address:",
        "home_info_landmark": "Landmark:",
        "home_info_coords": "Coordinates:",
        "passerby_card_title": "🤝 Show to a Passerby / Helper",
        "passerby_card_text": '"Hello! I am looking for my home. If I seem lost, please help me reach: {address}, or call my family: {phone}."',
        "passerby_card_note": "Note:",
        
        # Navigation Guidance Statuses
        "nav_at_home_title": "🟢 You are right by your Home!",
        "nav_at_home_dist": "{dist} meters (Within steps of home)",
        "nav_at_home_guidance": "Look around you — you are safe and back at your doorstep. Welcome home!",
        "nav_at_home_advice": "You can relax and breathe easy. There is no need to walk any further.",
        
        "nav_near_home_title": "🟡 You are near your home",
        "nav_near_home_dist": "~{dist} meters away (About 3 to 5 minutes walk)",
        "nav_near_home_guidance": "Walk gently towards the {heading}. Look out for your familiar lane and green gate.",
        "nav_near_home_advice": "Take your time and follow the arrow. If you feel tired, please sit down or call your caregiver.",
        
        "nav_mod_dist_title": "🟠 You are a little further from home",
        "nav_mod_dist_dist": "~{dist:.2f} km away",
        "nav_mod_dist_guidance": "Your home is towards the {heading}. It may take a longer walk.",
        "nav_mod_dist_advice": "Consider showing your Helper Card to a kind neighbor or shopkeeper, or tap the button below to call your family.",
        
        "nav_far_title": "⚠️ You are outside your usual neighborhood",
        "nav_far_dist": "~{dist:.1f} km away",
        "nav_far_guidance": "Please stay in a safe, visible, and comfortable spot (such as a nearby tea stall or shop).",
        "nav_far_advice": "Tap the large Call Caregiver button below right now so your family can come meet you with love.",
        
        # Caregiver View
        "cg_title": "Caregiver dashboard",
        "cg_subtitle": "A calm snapshot of recent activity. All information is stored on this device.",
        "cg_recent_activity": "Recent activity",
        "cg_no_activity": "No activity recorded yet.",
        "cg_reminder_status": "Reminder status",
        "btn_edit": "Edit",
        "btn_delete": "Delete",
        "reminder_form_title": "Reminder name",
        "reminder_form_type": "Type",
        "reminder_form_time": "Time (HH:MM)",
        "reminder_form_notes": "Note",
        "btn_save_changes": "Save changes",
        "expander_add_reminder": "Add a reminder",
        "btn_save_reminder": "Save reminder",
        "reminder_saved_msg": "Reminder saved on this device.",
        "cg_home_settings_heading": "🏠 Patient Home & Emergency Contact Settings",
        "cg_home_settings_caption": "Configure the patient's home coordinates, landmarks, and emergency contact phone number stored locally in SQLite.",
        "cg_input_home_label": "Home Label / Name",
        "cg_input_address": "Home Street Address",
        "cg_input_landmark": "Familiar Landmark (visible to patient)",
        "cg_input_lat": "Home Latitude (GPS)",
        "cg_input_lon": "Home Longitude (GPS)",
        "cg_input_cg_name": "Caregiver Name",
        "cg_input_cg_phone": "Caregiver Phone Number (for Emergency Call)",
        "cg_input_note": "Emergency Note (shown on Passerby Helper Card)",
        "btn_save_home_settings": "Save Home & Emergency Settings",
        "msg_home_saved": "✅ Home location and caregiver contact details successfully saved to SQLite!",
    },
    
    "as": {
        # Sidebar & General
        "app_title": "মেমোৰাকেয়াৰ",
        "app_subtitle": "উত্তৰ-পূৰ্বাঞ্চল স্মৃতি সংগী",
        "role_label": "মই ব্যৱহাৰ কৰিছোঁ:",
        "role_patient": "ৰোগী / জ্যেষ্ঠ ব্যক্তি",
        "role_caregiver": "যত্নদাতা (Caregiver)",
        "language_label": "ভাষা / Language",
        "local_date_label": "স্থানীয় তাৰিখ",
        "offline_notice_title": "অফলাইন প্ৰট'টাইপ",
        "offline_notice_body": "সকলো খেল, স্ক'ৰ, সোঁৱৰণী আৰু এআই পৰামৰ্শ এই যন্ত্ৰটোতে সংৰক্ষিত থাকে।",
        "btn_back_to_activities": "← কাৰ্যকলাপলৈ উভতি যাওক",
        "btn_find_home_sidebar": "🏠 ঘৰৰ দিশ আৰু সহায়",
        "btn_return_dashboard": "← মুখ্য পৃষ্ঠালৈ উভতি যাওক",
        "hero_eyebrow": "মেমোৰাকেয়াৰ · উত্তৰ-পূৰ্বাঞ্চল স্মৃতি সংগী",
        "hero_heading": "নমস্কাৰ, শান্তভাৱে আৰু আৰামেৰে আৰম্ভ কৰোঁ আহক।",
        "hero_subheading": "যিকোনো এটা সৰু কাৰ্য বাছি লওক। কোনো খৰখেদা নাই।",
        "hero_greeting_audio": "নমস্কাৰ, আপোনাক আন্তৰিক স্বাগতম। আজিৰ দিনটো শান্তভাৱে আৰু আৰামেৰে কটাওক। যিকোনো এটা সৰু খেল বাছি লওক, কোনো খৰখেদা নাই।",
        "find_home_banner_title": "🏠 ঘৰলৈ বাট বিচাৰক",
        "find_home_banner_sub": "ঘৰৰ দূৰত্ব আৰু দিশ চাওক, বা এক টিপতে আপোনাৰ পৰিয়ালক ফোন কৰক।",
        "find_home_banner_btn": "🏠 ঘৰৰ দিশ আৰু সহায় চাওক →",
        "choose_activity": "এটা মনোৰম কাৰ্য বাছক",
        "tab_card_pairs": "কাৰ্ড যোৰা মিলোৱা",
        "tab_sequence": "ক্ৰম মনত ৰখা",
        "tab_object_match": "সংগী বস্তু মিলোৱা",
        "tab_brain_exercise": "মগজুৰ ব্যায়াম",
        
        # Voice Common UI
        "voice_listen_aloud": "🔊 স্পষ্টকৈ শুনক",
        "voice_listen_greeting": "🔊 মৰমৰ মাতেৰে শুনক",
        "voice_listen_reminders": "🔊 আজিৰ সোঁৱৰণীসমূহ শুনক",
        "voice_reminders_spoken_intro": "আজি আপোনাৰ {count} টা মৰমৰ সোঁৱৰণী আছে: {items}। অনুগ্ৰহ কৰি নিজৰ যত্ন ল'ব।",
        "voice_reminders_none": "আজিৰ বাবে কোনো সোঁৱৰণী নাই। আপুনি আৰামেৰে আৰু শান্তভাৱে সময় কটাওক।",
        "voice_speak_brain_question": "🔊 প্ৰশ্ন আৰু বিকল্পবোৰ শুনক",
        "voice_mic_btn": "🎙️ মুখেৰে উত্তৰ কওক",
        "voice_mic_listening": "🎙️ শুনি থকা হৈছে... অনুগ্ৰহ কৰি স্পষ্টকৈ উত্তৰ কওক।",
        "voice_mic_heard": "🎙️ ধৰা পৰিল: \"{text}\"",
        "voice_mic_matched": "✅ বাছনি কৰা হ'ল: {choice}",
        "voice_mic_no_match": "💡 ধৰা পৰিল: \"{text}\"। অনুগ্ৰহ কৰি পুনৰ কওক বা বিকল্প বাছক।",
        "voice_caregiver_summary": "🔊 ৰোগীৰ অগ্ৰগতিৰ সাৰাংশ শুনক",
        "voice_caregiver_spoken": "ৰোগীয়ে {count} টা কাৰ্য সম্পন্ন কৰিছে, যাৰ গড় শুদ্ধতা {acc} শতাংশ আৰু সম্পূৰ্ণতা {comp} শতাংশ।",
        "audio_not_supported": "আপোনাৰ ব্ৰাউজাৰে মাত সমৰ্থন নকৰে।",
        "mic_not_supported": "আপোনাৰ ব্ৰাউজাৰে মাইক্ৰ'ফোন ইনপুট সমৰ্থন নকৰে।",

        # Reminders Panel
        "reminders_heading": "আজিৰ সোঁৱৰণীসমূহ",
        "no_reminders": "বৰ্তমান কোনো সোঁৱৰণী নাই।",
        "reminder_status_done": "সম্পূৰ্ণ",
        "reminder_status_now": "বৰ্তমান",
        "reminder_type_medication": "ঔষধ",
        "reminder_type_meal": "আহাৰ",
        "reminder_type_game": "মগজুৰ অনুশীলন",
        "reminder_type_appointment": "চিকিৎসক / সাক্ষাৎ",
        
        # Progress & Analytics
        "progress_heading": "দৈনিক প্ৰগতি",
        "progress_empty": "প্ৰগতি চাবলৈ যিকোনো এটা কাৰ্য সম্পূৰ্ণ কৰক।",
        "metric_activities": "মুঠ কাৰ্য",
        "metric_avg_accuracy": "গড় শুদ্ধতা",
        "metric_completed": "সম্পূৰ্ণতা",
        "chart_daily_accuracy": "দৈনিক শুদ্ধতাৰ লেখচিত্র",
        "chart_activity_accuracy": "কাৰ্য অনুসৰি শুদ্ধতা",
        
        # Card Pairs Game
        "pairs_title": "মিলা কাৰ্ডযোৰ বিচাৰি উলিওৱক",
        "difficulty_level": "কঠিনতাৰ স্তৰ",
        "level_easy": "সহজ (Easy)",
        "level_medium": "মধ্যম (Medium)",
        "level_hard": "কঠিন (Hard)",
        "pairs_caption_easy": "৩ যোৰা · ৬ খন কাৰ্ড",
        "pairs_caption_medium": "৫ যোৰা · ১০ খন কাৰ্ড",
        "pairs_caption_hard": "৮ যোৰা · ১৬ খন কাৰ্ড",
        "pairs_instruction": "দুখনকৈ কাৰ্ড লুটিয়াই মিলা ছবি বা শব্দ বিচাৰি লওক।",
        "pairs_mismatch": "কাৰ্ড দুখন মিলা নাই। কোনো চিন্তা নকৰিব, আন এখন কাৰ্ড চুই দিয়ক।",
        "pairs_matched_status": "মিলিল: {total} যোৰাৰ ভিতৰত {matched} যোৰা · প্ৰচেষ্টা: {attempts}",
        "pairs_win_msg": "🎉 বৰ সুন্দৰ! আপুনি ধৈৰ্য্যৰে {attempts} টা প্ৰচেষ্টাত সকলো যোৰা বিচাৰি পালে।",
        "ai_recommendation_msg": "AI ইঞ্জিনে আপোনাৰ স্ক'ৰ বিশ্লেষণ কৰিলে। পৰৱৰ্তী স্তৰৰ পৰামৰ্শ: **{rec}**.",
        "btn_play_next_level": "পৰৱৰ্তী স্তৰ খেলক ({level}) →",
        "btn_replay_same": "নতুন কাৰ্ডৰ সৈতে {level} পুনৰ খেলক",
        
        # Sequence Game
        "sequence_title": "বস্তুৰ ক্ৰম মনত ৰাখক",
        "seq_caption_easy": "৩ টা বস্তু · শান্ত",
        "seq_caption_medium": "৫ টা বস্তু · মধ্যম",
        "seq_caption_hard": "৭ টা বস্তু · প্ৰত্যাহ্বান",
        "seq_show_instruction": "প্ৰতিটো বস্তু ভালদৰে লক্ষ্য কৰক। কোনো খৰখেদা নাই। সাজু হ'লে **পৰৱৰ্তী বস্তু** টিপক।",
        "seq_item_counter": "বস্তু {curr} / {total} · পৰ্যায় {round_num}",
        "btn_next_item": "পৰৱৰ্তী বস্তু →",
        "btn_ready_recall": "ক্ৰম ক'বলৈ সাজু →",
        "btn_review_start": "আৰম্ভণিৰ পৰা পুনৰ চাওক",
        "seq_answer_instruction": "আপুনি দেখা ক্ৰমত তলৰ বুটামবোৰ একাদিক্ৰমে চুই দিয়ক।",
        "seq_selected_status": "{total} টাৰ ভিতৰত {count} টা বাছিলে · *আৰু {remaining} টা প্ৰয়োজন*",
        "seq_all_selected": "সকলো {total} টা বস্তু বাছনি হ'ল! পৰীক্ষা কৰিবলৈ সাজু।",
        "seq_no_items_yet": "এতিয়ালৈ কোনো বস্তু বাছনি কৰা হোৱা নাই।",
        "btn_undo_last": "শেষৰটো বাতিল কৰক",
        "btn_clear_answer": "সকলো মচক",
        "btn_check_sequence": "ক্ৰম পৰীক্ষা কৰক",
        "seq_round_success": "✨ চমৎকার! আপুনি {round_num} নং পৰ্যায় বৰ ধুনীয়াকৈ মনত ৰাখিলে।",
        "seq_round_take_time": "আৰাম কৰক। সাজু হ'লে পৰৱৰ্তী ক্ৰমৰ বাবে তলৰ বুটাম টিপক।",
        "btn_begin_next_round": "পৰৱৰ্তী পৰ্যায় আৰম্ভ কৰক →",
        "seq_win_msg": "🎉 বৰ আনন্দৰ কথা! আপুনি ৩ টা পৰ্যায় {attempts} টা প্ৰচেষ্টাত সফলভাৱে সম্পূৰ্ণ কৰিলে।",
        "seq_fail_msg": "বৰ মৰম লগা প্ৰচেষ্টা! আপুনি {rounds} টা পৰ্যায় শুদ্ধকৈ সম্পূৰ্ণ কৰিলে। আৰামেৰে লওক।",
        "seq_was_msg": "শুদ্ধ ক্ৰম আছিল: **{expected}**",
        "btn_replay_seq_same": "নতুন ক্ৰমৰ সৈতে {level} পুনৰ খেলক",
        
        # Object Match Game
        "object_title": "সংগী বস্তু মিলোৱা",
        "object_caption_easy": "৩ যোৰা · সহজ",
        "object_caption_medium": "৫ যোৰা · দৈনন্দিন জীৱন",
        "object_caption_hard": "৭ যোৰা + অতিৰিক্ত বিকল্প",
        "object_instruction": "বাওঁফালৰ প্ৰতিটো বস্তুৰ লগত সোঁফালৰ উপযুক্ত সংগী মিলাওক।",
        "object_how_to": "💡 **কেনেদৰে খেলিব:** ১. বাওঁফালৰ এটা বস্তু টিপি বাছক। ২. তাৰ পিছত সোঁফালৰ সংগী বস্তুটো টিপি সংযোগ কৰক।",
        "object_left_header": "১. মূল বস্তুসমূহ",
        "object_right_header": "২. সংগী বস্তুবোৰ",
        "object_selected_banner": "👉 **বাছনি কৰা হৈছে:** {name} · *এতিয়া সোঁফালৰ পৰা ইয়াৰ লগৰীয়া বাছক!*",
        "object_please_select_left": "👉 প্ৰথমে বাওঁফালৰ এটা বস্তু বাছি লওক!",
        "object_match_success": "✨ বৰ সুন্দৰ মিল! {left} আৰু {right} একেলগে ব্যৱহাৰ হয় ({explanation})।",
        "object_win_msg": "🎉 অতি উত্তম! আপুনি {attempts} টা প্ৰচেষ্টাত সকলো {total} যোৰা সংগী মিলালে!",
        "object_connected_header": "🏆 মিলি যোৱা সংগীসমূহ",
        "btn_replay_obj_same": "নতুন বস্তুৰ সৈতে {level} পুনৰ খেলক",
        
        # Brain Exercises
        "brain_title": "মগজুৰ শান্ত ব্যায়াম",
        "brain_caption_easy": "সহজ অংক আৰু চিনাকি বস্তু",
        "brain_caption_medium": "দৈনন্দিন হিচাপ আৰু উপমা",
        "brain_caption_hard": "যুক্তিমূলক চিন্তা আৰু আৰ্হি",
        "brain_sub_instruction": "চুটি আৰু আনন্দদায়ক প্ৰশ্নৰ উত্তৰ দিয়ক। আপুনি মাইক্ৰ'ফোন টিপি মুখেৰেও উত্তৰ ক'ব পাৰে।",
        "brain_question_counter": "প্ৰশ্ন {curr} / {total} · {cat}",
        "brain_choose_prompt": "আপোনাৰ উত্তৰ বাছক:",
        "btn_check_answer": "উত্তৰ পৰীক্ষা কৰক",
        "btn_continue_exercise": "পৰৱৰ্তী প্ৰশ্নলৈ যাওক →",
        "brain_correct_msg": "বৰ সুন্দৰ! উত্তৰ একেবাৰে সঠিক: {ans}। বহুত ভাল উত্তৰ দিলে!",
        "brain_incorrect_msg": "বৰ মৰম লগা প্ৰচেষ্টা! সঠিক উত্তৰটো আছিল {ans}। আৰামেৰে লওক, কোনো খৰখেদা নাই।",
        "brain_win_msg": "🎉 মগজুৰ ব্যায়াম সমাপ্ত: {total} টাৰ ভিতৰত {correct} টা শুদ্ধ! আপুনি বৰ ভাল কৰিলে।",
        "btn_replay_brain_same": "নতুন প্ৰশ্নৰ সৈতে {level} পুনৰ খেলক",
        
        # Find My Way Home & Compass
        "nav_page_caption": "মেমোৰাকেয়াৰ · শান্ত ঘৰৰ পথ নিৰ্দেশনা · অফলাইন ব্যৱস্থা",
        "nav_mode_label": "স্থান নিৰ্ধাৰণ পদ্ধতি",
        "nav_mode_sim": "🧪 ডেমো পৰীক্ষা পদ্ধতি (অফলাইন)",
        "nav_mode_manual": "✍️ হাতেৰে GPS স্থানাংক লিখক",
        "nav_mode_gps": "📡 ব্ৰাউজাৰ / ডিভাইচ GPS",
        "nav_sim_prompt": "পৰীক্ষা কৰিবলৈ এটা অৱস্থা বাছক:",
        "nav_sim_close": "🟢 ঘৰৰ একেবাৰে ওচৰত (~৩৫ মিটাৰ) · দুৱাৰমুখত",
        "nav_sim_park": "🟡 ওচৰৰ উদ্যান (~৩২০ মিটাৰ) · চুটি খোজৰ দূৰত্ব",
        "nav_sim_market": "🟠 দৈনিক বজাৰ (~৮৫০ মিটাৰ) · কেইটামান আলিবাট আঁতৰত",
        "nav_sim_far": "⚠️ দূৰৈৰ ঠাইত (~২.৪ কিঃমিঃ) · চহৰৰ অন্য প্ৰান্তত",
        "nav_lat_input": "আপোনাৰ বৰ্তমান অক্ষাংশ (Latitude)",
        "nav_lon_input": "আপোনাৰ বৰ্তমান দ্ৰাঘিমাংশ (Longitude)",
        "nav_gps_acquired": "📡 GPS স্থানাংক পোৱা গ'ল: {lat:.5f}° উত্তৰ, {lon:.5f}° পূব",
        "nav_gps_requesting": "📡 ব্ৰাউজাৰৰ পৰা GPS বিচৰা হৈছে... (অনুগ্ৰহ কৰি 'Allow' টিপক)",
        "nav_gps_fallback": "*(GPS নোপোৱালৈকে স্থানীয় স্থানাংক ব্যৱহাৰ কৰা হৈছে)*",
        "compass_title": "🧭 ঘৰলৈ যাবলৈ কম্পাছৰ দিশ",
        "compass_direction_prompt": "ঘৰলৈ যাবলৈ {heading} ({bearing}°) দিশত মুখ কৰক",
        "compass_instruction": "হাতত মোবাইলটো লৈ গাঢ় সেউজীয়া কাড় চিহ্নৰ দিশত খোজ কাঢ়ক।",
        "btn_listen_audio": "🔊 নিৰ্দেশনা স্পষ্টকৈ শুনিবলৈ ইয়াত টিপক",
        "btn_call_caregiver": "📞 পৰিয়ালক ফোন কৰক: {name} ({phone})",
        "home_info_title": "🏡 আপোনাৰ ঘৰৰ ঠিকনা",
        "home_info_address": "ঠিকনা:",
        "home_info_landmark": "চিনাকি স্থান:",
        "home_info_coords": "স্থানাংক:",
        "passerby_card_title": "🤝 পথচাৰী বা সহায়কক দেখুৱাওক",
        "passerby_card_text": '"নমস্কাৰ! মই মোৰ ঘৰৰ ঠিকনা বিচাৰি আছোঁ। মোক এই ঠিকনাত পোৱাই দিয়ক: {address}, বা মোৰ পৰিয়ালক ফোন কৰক: {phone}।"',
        "passerby_card_note": "বিশেষ জাননী:",
        
        # Navigation Guidance Statuses
        "nav_at_home_title": "🟢 আপুনি আপোনাৰ ঘৰৰ একেবাৰে কাষতে আছে!",
        "nav_at_home_dist": "{dist} মিটাৰ (ঘৰৰ দুৱাৰমুখতে)",
        "nav_at_home_guidance": "ওচৰ-পাঁজৰলৈ চাওক — আপুনি সুৰক্ষিত আৰু ঘৰৰ দুৱাৰমুখ পালেহি। স্বাগতম!",
        "nav_at_home_advice": "আপুনি আৰাম কৰিব পাৰে। আৰু খোজ কঢ়াৰ প্ৰয়োজন নাই।",
        
        "nav_near_home_title": "🟡 আপুনি ঘৰৰ ওচৰতে আছে",
        "nav_near_home_dist": "~{dist} মিটাৰ দূৰত (প্ৰায় ৩ ৰ পৰা ৫ মিনিটৰ খোজ)",
        "nav_near_home_guidance": "লাহে লাহে {heading} দিশত খোজ কাঢ়ক। আপোনাৰ চিনাকি আলিবাট আৰু সেউজীয়া গেটখনলৈ লক্ষ্য কৰক।",
        "nav_near_home_advice": "আৰামেৰে কাঁড় চিহ্নটো অনুসৰণ কৰক। ভাগৰ লাগিলে বহি লওক বা যত্নদাতাক ফোন কৰক।",
        
        "nav_mod_dist_title": "🟠 আপুনি ঘৰৰ পৰা কিছু আঁতৰত আছে",
        "nav_mod_dist_dist": "~{dist:.2f} কিঃমিঃ আঁতৰত",
        "nav_mod_dist_guidance": "আপোনাৰ ঘৰ {heading} দিশত। তালৈ যাবলৈ কিছু বেছি সময় লাগিব।",
        "nav_mod_dist_advice": "ওচৰৰ কোনো দোকান বা পথচাৰীক সহায়ক কাৰ্ডখন দেখুৱাওক, অথবা তলৰ বুটাম টিপি পৰিয়ালক ফোন কৰক।",
        
        "nav_far_title": "⚠️ আপুনি চিনাকি এলেকাৰ বাহিৰলৈ আহি পৰিছে",
        "nav_far_dist": "~{dist:.1f} কিঃমিঃ দূৰত",
        "nav_far_guidance": "অনুগ্ৰহ কৰি কোনো এখন নিৰাপদ দোকান বা চাহৰ দোকানত বহক আৰু অপেক্ষা কৰক।",
        "nav_far_advice": "এতিয়াই তলৰ ডাঙৰ ৰঙা বুটাম টিপি পৰিয়ালক ফোন কৰক যাতে তেওঁলোকে আপোনাক নিবলৈ আহিব পাৰে।",
        
        # Caregiver View
        "cg_title": "যত্নদাতাৰ ডেস্কব'ৰ্ড (Caregiver Dashboard)",
        "cg_subtitle": "ৰোগীৰ দৈনিক কাম-কাজৰ তথ্য। সকলো তথ্য এই যন্ত্ৰটোতে সুৰক্ষিত।",
        "cg_recent_activity": "সাম্প্ৰতিক কাৰ্যকলাপ",
        "cg_no_activity": "বৰ্তমান কোনো তথ্য নাই।",
        "cg_reminder_status": "সোঁৱৰণীৰ স্থিতি",
        "btn_edit": "সম্পাদনা",
        "btn_delete": "মচক",
        "reminder_form_title": "সোঁৱৰণীৰ নাম",
        "reminder_form_type": "প্ৰকাৰ",
        "reminder_form_time": "সময় (HH:MM)",
        "reminder_form_notes": "বিৱৰণ",
        "btn_save_changes": "পৰিৱৰ্তন সংৰক্ষণ কৰক",
        "expander_add_reminder": "নতুন সোঁৱৰণী যোগ কৰক",
        "btn_save_reminder": "সোঁৱৰণী সংৰক্ষণ কৰক",
        "reminder_saved_msg": "সোঁৱৰণী সফলতাৰে সংৰক্ষণ হ'ল।",
        "cg_home_settings_heading": "🏠 ঘৰৰ অৱস্থান আৰু জৰুৰীকালীন যোগাযোগৰ ছেটিংছ",
        "cg_home_settings_caption": "ৰোগীৰ ঘৰৰ স্থানাংক, চিনাকি স্থান আৰু জৰুৰীকালীন ফোন নম্বৰ স্থানীয়ভাৱে সংৰক্ষণ কৰক।",
        "cg_input_home_label": "ঘৰৰ নাম / পৰিচয়",
        "cg_input_address": "ঘৰৰ ঠিকনা",
        "cg_input_landmark": "চিনাকি স্থান (ৰোগীয়ে চিনি পোৱাকৈ)",
        "cg_input_lat": "ঘৰৰ অক্ষাংশ (Latitude)",
        "cg_input_lon": "ঘৰৰ দ্ৰাঘিমাংশ (Longitude)",
        "cg_input_cg_name": "যত্নদাতাৰ নাম",
        "cg_input_cg_phone": "যত্নদাতাৰ ফোন নম্বৰ (জৰুৰীকালীন)",
        "cg_input_note": "জৰুৰীকালীন জাননী (সহায়ক কাৰ্ডত দেখুৱাবলৈ)",
        "btn_save_home_settings": "ঘৰৰ তথ্য সংৰক্ষণ কৰক",
        "msg_home_saved": "✅ ঘৰৰ স্থানাংক আৰু যোগাযোগৰ তথ্য সফলতাৰে সংৰক্ষণ কৰা হ'ল!",
    },
    
    "bn": {
        # Sidebar & General
        "app_title": "মেমোরাকেয়ার",
        "app_subtitle": "স্মৃতি সহায়ক সঙ্গী",
        "role_label": "আমি ব্যবহার করছি:",
        "role_patient": "রোগী / বয়োজ্যেষ্ঠ",
        "role_caregiver": "যত্নদাতা (Caregiver)",
        "language_label": "ভাষা / Language",
        "local_date_label": "স্থানীয় তারিখ",
        "offline_notice_title": "অফলাইন প্রোটোটাইপ",
        "offline_notice_body": "সমস্ত গেম, স্কোর, রিমাইন্ডার এবং এআই সুপারিশ এই ডিভাইসেই সংরক্ষিত থাকে।",
        "btn_back_to_activities": "← কার্যকলাপে ফিরে যান",
        "btn_find_home_sidebar": "🏠 বাড়ির দিক ও সহায়তা",
        "btn_return_dashboard": "← ড্যাশবোর্ডে ফিরে যান",
        "hero_eyebrow": "মেমোরাকেয়ার · স্মৃতি সহায়ক সঙ্গী",
        "hero_heading": "নমস্কার, আসুন শান্ত ও ধীরেসুস্থে শুরু করি।",
        "hero_subheading": "যেকোনো একটি সহজ কাজ বেছে নিন। কোনো তাড়াহুড়ো নেই।",
        "hero_greeting_audio": "নমস্কার, আপনাকে আন্তরিক স্বাগতম। আজকের দিনটি খুব শান্তভাবে এবং স্বাচ্ছন্দে উপভোগ করুন। যেকোনো একটি ছোট খেলা বেছে নিন, কোনো তাড়া নেই।",
        "find_home_banner_title": "🏠 বাড়ি ফেরার পথ খুঁজুন",
        "find_home_banner_sub": "বাড়ির দূরত্ব ও দিক দেখুন, অথবা এক ট্যাপে পরিবারকে ফোন করুন।",
        "find_home_banner_btn": "🏠 বাড়ির দিক ও সহায়তা খুলুন →",
        "choose_activity": "একটি সহজ কাজ বেছে নিন",
        "tab_card_pairs": "কার্ড জোড়া মেলানো",
        "tab_sequence": "ক্রম মনে রাখা",
        "tab_object_match": "অনুষঙ্গ মেলানো",
        "tab_brain_exercise": "মস্তিষ্কের ব্যায়াম",
        
        # Voice Common UI
        "voice_listen_aloud": "🔊 স্পষ্ট শুনুন",
        "voice_listen_greeting": "🔊 মধুর কণ্ঠে শুনুন",
        "voice_listen_reminders": "🔊 আজকের রিমাইন্ডারগুলো শুনুন",
        "voice_reminders_spoken_intro": "আজ আপনার জন্য {count} টি স্নেহভরা রিমাইন্ডার রয়েছে: {items}। অনুগ্রহ করে নিজের খেয়াল রাখবেন।",
        "voice_reminders_none": "আজকের জন্য কোনো রিমাইন্ডার নেই। আপনি শান্তিতে বিশ্রাম নিন।",
        "voice_speak_brain_question": "🔊 প্রশ্ন ও বিকল্পসমূহ শুনুন",
        "voice_mic_btn": "🎙️ মুখে উত্তর বলুন",
        "voice_mic_listening": "🎙️ শোনা হচ্ছে... অনুগ্রহ করে স্পষ্ট করে উত্তর বলুন।",
        "voice_mic_heard": "🎙️ শোনা গেছে: \"{text}\"",
        "voice_mic_matched": "✅ নির্বাচিত হয়েছে: {choice}",
        "voice_mic_no_match": "💡 শোনা গেছে: \"{text}\"। অনুগ্রহ করে আবার বলুন বা ট্যাপ করুন।",
        "voice_caregiver_summary": "🔊 রোগীর অগ্রগতির সারসংক্ষেপ শুনুন",
        "voice_caregiver_spoken": "রোগী {count} টি কার্যকলাপ সম্পন্ন করেছেন, যার গড় সঠিকতা {acc} শতাংশ এবং সম্পূর্ণতা {comp} শতাংশ।",
        "audio_not_supported": "আপনার ব্রাউজারে অডিও সমর্থিত নয়।",
        "mic_not_supported": "আপনার ব্রাউজারে মাইক্রোফোন ইনপুট সমর্থিত নয়।",

        # Reminders Panel
        "reminders_heading": "আজকের রিমাইন্ডার",
        "no_reminders": "বর্তমানে কোনো রিমাইন্ডার নেই।",
        "reminder_status_done": "সম্পন্ন",
        "reminder_status_now": "এখন",
        "reminder_type_medication": "ওষুধ",
        "reminder_type_meal": "খাবার",
        "reminder_type_game": "মস্তিষ্কের চর্চা",
        "reminder_type_appointment": "ডাক্তার / সাক্ষাৎ",
        
        # Progress & Analytics
        "progress_heading": "দৈনিক অগ্রগতি",
        "progress_empty": "অগ্রগতি দেখতে যেকোনো একটি কাজ সম্পন্ন করুন।",
        "metric_activities": "মোট কাজ",
        "metric_avg_accuracy": "গড় সঠিকতা",
        "metric_completed": "সম্পূর্ণতা",
        "chart_daily_accuracy": "দৈনিক সঠিকতার লেখচিত্র",
        "chart_activity_accuracy": "কার্যকলাপ অনুযায়ী সঠিকতা",
        
        # Card Pairs Game
        "pairs_title": "মিল থাকা কার্ডজোড়া খুঁজুন",
        "difficulty_level": "কঠিনতার মাত্রা",
        "level_easy": "সহজ (Easy)",
        "level_medium": "মাঝারি (Medium)",
        "level_hard": "কঠিন (Hard)",
        "pairs_caption_easy": "৩ জোড়া · ৬ টি কার্ড",
        "pairs_caption_medium": "৫ জোড়া · ১০ টি কার্ড",
        "pairs_caption_hard": "৮ জোড়া · ১৬ টি কার্ড",
        "pairs_instruction": "দুটি করে কার্ড উল্টে মিল থাকা ছবি বা শব্দ খুঁজুন।",
        "pairs_mismatch": "কার্ড দুটি মেলেনি। কোনো চিন্তা নেই, অন্য একটি কার্ডে চাপ দিন।",
        "pairs_matched_status": "মেলেছে: {total} জোড়ার মধ্যে {matched} জোড়া · প্রচেষ্টা: {attempts}",
        "pairs_win_msg": "🎉 চমৎকার! আপনি ধৈর্যের সাথে {attempts} টি প্রচেষ্টায় সব জোড়া মিলিয়েছেন।",
        "ai_recommendation_msg": "AI ইঞ্জিন আপনার স্কোর বিশ্লেষণ করেছে। পরবর্তী স্তরের সুপারিশ: **{rec}**।",
        "btn_play_next_level": "পরবর্তী স্তরে খেলুন ({level}) →",
        "btn_replay_same": "নতুন কার্ড দিয়ে {level} আবার খেলুন",
        
        # Sequence Game
        "sequence_title": "ধারাবাহিক ক্রম মনে রাখুন",
        "seq_caption_easy": "৩ টি বস্তু · সহজ",
        "seq_caption_medium": "৫ টি বস্তু · সাধারণ",
        "seq_caption_hard": "৭ টি বস্তু · কঠিন",
        "seq_show_instruction": "প্রতিটি বস্তু মনোযোগ দিয়ে দেখুন। কোনো তাড়া নেই। প্রস্তুত হলে **পরবর্তী বস্তু** চাপুন।",
        "seq_item_counter": "বস্তু {curr} / {total} · রাউন্ড {round_num}",
        "btn_next_item": "পরবর্তী বস্তু →",
        "btn_ready_recall": "ক্রম মনে করতে প্রস্তুত →",
        "btn_review_start": "শুরু থেকে আবার দেখুন",
        "seq_answer_instruction": "আপনি যে ক্রমে দেখেছিলেন, সেই ক্রমে নিচের বোতামগুলোতে চাপ দিন।",
        "seq_selected_status": "{total} টির মধ্যে {count} টি নির্বাচিত · *আরও {remaining} টি প্রয়োজন*",
        "seq_all_selected": "সব {total} টি বস্তু নির্বাচিত হয়েছে! যাচাই করতে প্রস্তুত।",
        "seq_no_items_yet": "এখনও কোনো বস্তু নির্বাচন করা হয়নি।",
        "btn_undo_last": "শেষেরটি মুছুন",
        "btn_clear_answer": "সব মুছুন",
        "btn_check_sequence": "ক্রম যাচাই করুন",
        "seq_round_success": "✨ দারুণ! আপনি {round_num} নম্বর রাউন্ড খুব সুন্দরভাবে মনে রেখেছেন।",
        "seq_round_take_time": "শান্তভাবে শ্বাস নিন। প্রস্তুত হলে পরবর্তী রাউন্ডের জন্য নিচের বোতাম চাপুন।",
        "btn_begin_next_round": "পরবর্তী রাউন্ড শুরু করুন →",
        "seq_win_msg": "🎉 অসাধারণ! আপনি ৩ টি রাউন্ড {attempts} টি প্রচেষ্টায় সম্পন্ন করেছেন।",
        "seq_fail_msg": "খুব সুন্দর চেষ্টা ছিল! আপনি {rounds} টি রাউন্ড সঠিকভাবে সম্পন্ন করেছেন। শান্ত থাকুন।",
        "seq_was_msg": "সঠিক ক্রম ছিল: **{expected}**",
        "btn_replay_seq_same": "নতুন ক্রম দিয়ে {level} আবার খেলুন",
        
        # Object Match Game
        "object_title": "অনুষঙ্গ জোড়া মেলানো",
        "object_caption_easy": "৩ জোড়া · সহজ",
        "object_caption_medium": "৫ জোড়া · প্রাত্যহিক জীবন",
        "object_caption_hard": "৭ জোড়া + অতিরিক্ত বিকল্প",
        "object_instruction": "বামদিকের প্রতিটি বস্তুর সাথে ডানদিকের উপযুক্ত অনুষঙ্গ মেলান।",
        "object_how_to": "💡 **খেলার নিয়ম:** ১. বামদিকের একটি বস্তু নির্বাচন করুন। ২. তারপর ডানদিকের মিল থাকা সঙ্গীকে চাপুন।",
        "object_left_header": "১. মূল বস্তুসমূহ",
        "object_right_header": "২. সঙ্গী বস্তুবৃন্দ",
        "object_selected_banner": "👉 **নির্বাচিত:** {name} · *এখন ডানদিক থেকে এর সঙ্গী বাছুন!*",
        "object_please_select_left": "👉 প্রথমে বামদিকের একটি বস্তু নির্বাচন করুন!",
        "object_match_success": "✨ চমৎকার মিল! {left} এবং {right} একসঙ্গে ব্যবহৃত হয় ({explanation})।",
        "object_win_msg": "🎉 দুর্দান্ত! আপনি {attempts} টি প্রচেষ্টায় সব {total} জোড়া মিলিয়েছেন!",
        "object_connected_header": "🏆 মিলিত জোড়াসমূহ",
        "btn_replay_obj_same": "নতুন বস্তুর সাথে {level} আবার খেলুন",
        
        # Brain Exercises
        "brain_title": "মস্তিষ্কের সহজ ব্যায়াম",
        "brain_caption_easy": "সহজ গণিত ও পরিচিত বিষয়",
        "brain_caption_medium": "দৈনন্দিন হিসাব ও সাদৃশ্য",
        "brain_caption_hard": "যৌক্তিক চিন্তন ও বিন্যাস",
        "brain_sub_instruction": "ছোট ও আনন্দদায়ক প্রশ্নের উত্তর দিন। আপনি মাইক্রোফোন বোতাম চেপে মুখেও উত্তর বলতে পারেন।",
        "brain_question_counter": "প্রশ্ন {curr} / {total} · {cat}",
        "brain_choose_prompt": "আপনার উত্তর বেছে নিন:",
        "btn_check_answer": "উত্তর যাচাই করুন",
        "btn_continue_exercise": "পরবর্তী প্রশ্নে যান →",
        "brain_correct_msg": "অসাধারণ! আপনার উত্তরটি একদম সঠিক হয়েছে: {ans}। দারুণ করছেন!",
        "brain_incorrect_msg": "খুব সুন্দর চেষ্টা করেছেন! সঠিক উত্তরটি ছিল {ans}। মন শান্ত রাখুন, আপনি খুব ভালো করছেন।",
        "brain_win_msg": "🎉 মস্তিষ্কের ব্যায়াম সম্পন্ন: {total} টির মধ্যে {correct} টি সঠিক! খুব ভালো হয়েছে।",
        "btn_replay_brain_same": "নতুন প্রশ্নের সাথে {level} আবার খেলুন",
        
        # Find My Way Home & Compass
        "nav_page_caption": "মেমোরাকেয়ার · বাড়ির পথ নির্দেশনা · অফলাইন ব্যবস্থা",
        "nav_mode_label": "অবস্থান নির্ধারণের মাধ্যম",
        "nav_mode_sim": "🧪 ডেমো পরীক্ষা পদ্ধতি (অফলাইন)",
        "nav_mode_manual": "✍️ হাতে GPS স্থানাঙ্ক লিখুন",
        "nav_mode_gps": "📡 ব্রাউজার / ডিভাইস GPS",
        "nav_sim_prompt": "পরীক্ষা করার জন্য একটি অবস্থা নির্বাচন করুন:",
        "nav_sim_close": "🟢 বাড়ির খুব কাছে (~৩৫ মিটার) · দরজার সামনে",
        "nav_sim_park": "🟡 কাছের পার্ক (~৩২০ মিটার) · অল্প হাঁটার দূরত্ব",
        "nav_sim_market": "🟠 বাজার এলাকা (~৮৫০ মিটার) · কয়েকটি রাস্তা দূরে",
        "nav_sim_far": "⚠️ দূরে কোথাও (~২.৪ কিমি) · শহরের অন্য প্রান্তে",
        "nav_lat_input": "আপনার বর্তমান অক্ষাংশ (Latitude)",
        "nav_lon_input": "আপনার বর্তমান দ্রাঘিমাংশ (Longitude)",
        "nav_gps_acquired": "📡 GPS স্থানাঙ্ক পাওয়া গেছে: {lat:.5f}° উত্তর, {lon:.5f}° পূর্ব",
        "nav_gps_requesting": "📡 ব্রাউজার থেকে GPS চাওয়া হচ্ছে... (দয়া করে 'Allow' চাপুন)",
        "nav_gps_fallback": "*(GPS না পাওয়া পর্যন্ত স্থানীয় স্থানাঙ্ক ব্যবহৃত হচ্ছে)*",
        "compass_title": "🧭 বাড়ির দিকে কম্পাস অভিমুখ",
        "compass_direction_prompt": "বাড়ির দিকে যেতে {heading} ({bearing}°) মুখে হাঁটুন",
        "compass_instruction": "হাতে মোবাইল নিয়ে গাঢ় সবুজ তীরের দিকে মুখ করে হাঁটুন।",
        "btn_listen_audio": "🔊 মুখে বলা নির্দেশনা শুনুন",
        "btn_call_caregiver": "📞 পরিবারকে ফোন করুন: {name} ({phone})",
        "home_info_title": "🏡 আপনার বাড়ির ঠিকানা",
        "home_info_address": "ঠিকানা:",
        "home_info_landmark": "পরিচিত স্থান:",
        "home_info_coords": "স্থানাঙ্ক:",
        "passerby_card_title": "🤝 পথচারী বা সাহায্যকারীকে দেখান",
        "passerby_card_text": '"নমস্কার! আমি বাড়ি ফেরার পথ খুঁজছি। আমাকে এই ঠিকানায় পৌঁছাতে সাহায্য করুন: {address}, অথবা আমার পরিবারকে ফোন করুন: {phone}।"',
        "passerby_card_note": "জরুরি তথ্য:",
        
        # Navigation Guidance Statuses
        "nav_at_home_title": "🟢 আপনি আপনার বাড়ির একদম কাছে আছেন!",
        "nav_at_home_dist": "{dist} মিটার (বাড়ির দরজার সামনে)",
        "nav_at_home_guidance": "চারপাশে তাকান — আপনি নিরাপদ এবং বাড়ির সামনে পৌঁছেছেন। স্বাগতম!",
        "nav_at_home_advice": "আপনি শান্তিতে বিশ্রাম নিন। আর হাঁটার প্রয়োজন নেই।",
        
        "nav_near_home_title": "🟡 আপনি বাড়ির কাছাকাছি আছেন",
        "nav_near_home_dist": "~{dist} মিটার দূরে (প্রায় ৩ থেকে ৫ মিনিটের হাঁটা পথ)",
        "nav_near_home_guidance": "ধীরে ধীরে {heading} দিকে হাঁটুন। আপনার পরিচিত গলি ও সবুজ গেটটি লক্ষ্য করুন।",
        "nav_near_home_advice": "তীরের দিকটি অনুসরণ করুন। ক্লান্তি লাগলে বসে বিশ্রাম নিন অথবা অভিভাবককে ফোন করুন।",
        
        "nav_mod_dist_title": "🟠 আপনি বাড়ি থেকে কিছুটা দূরে আছেন",
        "nav_mod_dist_dist": "~{dist:.2f} কিমি দূরে",
        "nav_mod_dist_guidance": "আপনার বাড়ি {heading} অভিমুখে। পৌঁছাতে কিছুটা সময় লাগতে পারে।",
        "nav_mod_dist_advice": "কাছের কোনো দোকানদারকে সহায়তাকারী কার্ডটি দেখান, অথবা নিচে দেওয়া বোতাম চেপে পরিবারকে ফোন করুন।",
        
        "nav_far_title": "⚠️ আপনি অচেনা এলাকায় চলে এসেছেন",
        "nav_far_dist": "~{dist:.1f} কিমি দূরে",
        "nav_far_guidance": "অনুগ্রহ করে কোনো একটি নিরাপদ ও পরিচিত দোকানে বা চায়ের দোকানে বসুন।",
        "nav_far_advice": "এখনই নিচে থাকা বড় লাল বোতাম চেপে পরিবারকে ফোন করুন যাতে তারা আপনাকে নিতে আসতে পারে।",
        
        # Caregiver View
        "cg_title": "যত্নদাতার ড্যাশবোর্ড (Caregiver Dashboard)",
        "cg_subtitle": "রোগীর সাম্প্রতিক কার্যকলাপের সারসংক্ষেপ। সমস্ত তথ্য এই ডিভাইসেই সংরক্ষিত।",
        "cg_recent_activity": "সাম্প্রতিক কার্যকলাপ",
        "cg_no_activity": "এখনও কোনো তথ্য সংরক্ষিত নেই।",
        "cg_reminder_status": "রিমাইন্ডারের অবস্থা",
        "btn_edit": "সম্পাদনা",
        "btn_delete": "মুছুন",
        "reminder_form_title": "রিমাইন্ডারের নাম",
        "reminder_form_type": "ধরন",
        "reminder_form_time": "সময় (HH:MM)",
        "reminder_form_notes": "বিবরণ",
        "btn_save_changes": "পরিবর্তন সংরক্ষণ করুন",
        "expander_add_reminder": "নতুন রিমাইন্ডার যোগ করুন",
        "btn_save_reminder": "রিমাইন্ডার সংরক্ষণ করুন",
        "reminder_saved_msg": "রিমাইন্ডার সফলভাবে সংরক্ষিত হয়েছে।",
        "cg_home_settings_heading": "🏠 বাড়ির অবস্থান ও জরুরি যোগাযোগের সেটিংস",
        "cg_home_settings_caption": "রোগীর বাড়ির স্থানাঙ্ক, পরিচিত ল্যান্ডমার্ক এবং জরুরি ফোন নম্বর ডিভাইসে সংরক্ষণ করুন।",
        "cg_input_home_label": "বাড়ির নাম / লেবেল",
        "cg_input_address": "বাড়ির ঠিকানা",
        "cg_input_landmark": "পরিচিত ল্যান্ডমার্ক (রোগী যাতে চিনতে পারে)",
        "cg_input_lat": "বাড়ির অক্ষাংশ (Latitude)",
        "cg_input_lon": "বাড়ির দ্রাঘিমাংশ (Longitude)",
        "cg_input_cg_name": "যত্নদাতার নাম",
        "cg_input_cg_phone": "যত্নদাতার ফোন নম্বর (জরুরি কলের জন্য)",
        "cg_input_note": "জরুরি বার্তা (সহায়তাকারী কার্ডে দেখানোর জন্য)",
        "btn_save_home_settings": "বাড়ির তথ্য সংরক্ষণ করুন",
        "msg_home_saved": "✅ বাড়ির স্থানাঙ্ক এবং যোগাযোগের তথ্য সফলভাবে সংরক্ষিত হয়েছে!",
    },
    
    "hi": {
        # Sidebar & General
        "app_title": "मेमोराकेयर",
        "app_subtitle": "स्मृति साथी एवं मानसिक अभ्यास",
        "role_label": "उपयोगकर्ता प्रकार:",
        "role_patient": "मरीज / वरिष्ठ नागरिक",
        "role_caregiver": "देखभालकर्ता (Caregiver)",
        "language_label": "भाषा / Language",
        "local_date_label": "स्थानीय तिथि",
        "offline_notice_title": "ऑफलाइन-प्रथम प्रोटोटाइप",
        "offline_notice_body": "सभी खेल, अंक, अनुस्मारक और एआई सुझाव इसी उपकरण पर सुरक्षित रहते हैं।",
        "btn_back_to_activities": "← गतिविधियों पर वापस जाएं",
        "btn_find_home_sidebar": "🏠 घर का रास्ता और सहायता",
        "btn_return_dashboard": "← मुख्य पृष्ठ पर वापस जाएं",
        "hero_eyebrow": "मेमोराकेयर · पूर्वोत्तर स्मृति साथी",
        "hero_heading": "नमस्ते, आइए शांति और सुकून से शुरुआत करें।",
        "hero_subheading": "कोई एक छोटी गतिविधि चुनें। कोई जल्दबाजी नहीं है।",
        "hero_greeting_audio": "नमस्ते, आपका बहुत-बहुत स्वागत है। आज का दिन बड़े प्यार और सुकून से बिताएं। अपनी पसंद की कोई भी छोटी गतिविधि चुनें, कोई जल्दबाजी नहीं है।",
        "find_home_banner_title": "🏠 घर का रास्ता खोजें",
        "find_home_banner_sub": "घर की दूरी और दिशा देखें, या एक स्पर्श में अपने परिवार को कॉल करें।",
        "find_home_banner_btn": "🏠 घर की दिशा और सहायता खोलें →",
        "choose_activity": "एक सरल गतिविधि चुनें",
        "tab_card_pairs": "कार्ड जोड़े",
        "tab_sequence": "क्रम याद रखना",
        "tab_object_match": "वस्तु मिलान",
        "tab_brain_exercise": "मस्तिष्क व्यायाम",
        
        # Voice Common UI
        "voice_listen_aloud": "🔊 बोलकर सुनें",
        "voice_listen_greeting": "🔊 मधुर आवाज में संदेश सुनें",
        "voice_listen_reminders": "🔊 आज के अनुस्मारक सुनें",
        "voice_reminders_spoken_intro": "आज के प्यार भरे अनुस्मारक इस प्रकार हैं: {items}। कृपया अपना ध्यान रखें।",
        "voice_reminders_none": "आज के लिए कोई अनुस्मारक निर्धारित नहीं है। आप आराम से समय बिताएं।",
        "voice_speak_brain_question": "🔊 प्रश्न और विकल्प सुनें",
        "voice_mic_btn": "🎙️ बोलकर उत्तर दें",
        "voice_mic_listening": "🎙️ सुन रहे हैं... कृपया स्पष्ट आवाज में उत्तर बोलें।",
        "voice_mic_heard": "🎙️ सुना: \"{text}\"",
        "voice_mic_matched": "✅ चुना गया: {choice}",
        "voice_mic_no_match": "💡 सुना गया: \"{text}\"। कृपया पुनः बोलें या विकल्प दबाएं।",
        "voice_caregiver_summary": "🔊 मरीज की प्रगति का सारांश सुनें",
        "voice_caregiver_spoken": "मरीज ने कुल {count} गतिविधियां पूरी की हैं। औसत सटीकता {acc} प्रतिशत और पूर्णता दर {comp} प्रतिशत है।",
        "audio_not_supported": "इस ब्राउज़र में वॉइस सुविधा समर्थित नहीं है।",
        "mic_not_supported": "इस ब्राउज़र में माइक्रोफोन वॉइस इनपुट समर्थित नहीं है।",

        # Reminders Panel
        "reminders_heading": "आज के अनुस्मारक (Reminders)",
        "no_reminders": "वर्तमान में कोई अनुस्मारक नहीं है।",
        "reminder_status_done": "पूर्ण",
        "reminder_status_now": "अभी",
        "reminder_type_medication": "दवा",
        "reminder_type_meal": "भोजन",
        "reminder_type_game": "मस्तिष्क अभ्यास",
        "reminder_type_appointment": "अपॉइंटमेंट / डॉक्टर",
        
        # Progress & Analytics
        "progress_heading": "दैनिक प्रगति",
        "progress_empty": "प्रगति देखने के लिए कोई एक गतिविधि पूरी करें।",
        "metric_activities": "कुल गतिविधियाँ",
        "metric_avg_accuracy": "औसत सटीकता",
        "metric_completed": "पूर्णता दर",
        "chart_daily_accuracy": "दैनिक सटीकता चार्ट",
        "chart_activity_accuracy": "गतिविधि अनुसार सटीकता",
        
        # Card Pairs Game
        "pairs_title": "मिलते-जुलते जोड़े खोजें",
        "difficulty_level": "कठिनाई स्तर",
        "level_easy": "सरल (Easy)",
        "level_medium": "मध्यम (Medium)",
        "level_hard": "कठिन (Hard)",
        "pairs_caption_easy": "३ जोड़े · ६ कार्ड",
        "pairs_caption_medium": "५ जोड़े · १० कार्ड",
        "pairs_caption_hard": "८ जोड़े · १६ कार्ड",
        "pairs_instruction": "दो कार्ड पलटकर एक जैसे कार्डों की जोड़ी बनाएं।",
        "pairs_mismatch": "ये कार्ड आपस में नहीं मिलते। कोई बात नहीं, दूसरा कार्ड चुनें।",
        "pairs_matched_status": "मिले जोड़े: {total} में से {matched} · प्रयास: {attempts}",
        "pairs_win_msg": "🎉 बहुत बढ़िया! आपने धैर्यपूर्वक {attempts} प्रयासों में सभी जोड़े ढूंढ लिए।",
        "ai_recommendation_msg": "AI इंजन ने आपके प्रदर्शन का विश्लेषण किया। अगले स्तर का सुझाव: **{rec}**।",
        "btn_play_next_level": "अगला स्तर खेलें ({level}) →",
        "btn_replay_same": "नए कार्डों के साथ {level} फिर से खेलें",
        
        # Sequence Game
        "sequence_title": "क्रम याद रखें",
        "seq_caption_easy": "३ वस्तुएं · सरल",
        "seq_caption_medium": "५ वस्तुएं · मानक",
        "seq_caption_hard": "७ वस्तुएं · कठिन",
        "seq_show_instruction": "प्रत्येक वस्तु को ध्यान से देखें। कोई जल्दी नहीं है। तैयार होने पर **अगली वस्तु** दबाएं।",
        "seq_item_counter": "वस्तु {curr} / {total} · राउंड {round_num}",
        "btn_next_item": "अगली वस्तु →",
        "btn_ready_recall": "क्रम बताने के लिए तैयार →",
        "btn_review_start": "शुरुआत से फिर देखें",
        "seq_answer_instruction": "जिस क्रम में आपने वस्तुएं देखी थीं, उसी क्रम में नीचे दिए गए बटनों को दबाएं।",
        "seq_selected_status": "{total} में से {count} चुनी गईं · *{remaining} और शेष हैं*",
        "seq_all_selected": "सभी {total} वस्तुएं चुनी गईं! जांचने के लिए तैयार।",
        "seq_no_items_yet": "अभी तक कोई वस्तु नहीं चुनी गई।",
        "btn_undo_last": "अंतिम हटाएं",
        "btn_clear_answer": "सब हटाएं",
        "btn_check_sequence": "क्रम जांचें",
        "seq_round_success": "✨ शानदार! आपने राउंड {round_num} का क्रम बहुत सुंदर ढंग से याद रखा।",
        "seq_round_take_time": "आराम से गहरी सांस लें। जब आप तैयार हों, तो अगले राउंड के लिए नीचे बटन दबाएं।",
        "btn_begin_next_round": "अगला राउंड शुरू करें →",
        "seq_win_msg": "🎉 बधाई! आपने ३ राउंड {attempts} प्रयासों में सफलता से पूरे किए।",
        "seq_fail_msg": "बहुत प्यारा प्रयास! आपने {rounds} राउंड सही पूरे किए। शांति से आगे बढ़ें।",
        "seq_was_msg": "सही क्रम था: **{expected}**",
        "btn_replay_seq_same": "नए क्रम के साथ {level} फिर से खेलें",
        
        # Object Match Game
        "object_title": "साथी वस्तुओं का मिलान",
        "object_caption_easy": "३ जोड़े · सरल",
        "object_caption_medium": "५ जोड़े · दैनिक जीवन",
        "object_caption_hard": "७ जोड़े + अतिरिक्त विकल्प",
        "object_instruction": "बाईं ओर की वस्तु को दाईं ओर की उपयुक्त साथी वस्तु से जोड़ें।",
        "object_how_to": "💡 **खेलने का तरीका:** १. पहले बाईं ओर की किसी वस्तु को दबाएं। २. फिर दाईं ओर उसके साथी को दबाकर जोड़ें।",
        "object_left_header": "१. प्रारंभिक वस्तुएं",
        "object_right_header": "२. साथी वस्तुएं",
        "object_selected_banner": "👉 **चुना गया:** {name} · *अब दाईं ओर से इसका सही साथी चुनें!*",
        "object_please_select_left": "👉 कृपया पहले बाईं ओर से एक वस्तु चुनें!",
        "object_match_success": "✨ बहुत बढ़िया मिलान! {left} और {right} साथ उपयोग होते हैं ({explanation})।",
        "object_win_msg": "🎉 अति उत्तम! आपने {attempts} प्रयासों में सभी {total} जोड़े मिला दिए!",
        "object_connected_header": "🏆 जोड़े गए साथी",
        "btn_replay_obj_same": "नई वस्तुओं के साथ {level} फिर से खेलें",
        
        # Brain Exercises
        "brain_title": "मस्तिष्क का सरल अभ्यास",
        "brain_caption_easy": "सरल गणित और परिचित वस्तुएं",
        "brain_caption_medium": "दैनिक बाजार हिसाब और समानताएं",
        "brain_caption_hard": "तार्किक विचार और पैटर्न",
        "brain_sub_instruction": "छोटे और रोचक प्रश्नों के उत्तर दें। आप माइक्रोफोन दबाकर बोलकर भी उत्तर दे सकते हैं।",
        "brain_question_counter": "प्रश्न {curr} / {total} · {cat}",
        "brain_choose_prompt": "अपना उत्तर चुनें:",
        "btn_check_answer": "उत्तर जांचें",
        "btn_continue_exercise": "अगले प्रश्न पर जाएं →",
        "brain_correct_msg": "बहुत ही सुंदर! आपका उत्तर बिल्कुल सही है: {ans}। बहुत बढ़िया!",
        "brain_incorrect_msg": "बहुत प्यारा प्रयास! सही उत्तर था {ans}। आराम से आगे बढ़ें, आप बहुत अच्छा कर रहे हैं।",
        "brain_win_msg": "🎉 मस्तिष्क अभ्यास पूर्ण: {total} में से {correct} सही! बहुत शानदार प्रदर्शन।",
        "btn_replay_brain_same": "नए प्रश्नों के साथ {level} फिर से खेलें",
        
        # Find My Way Home & Compass
        "nav_page_caption": "मेमोराकेयर · घर का शांत मार्गदर्शन · ऑफलाइन प्रणाली",
        "nav_mode_label": "स्थान मोड (Location Mode)",
        "nav_mode_sim": "🧪 डेमो सिमुलेशन (ऑफलाइन)",
        "nav_mode_manual": "✍️ मैनुअल GPS निर्देशांक",
        "nav_mode_gps": "📡 ब्राउज़र / डिवाइस GPS",
        "nav_sim_prompt": "परीक्षण के लिए एक स्थिति चुनें:",
        "nav_sim_close": "🟢 घर के बिल्कुल पास (~३५ मी) · दरवाजे पर",
        "nav_sim_park": "🟡 पास का पार्क (~३२० मी) · थोड़ी दूरी पर टहलना",
        "nav_sim_market": "🟠 स्थानीय बाजार (~८५० मी) · कुछ गलियां दूर",
        "nav_sim_far": "⚠️ काफी दूर (~२.४ किमी) · शहर के दूसरे हिस्से में",
        "nav_lat_input": "आपका वर्तमान अक्षांश (Latitude)",
        "nav_lon_input": "आपका वर्तमान देशांतर (Longitude)",
        "nav_gps_acquired": "📡 डिवाइस GPS प्राप्त: {lat:.5f}° उत्तर, {lon:.5f}° पूर्व",
        "nav_gps_requesting": "📡 ब्राउज़र से GPS निर्देशांक प्राप्त किए जा रहे हैं... (कृपया 'Allow' दबाएं)",
        "nav_gps_fallback": "*(GPS मिलने तक स्थानीय निर्देशांक का उपयोग किया जा रहा है)*",
        "compass_title": "🧭 घर की ओर कम्पास दिशा",
        "compass_direction_prompt": "घर की ओर चलने के लिए {heading} ({bearing}°) की ओर मुंह करें",
        "compass_instruction": "मोबाइल को हाथ में रखकर गहरे हरे तीर की दिशा में आगे बढ़ें।",
        "btn_listen_audio": "🔊 दिशा-निर्देश बोलकर सुनने के लिए यहां दबाएं",
        "btn_call_caregiver": "📞 परिजन को कॉल करें: {name} ({phone})",
        "home_info_title": "🏡 आपके घर की जानकारी",
        "home_info_address": "पता:",
        "home_info_landmark": "पहचान स्थल:",
        "home_info_coords": "निर्देशांक:",
        "passerby_card_title": "🤝 राहगीर / मददगार को दिखाएं",
        "passerby_card_text": '"नमस्ते! मैं अपने घर का रास्ता ढूंढ रहा/रही हूँ। कृपया मुझे इस पते पर पहुंचाने में मदद करें: {address}, या मेरे परिवार को कॉल करें: {phone}।',
        "passerby_card_note": "विशेष सूचना:",
        
        # Navigation Guidance Statuses
        "nav_at_home_title": "🟢 आप अपने घर के बिल्कुल करीब हैं!",
        "nav_at_home_dist": "{dist} मीटर (घर के दरवाजे पर)",
        "nav_at_home_guidance": "आस-पास देखें — आप सुरक्षित हैं और घर पहुंच चुके हैं। स्वागत है!",
        "nav_at_home_advice": "आप आराम से बैठें। अब आगे चलने की कोई जरूरत नहीं है।",
        
        "nav_near_home_title": "🟡 आप अपने घर के पास हैं",
        "nav_near_home_dist": "~{dist} मीटर दूर (लगभग ३ से ५ मिनट की पैदल दूरी)",
        "nav_near_home_guidance": "आराम से {heading} दिशा में चलें। अपनी जानी-पहचानी गली और हरे गेट को देखें।",
        "nav_near_home_advice": "तीर के निशान का अनुसरण करें। थकान महसूस हो तो बैठ जाएं या परिजन को फोन करें।",
        
        "nav_mod_dist_title": "🟠 आप घर से थोड़ी दूरी पर हैं",
        "nav_mod_dist_dist": "~{dist:.2f} किमी दूर",
        "nav_mod_dist_guidance": "आपका घर {heading} दिशा में है। वहां तक पहुंचने में थोड़ा समय लगेगा।",
        "nav_mod_dist_advice": "पास के किसी दयालु दुकानदार या पड़ोसी को सहायता कार्ड दिखाएं, या नीचे दिया गया बटन दबाकर परिवार को फोन करें।",
        
        "nav_far_title": "⚠️ आप अपने परिचित इलाके से बाहर हैं",
        "nav_far_dist": "~{dist:.1f} किमी दूर",
        "nav_far_guidance": "कृपया किसी सुरक्षित चाय की दुकान या छांव में बैठें और प्रतीक्षा करें।",
        "nav_far_advice": "अभी नीचे दिया गया लाल बटन दबाकर अपने परिवार को फोन करें ताकि वे आपको लेने आ सकें।",
        
        # Caregiver View
        "cg_title": "देखभालकर्ता डैशबोर्ड (Caregiver Dashboard)",
        "cg_subtitle": "हाल की गतिविधियों का शांत सारांश। सभी जानकारी इसी उपकरण में सुरक्षित है।",
        "cg_recent_activity": "हाल की गतिविधियां",
        "cg_no_activity": "अभी तक कोई गतिविधि दर्ज नहीं है।",
        "cg_reminder_status": "अनुस्मारक स्थिति",
        "btn_edit": "संपादित करें",
        "btn_delete": "हटाएं",
        "reminder_form_title": "अनुस्मारक नाम",
        "reminder_form_type": "प्रकार",
        "reminder_form_time": "समय (HH:MM)",
        "reminder_form_notes": "विवरण",
        "btn_save_changes": "परिवर्तन सहेजें",
        "expander_add_reminder": "नया अनुस्मारक जोड़ें",
        "btn_save_reminder": "अनुस्मारक सहेजें",
        "reminder_saved_msg": "अनुस्मारक इस डिवाइस पर सहेजा गया।",
        "cg_home_settings_heading": "🏠 मरीज का घर और आपातकालीन संपर्क सेटिंग्स",
        "cg_home_settings_caption": "मरीज के घर के निर्देशांक, पहचान स्थल और आपातकालीन फोन नंबर को SQLite में सुरक्षित करें।",
        "cg_input_home_label": "घर का नाम / लेबल",
        "cg_input_address": "घर का पता",
        "cg_input_landmark": "पहचान स्थल (जो मरीज पहचान सके)",
        "cg_input_lat": "घर का अक्षांश (Latitude)",
        "cg_input_lon": "घर का देशांतर (Longitude)",
        "cg_input_cg_name": "देखभालकर्ता का नाम",
        "cg_input_cg_phone": "देखभालकर्ता का फोन नंबर (आपातकालीन कॉल)",
        "cg_input_note": "आपातकालीन संदेश (मददगार कार्ड पर दिखाने के लिए)",
        "btn_save_home_settings": "घर की सेटिंग्स सहेजें",
        "msg_home_saved": "✅ घर के निर्देशांक और संपर्क जानकारी सफलतापूर्वक सहेजी गई!",
    }
}


def t(key: str, lang: str = "en", **kwargs: Any) -> str:
    """Translate a key for the given language with fallback to English."""
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    text = lang_dict.get(key, TRANSLATIONS["en"].get(key, key))
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text


# ==========================================
# Localized Game Content Pools
# ==========================================

CARD_PAIRS_POOLS = {
    "en": [
        "Tea ☕", "River 🌊", "Hill ⛰️", "Sun ☀️", "Fish 🐟",
        "Flower 🌸", "House 🏠", "Tree 🌳", "Bird 🐦", "Fruit 🍎",
        "Bell 🔔", "Moon 🌙", "Book 📖", "Leaf 🍃", "Cloud ☁️",
        "Boat ⛵", "Lamp 💡", "Song 🎵", "Clock ⏰", "Star ⭐",
        "Garden 🪴", "Bridge 🌉", "Apple 🍏", "Bread 🍞", "Water 💧",
    ],
    "as": [
        "চাহ ☕", "নৈ 🌊", "পাহাৰ ⛰️", "সূৰ্য ☀️", "মাছ 🐟",
        "ফুল 🌸", "ঘৰ 🏠", "গছ 🌳", "চৰাই 🐦", "ফল 🍎",
        "ঘণ্টি 🔔", "জোন 🌙", "কিতাপ 📖", "পাত 🍃", "ডাৱৰ ☁️",
        "নাও ⛵", "চাকি 💡", "গীত 🎵", "ঘড়ী ⏰", "তৰা ⭐",
        "বাৰী 🪴", "দলং 🌉", "আপেল 🍏", "ৰুটি 🍞", "পানী 💧",
    ],
    "bn": [
        "চা ☕", "নদী 🌊", "পাহাড় ⛰️", "সূর্য ☀️", "মাছ 🐟",
        "ফুল 🌸", "বাড়ি 🏠", "গাছ 🌳", "পাখি 🐦", "ফল 🍎",
        "ঘণ্টা 🔔", "চাঁদ 🌙", "বই 📖", "পাতা 🍃", "মেঘ ☁️",
        "নৌকা ⛵", "প্রদীপ 💡", "গান 🎵", "ঘড়ি ⏰", "তারা ⭐",
        "বাগান 🪴", "সেতু 🌉", "আপেল 🍏", "রুটি 🍞", "জল 💧",
    ],
    "hi": [
        "चाय ☕", "नदी 🌊", "पहाड़ ⛰️", "सूरज ☀️", "मछली 🐟",
        "फूल 🌸", "घर 🏠", "पेड़ 🌳", "पक्षी 🐦", "फल 🍎",
        "घंटी 🔔", "चांद 🌙", "किताब 📖", "पत्ता 🍃", "बादल ☁️",
        "नाव ⛵", "दीपक 💡", "गीत 🎵", "घड़ी ⏰", "तारा ⭐",
        "बगीचा 🪴", "पुल 🌉", "सेब 🍏", "रोटी 🍞", "पानी 💧",
    ],
}

CARD_PAIRS_CLUSTERS = {
    "en": [
        ("River 🌊", "Stream 💧"), ("Sun ☀️", "Star ⭐"), ("Tea ☕", "Coffee 🍵"),
        ("Tree 🌳", "Plant 🌿"), ("Bird 🐦", "Duck 🦆"), ("House 🏠", "Cabin 🛖"),
        ("Cloud ☁️", "Rain 🌧️"), ("Leaf 🍃", "Branch 🪵"), ("Boat ⛵", "Ship 🚢"),
        ("Book 📖", "Letter ✉️"), ("Cat 🐱", "Kitten 🐾"), ("Apple 🍎", "Cherry 🍒"),
    ],
    "as": [
        ("নৈ 🌊", "জুৰি 💧"), ("সূৰ্য ☀️", "তৰা ⭐"), ("চাহ ☕", "কফি 🍵"),
        ("গছ 🌳", "লতা 🌿"), ("চৰাই 🐦", "হাঁহ 🦆"), ("ঘৰ 🏠", "পঁজা 🛖"),
        ("ডাৱৰ ☁️", "বৰষুণ 🌧️"), ("পাত 🍃", "ডাল 🪵"), ("নাও ⛵", "জাহাজ 🚢"),
        ("কিতাপ 📖", "চিঠি ✉️"), ("মেকুৰী 🐱", "পোৱালি 🐾"), ("আপেল 🍎", "টেঙা 🍒"),
    ],
    "bn": [
        ("নদী 🌊", "ঝর্ণা 💧"), ("সূর্য ☀️", "তারা ⭐"), ("চা ☕", "কফি 🍵"),
        ("গাছ 🌳", "লতা 🌿"), ("পাখি 🐦", "হাঁস 🦆"), ("বাড়ি 🏠", "কুঁড়েঘর 🛖"),
        ("মেঘ ☁️", "বৃষ্টি 🌧️"), ("পাতা 🍃", "ডাল 🪵"), ("নৌকা ⛵", "জাহাজ 🚢"),
        ("বই 📖", "চিঠি ✉️"), ("বিড়াল 🐱", "ছানা 🐾"), ("আপেল 🍎", "চেরি 🍒"),
    ],
    "hi": [
        ("नदी 🌊", "झरना 💧"), ("सूरज ☀️", "तारा ⭐"), ("चाय ☕", "कॉफ़ी 🍵"),
        ("पेड़ 🌳", "पौधा 🌿"), ("पक्षी 🐦", "बत्तख 🦆"), ("घर 🏠", "झोपड़ी 🛖"),
        ("बादल ☁️", "बारिश 🌧️"), ("पत्ता 🍃", "टहनी 🪵"), ("नाव ⛵", "जहाज 🚢"),
        ("किताब 📖", "पत्र ✉️"), ("बिल्ली 🐱", "शावक 🐾"), ("सेब 🍎", "बेर 🍒"),
    ],
}

SEQUENCE_THEMES = {
    "en": {
        "Nature & Wildlife 🌿": [
            ("Sun ☀️", "☀️"), ("Tree 🌳", "🌳"), ("Bird 🐦", "🐦"), ("Fish 🐟", "🐟"),
            ("Moon 🌙", "🌙"), ("Star ⭐", "⭐"), ("River 🌊", "🌊"), ("Flower 🌸", "🌸"),
            ("Butterfly 🦋", "🦋"), ("Leaf 🍃", "🍃"), ("Cloud ☁️", "☁️"), ("Rainbow 🌈", "🌈"),
        ],
        "Morning & Home 🏡": [
            ("Tea Cup 🍵", "🍵"), ("Clock ⏰", "⏰"), ("Book 📖", "📖"), ("Lamp 💡", "💡"),
            ("Bell 🔔", "🔔"), ("Key 🔑", "🔑"), ("Bread 🍞", "🍞"), ("Spoon 🥄", "🥄"),
            ("Blanket 🧶", "🧶"), ("House 🏠", "🏠"), ("Chair 🪑", "🪑"), ("Window 🪟", "🪟"),
        ],
        "Colors & Shapes 🎨": [
            ("Red Heart ❤️", "❤️"), ("Blue Circle 🔵", "🔵"), ("Yellow Star ⭐", "⭐"),
            ("Green Leaf 🟢", "🟢"), ("Orange Diamond 🔶", "🔶"), ("Purple Gem 🟣", "🟣"),
            ("Golden Bell 🔔", "🔔"), ("White Cloud ⚪", "⚪"), ("Brown Wood 🟤", "🟤"),
        ],
        "Playful Numbers 🎲": [
            ("One 1️⃣", "1️⃣"), ("Two 2️⃣", "2️⃣"), ("Three 3️⃣", "3️⃣"), ("Four 4️⃣", "4️⃣"),
            ("Five 5️⃣", "5️⃣"), ("Six 6️⃣", "6️⃣"), ("Seven 7️⃣", "7️⃣"), ("Eight 8️⃣", "8️⃣"),
            ("Nine 9️⃣", "9️⃣"),
        ],
    },
    "as": {
        "প্ৰকৃতি আৰু জীৱজগত 🌿": [
            ("সূৰ্য ☀️", "☀️"), ("গছ 🌳", "🌳"), ("চৰাই 🐦", "🐦"), ("মাছ 🐟", "🐟"),
            ("জোন 🌙", "🌙"), ("তৰা ⭐", "⭐"), ("নৈ 🌊", "🌊"), ("ফুল 🌸", "🌸"),
            ("পখিলী 🦋", "🦋"), ("পাত 🍃", "🍃"), ("ডাৱৰ ☁️", "☁️"), ("ৰামধেনু 🌈", "🌈"),
        ],
        "ৰাতিপুৱা আৰু ঘৰ 🏡": [
            ("চাহৰ কাপ 🍵", "🍵"), ("ঘড়ী ⏰", "⏰"), ("কিতাপ 📖", "📖"), ("চাকি 💡", "💡"),
            ("ঘণ্টি 🔔", "🔔"), ("চাবি 🔑", "🔑"), ("ৰুটি 🍞", "🍞"), ("চামুচ 🥄", "🥄"),
            ("চেলেং 🧶", "🧶"), ("ঘৰ 🏠", "🏠"), ("চকী 🪑", "🪑"), ("খিৰিকী 🪟", "🪟"),
        ],
        "ৰং আৰু আকৃতি 🎨": [
            ("ৰঙা হৃদয় ❤️", "❤️"), ("নীলা বৃত্ত 🔵", "🔵"), ("হালধীয়া তৰা ⭐", "⭐"),
            ("সেউজীয়া পাত 🟢", "🟢"), ("কমলা ৰং 🔶", "🔶"), ("বেঙুনীয়া মণি 🟣", "🟣"),
            ("সোণালী ঘণ্টি 🔔", "🔔"), ("বগা ডাৱৰ ⚪", "⚪"), ("মটীয়া কাঠ 🟤", "🟤"),
        ],
        "মৰমৰ সংখ্যা 🎲": [
            ("এক 1️⃣", "1️⃣"), ("দুই 2️⃣", "2️⃣"), ("তিনি 3️⃣", "3️⃣"), ("চাৰি 4️⃣", "4️⃣"),
            ("পাঁচ 5️⃣", "5️⃣"), ("ছয় 6️⃣", "6️⃣"), ("সাত 7️⃣", "7️⃣"), ("আঠ 8️⃣", "8️⃣"),
            ("ন 9️⃣", "9️⃣"),
        ],
    },
    "bn": {
        "প্রকৃতি ও বন্যপ্রাণী 🌿": [
            ("সূর্য ☀️", "☀️"), ("গাছ 🌳", "🌳"), ("পাখি 🐦", "🐦"), ("মাছ 🐟", "🐟"),
            ("চাঁদ 🌙", "🌙"), ("তারা ⭐", "⭐"), ("নদী 🌊", "🌊"), ("ফুল 🌸", "🌸"),
            ("প্রজাপতি 🦋", "🦋"), ("পাতা 🍃", "🍃"), ("মেঘ ☁️", "☁️"), ("রামধনু 🌈", "🌈"),
        ],
        "সকাল ও গৃহকোণ 🏡": [
            ("চায়ের কাপ 🍵", "🍵"), ("ঘড়ি ⏰", "⏰"), ("বই 📖", "📖"), ("প্রদীপ 💡", "💡"),
            ("ঘণ্টা 🔔", "🔔"), ("চাবি 🔑", "🔑"), ("রুটি 🍞", "🍞"), ("চামচ 🥄", "🥄"),
            ("শাল 🧶", "🧶"), ("বাড়ি 🏠", "🏠"), ("চেয়ার 🪑", "🪑"), ("জানালা 🪟", "🪟"),
        ],
        "রং ও আকার 🎨": [
            ("লাল হৃদয় ❤️", "❤️"), ("নীল বৃত্ত 🔵", "🔵"), ("হলুদ তারা ⭐", "⭐"),
            ("সবুজ পাতা 🟢", "🟢"), ("কমলা রত্ন 🔶", "🔶"), ("বেগুনি মণি 🟣", "🟣"),
            ("সোনালী ঘণ্টা 🔔", "🔔"), ("সাদা মেঘ ⚪", "⚪"), ("বাদামী কাঠ 🟤", "🟤"),
        ],
        "সুন্দর সংখ্যা 🎲": [
            ("এক 1️⃣", "1️⃣"), ("দুই 2️⃣", "2️⃣"), ("তিন 3️⃣", "3️⃣"), ("চার 4️⃣", "4️⃣"),
            ("পাঁচ 5️⃣", "5️⃣"), ("ছয় 6️⃣", "6️⃣"), ("সাত 7️⃣", "7️⃣"), ("আট 8️⃣", "8️⃣"),
            ("নয় 9️⃣", "9️⃣"),
        ],
    },
    "hi": {
        "प्रकृति एवं वन्यजीवन 🌿": [
            ("सूरज ☀️", "☀️"), ("पेड़ 🌳", "🌳"), ("पक्षी 🐦", "🐦"), ("मछली 🐟", "🐟"),
            ("चांद 🌙", "🌙"), ("तारा ⭐", "⭐"), ("नदी 🌊", "🌊"), ("फूल 🌸", "🌸"),
            ("तितली 🦋", "🦋"), ("पत्ता 🍃", "🍃"), ("बादल ☁️", "☁️"), ("इंद्रधनुष 🌈", "🌈"),
        ],
        "सुबह और घर 🏡": [
            ("चाय का प्याला 🍵", "🍵"), ("घड़ी ⏰", "⏰"), ("किताब 📖", "📖"), ("दीपक 💡", "💡"),
            ("घंटी 🔔", "🔔"), ("चाबी 🔑", "🔑"), ("रोटी 🍞", "🍞"), ("चम्मच 🥄", "🥄"),
            ("कंबल 🧶", "🧶"), ("घर 🏠", "🏠"), ("कुर्सी 🪑", "🪑"), ("खिड़की 🪟", "🪟"),
        ],
        "रंग और आकृतियां 🎨": [
            ("लाल दिल ❤️", "❤️"), ("नीला गोला 🔵", "🔵"), ("पीला तारा ⭐", "⭐"),
            ("हरा पत्ता 🟢", "🟢"), ("नारंगी रत्न 🔶", "🔶"), ("बैंगनी मणि 🟣", "🟣"),
            ("सुनहरी घंटी 🔔", "🔔"), ("सफेद बादल ⚪", "⚪"), ("भूरा काठ 🟤", "🟤"),
        ],
        "सुंदर संख्याएं 🎲": [
            ("एक 1️⃣", "1️⃣"), ("दो 2️⃣", "2️⃣"), ("तीन 3️⃣", "3️⃣"), ("चार 4️⃣", "4️⃣"),
            ("पांच 5️⃣", "5️⃣"), ("छह 6️⃣", "6️⃣"), ("सात 7️⃣", "7️⃣"), ("आठ 8️⃣", "8️⃣"),
            ("नौ 9️⃣", "9️⃣"),
        ],
    },
}

OBJECT_COMPANION_PAIRS = {
    "en": [
        ("🫖 Teapot", "☕ Tea Cup", "Pour and enjoy warm morning tea", "A teapot pours tea into something you drink from."),
        ("🔑 Door Key", "🔒 Padlock", "Unlock doors and keep home safe", "A key is inserted to unlock a padlock."),
        ("☂️ Rain Umbrella", "🌧️ Raincoat", "Stay dry on monsoon rainy days", "An umbrella pairs with rainwear to keep you dry."),
        ("🪥 Toothbrush", "🧴 Toothpaste", "Brush and clean teeth fresh", "Toothpaste is applied onto a toothbrush."),
        ("📖 Storybook", "👓 Reading Glasses", "Read stories and news clearly", "Reading glasses help you see text in a book clearly."),
        ("🪴 Flower Pot", "🚿 Watering Can", "Water and nourish home plants", "A watering can showers water into flower pots."),
        ("🧵 Needle & Thread", "🧷 Safety Pin", "Mend and fasten warm garments", "Needles and safety pins are used to stitch and pin cloth."),
        ("🍳 Frying Pan", "🥢 Cooking Spatula", "Stir and prepare nourishing meals", "A spatula stirs food cooking inside a frying pan."),
        ("🧹 Broom", "🗑️ Dustpan", "Sweep dust and keep rooms tidy", "A broom sweeps floor sweepings into a dustpan."),
        ("✉️ Postal Letter", "📮 Postbox", "Post and send letters to loved ones", "Letters are mailed inside a postal box."),
        ("👞 Walking Shoes", "🧦 Woolen Socks", "Wear together for morning walks", "Socks are worn inside shoes for warmth."),
        ("🕯️ Wax Candle", "🪵 Matchbox", "Strike and light up the room softly", "A match from a matchbox lights a candle."),
        ("📻 Classic Radio", "🎧 Headphones", "Listen to songs and morning news", "Headphones plug into a radio for listening."),
        ("🥣 Soup Bowl", "🥄 Soup Spoon", "Eat warm nutritious broth", "A spoon scoops broth from a soup bowl."),
        ("🧺 Laundry Basket", "🧼 Washing Soap", "Wash and clean household linens", "Washing soap cleans laundry in the basket."),
    ],
    "as": [
        ("🫖 চাহৰ কেটলি", "☕ চাহৰ কাপ", "গৰম ৰাতিপুৱাৰ চাহ বাকি খোৱা", "কেটলিৰে চাহ বাকি কাপত খোৱা হয়।"),
        ("🔑 চাবি", "🔒 তলা", "ঘৰ সুৰক্ষিত ৰখা আৰু দুৱাৰ খোলা", "চাবিৰে তলা খোলা হয়।"),
        ("☂️ ছাতি", "🌧️ বৰষুণৰ কাপোৰ", "বাৰিষাৰ বৰষুণত তিতাৰ পৰা ৰক্ষা পোৱা", "ছাতিয়ে বৰষুণৰ পৰা ৰক্ষা কৰে।"),
        ("🪥 দাঁত ঘঁহা ব্ৰাছ", "🧴 টুথপেষ্ট", "দাঁত পৰিষ্কাৰ আৰু সুস্থ ৰখা", "ব্ৰাছত পেষ্ট লগাই দাঁত মঁহা হয়।"),
        ("📖 সাধুকথাৰ পুথি", "👓 পঢ়া চশমা", "স্পষ্টকৈ বাতৰি আৰু কিতাপ পঢ়া", "চশমাই কিতাপ পঢ়াত সহায় কৰে।"),
        ("🪴 ফুলৰ টব", "🚿 পানী দিয়া পাত্ৰ", "বাৰীৰ ফুল-গছত পানী দিয়া", "পাত্ৰৰে ফুলৰ টবত পানী ঢলা হয়।"),
        ("🧵 বেজী আৰু সূতা", "🧷 চেফটি পিন", "কাপোৰ চিলাই আৰু জোৰা দিয়া", "বেজী-সূতাৰে কাপোৰ চিলাই কৰা হয়।"),
        ("🍳 কেৰাহী", "🥢 হেতা / খুৰপি", "সোৱাদভৰা খাদ্য ৰন্ধা", "হেতাৰে কেৰাহীত আঞ্জা লৰোৱা হয়।"),
        ("🧹 বাঢ়নী / ঝাড়ু", "🗑️ জাবৰৰ পাত্ৰ", "ঘৰ-দুৱাৰ পৰিষ্কাৰ আৰু চাফা ৰখা", "বাঢ়নীৰে ধূলি সাৰি পেলাই দিয়া হয়।"),
        ("✉️ চিঠিৰ খাম", "📮 ডাকবাকচ", "আপোনজনলৈ চিঠি পঠোৱা", "চিঠি ডাকবাকচত পেলোৱা হয়।"),
        ("👞 খোজকঢ়া জোতা", "🧦 মোজা", "ৰাতিপুৱা ফুৰিবলৈ যাওঁতে পিন্ধা", "জোতাৰ ভিতৰত মোজা পিন্ধা হয়।"),
        ("🕯️ মমবাতি", "🪵 জুইশলা / মেচ", "কোঠাটো পোহৰাই তোলা", "জুইশলা কাঠিৰে মমবাতি জ্বলোৱা হয়।"),
        ("📻 ৰেডিঅ'", "🎧 হেডফোন", "পুৱাৰ গীত আৰু বাতৰি শুনা", "ৰেডিঅ'ৰ লগত হেডফোন সংলগ্ন কৰা হয়।"),
        ("🥣 কাঁহী-বাটি", "🥄 চামুচ", "পুষ্টিকৰ খাদ্য তৃপ্তিৰে খোৱা", "বাটিৰ খাদ্য চামুচেৰে খোৱা হয়।"),
        ("🧺 কাপোৰৰ খৰাহী", "🧼 চাবোন", "কাপোৰ ধুই পৰিষ্কাৰ কৰা", "চাবোনেৰে কাপোৰ চাফা কৰা হয়।"),
    ],
    "bn": [
        ("🫖 চায়ের কেটলি", "☕ চায়ের কাপ", "গরম সকালের চা ঢেলে খাওয়া", "কেটলি থেকে চা কাপে ঢালা হয়।"),
        ("🔑 চাবি", "🔒 তালা", "ঘর সুরক্ষিত রাখা ও দরজা খোলা", "চাবি দিয়ে তালা খোলা হয়।"),
        ("☂️ ছাতা", "🌧️ রেইনকোট", "বর্ষায় বৃষ্টি থেকে বাঁচা", "ছাতা ও রেইনকোট বৃষ্টিতে রক্ষা করে।"),
        ("🪥 টুথব্রাশ", "🧴 টুথপেস্ট", "দাঁত পরিষ্কার ও সতেজ রাখা", "ব্রাশে পেস্ট লাগিয়ে দাঁত মাজা হয়।"),
        ("📖 গল্পের বই", "👓 পড়ার চশমা", "স্পষ্টভাবে বই ও খবর পড়া", "চশমা দিয়ে বইয়ের লেখা পড়া সহজ হয়।"),
        ("🪴 ফুলের টব", "🚿 জল দেওয়ার ঝাঁঝরি", "গাছে জল দিয়ে যত্ন নেওয়া", "ঝাঁঝরি দিয়ে টবে জল দেওয়া হয়।"),
        ("🧵 সুঁচ ও সুতো", "🧷 সেফটি পিন", "কাপড় সেলাই ও জোড়া দেওয়া", "সুঁচ-সুতো দিয়ে কাপড় সেলাই করা হয়।"),
        ("🍳 কড়াই", "🥢 খুন্তি", "সুস্বাদু খাবার রান্না করা", "খুন্তি দিয়ে কড়াইয়ের খাবার নাড়া হয়।"),
        ("🧹 ঝাঁটা", "🗑️ ধুলোর পাত্র", "ঘরবাড়ি পরিষ্কার ও পরিচ্ছন্ন রাখা", "ঝাঁটা দিয়ে ময়লা পরিষ্কার করা হয়।"),
        ("✉️ চিঠির খাম", "📮 ডাকবাক্স", "প্রিয়জনকে চিঠি পাঠানো", "চিঠি ডাকবাক্সে ফেলা হয়।"),
        ("👞 হাঁটার জুতো", "🧦 মোজা", "সকালের হাঁটার জন্য পরা", "জুতোর সাথে মোজা পরা হয়।"),
        ("🕯️ মোমবাতি", "🪵 দেশলাই", "আলো জ্বালিয়ে ঘর উজ্জ্বল করা", "দেশলাই দিয়ে মোমবাতি জ্বালানো হয়।"),
        ("📻 রেডিও", "🎧 হেডফোন", "গান ও সকালের খবর শোনা", "রেডিওর সাথে হেডফোন জুড়ে শোনা হয়।"),
        ("🥣 বাটি", "🥄 চামচ", "পুষ্টিকর খাবার খাওয়া", "বাটির খাবার চামচ দিয়ে খাওয়া হয়।"),
        ("🧺 কাপড়ের ঝুড়ি", "🧼 সাবান", "কাপড় ধুয়ে পরিষ্কার রাখা", "সাবান দিয়ে কাপড় কাচা হয়।"),
    ],
    "hi": [
        ("🫖 चाय की केतली", "☕ चाय का कप", "गरम सुबह की चाय परोसना", "केतली से चाय कप में डाली जाती है।"),
        ("🔑 चाबी", "🔒 ताला", "घर सुरक्षित रखना और ताला खोलना", "चाबी से ताला खोला जाता है।"),
        ("☂️ छाता", "🌧️ बरसाती (Raincoat)", "बारिश से सुरक्षित रहना", "छाता बारिश में भीगने से बचाता है।"),
        ("🪥 टूथब्रश", "🧴 टूथपेस्ट", "दांत साफ और तरोताजा रखना", "ब्रश पर पेस्ट लगाकर दांत साफ किए जाते हैं।"),
        ("📖 कहानी की किताब", "👓 पढ़ने का चश्मा", "किताब और अखबार साफ पढ़ना", "चश्मे की मदद से किताब पढ़ी जाती है।"),
        ("🪴 गमला", "🚿 फव्वारा (हजारा)", "पौधों को पानी देना", "हजारे से गमले में पानी डाला जाता है।"),
        ("🧵 सुई और धागा", "🧷 सेफ्टी पिन", "कपड़े सिलना और ठीक करना", "सुई-धागे से कपड़े सिले जाते हैं।"),
        ("🍳 कढ़ाई / तवा", "🥢 करछुल / पलटा", "स्वादिष्ट भोजन पकाना", "पलटे से कड़ाही में खाना चलाया जाता है।"),
        ("🧹 झाड़ू", "🗑️ कूड़ेदान", "घर साफ-सुथरा रखना", "झाड़ू से कचरा साफ किया जाता है।"),
        ("✉️ पत्र (खत)", "📮 डाक का डिब्बा", "अपनों को खत भेजना", "खत को लेटरबॉक्स में डाला जाता है।"),
        ("👞 चलने के जूते", "🧦 ऊनी मोजे", "सुबह टहलने के लिए पहनना", "जूते के साथ मोजे पहने जाते हैं।"),
        ("🕯️ मोमबत्ती", "🪵 माचिस", "कमरे को रोशनी से भरना", "माचिस से मोमबत्ती जलाई जाती है।"),
        ("📻 रेडियो", "🎧 हेडफ़ोन", "गीत और सुबह की खबरें सुनना", "रेडियो से गाने सुने जाते हैं।"),
        ("🥣 कटोरी", "🥄 चम्मच", "गरम पौष्टिक भोजन खाना", "कटोरी से चम्मच द्वारा खाया जाता है।"),
        ("🧺 कपड़ों की टोकरी", "🧼 धोने का साबुन", "कपड़े धोकर साफ रखना", "साबुन से कपड़े धोए जाते हैं।"),
    ],
}

OBJECT_DISTRACTORS = {
    "en": [
        ("🪚 Hand Saw", "Cut firewood in the yard"),
        ("🪁 Flying Kite", "Fly high on breezy hills"),
        ("⚓ Ship Anchor", "Hold boats securely in river waters"),
    ],
    "as": [
        ("🪚 কৰত", "বাৰীত কাঠ কটা সঁজুলি"),
        ("🪁 চিলা", "বতাহত পাহাৰৰ ওপৰত উৰুওৱা"),
        ("⚓ জাহাজৰ নাঙল", "নৈত নাও স্থিৰ কৰি ৰখা"),
    ],
    "bn": [
        ("🪚 করাত", "কাঠ কাটার জন্য ব্যবহৃত"),
        ("🪁 ঘুড়ি", "আকাশে ওড়ানোর খেলা"),
        ("⚓ জাহাজের নোঙ্গর", "নৌকা স্থির রাখার জন্য"),
    ],
    "hi": [
        ("🪚 आरी", "लकड़ी काटने का औजार"),
        ("🪁 पतंग", "हवा में उड़ने वाला खेल"),
        ("⚓ लंगर", "नाव को पानी में रोकने के लिए"),
    ],
}

# ==========================================
# Localized Brain Exercises Generator
# ==========================================

def generate_brain_exercises(level: str, lang: str = "en") -> list[dict]:
    lvl = level.capitalize() if level else "Easy"
    questions = []

    # 1. Story Math Question
    if lvl == "Easy":
        a = random.randint(2, 7)
        b = random.randint(2, 6)
        if random.choice([True, False]):
            correct = a + b
            distractors = [correct - 1, correct + 2, correct + 1]
            if lang == "as":
                prompt = f"ৰাতিপুৱাৰ চাহৰ দোকানত ককাদেউতাই {a} কাপ আৰু খুড়াই {b} কাপ চাহ খালে। মুঠতে কিমান কাপ চাহ তৈয়াৰ কৰা হ'ল?"
                explanation = f"সঠিক উত্তৰ হ'ল {correct} কাপ।"
            elif lang == "bn":
                prompt = f"সকালের চায়ের দোকানে দাদু {a} কাপ এবং কাকা আরও {b} কাপ চা নিলেন। মোট কত কাপ চা তৈরি হলো?"
                explanation = f"সঠিক উত্তর হলো {correct} কাপ।"
            elif lang == "hi":
                prompt = f"सुबह की चाय की दुकान पर दादाजी ने {a} कप और चाचाजी ने {b} कप चाय पी। कुल मिलाकर कितनी चाय बनी?"
                explanation = f"सही उत्तर है {correct} कप।"
            else:
                prompt = f"At the morning tea stall, grandfather had {a} cups of tea and uncle ordered {b} more. How many cups of tea were prepared in total?"
                explanation = f"The correct answer is {correct}."
        else:
            total = a + b
            correct = a
            distractors = [correct + 1, max(1, correct - 2), correct + 2]
            if lang == "as":
                prompt = f"আইতাই বাৰীৰ পৰা {total} টা সতেজ মধুৰীআম চিঙি {b} টা চুবুৰীয়াক দিলে। আইতাৰ ওচৰত এতিয়া কিমানটা মধুৰীআম বাকী ৰ'ল?"
                explanation = f"সঠিক উত্তৰ হ'ল {correct} টা।"
            elif lang == "bn":
                prompt = f"দিদিমা বাগান থেকে {total} টি পেয়ারা পেড়ে {b} টি প্রতিবেশীদের দিলেন। দিদিমার কাছে আর কতটি রইল?"
                explanation = f"সঠিক উত্তর হলো {correct} টি।"
            elif lang == "hi":
                prompt = f"दादीजी ने बगीचे से {total} अमरूदों में से {b} अमरूद पड़ोसियों को दे दिए। अब उनके पास कितने अमरूद बचे?"
                explanation = f"सही उत्तर है {correct}।"
            else:
                prompt = f"Grandmother picked {total} fresh sweet guavas from the garden and shared {b} with the neighbors. How many guavas remain?"
                explanation = f"The correct answer is {correct}."
    elif lvl == "Medium":
        a = random.randint(15, 45)
        b = random.randint(10, 35)
        if random.choice([True, False]):
            correct = a + b
            distractors = [correct - 5, correct + 10, correct + 5]
            if lang == "as":
                prompt = f"হস্তশিল্পৰ মেলাত এটা বাঁহৰ কাপ ষ্টেণ্ডৰ মূল্য ₹{a} আৰু এটা কাপোৰৰ মোনাৰ মূল্য ₹{b}। দুয়োটা সামগ্ৰীৰ মুঠ মূল্য কিমান?"
                explanation = f"মুঠ মূল্য হ'ল ₹{correct}।"
            elif lang == "bn":
                prompt = f"হস্তশিল্প মেলায় বাঁশের জিনিসের দাম ₹{a} এবং একটি থলির দাম ₹{b}। দুটির মোট দাম কত?"
                explanation = f"মোট দাম হলো ₹{correct}।"
            elif lang == "hi":
                prompt = f"हस्तशिल्प बाजार में बांस की टोकरी की कीमत ₹{a} और थैले की कीमत ₹{b} है। दोनों का कुल मूल्य क्या होगा?"
                explanation = f"कुल मूल्य ₹{correct} है।"
            else:
                prompt = f"At the local craft bazaar, bamboo coasters cost ₹{a} and a handmade pouch costs ₹{b}. What is the total cost for both?"
                explanation = f"The total cost is ₹{correct}."
        else:
            total = a + b
            correct = a
            distractors = [correct - 5, correct + 5, correct + 10]
            if lang == "as":
                prompt = f"পাহাৰৰ বাছ যাত্ৰাটোৰ বাবে মুঠ {total} মিনিট সময় লাগে। যদি ইতিমধ্যে {b} মিনিট পাৰ হৈ গৈছে, তেন্তে আৰু কিমান মিনিট বাকী আছে?"
                explanation = f"আৰু {correct} মিনিট বাকী আছে।"
            elif lang == "bn":
                prompt = f"পাহাড়ে বাসযাত্রার মোট সময় {total} মিনিট। যদি {b} মিনিট পার হয়ে গিয়ে থাকে, তবে আর কত মিনিট বাকি?"
                explanation = f"আর {correct} মিনিট বাকি।"
            elif lang == "hi":
                prompt = f"पहाड़ की बस यात्रा में {total} मिनट लगते हैं। यदि {b} मिनट बीत चुके हैं, तो और कितने मिनट शेष हैं?"
                explanation = f"और {correct} मिनट बाकी हैं।"
            else:
                prompt = f"A bus journey to the hill station takes {total} minutes. If {b} minutes have already passed, how many minutes are left?"
                explanation = f"There are {correct} minutes left."
    else:  # Hard
        unit_price = random.choice([10, 15, 20])
        qty = random.choice([2, 3])
        bill = unit_price * qty
        paid = 50 if bill < 50 else 100
        correct = paid - bill
        distractors = [correct - 5, correct + 10, max(5, correct - 10)]
        if lang == "as":
            prompt = f"আপুনি প্ৰতিখন ₹{unit_price} দৰত {qty} খন চাহৰ ৰুমাল কিনি দোকানীজনক ₹{paid} টকাৰ নোট এখন দিলে। আপুনি কিমান টকা ওভতাই পাব?"
            explanation = f"আপুনি ₹{correct} ঘূৰাই পাব।"
        elif lang == "bn":
            prompt = f"আপনি প্রতিটি ₹{unit_price} দরে {qty} টি চায়ের ন্যাপকিন কিনে দোকানদারকে ₹{paid} টাকার নোট দিলেন। কত টাকা ফেরত পাবেন?"
            explanation = f"আপনি ₹{correct} ফেরত পাবেন।"
        elif lang == "hi":
            prompt = f"आपने ₹{unit_price} प्रति पीस के हिसाब से {qty} चाय के नैपकिन खरीदे और दुकानदार को ₹{paid} का नोट दिया। आपको कितने रुपये वापस मिलेंगे?"
            explanation = f"आपको ₹{correct} वापस मिलेंगे।"
        else:
            prompt = f"You purchase {qty} handwoven tea napkins at ₹{unit_price} each and hand the shopkeeper a ₹{paid} note. How much change will you receive back?"
            explanation = f"You will receive ₹{correct} back."

    choices_math = list(set([str(correct)] + [str(d) for d in distractors if d != correct]))
    while len(choices_math) < 3:
        choices_math.append(str(correct + len(choices_math) + 1))
    random.shuffle(choices_math)
    
    cat_math = {
        "en": "Everyday Story Math 🧮",
        "as": "দৈনন্দিন হিচাপ-নিকাচ 🧮",
        "bn": "দৈনন্দিন সহজ অঙ্ক 🧮",
        "hi": "दैनिक हिसाब-किताब 🧮",
    }.get(lang, "Everyday Story Math 🧮")
    
    questions.append({
        "category": cat_math,
        "question": prompt,
        "choices": choices_math,
        "answer": str(correct),
        "explanation": explanation,
    })

    # 2. Number & Pattern Question
    if lvl == "Easy":
        pattern_type = random.choice(["twos", "fives", "tens"])
        if pattern_type == "twos":
            start = random.choice([2, 4, 6])
            seq = [start + 2 * i for i in range(4)]
            correct = seq[3]
            distractors = [correct - 1, correct + 2, correct + 1]
            prompts = {
                "en": f"What number comes next in this count: {seq[0]}, {seq[1]}, {seq[2]}, ...?",
                "as": f"এই সহজ গণনাত পৰৱৰ্তী সংখ্যাটো কি হ'ব: {seq[0]}, {seq[1]}, {seq[2]}, ...?",
                "bn": f"এই সহজ গণনায় পরবর্তী সংখ্যাটি কি হবে: {seq[0]}, {seq[1]}, {seq[2]}, ...?",
                "hi": f"इस गिनती में अगला अंक क्या होगा: {seq[0]}, {seq[1]}, {seq[2]}, ...?",
            }
        elif pattern_type == "fives":
            start = random.choice([5, 10, 15])
            seq = [start + 5 * i for i in range(4)]
            correct = seq[3]
            distractors = [correct - 5, correct + 5, correct + 2]
            prompts = {
                "en": f"Counting by 5s: {seq[0]}, {seq[1]}, {seq[2]}, ... what comes next?",
                "as": f"৫ কৈ গণনা: {seq[0]}, {seq[1]}, {seq[2]}, ... ইয়াৰ পিছত কি আহিব?",
                "bn": f"৫ করে গণনা: {seq[0]}, {seq[1]}, {seq[2]}, ... এরপর কি আসবে?",
                "hi": f"५-५ की गिनती: {seq[0]}, {seq[1]}, {seq[2]}, ... आगे क्या आएगा?",
            }
        else:
            start = random.choice([10, 20, 30])
            seq = [start + 10 * i for i in range(4)]
            correct = seq[3]
            distractors = [correct - 10, correct + 10, correct + 5]
            prompts = {
                "en": f"Counting by 10s: {seq[0]}, {seq[1]}, {seq[2]}, ... what comes next?",
                "as": f"১০ কৈ গণনা: {seq[0]}, {seq[1]}, {seq[2]}, ... পৰৱৰ্তী সংখ্যাটো কি?",
                "bn": f"১০ করে গণনা: {seq[0]}, {seq[1]}, {seq[2]}, ... এর পরের সংখ্যাটি কি?",
                "hi": f"१०-१० की गिनती: {seq[0]}, {seq[1]}, {seq[2]}, ... अगली संख्या क्या होगी?",
            }
    elif lvl == "Medium":
        step = random.choice([3, 4, -5])
        if step > 0:
            start = random.choice([3, 6, 9])
            seq = [start + step * i for i in range(5)]
            correct = seq[4]
            distractors = [correct - step, correct + step, correct + 2]
            prompts = {
                "en": f"Find the next number in pattern: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?",
                "as": f"আৰ্হিটো লক্ষ্য কৰি পৰৱৰ্তী সংখ্যা বাছক: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?",
                "bn": f"প্যাটার্ন অনুযায়ী পরবর্তী সংখ্যাটি খুঁজুন: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?",
                "hi": f"पैटर्न के अनुसार अगली संख्या पहचानें: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?",
            }
        else:
            start = random.choice([50, 45, 40])
            seq = [start + step * i for i in range(5)]
            correct = seq[4]
            distractors = [correct + 5, correct - 5, correct - 2]
            prompts = {
                "en": f"Counting backwards: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?",
                "as": f"পিছলৈ গণনা: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?",
                "bn": f"উল্টো দিকে গণনা: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?",
                "hi": f"उल्टी गिनती: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?",
            }
    else:  # Hard
        p_type = random.choice(["doubling", "step7"])
        if p_type == "doubling":
            seq = [2, 4, 8, 16]
            correct = 32
            distractors = [24, 30, 36]
            prompts = {
                "en": f"Each step doubles: 2, 4, 8, 16, ... what comes next?",
                "as": f"প্ৰতিটো খোজত দুগুণ হয়: ২, ৪, ৮, ১৬, ... ইয়াৰ পিছত কি আহিব?",
                "bn": f"প্রতি পদে দ্বিগুণ হচ্ছে: ২, ৪, ৮, ১৬, ... এরপর কি আসবে?",
                "hi": f"हर कदम पर दोगुना हो रहा है: २, ४, ८, १६, ... आगे क्या होगा?",
            }
        else:
            seq = [7, 14, 21, 28]
            correct = 35
            distractors = [32, 34, 42]
            prompts = {
                "en": f"Multiples of 7 (Weekly cycle): 7, 14, 21, 28, ...?",
                "as": f"৭ ৰ গুণনীয়ক (সপ্তাহৰ চক্ৰ): ৭, ১৪, ২১, ২৮, ...?",
                "bn": f"৭ এর গুণিতক (সাপ্তাহিক চক্র): ৭, ১৪, ২১, ২৮, ...?",
                "hi": f"७ का पहाड़ा (साप्ताहिक क्रम): ७, १४, २१, २८, ...?",
            }

    choices_pat = list(set([str(correct)] + [str(d) for d in distractors if d != correct]))
    while len(choices_pat) < 3:
        choices_pat.append(str(correct + len(choices_pat) + 1))
    random.shuffle(choices_pat)
    
    cat_pat = {
        "en": "Number & Time Patterns ⏰",
        "as": "সংখ্যা আৰু সময়ৰ আৰ্হি ⏰",
        "bn": "সংখ্যা ও সময়ের বিন্যাস ⏰",
        "hi": "संख्या एवं समय पैटर्न ⏰",
    }.get(lang, "Number & Time Patterns ⏰")

    expl_pat = {
        "en": f"The next number is {correct}.",
        "as": f"পৰৱৰ্তী সংখ্যাটো হ'ল {correct}।",
        "bn": f"পরবর্তী সংখ্যাটি হলো {correct}।",
        "hi": f"अगला अंक {correct} है।",
    }.get(lang, f"The next number is {correct}.")

    questions.append({
        "category": cat_pat,
        "question": prompts.get(lang, prompts["en"]),
        "choices": choices_pat,
        "answer": str(correct),
        "explanation": expl_pat,
    })

    # 3. Word Association & Cognitive Knowledge
    WORD_BANKS = {
        "en": {
            "Easy": [
                ("Which of these flowers is traditionally welcomed in home gardens across Northeast India?", ["Marigold 🌼", "Teapot 🫖", "Blanket 🧶"], "Marigold 🌼"),
                ("Which of these is a fresh, crisp fruit you can slice and enjoy for breakfast?", ["Juicy Apple 🍎", "Warm Shawl 🧣", "Reading Glasses 👓"], "Juicy Apple 🍎"),
                ("Which of these items would you wear when the morning air is chilly?", ["Warm Shawl 🧣", "Hand Fan 🪭", "Sunglasses 🕶️"], "Warm Shawl 🧣"),
                ("Which of these objects helps you pour and share warm morning tea?", ["Teapot 🫖", "Hammer 🔨", "Umbrella ☂️"], "Teapot 🫖"),
                ("Which animal is known for singing sweet morning songs from the treetops?", ["Songbird 🐦", "Goldfish 🐟", "Tortoise 🐢"], "Songbird 🐦"),
            ],
            "Medium": [
                ("Complete the analogy: **Sun** is to **Daytime** as **Moon** is to [ ? ]", ["Nighttime 🌙", "Afternoon ☀️", "Rainstorm 🌧️"], "Nighttime 🌙"),
                ("Complete the analogy: **Fish** is to **River** as **Bird** is to [ ? ]", ["Sky & Trees 🌳", "Deep Ocean 🌊", "Dark Cave 🪨"], "Sky & Trees 🌳"),
                ("Complete the association: **Book** is to **Reading** as **Music** is to [ ? ]", ["Listening 🎧", "Cooking 🍳", "Writing ✏️"], "Listening 🎧"),
                ("Which of these pairs belong together in the traditional kitchen?", ["Mortar & Pestle 🥣", "Bicycle & Oar 🚲", "Clock & Umbrella ⏰"], "Mortar & Pestle 🥣"),
            ],
            "Hard": [
                ("Odd one out: Which item does NOT belong with the others in this transport group?", ["Sparrow 🐦", "Bicycle 🚲", "Ferry Boat ⛵", "Bullock Cart 🛺"], "Sparrow 🐦"),
                ("Which craft is Assam and the Northeast world-renowned for weaving from golden threads?", ["Muga Golden Silk 🧵", "Terracotta Tiles 🧱", "Glass Beads 🔮"], "Muga Golden Silk 🧵"),
                ("Odd one out: Which of these items is NOT used for writing or sending messages?", ["Iron Key 🔑", "Postcard ✉️", "Fountain Pen ✒️"], "Iron Key 🔑"),
            ],
        },
        "as": {
            "Easy": [
                ("অসম তথা উত্তৰ-পূৰ্বাঞ্চলৰ ঘৰৰ ফুলনি বাৰীত সাধাৰণতে কোনবিধ ফুল দেখা পোৱা যায়?", ["গেন্দা ফুল 🌼", "চাহৰ কেটলি 🫖", "চেলেং 🧶"], "গেন্দা ফুল 🌼"),
                ("ৰাতিপুৱা স্বাস্থ্যৰ বাবে খাব পৰা এবিধ সতেজ আৰু সোৱাদভৰা ফল কি?", ["ৰসাল আপেল 🍎", "উমাল চাদৰ 🧣", "চশমা 👓"], "ৰসাল আপেল 🍎"),
                ("ৰাতিপুৱা জাৰ বা ঠাণ্ডা পৰিলে আপুনি কি কাপোৰ ল'ব?", ["উমাল চাদৰ 🧣", "বিচনী 🪭", "ৰ'দচশমা 🕶️"], "উমাল চাদৰ 🧣"),
                ("ৰাতিপুৱা গৰম চাহ বাকি খোৱাত কি পাত্ৰই সহায় কৰে?", ["চাহৰ কেটলি 🫖", "হাতুৰী 🔨", "ছাতি ☂️"], "চাহৰ কেটলি 🫖"),
                ("গছৰ ডালত বহি মিঠা মাত মাতি পুৱা শুনোৱা প্ৰাণীবিধ কি?", ["গায়ক চৰাই 🐦", "সোণালী মাছ 🐟", "কাছ 🐢"], "গায়ক চৰাই 🐦"),
            ],
            "Medium": [
                ("উপমা সম্পূৰ্ণ কৰক: **সূৰ্য** যদি **দিনৰ** হয়, তেন্তে **জোন** কাৰ [ ? ]", ["ৰাতিৰ 🌙", "দুপৰীয়াৰ ☀️", "বৰষুণৰ 🌧️"], "ৰাতিৰ 🌙"),
                ("উপমা সম্পূৰ্ণ কৰক: **মাছ** থাকে **নৈত**, তেন্তে **চৰাই** থাকে [ ? ]", ["আকাশ আৰু গছত 🌳", "সাগৰৰ তলিত 🌊", "গুহাত 🪨"], "আকাশ আৰু গছত 🌳"),
                ("সম্পৰ্ক মিলাওক: **কিতাপ** হ'ল **পঢ়াৰ** বাবে, তেন্তে **সংগীত** হ'ল [ ? ]", ["শুনাৰ বাবে 🎧", "ৰন্ধাৰ বাবে 🍳", "লিখাৰ বাবে ✏️"], "শুনাৰ বাবে 🎧"),
                ("পুৰণি পাকঘৰত কোনযোৰ বস্তু সদায় একেলগে থাকে?", ["উখল আৰু পটা 🥣", "চাইকেল আৰু বঠা 🚲", "ঘড়ী আৰু ছাতি ⏰"], "উখল আৰু পটা 🥣"),
            ],
            "Hard": [
                ("অমিলটো বাছক: তলৰ যাতায়াতৰ মাধ্যমসমূহৰ ভিতৰত কোনটো সুকীয়া?", ["ঘৰচিৰিকা 🐦", "চাইকেল 🚲", "নাও ⛵", "গৰু গাড়ী 🛺"], "ঘৰচিৰিকা 🐦"),
                ("অসমৰ কোনটো বিখ্যাত বস্ত্ৰশিল্প সোণালী সূতাৰ বাবে বিশ্বখ্যাত?", ["মুগা ৰেচম 🧵", "মাটিৰ টাইলছ 🧱", "কাঁচৰ মণি 🔮"], "মুগা ৰেচম 🧵"),
                ("অমিলটো বাছক: বাৰ্তা প্ৰেৰণ বা লিখাৰ লগত কোনটো বস্তু জড়িত নহয়?", ["লোৰ চাবি 🔑", "ডাক চিঠি ✉️", "ফাউণ্টেন পেন ✒️"], "লোৰ চাবি 🔑"),
            ],
        },
        "bn": {
            "Easy": [
                ("উত্তর-পূর্বাঞ্চল ও বাংলার বাগানে কোন ফুলটি প্রায়ই ফুটে থাকতে দেখা যায়?", ["গাঁদা ফুল 🌼", "চায়ের কেটলি 🫖", "কंबल 🧶"], "গাঁদা ফুল 🌼"),
                ("সকালে খাওয়ার মতো একটি তাজা ও পুষ্টিকর ফল কোনটি?", ["মিষ্টি আপেল 🍎", "উলের শাল 🧣", "পড়ার চশমা 👓"], "মিষ্টি আপেল 🍎"),
                ("সকালে শীত লাগলে গায়ে দেওয়ার উপযোগী কোনটি?", ["উলের শাল 🧣", "হাতপাখা 🪭", "রোদচশমা 🕶️"], "উলের শাল 🧣"),
                ("সকালের গরম চা ঢেলে দেওয়ার জন্য কোনটি ব্যবহৃত হয়?", ["চায়ের কেটলি 🫖", "হাতুড়ি 🔨", "ছাতা ☂️"], "চায়ের কেটলি 🫖"),
                ("গাছের ডালে বসে মিষ্টি গান শোনায় কোন প্রাণী?", ["দোয়েল পাখি 🐦", "রুই মাছ 🐟", "কচ্ছপ 🐢"], "দোয়েল পাখি 🐦"),
            ],
            "Medium": [
                ("সাদৃশ্য পূরণ করুন: **সূর্য** যেমন **দিনের**, তেমনি **চাঁদ** হলো [ ? ]", ["রাতের 🌙", "দুপুরের ☀️", "ঝড়ের 🌧️"], "রাতের 🌙"),
                ("সাদৃশ্য পূরণ করুন: **মাছ** থাকে **নদীতে**, তেমনি **পাখি** থাকে [ ? ]", ["গাছে ও আকাশে 🌳", "সমুদ্রের গভীরে 🌊", "গুহায় 🪨"], "গাছে ও আকাশে 🌳"),
                ("সম্পর্ক মেলান: **বই** যদি **পড়ার** হয়, তবে **গান** হলো [ ? ]", ["শোনার 🎧", "রান্না করার 🍳", "লেখার ✏️"], "শোনার 🎧"),
                ("রান্নাঘরে নিচের কোন জোড়াটি একসঙ্গে ব্যবহৃত হয়?", ["শিল ও নোড়া 🥣", "সাইকেল ও দাঁড় 🚲", "ঘড়ি ও ছাতা ⏰"], "শিল ও নোড়া 🥣"),
            ],
            "Hard": [
                ("বেমানান শব্দটি খুঁজুন: যাতায়াতের মাধ্যমের মধ্যে কোনটি আলাদা?", ["চড়ুই পাখি 🐦", "সাইকেল 🚲", "নৌকা ⛵", "গরুর গাড়ি 🛺"], "চড়ুই পাখি 🐦"),
                ("আসামের কোন ঐতিহ্যবাহী রেশম সোনালী রঙের জন্য বিশ্বখ্যাত?", ["মুগা সিল্ক 🧵", "টেরাকোটা 🧱", "কাঁচের পুঁতি 🔮"], "মুগা সিল্ক 🧵"),
                ("বেমানান কোনটি: বার্তা পাঠানো বা লেখার সাথে কোনটি সম্পর্কিত নয়?", ["লোহার চাবি 🔑", "পোস্টকার্ড ✉️", "কলম ✒️"], "লোহার চাবি 🔑"),
            ],
        },
        "hi": {
            "Easy": [
                ("घरों के बगीचों में आमतौर पर कौन सा सुंदर फूल दिखाई देता है?", ["गेंदा फूल 🌼", "चाय की केतली 🫖", "कंबल 🧶"], "गेंदा फूल 🌼"),
                ("सुबह के समय खाने योग्य ताजा एवं मीठा फल कौन सा है?", ["रसीला सेब 🍎", "ऊनी शॉल 🧣", "चश्मा 👓"], "रसीला सेब 🍎"),
                ("सुबह के समय हल्की ठंड होने पर आप क्या ओढ़ना पसंद करेंगे?", ["ऊनी शॉल 🧣", "हाथ का पंखा 🪭", "धूप का चश्मा 🕶️"], "ऊनी शॉल 🧣"),
                ("गरमा-गरम चाय परोसने के लिए किसका उपयोग किया जाता है?", ["चाय की केतली 🫖", "हथौड़ा 🔨", "छाता ☂️"], "चाय की केतली 🫖"),
                ("पेड़ की डाल पर बैठकर मधुर गीत गाने वाला जीव कौन सा है?", ["गायक पक्षी 🐦", "सुनहरी मछली 🐟", "कछुआ 🐢"], "गायक पक्षी 🐦"),
            ],
            "Medium": [
                ("समानता पूरी करें: **सूरज** यदि **दिन** का है, तो **चांद** किसका है [ ? ]", ["रात का 🌙", "दोपहर का ☀️", "आंधी-तूफान का 🌧️"], "रात का 🌙"),
                ("समानता पूरी करें: **मछली** रहती है **नदी** में, तो **पक्षी** रहता है [ ? ]", ["आकाश व पेड़ों पर 🌳", "गहरे समुद्र में 🌊", "गुफा में 🪨"], "आकाश व पेड़ों पर 🌳"),
                ("संबंध जोड़ें: **किताब** यदि **पढ़ने** के लिए है, तो **संगीत** किसके लिए है [ ? ]", ["सुनने के लिए 🎧", "खाना पकाने के लिए 🍳", "लिखने के लिए ✏️"], "सुनने के लिए 🎧"),
                ("पारंपरिक रसोई में कौन सी जोड़ी एक साथ इस्तेमाल होती है?", ["ओखली और मूसल 🥣", "साइकिल और पतवार 🚲", "घड़ी और छाता ⏰"], "ओखली और मूसल 🥣"),
            ],
            "Hard": [
                ("भिन्न को पहचानें: यातायात के साधनों में कौन सा अलग है?", ["गौरैया 🐦", "साइकिल 🚲", "नाव ⛵", "बैलगाड़ी 🛺"], "गौरैया 🐦"),
                ("असम का कौन सा रेशम सुनहरे धागों के लिए विश्व प्रसिद्ध है?", ["मूंगा सिल्क 🧵", "टेराकोटा टाइल्स 🧱", "कांच के मोती 🔮"], "मूंगा सिल्क 🧵"),
                ("भिन्न को पहचानें: संदेश भेजने या लिखने से क्या संबंधित नहीं है?", ["लोहे की चाबी 🔑", "पोस्टकार्ड ✉️", "स्याही वाला पेन ✒️"], "लोहे की चाबी 🔑"),
            ],
        },
    }

    w_dict = WORD_BANKS.get(lang, WORD_BANKS["en"])
    bank = w_dict.get(lvl, w_dict["Easy"])
    w_prompt, w_choices, w_ans = random.choice(bank)
    w_shuffled = list(w_choices)
    random.shuffle(w_shuffled)
    
    cat_word = {
        "en": "Word & World Association 🌿",
        "as": "শব্দ আৰু চিনাকি জগত 🌿",
        "bn": "শব্দ ও পরিচিত জগৎ 🌿",
        "hi": "शब्द एवं सांसारिक ज्ञान 🌿",
    }.get(lang, "Word & World Association 🌿")

    questions.append({
        "category": cat_word,
        "question": w_prompt,
        "choices": w_shuffled,
        "answer": w_ans,
        "explanation": f"{w_ans}",
    })

    return questions


# ==========================================
# Localized Cardinal Directions & Guidance
# ==========================================

COMPASS_CARDINALS = {
    "en": [
        ("North", "⬆️"), ("North-East", "↗️"), ("East", "➡️"), ("South-East", "↘️"),
        ("South", "⬇️"), ("South-West", "↙️"), ("West", "⬅️"), ("North-West", "↖️"),
    ],
    "as": [
        ("উত্তৰ (North)", "⬆️"), ("উত্তৰ-পূব (North-East)", "↗️"), ("পূব (East)", "➡️"), ("দক্ষিণ-পূব (South-East)", "↘️"),
        ("দক্ষিণ (South)", "⬇️"), ("দক্ষিণ-পশ্চিম (South-West)", "↙️"), ("পশ্চিম (West)", "⬅️"), ("উত্তৰ-পশ্চিম (North-West)", "↖️"),
    ],
    "bn": [
        ("উত্তর (North)", "⬆️"), ("উত্তর-পূর্ব (North-East)", "↗️"), ("পূর্ব (East)", "➡️"), ("দক্ষিণ-পূর্ব (South-East)", "↘️"),
        ("দক্ষিণ (South)", "⬇️"), ("দক্ষিণ-পশ্চিম (South-West)", "↙️"), ("পশ্চিম (West)", "⬅️"), ("উত্তর-পশ্চিম (North-West)", "↖️"),
    ],
    "hi": [
        ("उत्तर (North)", "⬆️"), ("उत्तर-पूर्व (North-East)", "↗️"), ("पूर्व (East)", "➡️"), ("दक्षिण-पूर्व (South-East)", "↘️"),
        ("दक्षिण (South)", "⬇️"), ("दक्षिण-पश्चिम (South-West)", "↙️"), ("पश्चिम (West)", "⬅️"), ("उत्तर-पश्चिम (North-West)", "↖️"),
    ],
}


def get_compass_cardinal(bearing: float, lang: str = "en") -> str:
    cardinals = COMPASS_CARDINALS.get(lang, COMPASS_CARDINALS["en"])
    idx = int((bearing + 22.5) // 45) % 8
    name, arrow = cardinals[idx]
    return f"{name} {arrow}"


def get_navigation_guidance_dict(distance_m: float, heading: str, lang: str = "en") -> dict[str, str]:
    """Return localized navigation guidance based on distance."""
    if distance_m < 60:
        return {
            "status": "at_home",
            "badge_color": "#2f6f68",
            "badge_bg": "#dcebe5",
            "title": t("nav_at_home_title", lang),
            "distance_text": t("nav_at_home_dist", lang, dist=int(distance_m)),
            "guidance": t("nav_at_home_guidance", lang),
            "action_advice": t("nav_at_home_advice", lang),
        }
    elif distance_m < 500:
        return {
            "status": "near_home",
            "badge_color": "#1f554f",
            "badge_bg": "#e6f0ea",
            "title": t("nav_near_home_title", lang),
            "distance_text": t("nav_near_home_dist", lang, dist=int(distance_m)),
            "guidance": t("nav_near_home_guidance", lang, heading=heading),
            "action_advice": t("nav_near_home_advice", lang),
        }
    elif distance_m < 2000:
        km = distance_m / 1000.0
        return {
            "status": "moderate_distance",
            "badge_color": "#9a6410",
            "badge_bg": "#fff4dc",
            "title": t("nav_mod_dist_title", lang),
            "distance_text": t("nav_mod_dist_dist", lang, dist=km),
            "guidance": t("nav_mod_dist_guidance", lang, heading=heading),
            "action_advice": t("nav_mod_dist_advice", lang),
        }
    else:
        km = distance_m / 1000.0
        return {
            "status": "far",
            "badge_color": "#8f3f35",
            "badge_bg": "#fde8e5",
            "title": t("nav_far_title", lang),
            "distance_text": t("nav_far_dist", lang, dist=km),
            "guidance": t("nav_far_guidance", lang),
            "action_advice": t("nav_far_advice", lang),
        }
