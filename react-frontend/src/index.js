import React from "react";
import ReactDOM from "react-dom";
import FixedMenuLayout from "./FixedMenuLayout";
import Myheader from "./MainGrid";
import Mygrid from "./BottomNav";
import App from './App.js'

// const App = () => (
//   <div>
//     hi
//   <FixedMenuLayout />
//   <Myheader /> 
//   <Mygrid />
//   </div>
// );

// TODO: Switch to https://github.com/palmerhq/the-platform#stylesheet when it will be stable
const styleLink = document.createElement("link");
styleLink.rel = "stylesheet";
styleLink.href = "https://cdn.jsdelivr.net/npm/semantic-ui/dist/semantic.min.css";
document.head.appendChild(styleLink);

ReactDOM.render(
  <App/>,document.getElementById("root")
);
