
import { useState } from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Homepage from "./pages/home/Homepage";
import Sign from "./pages/sign/Sign"


function App() {

  // useState is a VERY important concept here, please read up on it!
  // https://react.dev/reference/react/useState
  const [userData, setData] = useState({
    username: null,
    password: null
  });
  // we will also be using this to PASS STATE DOWN (another really important concept)
  // https://react.dev/learn/sharing-state-between-components

  const router = createBrowserRouter([
    {
      path: "/",
      element:(
    
        <Homepage />
      )
      
    },
    {
      path: "/sign", // Add the new route
      element: <Sign />
    }
 
  ]);

  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  );


}




export default App;
