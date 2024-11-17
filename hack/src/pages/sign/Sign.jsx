import React from 'react';
import './Sign.css';

function Sign() {
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
      </div>
      
    </div>
  );
}

export default Sign;