from flask import Flask, render_template, request
import requests

API_BASE = "http://127.0.0.1:8000"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/improver", methods=["GET", "POST"])
def improver():
    analysis = None
    improved = None

    if request.method == "POST":
        text = request.form["text"]
        rewrite = request.form.get("rewrite") == "on"

        payload = {
            "text": text,
            "rewrite": rewrite
        }

        response = requests.post(f"{API_BASE}/improver/improve-paper", json=payload)
        data = response.json()
        analysis = data["analysis"]
        improved = data.get("improved_text")

    return render_template("improver.html", analysis=analysis, improved=improved)


@app.route("/suggestion", methods=["GET", "POST"])
def suggestion():
    results = None

    if request.method == "POST":
        query = request.form["query"]
        domains = request.form.getlist("domains")
        top_n = int(request.form.get("top_n", 5))

        payload = {
            "query": query,
            "domains": domains,
            "top_n": top_n
        }

        try:
            response = requests.post(f"{API_BASE}/suggestion/suggest-papers", json=payload)
            data = response.json()
            results = data.get("results")
        except Exception as e:
            print("ERROR:", e)

    return render_template("suggestion.html", results=results)


@app.route("/qa", methods=["GET", "POST"])
def qa():
    answer = None
    sources = None

    if request.method == "POST":
        question = request.form.get("question")
        domain = request.form.get("domain")

        payload = {
            "question": question,
            "domain": domain
        }

        try:
            response = requests.post(f"{API_BASE}/qa/ask", json=payload)
            data = response.json()

            answer = data.get("answer")
            sources = data.get("sources")

        except Exception as e:
            answer = f"Error: {e}"

    return render_template(
        "qa.html",
        answer=answer,
        sources=sources
    )


if __name__ == "__main__":
    app.run(debug=True)