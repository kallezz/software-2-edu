from flask import Flask

app = Flask(__name__)


@app.route("/alkuluku/<int:number>")
def alkuluku(number):
    if number <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        return {"number": number, "isPrime": True}
    else:
        return {"number": number, "isPrime": False}
