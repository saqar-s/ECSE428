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
import { useAuth } from "../AuthContext";
import { useFavorites } from "../Components/FavoritesProvider";

const FavoritesScreen = () => {
  const [recipes, setRecipes] = React.useState([]);
  const { isLoggedInUser } = useAuth();

  const email = localStorage.getItem("username");
  const { favorites } = useFavorites();
  React.useEffect(() => {
    if (!isLoggedInUser) {
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
  }, [isLoggedInUser, email]);

  React.useEffect(() => {
    const favoriteRecipeIds = new Set(favorites);
    setRecipes((prevRecipes) =>
      prevRecipes.filter((recipe) => favoriteRecipeIds.has(recipe.id))
    );
  }, [favorites]);

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
      {isLoggedInUser ? (
        recipes.length === 0 ? (
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
        )
      ) : (
        <div>
          You need to be logged in to be able to view your favourite recipes
        </div>
      )}
    </div>
  );
};

export default FavoritesScreen;
