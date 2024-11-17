import React, { useState, useEffect } from 'react';
import './Sign.css';

function Sign() {
  const [selectedLetter, setSelectedLetter] = useState('');

  // Function to handle letter click
  const handleLetterClick = (letter) => {
    setSelectedLetter(letter);
  };
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
          <div id="p6"><h2>games</h2></div>
          <div id="request"><h2>request a live interpreter</h2></div>
        </div>
      </div>
      <div className="container">
        
              {/* Display an image based on the selected letter */}
      {selectedLetter && (
        <div className="display">
         
         
          <img
            src={`/images/${selectedLetter}.png`} // Dynamically require the image
            alt={`Representation of ${selectedLetter}`}
            style={{ width: '250px', height: '325.5px' }} // Optional styling
          />
        </div>
      )}
        <img
          src="http://localhost:5000/video"
          alt="Hand Detection Stream"
          id="cam"
          style={{ width: '30vw', height: 'auto' }}
        />
        <div className="alphabet">
        {'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').map((letter) => (
          <div
            key={letter}
            className="letter"
            onClick={() => handleLetterClick(letter)}
            style={{ cursor: 'pointer' }} // Makes it clear that letters are clickable
          >
            {letter}
          </div>
        ))}
      </div>


       
      </div>
    </div>
  );
}

export default Sign;
