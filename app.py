from flask import Flask, request, render_template 
from gemini import genContent
from audio import s2t, speakNow

app = Flask(__name__)

class StaticList:
    user_list = []
    gen_list = []

    def get_user_list(self, user_data):
        list1 = self.user_list.append(user_data)
        return list1
    def get_gen_list(self, gen_data):
        list2 = self.gen_list.append(gen_data)
        return list2
    




@app.route('/', methods = ['POST', 'GET'])
def index():
    method = request.method
    user = StaticList()
    if method == 'GET':
        return render_template('index.html')
    else:
        try:
            user_text = request.form['user_text']
            user.user_list.clear()
            user.gen_list.clear()
            user.get_user_list(user_text)
            print(user.user_list)
        except Exception as e:
            print(e)
        try:
            mic = request.form['mic']
            print(mic)
            user_text = s2t()
            user.user_list.clear()
            user.gen_list.clear()
            user.get_user_list(user_text)
            print(user.user_list)
            # print(user_text)
        except Exception as e:
            print(e)

        try:
            speak = request.form['speak-btn']
            speakNow(user.gen_list[0])
            return render_template('index.html', text = user.user_list[0], genText = user.gen_list[0])
        except Exception as e:
            print(e)

        
        
        genText = genContent(user_text)
        user.get_gen_list(genText)
        print(user.gen_list)
        
        return render_template('index.html', text = user_text, genText = genText)

# @app.route('/', methode = ['GET', 'POST'])
# def mic()

if __name__ == '__main__':
    app.run(debug = True)