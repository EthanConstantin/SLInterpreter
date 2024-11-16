import React from 'react';
import './Homepage.css';
import videobg from './videobg.mp4';
import { useNavigate } from 'react-router-dom';


function Homepage() {
  const navigate = useNavigate();

  const navButton = () => {
      navigate('/sign'); // Replace '/start-learning' with your desired route
  };
  
  return (
    <div className="main">
     
      <div className="overlay"></div>
      <video src={videobg} autoPlay loop muted />
      <div className="header">
        
        
        <h2> home </h2>
        <h2> about </h2>
        <h2> contact us </h2>
      </div>
      <div className="content">
        <h1 id="title"> thumbs.up </h1>
        <h1 id="learn" onClick={navButton}> start learning </h1>
      </div>
     
    </div>
  );
}

export default Homepage;
