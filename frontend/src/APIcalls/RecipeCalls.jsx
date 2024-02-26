import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: BASE_URL,

  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Credentials": true,
  },
});

export const createRecipe = async (data) => {
  try {
    const response = await api.post('/createRecipe', data);
    return { status: response.status, message: "Created recipe successfully" };
  } catch (error) {
    if (error.response) {
      const status = error.response.status;
      let errorMessage;

      switch (status) {
        case 400:
          errorMessage = "The recipe must have a name";
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

export const deleteRecipe = async (data) => {
  try{
    const response = await api.post('/deleteRecipe', data);
    return { status: response.status, message: "Recipe has been deleted" };
  }
  catch (error) {
    if (error.response) {
      const status = error.response.status;
      let errorMessage;

      switch (status) {
        case 400:
          errorMessage = "Recipe with the given name could not be found";
          break;
        default:
          errorMessage = "Deletion failed";
          break;
      }
    } else {
    return { status: 500, message: "Internal server error" };
    } 
  }
};