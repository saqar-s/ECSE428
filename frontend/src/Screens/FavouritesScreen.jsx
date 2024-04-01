import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
  RecipeCard,
} from "../Components";
import { Grid } from "@mui/material";
import { getFavourites } from "../APIcalls/RecipeCalls";

const FavoritesScreen = () => {
  const [recipes, setRecipes] = React.useState([]);
  const [loggedIn, setLoggedIn] = React.useState(true); // Assuming initially logged in
  const email = localStorage.getItem("username");

  React.useEffect(() => {
    if (!email) {
      setLoggedIn(false);
      return;
    }

    getFavourites(email)
      .then((response) => {
        console.log(response.data.favourites);
        setRecipes(response.data.favourites);
      })
      .catch((error) => {
        console.error("Error fetching recipes:", error);
      });
  }, [email]); // Include email in the dependency array to trigger useEffect on email changes

  if (!loggedIn) {
    return (
      <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        margin: 12,
      }}
    >
       < SubTitleText text={"You must be signed in to view favourites!"} />
      </div>
    );
  }

  const cardsPerRow = Math.min(4, recipes.length);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        margin: 12,
      }}
    >
      <TitleText text={"Welcome to Gourmet Guru!"} />
      <div style={{ marginBottom: "6%" }}>
        <SubTitleText text={"Your favourite recipes!"} />
      </div>
      {recipes.length === 0 ? (
        <p>No favorite recipes found.</p>
      ) : (
        <Grid container spacing={2} marginLeft={2}>
          {recipes.map((recipe, index) => (
            <Grid item xs={12 / cardsPerRow} key={index}>
              <RecipeCard
                title={recipe.name}
                imageURL={recipe.image}
                description={recipe.description}
                author={recipe.email}
                recipeId={recipe.id}
              />
            </Grid>
          ))}
        </Grid>
      )}
    </div>
  );
};

export default FavoritesScreen;
