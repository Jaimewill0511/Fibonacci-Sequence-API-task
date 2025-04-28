from flask import Flask, request, jsonify
import logging; logging.basicConfig(level=logging.INFO)


MAX_N = 92  # keep the 64-bit-safe guardrail

def create_app():
    app = Flask(__name__)

    def fibonacci_sequence(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    @app.route("/health")
    def health():
        return jsonify(status="healthy"), 200 # health check endpoint


    @app.route("/fibonacci")
    def fibonacci_endpoint():
        # param missing
        if "n" not in request.args:
            return jsonify(error="query param 'n' is required"), 400

        try:
            n = int(request.args["n"])
            
        except (KeyError, ValueError):
            return jsonify(error="query param 'n' must be an integer"), 400 # check if n is an integer
        
        # Negative n
        if n < 0:
            return jsonify(error="Parameter 'n' must be a non-negative integer"), 400 # check if n is non-negative
        
         # too large
        if n > MAX_N:
            return jsonify(error=f"Parameter 'n' exceeds maximum allowed value ({MAX_N})"), 400 # check if n is in the range of 0 to 92 to avoid overflow and performance issues(e,g DOS attacks)
        
        logging.info("Request handled: n=%s", n) # log the request for debugging purposes
        return jsonify(n=n, fibonacci=fibonacci_sequence(n))

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000)
