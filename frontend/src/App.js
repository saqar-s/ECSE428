import axios from "axios";
import { useEffect, useState } from "react";

const baseURL = "http://localhost:8000";

function App() {
  const [events, setEvents] = useState([]);

  const fetchEvents = async () => {
    try {
      const response = await axios.get(`${baseURL}/event`);
      setEvents(response.data.events);
    } catch (error) {
      console.error("Error fetching events:", error);
    }
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  return (
    <div className="App">
      <h1>Event List</h1>
      {events.map((event) => (
        <div key={event.id}>
          <p>{`Event ID: ${event.id}`}</p>
          <p>{`Created At: ${event.created_at}`}</p>
          <p>{`Description: ${event.description}`}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default App;
