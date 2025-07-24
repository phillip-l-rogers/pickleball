import { BrowserRouter, Route, Routes } from "react-router-dom";
import CreateTournament from "./pages/CreateTournament";
import Home from "./pages/Home";
import TournamentDetail from "./pages/TournamentDetail";
import TournamentList from "./pages/TournamentList";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/tournaments" element={<TournamentList />} />        
        <Route path="/tournaments/new" element={<CreateTournament />} />
        <Route path="/tournaments/:id" element={<TournamentDetail />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
