import Hamming from "./pages/Hamming";
import Home from "./pages/Home";
import Testing from "./pages/Testing";

import { Routes, Route } from "react-router-dom";
import AppBar from "./components/AppBar";
import Repetition from "./pages/Repetition";
import ReedSolomon from "./pages/ReedSolomon";

// style={{ backgroundColor: "grey", minHeight: "100vh" }}

function App() {
  return (
    <>
      <div>
        <AppBar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/home" element={<Home />} />
            <Route path="/hamming" element={<Hamming />} />
            <Route path="/repetition" element={<Repetition />} />
            <Route path="/reed-solomon" element={<ReedSolomon />} />
            <Route path="/testing" element={<Testing />} />
          </Routes>
        </main>
      </div>
    </>
  );
}

export default App;
