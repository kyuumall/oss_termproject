mood_grouping = {
    "happy"    : ["happy", "amazing", "wonderful", "excited", "contented", "cheerful", "joyful", 
                  "delighted", "smiling", "beaming", "grinning", "satisfied", "blessed", "elated", 
                  "exhilarated", "ecstatic", "blissful", "euphoric", "overjoyed", "on cloud nine", 
                  "over the moon", "glad", "fortunate", "lucky"],

    "sad"      : ["sad", "terrible", "depressed", "unhappy", "sorrow", "dejected", "miserable",
                   "low", "down", "gloomy", "blue", "melancholy", "low-spirited", "heartbroken", 
                   "awful", "wretched", "pitiful", "upset", "pathetic", "shameful", "dreadful"],

    "angry"    : ["angry", "furious", "mad", "annoyed", "irritated", "displeased", "provoked", 
                  "resentful", "enraged", "fuming", "outraged", "bad-tempered", "hot-tempered", 
                  "short-tempered", "riled", "pissed", "annoying", "grumpy"],

    "neutral"  : ["neutral", "okay", "fine", "good", "so-so", "alright", "nothing special", "normal",
                  "average"],

    "nervous"  : ["nervous", "anxious", "worried", "uneasy", "overthink", "restless", "uptight", "tense",
                  "on edge", "apprehensive", "troubled", "hesitant", "concerned", "jumpy", "antsy", 
                  "distraught", "nerve-racking"],

    "tired"    : ["tired", "sleepy", "exhausted", "fatigued", "worn out", "drained", "drowsy", "burnt out",
                  "overworked", "weary", "worn", "lethargic", "worn-down"],

    "stressed" : ["stressed", "overwhelmed", "pressured", "tense", "distressed", "burdened", "burnout", 
                  "overloaded", "strained", "overburdened", "on the rack", "stressed-out", "aggravated"],

    "good"     : ["good", "great", "nice", "pleasant", "delightful", "pleasing", "fine", "adequate", 
                  "decent", "tolerable", "passable" ]
}

def sentence_checker(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace("-", " ")

    for p in ["!", "@", "#", "$", "%", "^", "&", "*", "_", ".", ",", "?", ";", ":", "'"]:
        sentence = sentence.replace(p, "")

    sentence = " ".join(sentence.split())
    return sentence

training_text = []
training_mood = []

with open("training_data.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if line.startswith('#') or line == "":
            continue
        text, mood = line.split(",")
        text_checked = sentence_checker(text)
        training_text.append(text_checked)
        training_mood.append(mood)

def mood_counter(text):
    text = sentence_checker(text)
    words = text.split()
    emotion = {mood: 0 for mood in mood_grouping}

    for mood, group in mood_grouping.items():
        for word in group:
            if " " in word:
                if f" {word} " in f" {text} ":
                    emotion[mood] += 1
            
            else:
                if word in words:
                    emotion[mood] += 1

    return emotion

def predicting_current_mood(text):
    emotion = mood_counter(text)
    max_value = max(emotion.values())

    if max_value == 0:
        return "neutral"
    
    tied_moods = [mood for mood, count in emotion.items() if count == max_value]

    if len(tied_moods) > 1:
        mood_options = " or ".join(tied_moods)
        user_choice = input(f"I’m sorry but could you clarify again once more whether you feel {mood_options}? ")
        return user_choice.lower()
    
    return tied_moods[0]

import time

def weekly_update():
    log_file = "mood_log.txt"
    counts = {}
    current_week = time.strftime("%U", time.localtime())

    with open(log_file, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            section = line.strip().split(",")
            if len(section) < 2:  # skip lines that don’t have date + mood
                continue
            
            date_str = section[0].strip()
            mood = section[1].strip()

            entry_week = time.strftime("%U", time.strptime(date_str, "%Y-%m-%d %H:%M:%S %A"))

            if entry_week == current_week:
                if mood in counts:
                    counts[mood] += 1
                else:
                    counts[mood] = 1

    if counts:
        print("This week:")
        for m, c in counts.items():
            print(f"{m} → {c}")

        with open("weekly_summary.txt", "a", encoding="utf-8") as f:
            summary = f"Week {current_week}: " + ", ".join(f"{m} → {c}" for m, c in counts.items())
            f.write(summary + "\n")

    else:
        print("No entries for this week yet.")


if __name__ == "__main__":
    import time

    user_text = input("What is your current mood today? ")
    predicted_mood = predicting_current_mood(user_text)

    confirmation = input(f"Do you want to log your mood entry as '{predicted_mood}'? (Y/N) ")

    if confirmation.lower() == "y":
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime())

        tag = input("Any additional notes or tags? (press Enter to skip) ")

        with open("mood_log.txt", "a", encoding="utf-8") as f:
            f.write(f'{timestamp}, {predicted_mood}, "{user_text}", "{tag}"\n')
        print(f"Mood '{predicted_mood}' saved. \n")

        weekly_update()

    else:
        print("Mood entry not saved.")