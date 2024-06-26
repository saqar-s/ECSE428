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
    const response = await api.post("/createRecipe", data);

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
          errorMessage = "Recipe creation failed";
          break;
      }

      return { status, message: errorMessage };
    } else {
      return { status: 500, message: "Internal server error" };
    }
  }
};

//add a picture to the recipe
export const addPicture = async (data) => {
  try {
    const response = await api.put("/addPicture", data);
    return { status: response.status, message: "Added picture successfully" };
  } catch (error) {
    return { status: 500, message: "Internal server error" };
  }
};

//delete a recipe
export const deleteRecipe = async (data) => {
  try {
    const response = await api.delete("/deleteRecipe", { data });
    return { status: response.status, message: "Deleted recipe successfully" };
  } catch (error) {
    return { status: 500, message: "Internal server error" };
  }
};

//get the recipes
export const getRecipes = async (user_email = null) => {
  try {
    //When getting the recipe, it is important to get the id also for the delete process
    const response = user_email
      ? await api.get(`/getRecipes?user_email=${user_email}`)
      : await api.get("/getRecipes");

    return { status: response.status, data: response.data };
  } catch (error) {
    return { status: 500, message: "Internal server error" };
  }
};

export const addToFavourites = async (data) => {
  try {
    const response = await api.post("/addFavourite", data);
    return {
      status: response.status,
      message: "Added to favourites successfully",
    };
  } catch (error) {
    return { status: 500, message: "Internal server error" };
  }
};

export const getFavourites = async (email) => {
  try {
    const response = await api.get(`/favourites?email=${email}`);

    return { status: response.status, data: response.data };
  } catch (error) {
    return { error };
  }
};

export const deleteFavourite = async (data) => {
  try {
    const response = await api.delete("/removeRecipeFromFavourites", { data });
    return { status: response.status, data: response.data };
  } catch (error) {
    return { status: 500, message: "Internal server error" };
  }
};
