// import React from "react";

// const DashboardScreen = () => {
//   return <div>dashboard</div>;
// };

// export default DashboardScreen;
import React, { useState, useEffect } from "react";
import { TitleText, SubTitleText, CustomButton, TextInput } from "../Components";
import { COLORS, FONTS } from "../GLOBAL";
import { getAllRecipes, getRecipesByEmail } from "../APIcalls/RecipeCalls";

const DashboardScreen = () => {
  const [recipes, setRecipes] = useState([]);
  const [userEmail, setUserEmail] = useState("");

  useEffect(() => {
    fetchAllRecipes();
  }, []);

  const fetchAllRecipes = async () => {
    try {
      const { data, status } = await getAllRecipes();
      if (status === 200) {
        setRecipes(data);
      } else {
        console.error("Failed to fetch recipes");
      }
    } catch (error) {
      console.error("Error fetching recipes:", error);
    }
  };

  const handleViewByEmail = async () => {
    try {
      const { data, status } = await getRecipesByEmail(userEmail);
      if (status === 200) {
        setRecipes(data);
      } else {
        console.error("Failed to fetch recipes");
      }
    } catch (error) {
      console.error("Error fetching recipes:", error);
    }
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", margin: 12 }}>
      <TitleText text={"Welcome to Gourmet Guru!"} />
      <div style={{ marginBottom: "6%" }}>
        <SubTitleText text={"Check out the latest recipes shared by our community!"} />
      </div>
      <CustomButton label={"Refresh Recipes"} onClick={fetchAllRecipes} />
      <div style={{ marginTop: "2rem", width: "50%", display: "flex", alignItems: "center" }}>
        <TextInput
          label={"Enter Email to Filter Recipes"}
          value={userEmail}
          onChange={(e) => setUserEmail(e.target.value)}
          style={{ width: "100%", height: "40px" }}
        />
        <CustomButton label={"View Recipes"} onClick={handleViewByEmail} style={{ marginLeft: "10px", width: "50%", height: "40px", marginTop: "60px" }} />
      </div>
      <div>
        {recipes.map((recipe) => (
          <div key={recipe.id} style={{ marginBottom: "2rem" }}>
            <h2>{recipe.name}</h2>
            <p><strong>Ingredients:</strong> {recipe.ingredients.join(", ")}</p>
            <p><strong>Description:</strong> {recipe.description}</p>
            <p><strong>Email:</strong> {recipe.email}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DashboardScreen;
