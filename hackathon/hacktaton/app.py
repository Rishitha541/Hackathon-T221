# from flask import Flask, request, jsonify
# from traffic_logger import log_request, is_ip_blocked

# app = Flask(__name__)

# @app.route('/')
# def home():
#     ip = request.remote_addr
#     if is_ip_blocked(ip):
#         return jsonify({"message": "Access denied"}), 403
#     log_request(ip)
#     return jsonify({"message": "Welcome to the cloud-hosted website!"})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


from flask import Flask, request, render_template
from traffic_logger import log_request, is_ip_blocked

app = Flask(__name__)

@app.route('/')
def home():
    ip = request.remote_addr
    if is_ip_blocked(ip):
        return render_template('index.html', status="blocked", ip=ip)
    log_request(ip)
    return render_template('index.html', status="allowed", ip=ip)

@app.route('/status')
def status():
    ip = request.remote_addr
    blocked = is_ip_blocked(ip)
    return {
        "ip": ip,
        "blocked": blocked,
        "message": "Access Denied" if blocked else "Access Granted"
    }

if __name__ == '__main__':
    app.run(debug=True, port=5000)
