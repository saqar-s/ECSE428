import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: BASE_URL,

  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Credentials": true,
  },
});

export const registerUser = async (data) => {
  try {
    const response = await api.post("/register", data);
    return { status: response.status, message: "Registration successful" };
  } catch (error) {
    if (error.response) {
      const status = error.response.status;
      let errorMessage;

      switch (status) {
        case 400:
          errorMessage = "Email already exists";
          break;
        default:
          errorMessage = "Registration failed";
          break;
      }

      return { status, message: errorMessage };
    } else {
      return { status: 500, message: "Internal server error" };
    }
  }
};

export const loginUser = async (data) => {
  try {
    const response = await api.post("/login", data);
    return {
      response: response,
      status: response.status,
      message: "Login successful",
    };
  } catch (error) {
    if (error.response) {
      const status = error.response.status;
      let errorMessage;
      switch (status) {
        case 404:
          errorMessage = "Email Does not exist";
          break;
        case 401:
          errorMessage = "Invalid password";
          break;
        default:
          errorMessage = "Registration failed";
          break;
      }

      return { status, message: errorMessage };
    } else {
      return { status: 500, message: "Internal server error" };
    }
  }
};

export const logoutUser = async () => {
  try {
    const response = await api.get("/logout");
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const modifyUserDetails = async (data) => {
  try {
    //const response = await api.post("/modify", data);
    const response = await api.put('/modify', data)
    return {
      response: response,
      status: response.status,
      message: "User details modified successfully",
    };
  } catch (error) {
    if (error.response) {
      const status = error.response.status;
      let errorMessage;
      switch (status) {
        /** 
        case 401:
          errorMessage = "User not logged in";
          break;*/
        default:
          errorMessage = "Failed to modify user details";
          break;
      }
      return { status, message: errorMessage };
    } else {
      return { status: 500, message: "Internal server error" };
    }
  }
};