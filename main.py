from flask import Flask, render_template, redirect, url_for, request
from google_play_scraper import app, Sort, reviews





app = Flask(__name__)


@app.route('/app/<app_name>')
def app_name(app_name):   # <-- function called app_name
    result = app (
        app_name,
        lang="en",
        country="us",
    )
    review, continuation_token = reviews(
        app_name,
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.NEWEST
        count=3, # defaults to 100
        filter_score_with=5 # defaults to None(means all score)
    )
    realInstalls = result['realInstalls']
    score = result['score']

    return render_template("app.html", app_name=app_name,installs=realInstalls,score=score,review=review)

@app.route('/', methods=['POST','GET'])
def default():
    if request.method == "POST":
        app_name = request.form.get("link")
        app_name = app_name.split('id=')[1]
        return redirect(url_for("app_name", app_name=app_name))  # <-- matches function
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=1001)


# from google_play_scraper import app
# from google_play_scraper import Sort, reviews



# app_name = "np.edu.dwit.dlc"

# result = app (
#     app_name,
#     lang="en",
#     country="us",
# )

# review, continuation_token = reviews(
#     'com.fantome.penguinisle',
#     lang='en', # defaults to 'en'
#     country='us', # defaults to 'us'
#     sort=Sort.NEWEST, # defaults to Sort.NEWEST
#     count=3, # defaults to 100
#     filter_score_with=5 # defaults to None(means all score)
# )

# # If you pass `continuation_token` as an argument to the reviews function at this point,
# # it will crawl the items after 3 review items.

# review, _ = reviews(
#     'com.fantome.penguinisle',
#     continuation_token=continuation_token # defaults to None(load from the beginning)
# )

# realInstalls = result['realInstalls']
# score = result['score']
# reviewNumber = 2

# while reviewNumber != 0:
#     print(review[reviewNumber])
#     reviewNumber = reviewNumber - 1


