from flask import Flask, render_template

app = Flask(__name__, template_folder = "templates")

tourist_dict = {
"Daniel": "Male",
"Hadar": "Female",
"Osama": "Male",
"Katherine":"Female"
}

# tourist_dict = {
# 	"Majd":"Male",
# 	"Ella":"Female",
# 	"Nadav":"Male",
# 	"Hala":"Female"
# }

@app.route("/")
def home():
	return render_template("Kazakh_Guide.html", tourist_dict=tourist_dict)


@app.route("/personal/<name>")
def personal(name):
	return render_template("Personal.html", name = name)

if __name__ == '__main__':
	app.run(debug = True)