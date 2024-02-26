import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
} from "../Components";
import { FONTS } from "../GLOBAL";
import { useNavigate } from "react-router-dom";
import { createRecipe } from "../APIcalls/RecipeCalls";
import { deleteRecipe } from "../APIcalls/RecipeCalls";
import { Alert, Snackbar } from "@mui/material";

const PostScreen = () => {
  const [recipeName, setRecipeName] = React.useState("");
  const [servingSize, setServingSize] = React.useState("");
  const [origin, setOrigin] = React.useState("");
  const [mealType, setMealType] = React.useState("");
  const [description, setDescription] = React.useState("");
  // const [passwordError, setPasswordError] = React.useState("");
  const [error, setError] = React.useState("");
  const [open, setOpen] = React.useState(false);
  const [recipeNameToDelete, setRecipeNameToDelete] = React.useState("");


  const handleRecipeNameChange = (text) => {
    setRecipeName(text);
  };
  const handleServingSizeChange = (text) => {
    setServingSize(text);
  };
  const handleOriginChange = (text) => {
    setOrigin(text);
  };
  const handleMealTypeChange = (text) => {
    setMealType(text);
  };
  const handleDescriptionChange = (text) => {
    setDescription(text);
  };
  const handleCreateRecipe = async () => {
    try {
      const userData = {
        name: recipeName,
        servingSize: servingSize,
        origin: origin,
        category: mealType,
        description: description,
      };

      const result = await createRecipe(userData);

      if (result && result.status === 200) {
        setRecipeName("");
        setServingSize("");
        setOrigin("");
        setMealType("");
        setDescription("");
        // setError("createdRecipe")
      } else if (result.status === 400) {
        // setError(result.message);
      } else {
        // setError("Registration failed");
        // setOpen(true);
        
      }
    } catch (error) {
      // setError("Error creating recipe:", error.message);
      // setOpen(true);
    }


  };

  const handleCLose = (reason) => {
    if (reason === "clickaway") {
      return;
    }
    setOpen(false);
  };

  const handleNameForDelete = (text) => {
    setRecipeNameToDelete(text);
  };

  const handleDeleteRecipe = async () => {
    try {
      const userData = {
        name : recipeNameToDelete,

      };

      const result = await deleteRecipe(userData);
      console.log(`this is what result is giving me ${result}`);
      if (result && result.status === 200) {
        recipeNameToDelete("");
      }
      else {
        console.log(`something bad is hapenning bobby ${recipeNameToDelete}`)
      }
    }
    catch (error) {

    }
  }



  return (
    <>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          margin: 12,
        }}
      >
        <TitleText text={"Hello!"} />
        <div style={{ marginBottom: "6%" }}>
          <SubTitleText
            text={"Make a post by filling the boxes!"}
          />
        </div>

        <TextInput
          label={"Name of the recipe"}
          text={recipeName}
          onClick={handleRecipeNameChange}
          style={{ marginBottom: 6 }}
          //hasError
          //helpertext={emailError}
        />
        <TextInput
          label={"Serving size (number of portions)"}
          text={servingSize}
          onClick={handleServingSizeChange}
          style={{ marginBottom: 6 }}
        />

        <TextInput
          label={"Origin of the recipe (eg. Indian or Italian)"}
          text={origin}
          onClick={handleOriginChange}
          style={{ marginBottom: 6 }}
        />
        <TextInput
          label={"Type of meal (eg. desert or appetizer)"}
          text={mealType}
          onClick={handleMealTypeChange}
          style={{ marginBottom: 6 }}
        />
        <TextInput
          label={"Description"}
          text={description}
          onClick={handleDescriptionChange}
          style={{ marginBottom: 6 }}
        />

        <CustomButton
          label={"Create Recipe"}
          onClick={handleCreateRecipe}
          style={{ width: "10%", height: "40px", marginBottom: 6 }}
        />
        <TextInput
          label={"Delete a Recipe"}
          text={recipeNameToDelete}
          onClick={handleNameForDelete}
          style={{ marginBottom: 6 }}
        />
        <CustomButton
          label={"Delete Recipe"}
          onClick={handleDeleteRecipe}
          style={{ width: "10%", height: "40px", marginBottom: 6 }}
        />
        
      </div> /* not fully functional */
      <Snackbar open={open} autoHideDuration={3000} onClose={handleCLose}>
        <Alert variant="filled" severity="danger" sx={{ width: "100%" }}>
          {error} 
        </Alert>
      </Snackbar>
    </>
  );
};

export default PostScreen;