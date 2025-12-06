mood_grouping = {
    "happy" : ["happy", "amazing", "wonderful", "excited", "contented", "cheerful", "cheery", 
              "joyful", "jolly", "gleeful", "delighted", "smiling", "beaming", "grinning", 
              "glowing", "satisfied", "blithe", "joyous", "beatific", "blessed", "thrilled", 
              "elated", "exhilarated", "ecstatic", "blissful", "euphoric", "overjoyed", 
              "on cloud nine", "over the moon", "glad", "fortunate", "lucky", "favourable",
               "good", "right"],

    "sad"   : ["sad", "terrible", "depressed", "unhappy", "sorrowful", "dejected", "miserable", "low",
               "down", "gloomy", "blue", "melancholy", "melancholic", "low-spirited", "heartbroken",
               "awful", "wretched", "sorry", "pitiful", "upset", "pathetic", "shameful", "dreadful"],

    "angry" : ["angry", "furious", "mad", "annoyed", "irritated", "displeased", "provoked", "resentful",
               "enraged", "fuming", "outraged", "bad-tempered", "hot-tempered", "short-tempered", 
               "riled", "pissed"]
}

def sentence_checker(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace("-", " ")

    for p in ["!", "@", "#", "$", "%", "^", "&", "*", "_", ".", ",", "?", ";", ":", "'"]:
        sentence = sentence.replace(p, "")

    sentence = " ".join(sentence.split())
    return sentence
