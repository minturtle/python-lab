import Header from "./components/Header"
import AudioConvert  from "./components/AudioConvert";
import Home from "./components/Home";

import { BrowserRouter as Router ,Route, Routes} from "react-router-dom";

function App() {
  return (
    <>
      <Router>
        <Header />
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/audio/convert" element={<AudioConvert />}/>
        </Routes>
      </Router>
    </>
  );
}

export default App;
