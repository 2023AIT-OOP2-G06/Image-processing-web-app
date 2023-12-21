import datetime

from flask import Flask, request, render_template
import random  # ランダムデータ作成のためのライブラリ

app = Flask(__name__)

# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）


@app.route('/')
def index():
    return render_template('index.html')


# 2. じゃんけんアプリの入力フォーム
@app.route('/janken')
def janken():
    # じゃんけんの入力画面のテンプレートを呼び出し
    return render_template('janken_form.html')


@app.route('/janken/play', methods=["POST"])
def janken_play():

    # <input type="text" id="your_name" name="name">
    name = request.form.get("name")
    if not name:
        name = "名無しさん"

    # <input type="radio" id="hand_rock" value="rock" name="hand">
    # <input type="radio" id="hand_scissor" value="scissor" name="hand">
    # <input type="radio" id="hand_paper" value="paper" name="hand">
    hand = request.form.get("hand", None)

    settai_value = request.form.get("is_settai", "False")
    is_settai = True if settai_value == "True" else False

    # リストの中からランダムに選ぶ
    cpu = random.choice(["rock", "scissor", "paper"])

    # 接待モードの場合は、必ず勝つようにする
    if is_settai and hand is None:
        hand = "rock"

    if is_settai:
        if hand == "rock":
            cpu = "scissor"
        elif hand == "scissor":
            cpu = "paper"
        elif hand == "paper":
            cpu = "rock"

    # じゃんけん処理
    result_message = ""
    result_message_style = ""
    if hand == cpu:
        result_message = "あいこ"
    else:
        if hand == "rock":
            if cpu == "scissor":
                result_message = "{}の勝ち".format(name)
                result_message_style = "color: red;"
            else:
                result_message = "{}の負け".format(name)
        elif hand == "scissor":
            if cpu == "paper":
                result_message = "{}の勝ち".format(name)
                result_message_style = "color: red;"
            else:
                result_message = "{}の負け".format(name)
        elif hand == "paper":
            if cpu == "rock":
                result_message = "{}の勝ち".format(name)
                result_message_style = "color: red;"
            else:
                result_message = "{}の負け".format(name)
        else:
            result_message = "後出しはダメです。"

    # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
    return render_template('janken_play.html',
                           result_message=result_message,
                           name=name,
                           hand=hand,
                           cpu=cpu,
                           result_message_style=result_message_style)

# ====================================================================================================
# 3. 占いアプリの入力フォーム
def generate_star(result: int) -> str:
    return "★" * result + "☆" * (5 - result)

def calculate_fortune(birthdate, name):
    try:
        # 入力不備のチェック
        if not birthdate or not name:
            return 1, "入力不備で占えませんでした"

        # 生年月日のフォーマットチェックと計算
        birthdate_obj = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.datetime.now()
        
        # 計算式に基づく占いの算出
        date_diff = abs(int(today.strftime("%Y%m%d")) - int(birthdate_obj.strftime("%Y%m%d")))
        index_list = [5, 1, 3, 2, 4]

        result = index_list[(date_diff * len(name)) % 5]

        fortune_messages = [
            "運勢はあまり良くないです。",
            "ちょっと注意が必要です。",
            "普通の運勢です。",
            "良い運勢です。",
            "最高の運勢です！",
        ]
        
        message = fortune_messages[result-1]
        
        return generate_star(result), message
    except ValueError:
        return 1, "入力不備で占えませんでした"

@app.route('/uranai', methods=['GET'])
def uranai():
    return render_template('uranai_form.html')

@app.route('/uranai/play', methods=['POST'])
def uranai_play():
    birthdate = request.form['birthdate']
    name = request.form['name']
    
    fortune_result, message = calculate_fortune(birthdate, name)
    return render_template('uranai_play.html', fortune_result=fortune_result, message=message)


if __name__ == '__main__':
    app.run()
