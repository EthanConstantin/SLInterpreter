@app.route('/predict-gesture', methods=['POST'])
def predict_gesture():
    # Extract the frame data from the request
    try:
        data = request.json
        preprocessed_frame = np.array(data['frame'])  # Assuming the input is provided as a 2D array
        
        # Make prediction
        predicted_letter = predict_gesture_from_frame(preprocessed_frame)
        
        # Smooth prediction (optional if you want smoothing logic here too)
        smoothed_prediction = smoother.add_prediction(predicted_letter)
        
        return jsonify({"predicted_letter": smoothed_prediction})
    except Exception as e:
        print(f"Error making prediction: {e}")
        return jsonify({"error": str(e)}), 400