import React, { useState, useEffect } from 'react';
import './Sign.css';

function Sign() {
  const [predictedLetter, setPredictedLetter] = useState('');

  useEffect(() => {
    // Function to fetch predicted letter from backend
    const fetchPrediction = async () => {
      try {
        const response = await fetch('http://localhost:5000/predict-gesture', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          // Assuming you send some frame data for prediction. This is a placeholder.
          body: JSON.stringify({ frame: [/* preprocessed frame data here */] }),
        });
        const data = await response.json();
        setPredictedLetter(data.predicted_letter);
        console.log('Predicted Letter:', data.predicted_letter); 
      } catch (error) {
        console.error('Error fetching predicted letter:', error);
      }
    };

    // Call the fetch function at regular intervals or based on certain conditions
    // You can customize this as per your requirement, e.g., on button click, or on video frame change
    const interval = setInterval(fetchPrediction, 2000); // Fetch prediction every 2 seconds
    return () => clearInterval(interval); // Clean up interval on component unmount
  }, []);

  return (
    <div className="mainSign">
      <div className="container1">
        <header className="headers">
          <h1 id="tup">thumbs.up</h1>
        </header>
        <div className="sidebar">
          <div id="p1"><h2>learn</h2></div>
          <div id="p2"><h2>practice</h2></div>
          <div id="p3"><h2>profile</h2></div>
          <div id="p4"><h2>mentors</h2></div>
          <div id="p5"><h2>leaderboards</h2></div>
          <div id="p6"><h2>achievements</h2></div>
          <div id="request"><h2>request a live interpreter</h2></div>
        </div>
      </div>
      <div className="container">
        <img
          src="http://localhost:5000/video"
          alt="Hand Detection Stream"
          id="cam"
          style={{ width: '30vw', height: 'auto' }}
        />
        <div className="alphabet">
          <div className="letter">A</div>
          <div className="letter">B</div>
          <div className="letter">C</div>
          <div className="letter">D</div>
          <div className="letter">E</div>
          <div className="letter">F</div>
          <div className="letter">G</div>
          <div className="letter">H</div>
          <div className="letter">I</div>
          <div className="letter">J</div>
          <div className="letter">K</div>
          <div className="letter">L</div>
          <div className="letter">M</div>
          <div className="letter">N</div>
          <div className="letter">O</div>
          <div className="letter">P</div>
          <div className="letter">Q</div>
          <div className="letter">R</div>
          <div className="letter">S</div>
          <div className="letter">T</div>
          <div className="letter">U</div>
          <div className="letter">V</div>
          <div className="letter">W</div>
          <div className="letter">X</div>
          <div className="letter">Y</div>
          <div className="letter">Z</div>
        </div>
        {/* Display the predicted letter */}
        <div className="predicted-letter">
          <h2>Predicted Letter: {predictedLetter}</h2>
        </div>
      </div>
    </div>
  );
}

export default Sign;
