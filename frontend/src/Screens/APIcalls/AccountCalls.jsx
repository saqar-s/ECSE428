import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: BASE_URL,
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

const registerUser = async (data) => {
  try {
    const response = await api.post("/register", data);
    console.log(response);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const loginUser = async (userData) => {
  try {
    const response = await api.post("/login", userData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const logoutUser = async () => {
  try {
    const response = await api.get("/logout");
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export { registerUser, loginUser, logoutUser };
