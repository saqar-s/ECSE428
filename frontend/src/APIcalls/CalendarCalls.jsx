import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Credentials": true,
  },
});

export const addToCalendar = async (data) => {
    try {
        const response = await api.post('/addToCalendar', data);
        return { status: response.status, message: "Added to calendar successfully" };
    } catch (error) {
        if (error.response) {
        const status = error.response.status;
        let errorMessage;
    
        switch (status) {
            case 400:
            errorMessage = "All fields are required";
            break;
            default:
            errorMessage = "Failed to add to calendar";
            break;
        }
    
        return { status, message: errorMessage };
        } else {
        return { status: 500, message: "Internal server error" };
        }
    }
};