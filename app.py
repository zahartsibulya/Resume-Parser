# app.py
from flask import Flask, request, jsonify
from infrastructure import parse_cv
from use_cases import evaluate_candidate

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/v1/analyze-cv', methods=['POST'])
def analyze_cv_api():
    data = request.json
    if not data or 'cv_text' not in data:
        return jsonify({"error": "Missing 'cv_text'"}), 400
        
    try:
        candidate_dto = parse_cv(data['cv_text'])#отримуємо DTO
        evaluation_result = evaluate_candidate(candidate_dto)
        return jsonify(evaluation_result), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
