from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/quiz', methods=['POST'])
def quiz():
    data = request.json
    count = sum(data['answers'])
    step = len(data['answers'])
    response = {}

    if step == 1:
        response['question'] = "Your significant other just cheated on you... what do you do?"
        response['choices'] = [
            "Burn his picture... Duh!", 
            "Cry and cry and cry", 
            "Who needs them! I will find someone new!", 
            "Try to work it out", 
            "Revenge."
        ]
    elif step == 2:
        response['question'] = "How do you describe yourself?"
        response['choices'] = [
            "A hopeless romantic", 
            "Loyal", 
            "Caring and fun", 
            "Day dreamer", 
            "Empowered and strong"
        ]
    elif step == 3:
        response['question'] = "Which lyrics resonate most with you?"
        response['choices'] = [
            "This love is difficult, but it's real", 
            "I'd like to be my old self again, But I'm still trying to find it", 
            "Oh my God, look at that face! You look like my next mistake", 
            "August sipped away like a bottle of wine, because you were never mine", 
            "Don't get sad, get even"
        ]
    elif step == 4:
        if count in [4, 5]:
            # Taylor Swift Debut or Fearless
            response['question'] = "Choose a country singer:"
            response['choices'] = ["Tim McGraw", "Keith Urban"]
        elif count in [6, 7, 8, 9]:
            # Speak Now or Red
            response['question'] = "Who do you hate more:"
            response['choices'] = ["John Mayer", "Jake Gyllenhaal"]
        elif count in [10, 11, 12, 13]:
            # 1989 or Lover
            response['question'] = "Choose a hairstyle:"
            response['choices'] = ["Short hair", "Long hair"]
        elif count in [14, 15, 16, 17]:
            # Folklore or Evermore
            response['question'] = "Choose a hairstyle:"
            response['choices'] = ["Flowy hair", "Braids"]
        elif count in [18, 19, 20]:
            # Reputation or Midnights
            response['question'] = "Choose an activity:"
            response['choices'] = ["Doing something bad... but it feels good!", "Going out tonight!"]
        else:
            response['question'] = "End of quiz!"
            response['choices'] = []
    elif step == 5:
        # Last step determines the album
        response = determine_result(count)

    return jsonify(response)

@app.route('/result', methods=['POST'])
def result():
    data = request.json
    count = sum(data['answers'])
    
    result = determine_result(count)
    
    return jsonify(result)

def determine_result(count):
    if count == 3 or count == 4:
        result = "You are... Taylor Swift Debut!"
    elif count == 5 or count == 6:
        result = "You are... Fearless! (Taylor's Version)"
    elif count == 7 or count == 8:
        result = "You are... Speak Now (Taylor's Version)"
    elif count == 9 or count == 10:
        result = "You are... Red! (Taylor's Version)"
    elif count == 11 or count == 12:
        result = "You are... 1989!"
    elif count == 13 or count == 14:
        result = "You are... Lover!"
    elif count == 15 or count == 16:
        result = "You are... Folklore!"
    elif count == 17 or count == 18:
        result = "You are... Evermore!"
    elif count == 19 or count == 20:
        result = "You are... Reputation!"
    elif count == 21 or count == 22:
        result = "You are... Midnights"
    else:
        result = "Sorry, we couldn't determine your album."

    return {'result': result}

if __name__ == '__main__':
    app.run(debug=True)
