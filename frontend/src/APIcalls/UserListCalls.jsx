import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const api = axios.create({
    baseURL: BASE_URL,
  
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Credentials": true,
    },
  });

  export const getUserList = async () => {
    try {
      const response = api.get("/searchuser");
      return response.json; //return user names
    } catch (error) {
      if (error.response) {
        const status = error.response.status;
        let errorMessage;
  
        errorMessage = "Data base was empty of Users!"
  
        return { status, message: errorMessage };
      } else {
        return { status: 500, message: "Internal server error" };
      }
    }
  };