// import "./css/App.css";
// import MovieCard from "./components/MovieCard";
import Hamming from "./pages/Hamming";
import Home from "./pages/Home";
import { Routes, Route } from "react-router-dom";
import AppBar from "./components/AppBar";

function App() {
  return (
    <>
      <div style={{ backgroundColor: "grey", minHeight: "100vh" }}>
        <AppBar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/Hamming" element={<Hamming />} />
          </Routes>
        </main>
      </div>
    </>
  );
}

export default App;
