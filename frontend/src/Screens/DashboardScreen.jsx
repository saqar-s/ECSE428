import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
  RecipeCard,
} from "../Components";
import { Grid } from "@mui/material";
import { getRecipes } from "../APIcalls/RecipeCalls";
const DashboardScreen = () => {
  const [recipes, setRecipes] = React.useState([]);

  React.useEffect(() => {
    getRecipes()
      .then((response) => {
        console.log(response.data.recipes);
        setRecipes(response.data.recipes);
      })
      .catch((error) => {
        console.error("Error fetching recipes:", error);
      });
  }, []);
  const cardsPerRow = Math.min(4, recipes.length);
  console.log(cardsPerRow);
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
        <SubTitleText text={"Make a post and share it with others to enjoy!"} />
      </div>
      <Grid container spacing={2} marginLeft={2}>
        {recipes.map((recipe, index) => (
          <Grid item xs={12 / cardsPerRow} key={index}>
            <RecipeCard
              title={recipe.name}
              imageURL={recipe.image}
              description={recipe.description}
              author={recipe.email}
            />
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default DashboardScreen;
